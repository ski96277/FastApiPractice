from typing import Optional

from fastapi import FastAPI

from createblogmodel import CreateBlogModel

# Create instance of FastAPI
app = FastAPI()


@app.get('/')
def index():
    return {"name": "Imran", "age": 30, }


# Query parameter api with required and optional data
@app.get('/blog')
def get_blog(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # fetch 10 blog list publish

    if published:
        return {"data": f"{limit} published blogs list from database", "isPublished": published}
    else:
        return {"data": f"{limit} unpublished blogs list from database", "isPublished": published}


@app.get('/blog/unpublished')
def unpublished_blog():
    return {'data': "Hello unpublished Blog"}


# path parameter api
@app.get('/blog/{id}')
def show(id: int):
    return {'blog_id': int(id)}


@app.get('/blog/{id}/comments')
def fetch_comments(id):
    return {'blog_id': id, 'data': {'1', '2'}, }


@app.post('/blog/')
async def create_blog(item: CreateBlogModel):

    return item
