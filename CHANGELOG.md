# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.0.0] - 2025-08-12

### Added
- Scoring system for **7 key evaluation criteria**:
    - Relevance
    - Accuracy
    - Completeness
    - Coherence
    - Creativity
    - Tone
    - Alignment with Intent
- **Semantic similarity** scoring using Sentence Transformers
- **Text quality analysis** with NLTK & TextStat
- **Interactive charts** using Plotly
- **Evaluation history & analytics dashboard** with persistent SQLite storage
- **Customizable scoring weights** via `core/config.py`
- **Modular architecture** with dedicated folders for AI logic, UI components, models, repositories, and pages
- **Deployment ready**:
    - Run via **Docker Compose** for production
    - Run locally with **UV** package manager for development

[1.0.0]: https://github.com/ysskrishna/llm-text-evaluation-framework/releases/tag/v1.0.0