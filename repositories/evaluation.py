from models.models import Evaluation
from core.database import Session, engine

def create_evaluation(
    llm_response: str,
    actual_response: str,
    scores: dict,
    overall_score: float,
    notes: str = None
) -> Evaluation:
    """Store an evaluation in the database"""
    evaluation = Evaluation(
        llm_response=llm_response,
        actual_response=actual_response,
        relevance=scores.get("relevance", 0.0),
        accuracy=scores.get("accuracy", 0.0),
        coherence=scores.get("coherence", 0.0),
        completeness=scores.get("completeness", 0.0),
        creativity=scores.get("creativity", 0.0),
        tone=scores.get("tone", 0.0),
        alignment_with_intent=scores.get("alignment_with_intent", 0.0),
        overall_score=overall_score,
        notes=notes
    )
    
    with Session(engine) as session:
        session.add(evaluation)
        session.commit()
        session.refresh(evaluation)
        return evaluation
