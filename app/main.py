import uvicorn

from config import settings

if __name__ == "__main__":
    uvicorn.run(
        settings.uvicorn.app,
        host=settings.uvicorn.host,
        port=settings.uvicorn.port,
        log_config=settings.logging.log_config_path,
        reload = settings.uvicorn.reload
    )
