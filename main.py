import streamlit as st
from components.sidebar import show_sidebar

def main():
    st.set_page_config(page_title="LLM Text Evaluation Framework", layout="wide")
    
    show_sidebar()
    
    st.title("LLM Text Evaluation Framework")
    st.write("This is the home page")


if __name__ == "__main__":
    main()
