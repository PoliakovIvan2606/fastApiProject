from pydantic import BaseModel

class User(BaseModel):
    id: int = None
    name: str = None
    last_name: str = None