from pydantic import BaseModel
from typing import Dict, Optional


class Account(BaseModel):
    name: str
    description: Optional[str] = None
    balance: float
    active: bool = True