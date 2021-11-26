import os.path
import sys

import uvicorn

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from app.config import settings

if __name__ == "__main__":
    uvicorn.run(
        settings.uvicorn.app,
        host=settings.uvicorn.host,
        port=settings.uvicorn.port,
        log_config=settings.logging.log_config_path,
        reload=settings.uvicorn.reload,
    )
