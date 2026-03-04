"""
Create a "Contract" for your Agent's bug reports.

Task: Define a Pydantic class called BugReport. It should have:

file_path (string)

line_number (integer)

severity (An Enum or String that must be "LOW", "MEDIUM", or "HIGH")

is_fixable (boolean)

Challenge: Try to create an instance of your BugReport where the line_number is a string like "twelve". Observe the error Python gives you.
"""

from enum import Enum
from math import e
from pydantic import BaseModel, ValidationError

class Severity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class bug_report(BaseModel):
    file_path: str
    line_number: int
    severity: Severity
    is_fixable: bool

data = {"file_path": "/bin", "line_number": "twelve", "severity": Severity.HIGH, "is_fixable": "True"}


try:
    my_bug_report = bug_report(**data)
    print (my_bug_report.file_path)
    print (my_bug_report.line_number)
except ValidationError as ve:
    print("validation error occurred during schema validation for input data", ve)


   

