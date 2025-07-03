from fastapi import FastAPI
import uvicorn
from house_app.api import house


house_app = FastAPI(title='House')
house_app.include_router(house.house_router)


if __name__ == '__main__':
    uvicorn.run(house_app, host='127.0.0.1', port=8000)
