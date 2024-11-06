from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Book(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the book")
    author: str = Field(..., min_length=1, description="Author of the book")
    genre: Optional[str] = Field(None, description="Genre of the book")
    status: str = Field(..., pattern="^(to-read|reading|finished)$", description="Reading status")
    start_date: Optional[date] = None
    end_date: Optional[date] = None
