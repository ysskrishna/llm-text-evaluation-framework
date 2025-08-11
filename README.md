# LLM Text Evaluation Framework

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.48+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com/)
[![Status](https://img.shields.io/badge/Status-Beta-orange.svg)](https://github.com/ysskrishna/llm-text-evaluation-framework)

A powerful, production-ready Streamlit web application for comprehensive LLM response evaluation and benchmarking. Features multi-dimensional scoring across 7 key criteria, interactive analytics dashboard, persistent evaluation history, and Docker deployment. Perfect for AI researchers, developers, and organizations seeking to systematically assess and improve their language model outputs with detailed metrics and visual insights.

---

## 📌 Features

### **Evaluation Metrics**

Scores responses across seven weighted criteria:

| Criteria         | Description                                                                         |
| ---------------- | ----------------------------------------------------------------------------------- |
| Relevance        | Measures how semantically similar the LLM response is to the expected response      |
| Accuracy         | Assesses the factual correctness and precision of the content                       |
| Completeness     | Evaluates the logical flow, readability, and sentence structure                     |
| Coherence        | Checks how well the response covers all expected content points                     |
| Creativity       | Measures originality and unique expression while maintaining relevance              |
| Tone             | Assesses appropriateness, consistency, and professional language use                |
| Intent Alignment | Evaluates how well the response matches the user's intended purpose                 |

---

## 🛠 Tech Stack

* **Python 3.10+**
* **Streamlit** (UI)
* **SQLite** (local storage)
* **Sentence Transformers** (semantic similarity)
* **NLTK & TextStat** (text quality analysis)
* **Plotly** (interactive charts)

---

## 🚀 Quick Start

### **1. Clone the Repository**

```bash
git clone https://github.com/ysskrishna/llm-text-evaluation-framework.git
cd llm-text-evaluation-framework
```

### **2.1 Run using docker compose (Preferred)**
```bash
docker-compose up --build
```


### **2.2 Run using uv**

```bash
uv sync
uv run streamlit run main.py
```


### **3. Open in Browser**

Visit **[http://localhost:8501](http://localhost:8501)**

---

## 📂 Project Structure

```
llm-text-evaluation-framework/
├── ai/                          # AI evaluation logic
│   ├── evaluator.py            # Main evaluation functions
│   └── evaluator_utils.py      # Utility functions for scoring algorithms
├── components/                  # Streamlit UI components
│   ├── evaluation_result.py    # Results display with charts and analytics
│   └── sidebar.py              # Sidebar navigation
├── core/                       # Core application logic
│   ├── config.py              # Configuration settings and weights
│   └── database.py            # Database initialization and setup
├── models/                     # Data models
│   ├── enums.py               # Evaluation criteria enums
│   └── models.py              # SQLModel data models
├── pages/                      # Streamlit pages
│   └── 1_history.py          # Evaluation history and analytics dashboard
├── repositories/               # Data access layer
│   └── evaluation.py          # Evaluation CRUD operations
├── main.py                     # Main application entry point
├── pyproject.toml             # Project configuration and dependencies
├── Dockerfile                  # Docker container configuration
├── docker-compose.yml          # Docker Compose setup
└── README.md                  # This file
```

---

## ⚙️ Customization

Adjust scoring weights, and database settings in **`core/config.py`**.

---

## 📜 License

This project is released under the **MIT License**.
See [LICENSE](LICENSE) for details.