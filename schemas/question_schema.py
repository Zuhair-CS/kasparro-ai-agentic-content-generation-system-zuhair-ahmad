from pydantic import BaseModel
from typing import List, Literal

class QuestionSchema(BaseModel):
    category: Literal[
        "Informational", "Usage", "Safety", "Purchase", "Comparison"
    ]
    question: str
