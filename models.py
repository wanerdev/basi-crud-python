from typing import List,Optional
from uuid import uuid4,UUID
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = 'Male'
    female = 'Female'

class Role(str, Enum):
    admin = 'admin'
    user = 'user'

class User(BaseModel):
    id:Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]