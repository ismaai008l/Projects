from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    id: int
    title: str = Field(..., max_length=100)
    description: Optional[str] = None
    completed: bool = False
    due_date: Optional[datetime] = None

    # Updated configuration using ConfigDict
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "Buy groceries",
                "description": "Milk, Eggs, Bread",
                "completed": False,
                "due_date": "2024-10-25T12:00:00"
            }
        }
    )
