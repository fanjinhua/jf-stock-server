import uvicorn
import os

if __name__ == "__main__":
    # 确保在 stock-data 目录下运行
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 导入 FastAPI 应用
    from api.main_api import app
    
    # 运行应用
    uvicorn.run(
        "api.main_api:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )