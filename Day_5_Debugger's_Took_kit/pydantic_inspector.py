#Intentionality break a Pydantic model by passing it a nested 
# dictionary instead of a flat one. Use try...except ValidationError 
# as e: and print e.json().

#Architect Insight: Notice how Pydantic tells you exactly which 
# "key" failed. This is what you log in production to find out why 
# an LLM is failing.

from pydantic import BaseModel, ValidationError


class book(BaseModel):
    id: int
    name: str
    authorName: str

data = {"id": {"nested": 1}, "name": "xyz", "authorName": "same"}  # nested dict triggers ValidationError

try:
    bookExample = book(**data)
except ValidationError as e:
    print("error reading book", e)

