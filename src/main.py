import uvicorn
from fastapi import FastAPI, APIRouter

from src.api.routes import equipments, parts, consumables

app = FastAPI()
routes = APIRouter()


@app.get('/')
def welcome_page():
    return {'msg': 'Welcome to Equipment catalog'}


routes.include_router(equipments.route)
routes.include_router(parts.route)
routes.include_router(consumables.route)

app.include_router(routes)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)