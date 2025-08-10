from models.models import Evaluation
from core.database import get_session
from typing import List, Tuple
from sqlalchemy import func

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
    
    with get_session() as session:
        session.add(evaluation)
        session.commit()
        session.refresh(evaluation)
        return evaluation


def get_evaluations_paginated(
    page: int = 1, 
    page_size: int = 10,
    date_filter: str = None,
    score_filter: float = None,
    search_term: str = None
) -> Tuple[List[Evaluation], int]:
    """
    Retrieve paginated evaluations with optional filters
    
    Returns:
        Tuple of (evaluations, total_count)
    """
    with get_session() as session:
        query = session.query(Evaluation)
        
        # Apply filters
        if date_filter:
            query = query.filter(func.date(Evaluation.created_at) == date_filter)
        
        if score_filter is not None:
            query = query.filter(Evaluation.overall_score >= score_filter)
        
        if search_term:
            search_pattern = f"%{search_term}%"
            query = query.filter(
                (Evaluation.llm_response.ilike(search_pattern)) |
                (Evaluation.actual_response.ilike(search_pattern))
            )
        
        # Get total count for pagination
        total_count = query.count()
        
        # Apply pagination
        offset = (page - 1) * page_size
        evaluations = query.order_by(Evaluation.created_at.desc()).offset(offset).limit(page_size).all()
        
        return evaluations, total_count

def get_evaluations_count(
    date_filter: str = None,
    score_filter: float = None,
    search_term: str = None
) -> int:
    """Get total count of evaluations with optional filters"""
    with get_session() as session:
        query = session.query(Evaluation)
        
        # Apply filters
        if date_filter:
            query = query.filter(func.date(Evaluation.created_at) == date_filter)
        
        if score_filter is not None:
            query = query.filter(Evaluation.overall_score >= score_filter)
        
        if search_term:
            search_pattern = f"%{search_term}%"
            query = query.filter(
                (Evaluation.llm_response.ilike(search_pattern)) |
                (Evaluation.actual_response.ilike(search_pattern))
            )
        
        return query.count()
