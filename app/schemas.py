from pydantic import BaseModel, Field

class PostDefaultCreate(BaseModel):
    post_text: str = Field(..., max_length=20000, description="Максимальная длина текста = 20000")

