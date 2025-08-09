from enum import Enum

class EvaluationCriteria(Enum):
    RELEVANCE = "relevance"
    ACCURACY = "accuracy"
    COHERENCE = "coherence"
    COMPLETENESS = "completeness"
    CREATIVITY = "creativity"
    TONE = "tone"
    ALIGNMENT_WITH_INTENT = "alignment_with_intent"