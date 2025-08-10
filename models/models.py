from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class Evaluation(SQLModel, table=True):
    evaluation_id: Optional[int] = Field(default=None, primary_key=True)
    llm_response: str
    actual_response: str
    relevance: float
    accuracy: float
    coherence: float
    completeness: float
    creativity: float
    tone: float
    alignment_with_intent: float
    overall_score: float
    notes: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
