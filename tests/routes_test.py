from httpx import AsyncClient
import pytest
from app.main import app


class PostExample:
    def __init__(self, post_text, post_id=None, author_id=None):
        self.post_id = post_id
        self.post_text = post_text
        self.author_id = author_id

@pytest.fixture(scope="module")
def get_post_info():
    post_example = PostExample("example_text12345")
    return post_example


@pytest.mark.anyio
async def test_post_default(get_post_info):
    async with AsyncClient(base_url="http://127.0.0.1:8000") as client:
        response = await client.post(
            url="/default_post",
            json={
                "post_text": get_post_info.post_text
            }
        )
    assert 200 <= response.status_code < 300
    get_post_info.post_id = response.json()["post_id"]


@pytest.mark.anyio
async def test_get_post(get_post_info):
    async with AsyncClient(base_url="http://127.0.0.1:8000") as client:
        response = await client.get(f"/post/{get_post_info.post_id}")

    assert 200 <= response.status_code < 300
    assert response.json()["post_id"] == get_post_info.post_id
    assert response.json()["post_text"] == get_post_info.post_text
    assert response.json()["author_id"] == get_post_info.author_id
