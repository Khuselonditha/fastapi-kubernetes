# imports
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum

# Enum class for Gender
class Gender(str, Enum):
    male = "male"
    female = "female"


# Enum class for Gender
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


# Define the model of our user
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    gender: Gender
    roles: list[Role]


# Create a class for updating user information
class UserUpdateRequest(BaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    roles: Optional[List[Role]] = None