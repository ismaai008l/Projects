from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

class Question(BaseModel):
    question_text: str
    question_type: str
    choices: Optional[List[str]] = None  # For multiple-choice questions
    rating_scale: Optional[tuple[int, int]] = None  # Min and Max for ratings

    @field_validator("question_type")
    def validate_question_type(cls, v):
        allowed_types = ["multiple_choice", "rating", "text"]
        if v not in allowed_types:
            raise ValueError(f"Invalid question type: {v}. Allowed types: {allowed_types}")
        return v

    @field_validator("choices", mode="before")
    def validate_choices(cls, v, values):
        if values.get("question_type") == "multiple_choice" and not v:
            raise ValueError("Choices are required for multiple-choice questions.")
        return v

    @field_validator("rating_scale", mode="before")
    def validate_rating_scale(cls, v, values):
        if values.get("question_type") == "rating":
            if not isinstance(v, tuple) or len(v) != 2 or v[0] >= v[1]:
                raise ValueError("Rating scale must be a tuple of two integers (min, max) where min < max.")
        return v


class Survey(BaseModel):
    title: str
    description: str
    questions: List[Question] = Field(default_factory=list)
