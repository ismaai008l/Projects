from typing import List, Optional
from pydantic import BaseModel, Field

class Question(BaseModel):
    question_text: str = Field(..., description="The text of the question")
    question_type: str = Field(..., description="The type of question (text, multiple_choice, rating)")

class Survey(BaseModel):
    title: str = Field(..., description="Title of the survey")
    description: Optional[str] = Field(None, description="Description of the survey")
    questions: List[Question] = Field(default_factory=list)
