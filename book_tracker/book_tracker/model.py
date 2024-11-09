from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date

class Book(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the book")
    author: str = Field(..., min_length=1, description="Author of the book")
    genre: Optional[str] = Field(None, description="Genre of the book")
    status: Literal["to-read", "reading", "finished"] = Field(..., description="Reading status of the Book")
    start_date: Optional[date] = None
    end_date: Optional[date] = None
