# survey_builder/models.py
from pydantic import BaseModel, validator
from typing import List, Union

class MultipleChoiceQuestion(BaseModel):
    question_text: str
    choices: List[str]
    answer: str = None

    @validator("answer")
    def validate_answer(cls, answer, values):
        if answer and answer not in values["choices"]:
            raise ValueError("Answer must be one of the provided choices")
        return answer

class RatingQuestion(BaseModel):
    question_text: str
    min_rating: int
    max_rating: int
    answer: int = None

    @validator("answer")
    def validate_rating(cls, answer, values):
        if answer and not (values["min_rating"] <= answer <= values["max_rating"]):
            raise ValueError(f"Answer must be between {values['min_rating']} and {values['max_rating']}")
        return answer

class TextQuestion(BaseModel):
    question_text: str
    answer: str = None

Question = Union[MultipleChoiceQuestion, RatingQuestion, TextQuestion]

class Survey(BaseModel):
    title: str
    description: str
    questions: List[Question] = []
