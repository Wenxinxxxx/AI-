class ServerConfig():

    AK = "6bmuma7paCflikKVXhK73ktX"
    SK = "SahDiwj74PN9X3vln5BDcfp7BSLIR6TY"
    ERNIE_SPEED_8K_URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token="
    ERNIE_SPEED_128K_URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token="
    ERNIE_LITE_8K_URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-lite-8k?access_token="
    ERNIE_TINY_8K_URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-tiny-8k?access_token="

    M3E_BASE_MODEL = "D:\proj\paper_rag_demo\paper_rag_demo\server\m3e-base"#"/home/customer/proj/m3e-base"

    log_path = "D:\proj\paper_rag_demo\log"
    log_prefix = "paper_rag_"
    log_rotation = "14:30"
    log_retention = "15 days"
    log_encoding = "utf-8"
    log_backtrace = True
    log_diagnose = True

server_config = ServerConfig()
