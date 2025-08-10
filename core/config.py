from models.enums import EvaluationCriteria

class Config:
    DATABASE_URL = "sqlite:///./llm_evaluations.db"
    
    EVALUATION_CRITERIA_LIST = [
        EvaluationCriteria.RELEVANCE,
        EvaluationCriteria.ACCURACY,
        EvaluationCriteria.COHERENCE,
        EvaluationCriteria.COMPLETENESS,
        EvaluationCriteria.CREATIVITY,
        EvaluationCriteria.TONE,
        EvaluationCriteria.ALIGNMENT_WITH_INTENT
    ]

    EVALUATION_CRITERIA_WEIGHTS = {
        EvaluationCriteria.RELEVANCE: 0.2,
        EvaluationCriteria.ACCURACY: 0.2,
        EvaluationCriteria.COHERENCE: 0.1,
        EvaluationCriteria.COMPLETENESS: 0.2,
        EvaluationCriteria.CREATIVITY: 0.1,
        EvaluationCriteria.TONE: 0.1,
        EvaluationCriteria.ALIGNMENT_WITH_INTENT: 0.1
    }