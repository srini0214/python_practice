from pydantic import BaseModel, Field

class BankAccount(BaseModel):
    # This forces the input to be a float. If it's a string like "1000", Pydantic converts it!
    balance: float 
    is_active: bool
    # You can even add metadata for the AI to read
    account_id: str = Field(description="The unique 10-digit IBAN")

# Validation in action
data = {"balance": "1000.50", "is_active": "True", "account_id": "IN12345678"}
account = BankAccount(**data)

print(account.balance)   # 1000.5 (It converted the string to a float!)
print(type(account.is_active)) # <class 'bool'>
print(account.account_id)