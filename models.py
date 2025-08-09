from pydantic import BaseModel

class Event(BaseModel):
    agent_id: str
    cpu_usage: float
    memory_usage: float
    response_time: float

class User(BaseModel):
    username: str
    password: str
    
    
    
    
