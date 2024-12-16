from pydantic import BaseModel, Field
from typing import Optional, List


class Pelicula(BaseModel):
    Title: str
    Year: str
    imdbID: str
    Type: str
    Poster: Optional[str]
