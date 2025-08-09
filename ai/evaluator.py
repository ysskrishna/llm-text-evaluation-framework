from typing import Dict
from models.enums import EvaluationCriteria
from ai.evaluator_utils import calculate_relevance, calculate_accuracy, calculate_coherence, calculate_completeness, calculate_creativity, calculate_tone, calculate_alignment_with_intent


EVALUATION_CRITERIA_LIST = [
    EvaluationCriteria.RELEVANCE,
    EvaluationCriteria.ACCURACY,
    EvaluationCriteria.COHERENCE,
    EvaluationCriteria.COMPLETENESS,
    EvaluationCriteria.CREATIVITY,
    EvaluationCriteria.TONE,
    EvaluationCriteria.ALIGNMENT_WITH_INTENT
]


def evaluate_response(llm_response: str, actual_response: str) -> Dict[str, float]:
    if not llm_response or not actual_response:
        return {criterion: 0.0 for criterion in EVALUATION_CRITERIA_LIST}
    
    scores = {}
    
    # Relevance: Semantic similarity between LLM and actual response
    scores['relevance'] = calculate_relevance(llm_response, actual_response)
    
    # Accuracy: Content accuracy and factual correctness
    scores['accuracy'] = calculate_accuracy(llm_response, actual_response)
    
    # Coherence: Logical flow and readability
    scores['coherence'] = calculate_coherence(llm_response)
    
    # Completeness: Coverage of expected content
    scores['completeness'] = calculate_completeness(llm_response, actual_response)
    
    # Creativity: Originality and unique expression
    scores['creativity'] = calculate_creativity(llm_response, actual_response)
    
    # Tone: Appropriateness and consistency
    scores['tone'] = calculate_tone(llm_response)
    
     # Alignment with intent: How well it matches user's intended purpose
    scores['alignment_with_intent'] = calculate_alignment_with_intent(llm_response, actual_response)
    
    return scores