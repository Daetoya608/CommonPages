from fastapi import APIRouter, HTTPException
from .models import Post, add_post, find_post
from fastapi.responses import JSONResponse
from .schemas import PostDefaultCreate

router = APIRouter()

@router.post("/default_post")
async def add_default_post(default_post: PostDefaultCreate):
    try_new_post = await add_post(post_text=default_post.post_text)
    if not try_new_post:
        return HTTPException(status_code=400, detail="Ошибка создания поста")

    return JSONResponse(
        status_code=201,
        content={
            "post_id": try_new_post.id,
        }
    )


@router.get("/post/{post_id}")
async def get_post(post_id):
    post_id = int(post_id)
    try_find_post = await find_post(post_id)
    if not try_find_post:
        return HTTPException(status_code=404, detail="Пост не найден")

    return JSONResponse(
        status_code=200,
        content={
            "post_id": try_find_post.id,
            "post_text": try_find_post.post_text,
            "author_id": try_find_post.author_id
        }
    )
