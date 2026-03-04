In AI, LLMs are "messy." They might return a string when you wanted a number.

Pydantic is the "Contract" that ensures your AI Agent stays within its architectural bounds.

1. The Problem: The "JSON Hallucination"

You ask an AI for a user's bank details in JSON. It sends back:

JSON
{
  "account_balance": "one thousand dollars", 
  "is_active": "maybe"
}
If your Java/Go backend expects a float and a bool, your system breaks.

2. The Solution: Pydantic Models

Pydantic is a data validation library that uses Python Type Hints to enforce schemas.


3. Why Architects Love Pydantic

Self-Documenting: Your code is your schema.

Fail-Fast: It throws a ValidationError the millisecond data doesn't match the contract.

AI Integration: Frameworks like LangGraph and Instructor use Pydantic models to literally "shape" the AI's brain. You pass the Pydantic class to the AI, and the AI uses it as a template for its response.


1. The Mechanism: Structured Output

When you "connect" Pydantic to an LLM, the following happens under the hood:

Schema Extraction: The framework (like LangGraph or Instructor) converts your Pydantic class into a JSON Schema.

System Prompting: That schema is sent to the LLM with a command: "You must respond ONLY in valid JSON that matches this schema."

Validation Loop: The LLM's string output is fed into BugReport(**llm_output). If it fails, the error is sent back to the LLM to "fix itself," or it throws a Python exception you can catch.

2. The Implementation (Using the instructor library)

The instructor library is the industry standard for this. It "patches" the LLM client to return Pydantic objects directly.

Python
import instructor
from openai import OpenAI # Works with Ollama too!
from pydantic import BaseModel, Field
from enum import Enum

# 1. Define the Contract (The "Science" from Day 3)
class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class BugReport(BaseModel):
    file_path: str = Field(description="Path to the broken file")
    line_number: int = Field(description="The exact line where the error occurs")
    severity: Severity
    explanation: str = Field(description="A 1-sentence explanation of the fix")

# 2. Patch the client (This works with local Ollama via the OpenAI-compatible API)
client = instructor.from_openai(
    OpenAI(base_url="http://localhost:11434/v1", api_url="ollama"),
    mode=instructor.Mode.JSON
)

# 3. The "Architectural" Call
# The return type 'report' is NOT a string. It is a 'BugReport' Python object.
report = client.chat.completions.create(
    model="llama3.1:8b",
    response_model=BugReport,
    messages=[{"role": "user", "content": "The Go server crashed in main.go at line 42 because of a nil pointer."}]
)

print(f"File: {report.file_path}")
print(f"Severity: {report.severity.value}")
3. Why this is the "Sovereign" Way

In Path B, we care about Interoperability.

Because report is a Pydantic object, you can immediately send it to a PostgreSQL database (via an ORM) or a Java Microservice (via JSON serialization).

You have Type Safety in your IDE. If you try to type report.file_name (instead of file_path), your IDE will flag it before you even run the code.


https://www.youtube.com/watch?v=yj-wSRJwrrc