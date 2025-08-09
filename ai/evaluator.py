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

EVALUATION_CRITERIA_WEIGHTS = {
    EvaluationCriteria.RELEVANCE: 0.2,
    EvaluationCriteria.ACCURACY: 0.2,
    EvaluationCriteria.COHERENCE: 0.1,
    EvaluationCriteria.COMPLETENESS: 0.2,
    EvaluationCriteria.CREATIVITY: 0.1,
    EvaluationCriteria.TONE: 0.1,
    EvaluationCriteria.ALIGNMENT_WITH_INTENT: 0.1
}


def evaluate_response(llm_response: str, actual_response: str) -> Dict[str, float]:
    if not llm_response or not actual_response:
        return {criterion: 0.0 for criterion in EVALUATION_CRITERIA_LIST}
    
    scores = {}
    
    # Relevance: Semantic similarity between LLM and actual response
    scores[EvaluationCriteria.RELEVANCE.value] = calculate_relevance(llm_response, actual_response)
    
    # Accuracy: Content accuracy and factual correctness
    scores[EvaluationCriteria.ACCURACY.value] = calculate_accuracy(llm_response, actual_response)
    
    # Coherence: Logical flow and readability
    scores[EvaluationCriteria.COHERENCE.value] = calculate_coherence(llm_response)
    
    # Completeness: Coverage of expected content
    scores[EvaluationCriteria.COMPLETENESS.value] = calculate_completeness(llm_response, actual_response)
    
    # Creativity: Originality and unique expression
    scores[EvaluationCriteria.CREATIVITY.value] = calculate_creativity(llm_response, actual_response)
    
    # Tone: Appropriateness and consistency
    scores[EvaluationCriteria.TONE.value] = calculate_tone(llm_response)
    
     # Alignment with intent: How well it matches user's intended purpose
    scores[EvaluationCriteria.ALIGNMENT_WITH_INTENT.value] = calculate_alignment_with_intent(llm_response, actual_response)
    
    return scores

def get_overall_score(scores: Dict[str, float]) -> float:
    return sum(scores[criterion] * EVALUATION_CRITERIA_WEIGHTS[criterion] for criterion in EVALUATION_CRITERIA_LIST)