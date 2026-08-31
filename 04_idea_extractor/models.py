# Pydantic is a library for defining data shapes with Python type hints, and validating that real data matches 
from pydantic import BaseModel, Field

#Idea is a class that inherits from Pydantics BaseModel
class Idea(BaseModel):
    title: str
    description: str
    priority: str = Field(description="One of: high, medium, low") #required field. The `description` gets sent to the model as part of the schema, so it functions as an instruction about what values to produce
    owner: str | None = None #the value can be a string or nothing 

