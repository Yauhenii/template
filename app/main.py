import uvicorn

from config import settings 

if __name__ == "__main__":
    uvicorn.run(
        settings.uvicorn.app,
        host=settings.uvicorn.host,
        port=settings.uvicorn.port,
        log_level=settings.uvicorn.log_level,
        reload = settings.uvicorn.reload
    )
