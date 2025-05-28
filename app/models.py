from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from database import Base, new_session


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    post_text = Column(Text, unique=False, nullable=False)
    author_id = Column(Integer, default=None)


async def add_post(post_text, author_id=None):
    async with new_session() as session:
        new_post = Post(post_text=post_text, author_id=author_id)
        session.add(new_post)
        try:
            await session.commit()
            return new_post
        except IntegrityError:
            await session.rollback()
            return None


async def find_post(post_id):
    async with new_session() as session:
        post = await session.get(Post, post_id)
        return post
