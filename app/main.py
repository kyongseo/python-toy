from typing import Union
from app.core.metadata import swagger_metadata

from fastapi import FastAPI
from pydantic import BaseModel
from app.router import post, user

app = FastAPI(**swagger_metadata, debug=True)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


app.include_router(post.router)
app.include_router(user.router)

