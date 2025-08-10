import streamlit as st
import pandas as pd
from components.sidebar import show_sidebar
from repositories.evaluation import get_evaluations_paginated, get_evaluations_count


# Page configuration
st.set_page_config(
    page_title="Evaluation History",
    page_icon="📊",
    layout="wide"
)

show_sidebar()

def convert_evaluations_to_dict(evaluations):
    """Convert SQLModel evaluations to dictionaries for easier handling"""
    return [e.model_dump() for e in evaluations]

def show_analytics_dashboard(evaluations_data):
    """Display comprehensive analytics dashboard"""
    if not evaluations_data:
        return
    
    df = pd.DataFrame(evaluations_data)
    df['created_at'] = pd.to_datetime(df['created_at'])
    
    # Key metrics
    st.markdown("### 📊 Key Performance Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_score = df['overall_score'].mean()
        st.metric(
            "Average Overall Score", 
            f"{avg_score:.3f}",
            delta=f"{avg_score - 0.5:.3f}" if avg_score > 0.5 else f"{avg_score - 0.5:.3f}"
        )
    
    with col2:
        total_evaluations = len(df)
        st.metric("Total Evaluations", total_evaluations)
    
    with col3:
        best_score = df['overall_score'].max()
        st.metric("Best Score", f"{best_score:.3f}")
    
    with col4:
        worst_score = df['overall_score'].min()
        st.metric("Lowest Score", f"{worst_score:.3f}")

    

def show_filtered_table():
    """Display filtered and paginated table of evaluations"""
    st.markdown("### 📋 Evaluation Records")
    
    # Filter options
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        date_filter = st.date_input(
            "Filter by date:",
            value=None,
            help="Select a specific date to filter evaluations"
        )
    
    with col2:
        score_filter = st.slider(
            "Minimum overall score:",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            step=0.1,
            help="Filter evaluations with scores above this threshold"
        )
    
    with col3:
        search_term = st.text_input(
            "Search in responses:", 
            placeholder="Enter keywords...",
            help="Search in both LLM and actual responses"
        )
    
    with col4:
        items_per_page = st.selectbox(
            "Items per page:",
            options=[5, 10, 20, 50],
            index=1,
            help="Number of evaluations to show per page"
        )
    
    # Get total count for pagination
    total_items = get_evaluations_count(
        date_filter=date_filter.strftime('%Y-%m-%d') if date_filter else None,
        score_filter=score_filter,
        search_term=search_term
    )
    
    if total_items == 0:
        st.warning("No evaluations match the current filters.")
        return
    
    # Pagination
    total_pages = (total_items + items_per_page - 1) // items_per_page
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        current_page = st.selectbox(
            f"Page (1-{total_pages}):",
            range(1, total_pages + 1),
            index=0
        )
    
    # Fetch paginated data from database
    evaluations, _ = get_evaluations_paginated(
        page=current_page,
        page_size=items_per_page,
        date_filter=date_filter.strftime('%Y-%m-%d') if date_filter else None,
        score_filter=score_filter,
        search_term=search_term
    )
    
    evaluations_data = convert_evaluations_to_dict(evaluations)
    
    start_idx = (current_page - 1) * items_per_page + 1
    end_idx = min(start_idx + items_per_page - 1, total_items)
    st.info(f"Showing {start_idx}-{end_idx} of {total_items} evaluations")
    
    # Display table
    for idx, evaluation in enumerate(evaluations_data):
        with st.expander(f"Evaluation #{evaluation['evaluation_id']} - Score: {evaluation['overall_score']:.3f} - {evaluation['created_at'].strftime('%Y-%m-%d %H:%M')}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**LLM Response:**")
                st.text_area(
                    "LLM Response",
                    value=evaluation['llm_response'],
                    height=150,
                    key=f"llm_{evaluation['evaluation_id']}",
                    disabled=True
                )
            
            with col2:
                st.markdown("**Actual Response:**")
                st.text_area(
                    "Actual Response",
                    value=evaluation['actual_response'],
                    height=150,
                    key=f"actual_{evaluation['evaluation_id']}",
                    disabled=True
                )
            
            # Individual metrics
            st.markdown("**Individual Metrics:**")
            metrics_cols = ['relevance', 'accuracy', 'coherence', 'completeness', 'creativity', 'tone', 'alignment_with_intent']
            
            metric_cols = st.columns(len(metrics_cols))
            for i, metric in enumerate(metrics_cols):
                with metric_cols[i]:
                    score = evaluation[metric]
                    color = "green" if score >= 0.7 else "orange" if score >= 0.5 else "red"
                    st.markdown(f"**{metric.title()}:** <span style='color:{color}'>{score:.3f}</span>", unsafe_allow_html=True)
            
            if evaluation['notes']:
                st.markdown("**Notes:**")
                st.info(evaluation['notes'])

def main():
    st.title("📊 Evaluation History & Analytics")
    st.markdown("---")
    
    try:
        # Get total count for analytics (we need some data for the dashboard)
        total_count = get_evaluations_count()
        
        if total_count == 0:
            st.info("📝 No evaluation history yet. Start by evaluating some responses!")
            return
        
        # For analytics dashboard, we'll fetch a sample of recent data
        # This is more efficient than fetching all data for analytics
        recent_evaluations, _ = get_evaluations_paginated(page=1, page_size=100)
        evaluations_data = convert_evaluations_to_dict(recent_evaluations)
        
        # Show analytics dashboard with recent data
        show_analytics_dashboard(evaluations_data)
        
        st.markdown("---")
        
        # Show filtered table with pagination
        show_filtered_table()
        
        
    except Exception as e:
        st.error(f"❌ Error loading evaluation data: {str(e)}")
        st.info("Please ensure the database is properly configured and contains evaluation data.")

if __name__ == "__main__":
    main()
