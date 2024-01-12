from pydantic import BaseModel


class Acta(BaseModel):
    id: str
    name: str
    autor: str
    url: str
