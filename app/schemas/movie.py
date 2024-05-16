from pydantic import BaseModel


class MovieBase(BaseModel):
    name: str
    year: int
    actors: str


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass