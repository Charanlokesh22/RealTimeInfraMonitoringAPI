from fastapi import FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from app import monitor, auth, models, database
from jose import jwt
import os

app = FastAPI()
app.include_router(monitor.router)

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = database.users_collection.find_one({"username": form_data.username})
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = jwt.encode({"sub": user["username"]}, os.getenv("JWT_SECRET"), algorithm=os.getenv("JWT_ALGORITHM"))
    return {"access_token": token, "token_type": "bearer"}

@app.get("/")
def root():
    return {"message": "Real-Time Monitoring API"}
