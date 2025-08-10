import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.title("LLM Text Evaluation Framework")
        
        st.sidebar.markdown("""
        This framework evaluates LLM responses based on:
        - **Relevance**: Semantic similarity
        - **Accuracy**: Content correctness
        - **Coherence**: Logical flow
        - **Completeness**: Content coverage
        - **Creativity**: Originality
        - **Tone**: Appropriateness
        - **Alignment**: Intent matching
        """)
                
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
        


        if st.sidebar.button("🐙 GitHub: @ysskrishna", key="github_link"):
            st.markdown("[GitHub Profile](https://github.com/ysskrishna)")
        
        if st.sidebar.button("💼 LinkedIn: @ysskrishna", key="linkedin_link"):
            st.markdown("[LinkedIn Profile](https://linkedin.com/in/ysskrishna)")
        
        if st.sidebar.button("📁 View Source", type="primary", key="repo_link"):
            st.markdown("[Repository](https://github.com/ysskrishna/llm-text-evaluation-framework)")
