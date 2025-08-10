import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def get_score_summary(scores: dict) -> dict:
    """Convert numerical scores to rating categories"""
    summary = {}
    for criterion, score in scores.items():
        if score >= 0.7:
            summary[criterion] = 'Excellent'
        elif score >= 0.4:
            summary[criterion] = 'Good'
        else:
            summary[criterion] = 'Needs Improvement'
    return summary

def display_evaluation_results(evaluation_data: dict):
    """Display evaluation results in a comprehensive format"""
    st.markdown("## 📊 Evaluation Results")
    
    # Detailed scores
    st.markdown("### 📈 Detailed Scores by Criterion")
    
    scores = {
        'relevance': evaluation_data['relevance'],
        'accuracy': evaluation_data['accuracy'],
        'coherence': evaluation_data['coherence'],
        'completeness': evaluation_data['completeness'],
        'creativity': evaluation_data['creativity'],
        'tone': evaluation_data['tone'],
        'alignment_with_intent': evaluation_data['alignment_with_intent']
    }
    
    score_summary = get_score_summary(scores)
    
    # Bar chart
    fig = px.bar(
        x=list(scores.keys()),
        y=list(scores.values()),
        labels={'x': 'Criterion', 'y': 'Score'},
        color=list(scores.values()),
        color_continuous_scale='RdYlGn'
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
        
    # Score breakdown table
    score_df = pd.DataFrame([
        {
            'Criterion': criterion.replace('_', ' ').title(),
            'Score': f"{score:.3f}",
            'Rating': rating
        }
        for criterion, score in scores.items()
        for rating in [score_summary[criterion]]
    ])
    
    st.dataframe(score_df, use_container_width=True, hide_index=True)
    
    # Radar chart
    st.markdown("### 🎯 Radar Chart View")
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=list(scores.values()),
        theta=list(scores.keys()),
        fill='toself',
        name='LLM Response',
        line_color='#1f77b4'
    ))
    
    fig.update_layout(
        polar=dict(
            bgcolor="darkgrey",
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )),
        font=dict(color='white'),
        showlegend=False,
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Response comparison
    st.markdown("### 📝 Response Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**LLM Response:**")
        st.text_area("", value=evaluation_data['llm_response'], height=200, disabled=True, key="llm_display")
    
    with col2:
        st.markdown("**Expected Response:**")
        st.text_area("", value=evaluation_data['actual_response'], height=200, disabled=True, key="expected_display")
    
    # Notes if available
    if evaluation_data.get('notes'):
        st.markdown("### 📌 Notes")
        st.info(evaluation_data['notes'])