from fastapi import FastAPI
import uvicorn
from mashroom.api import mushroom


mushroom_app = FastAPI(title='Mushroom')
mushroom_app.include_router(mushroom.mushroom_router)


if __name__ == '__main__':
    uvicorn.run(mushroom_app, host='127.0.0.1', port=8000)
