import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.title("LLM Text Evaluation Framework")
        st.sidebar.text("This framework scores responses based on the following criteria:")

        criteria_info = {
            'Relevance': "Measures how semantically similar the LLM response is to the expected response.",
            'Accuracy': "Assesses the factual correctness and precision of the content.",
            'Coherence': "Evaluates the logical flow, readability, and sentence structure.",
            'Completeness': "Checks how well the response covers all expected content points.",
            'Creativity': "Measures originality and unique expression while maintaining relevance.",
            'Tone': "Assesses appropriateness, consistency, and professional language use.",
            'Alignment': "Evaluates how well the response matches the user's intended purpose."
        }
        for criterion, description in criteria_info.items():
            st.sidebar.text(criterion, help=description)
        
        st.sidebar.markdown("---")
        # Author Section using Streamlit native components
        st.sidebar.markdown("### Author")
        st.sidebar.markdown("""
            <div class="author-header" style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
                <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: bold; color: white;">
                    Y
                </div>
                <div class="author-info" style="display: flex; flex-direction: column; gap: 0px;">
                    <p style="margin: 0; font-size: 16px; font-weight: bold;">ysskrishna</p>
                    <p style="margin: 0; font-size: 15px; color: #666;">Full Stack Developer</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        


        st.sidebar.link_button("🐙 GitHub: @ysskrishna", "https://github.com/ysskrishna")
        
        st.sidebar.link_button("💼 LinkedIn: @ysskrishna", "https://linkedin.com/in/ysskrishna")
        
        st.sidebar.link_button("📁 View Source", "https://github.com/ysskrishna/llm-text-evaluation-framework", type="primary")
