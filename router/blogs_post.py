from fastapi import APIRouter, status, Response, Query, Body, Path
from typing import List, Optional, Dict
from pydantic import BaseModel
router = APIRouter(prefix="/blog", tags=["blog"])


class Image(BaseModel):
    url: str
    alias: str


class Blog_Model(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    meta_data: Dict[str, str] = {'key': 'val1'}
    image: Optional[Image] = None


@router.post("/new", status_code=status.HTTP_201_CREATED)
def post_blog(blog: Blog_Model, response: Response):
    response.status_code = status.HTTP_202_ACCEPTED
    return {"message": "Blog is posted successfully", "data": blog}


@router.post("/new/{id}")
def create_blog(blog: Blog_Model, id: int, version: int = 1):
    return {
        "id": id,
        "version": version,
        "blog": blog
    }


@router.post("/new/{id}/comments")
def create_comment(blog: Blog_Model,
                   id: int,
                   comment: int = Query(None,
                                        title="Id of the comment",
                                        description="Some description of the comment",
                                        alias="commentID",
                                        deprecated=True),
                   content: str = Body(...),
                   v: Optional[List[str]] = Query(
                       ['1.0', '2.0', '3.0', '4.0', '5.0']),
                   ):
    return {
        "blog": blog,
        "id": id,
        "comment": comment,
        "content": content,
        "v": v,
        "comment_id": comment_id,

    }
