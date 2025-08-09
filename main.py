import streamlit as st
from core.database import init_db
from components.sidebar import show_sidebar

def main():
    st.set_page_config(page_title="LLM Text Evaluation Framework", layout="wide")
    init_db()
    show_sidebar()
    
    st.title("LLM Text Evaluation Framework")
    
    with st.form("evaluation_form"):
        llm_response = st.text_area("LLM Response", height=150, placeholder="Paste the LLM response here...")
        actual_response = st.text_area("Actual/Ideal Response", height=150, placeholder="Paste the actual/ideal response here...")
        notes = st.text_area(
            "Add any notes about this evaluation: (Optional)",
            height=100,
            placeholder="e.g., 'Testing new prompt template'"
        )
        submitted = st.form_submit_button("Evaluate")

    if submitted:
        if not llm_response.strip() or not actual_response.strip():
            st.error("Please provide both responses.")
        else:
            with st.spinner("Evaluating response..."):
                pass

if __name__ == "__main__":
    main()
