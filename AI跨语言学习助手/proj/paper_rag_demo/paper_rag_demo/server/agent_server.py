from fastapi import FastAPI
from logger import logger
import json
import requests
import numpy as np
import cv2

import warnings
warnings.filterwarnings("ignore")

from index import load_index
from utils import get_chat_access_token
from request_data import RetrievalRequest, PaperRagRequest
from config import server_config

app = FastAPI()

index_db = load_index()

AK = server_config.AK
SK = server_config.SK

@app.get("/")
async def root():
    return {"message": "The Intercultural Communication AI Bot is on its way!"}

@app.post("/rag_retrieval")
async def rag_retrieval(data: RetrievalRequest):
    query = data.query
    recall_chunks = index_db.similarity_search(query)
    context = ""
    if len(recall_chunks) > 0:
        for chunk in recall_chunks:
            context += chunk.page_content + "\t"
    logger.info(f"rag_retrieval info---query: {query}, content: {context}")
    return {"content": context}

@app.post("/paper_rag_chat")
async def paper_rag_chat(data: PaperRagRequest):
    query = data.query
    retrieval_cunks = data.retrieval_chunks
    temperature = data.temperature
    url = server_config.ERNIE_SPEED_8K_URL + get_chat_access_token(AK, SK)
    
    prompt = f'''Please act as an expert in English and help me answer questions. Most questions are related to the course Intercultural Communication, and some information relevant to this course is stored in one of the files I provide to you called Admin Info, including course title, code, lecturer, email, location, etc. I will provide some reference information, and you need to combine it with the user's actual question to give the final answer. 
The materials I provide are in English, containing known questions and their cause analyses. You should match the appropriate answer for the current question and return it in concise English.
The reference knowledge is as follows:\n
    ------------------\n
    {retrieval_cunks}\n
    ------------------\n
    The user's question is as follows: \n
    {query}\n
    ------------------\n
    Now, please answer based on the provided materials. If no suitable answer can be found, simply return no response. In all other cases, provide the answer as usual.
    '''

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": temperature
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    if response.text:
        answer = json.loads(response.text)
        result = answer["result"]
        logger.info(f"problem_answer_chat info---query: {query}, retrieval_chunks: {retrieval_cunks}, temperature: {temperature}")
        return {"content": result}
    else:
        return {"content": "Sorry, the information is not available at the moment."}
    
