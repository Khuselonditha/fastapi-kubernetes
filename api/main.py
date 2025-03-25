# imports
from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role, UserUpdateRequest
from uuid import UUID

# Create an instance of the fastAPI
app = FastAPI()

# Our database with the users
db: List[User] = [
    User(
        id=UUID("32c229c9-27a7-4b01-8c80-4dcf4f881ec1"), 
        first_name="Avuya", 
        last_name="Nditha",
        gender=Gender.male,
        roles=[Role.user, Role.admin]
    ),
    User(
        id=UUID("73cd7b39-94dc-434b-b32c-529018cecc99"), 
        first_name="Deneline",
        middle_name="Samira", 
        last_name="Mathebula",
        gender=Gender.female,
        roles=[Role.student]
    )
]               


# Create a GET request (Home route)
@app.get("/")
async def root():
    return {"Hello": "World"}

# Create a GET request to return all the user in our db
@app.get("/api/v1/users")
async def fetch_users():
    if not db:
        raise HTTPException(
            status_code=404,
            detail="No users found in the database."
        )
    return db;

# Create a POST request to add a user to our database
@app.post("/api/v1/users")
async def register_user(user: User):
    if any(existing_user.id == user.id for existing_user in db):
        raise HTTPException(
            status_code=400,
            detail=f"User with id: {user.id} already exists."
        )
    db.append(user)
    return {"id": user.id, "message": "User successfully added."}

# Create a DELETE request to remove a user from the database
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"id": user.id, "message":"User successfully removed."}
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exist."
    )

# Create a PUT request for updating user info on the database
@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"id": user.id, "message": "User successfully updated."}
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exist."
    )