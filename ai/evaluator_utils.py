import re
import numpy as np
import nltk
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from textstat import flesch_reading_ease
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer

nltk.download('punkt')
nltk.download('stopwords')

STOP_WORDS = set(stopwords.words('english'))

# Initialize SentenceTransformer model
try:
    sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
except:
    sentence_model = None

def calculate_relevance(llm_response: str, actual_response: str) -> float:
    """Semantic similarity with embedding fallback to Jaccard."""
    if not llm_response or not actual_response:
        return 0.0
    
    if sentence_model:
        try:
            emb_a = sentence_model.encode([llm_response])
            emb_b = sentence_model.encode([actual_response])
            return float(cosine_similarity(emb_a, emb_b)[0][0])
        except:
            pass
    
    # Fallback Jaccard similarity
    words_a = set(re.findall(r'\w+', llm_response.lower()))
    words_b = set(re.findall(r'\w+', actual_response.lower()))
    if not words_a or not words_b:
        return 0.0
    return len(words_a & words_b) / len(words_a | words_b)

def calculate_accuracy(llm_response: str, actual_response: str) -> float:
    """F1-based keyword overlap (ignores stopwords)."""
    if not llm_response or not actual_response:
        return 0.0
    
    words_a = set(re.findall(r'\w+', llm_response.lower())) - STOP_WORDS
    words_b = set(re.findall(r'\w+', actual_response.lower())) - STOP_WORDS
    
    if not words_b:
        return 1.0 if not words_a else 0.0
    
    tp = len(words_a & words_b)
    precision = tp / len(words_a) if words_a else 0.0
    recall = tp / len(words_b) if words_b else 0.0
    
    return (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0

def calculate_coherence(llm_response: str) -> float:
    """Readability + sentence length balance."""
    if not llm_response:
        return 0.0
    
    sentences = sent_tokenize(llm_response)
    if not sentences:
        return 0.0
    
    avg_len = np.mean([len(s.split()) for s in sentences])
    try:
        flesch_score = flesch_reading_ease(llm_response)
        flesch_norm = max(0, min(1, flesch_score / 100))
    except:
        flesch_norm = 0.5
    
    length_score = 1.0
    if avg_len < 5:
        length_score = 0.7
    elif avg_len > 30:
        length_score = 0.6
    
    return min(1.0, max(0.0, (flesch_norm + length_score) / 2))

def calculate_completeness(llm_response: str, actual_response: str) -> float:
    """Coverage of key concepts + length ratio."""
    if not actual_response:
        return 1.0 if llm_response else 0.0
    
    actual_concepts = set(re.findall(r'\w+', actual_response.lower())) - STOP_WORDS
    llm_concepts = set(re.findall(r'\w+', llm_response.lower())) - STOP_WORDS
    
    if not actual_concepts:
        return 1.0 if llm_response else 0.0
    
    coverage = len(actual_concepts & llm_concepts) / len(actual_concepts)
    length_ratio = min(1.0, len(llm_response) / max(len(actual_response), 1))
    
    return (coverage + length_ratio) / 2

def calculate_creativity(llm_response: str, actual_response: str) -> float:
    """Lexical diversity + sentence variety − similarity penalty."""
    if not llm_response:
        return 0.0
    
    words = re.findall(r'\w+', llm_response.lower())
    if not words:
        return 0.0
    
    diversity = len(set(words)) / len(words)
    
    sentences = sent_tokenize(llm_response)
    if len(sentences) > 1:
        sentence_lengths = [len(s.split()) for s in sentences]
        variety = 1.0 - (np.std(sentence_lengths) / np.mean(sentence_lengths)) if np.mean(sentence_lengths) > 0 else 0.0
    else:
        variety = 0.5
    
    # Penalize if too similar to actual_response
    similarity_penalty = 0.0
    if actual_response:
        similarity_penalty = calculate_relevance(llm_response, actual_response) * 0.3
    
    return min(1.0, max(0.0, (diversity + variety) / 2 - similarity_penalty))

def calculate_tone(llm_response: str) -> float:
    """Structural consistency & professionalism."""
    if not llm_response:
        return 0.0
    
    sentences = sent_tokenize(llm_response)
    if not sentences:
        return 0.5
    
    proper_endings = sum(1 for s in sentences if s.strip().endswith(('.', '!', '?')))
    ending_consistency = proper_endings / len(sentences)
    
    sentence_lengths = [len(s.split()) for s in sentences]
    if len(sentence_lengths) > 1:
        length_balance = 1.0 - (np.std(sentence_lengths) / np.mean(sentence_lengths)) if np.mean(sentence_lengths) > 0 else 0.0
    else:
        length_balance = 0.8
    
    exclamations = llm_response.count('!')
    questions = llm_response.count('?')
    professionalism = 1.0
    if exclamations > len(sentences) * 0.3:
        professionalism = 0.7
    if questions > len(sentences) * 0.5:
        professionalism = 0.8
    
    return min(1.0, max(0.0, (ending_consistency + length_balance + professionalism) / 3))

def calculate_alignment_with_intent(llm_response: str, user_intent: str) -> float:
    """Semantic similarity with fallback keyword match."""
    if not user_intent:
        return 0.5
    if not llm_response:
        return 0.0
    
    if sentence_model:
        try:
            emb_a = sentence_model.encode([llm_response])
            emb_b = sentence_model.encode([user_intent])
            return float(cosine_similarity(emb_a, emb_b)[0][0])
        except:
            pass
    
    intent_words = set(re.findall(r'\w+', user_intent.lower())) - STOP_WORDS
    response_words = set(re.findall(r'\w+', llm_response.lower())) - STOP_WORDS
    
    if not intent_words:
        return 0.5
    
    addressed = intent_words & response_words
    return len(addressed) / len(intent_words)
