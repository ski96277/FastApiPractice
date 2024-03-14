from typing import Optional

from pydantic import BaseModel


class CreateBlogModel(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False
    tax: float | None = None
