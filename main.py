from fastapi import FastAPI, APIRouter
from routers.post import post_router

app = FastAPI()

router = APIRouter()
router.include_router(
    post_router,
    prefix='/posts'
)
app.include_router(router)