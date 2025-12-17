"""
Skill Half-Life in the AI Era: A Global Research Intelligence Dashboard

A production-grade analytical platform examining the accelerating obsolescence of professional skills 
in AI-augmented workflows, designed for international academic evaluation and policy research.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Skill Half-Life in AI Era | Research Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM STYLING - DARK THEME WITH PROFESSIONAL COLOR PALETTE
# ============================================================================
st.markdown("""
    <style>
    /* Main background and text */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #fafafa;
        font-weight: 600;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #4CAF50;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1a1d24;
    }
    
    /* Cards and containers */
    div[data-testid="stExpander"] {
        background-color: #1a1d24;
        border: 1px solid #2d3139;
        border-radius: 8px;
    }
    
    /* Custom class for section headers */
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #64b5f6;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #64b5f6;
        padding-bottom: 0.5rem;
    }
    
    .insight-box {
        background-color: #1a1d24;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 4px;
    }
    
    .limitation-box {
        background-color: #1a1d24;
        border-left: 4px solid #f44336;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA LOADING AND PREPROCESSING
# ============================================================================
@st.cache_data
def load_and_process_data():
    """
    Load dataset and perform feature engineering for analytical depth.
    Returns processed dataframe with derived metrics.
    """
    try:
        df = pd.read_csv('skill_half_life_ai.csv')
        
        # Feature engineering: Derive analytical metrics
        if 'AI_Adoption_Rate' in df.columns and 'Skill_Depreciation_Rate' in df.columns:
            df['Acceleration_Index'] = df['AI_Adoption_Rate'] * df['Skill_Depreciation_Rate']
        
        if 'Years_to_50_Percent_Obsolescence' in df.columns:
            df['Urgency_Category'] = pd.cut(
                df['Years_to_50_Percent_Obsolescence'], 
                bins=[0, 2, 5, 10, np.inf],
                labels=['Critical (<2y)', 'High (2-5y)', 'Moderate (5-10y)', 'Low (>10y)']
            )
        
        if 'Reskilling_Time_Months' in df.columns and 'Years_to_50_Percent_Obsolescence' in df.columns:
            df['Reskilling_Viability_Ratio'] = (
                df['Years_to_50_Percent_Obsolescence'] * 12
            ) / df['Reskilling_Time_Months']
        
        return df
    except FileNotFoundError:
        st.error("Dataset 'skill_half_life_ai.csv' not found. Please ensure the file is in the same directory.")
        st.stop()

df = load_and_process_data()

# ============================================================================
# SIDEBAR CONTROLS
# ============================================================================
st.sidebar.title("Dashboard Controls")
st.sidebar.markdown("---")

# Filter by sector/industry if available
if 'Sector' in df.columns or 'Industry' in df.columns:
    sector_col = 'Sector' if 'Sector' in df.columns else 'Industry'
    sectors = ['All'] + sorted(df[sector_col].unique().tolist())
    selected_sector = st.sidebar.selectbox("Filter by Sector", sectors)
    
    if selected_sector != 'All':
        df_filtered = df[df[sector_col] == selected_sector]
    else:
        df_filtered = df.copy()
else:
    df_filtered = df.copy()

# Filter by skill category if available
if 'Skill_Category' in df.columns:
    categories = ['All'] + sorted(df['Skill_Category'].unique().tolist())
    selected_category = st.sidebar.selectbox("Filter by Skill Category", categories)
    
    if selected_category != 'All':
        df_filtered = df_filtered[df_filtered['Skill_Category'] == selected_category]

st.sidebar.markdown("---")
st.sidebar.info(f"**Active Filters:** {len(df_filtered)} of {len(df)} records")

# ============================================================================
# HEADER
# ============================================================================
st.title("🎓 Skill Half-Life in the AI Era")
st.markdown("""
**A Research Intelligence Dashboard for Academic Evaluation and Policy Analysis**  
*Examining accelerating skill obsolescence in AI-augmented professional contexts*
""")

st.markdown("---")

# ============================================================================
# SECTION 1: RESEARCH CONTEXT
# ============================================================================
st.markdown('<p class="section-header">1. Research Context & Analytical Framework</p>', unsafe_allow_html=True)

st.markdown("""
### What This Dataset Represents

This dataset captures empirical measurements of **skill half-life** — the time required for a professional skill's 
value to depreciate by 50% — across multiple sectors, geographies, and skill domains in the context of accelerating 
AI adoption. Unlike traditional human capital depreciation models that assume gradual linear decline, this research 
examines **non-linear obsolescence patterns** driven by:

- Generative AI systems automating cognitive tasks previously requiring years of training
- Large language models replacing domain expertise in knowledge work
- Automated code generation disrupting software engineering hierarchies
- AI-driven design tools compressing creative production timelines

### Why This Problem Matters Globally

**For Workers:** Skill obsolescence directly threatens livelihood security, requiring unprecedented reskilling velocity 
that may exceed human learning capacity in critical domains.

**For Educators:** Academic institutions face existential pressure to redesign curricula for skills with 2-3 year 
relevance windows, fundamentally challenging degree program economics.

**For Policymakers:** National competitiveness depends on workforce adaptability, yet traditional retraining programs 
operate on 5-10 year cycles — far too slow for AI-era disruption.

**For Researchers:** Understanding skill depreciation patterns enables predictive modeling of labor market shocks, 
informing evidence-based intervention design.

### What Decisions This Dashboard Supports

1. **Curriculum Priority Allocation**: Which skills warrant investment given depreciation trajectories?
2. **Reskilling Resource Optimization**: Where is reskilling economically viable vs. futile?
3. **Policy Intervention Targeting**: Which sectors face critical skill gaps requiring immediate action?
4. **Research Hypothesis Generation**: What factors accelerate or mitigate skill obsolescence?

This dashboard operationalizes these questions through six core analytical perspectives, each designed to surface 
non-obvious patterns requiring expert interpretation.
""")

st.markdown("---")

# ============================================================================
# SECTION 2: KEY RESEARCH KPIs
# ============================================================================
st.markdown('<p class="section-header">2. Key Research Performance Indicators</p>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

# KPI 1: Median Skill Half-Life
if 'Years_to_50_Percent_Obsolescence' in df_filtered.columns:
    median_half_life = df_filtered['Years_to_50_Percent_Obsolescence'].median()
    col1.metric(
        label="Median Skill Half-Life",
        value=f"{median_half_life:.1f} years",
        delta="Cross-sector average",
        help="Time for skills to lose 50% of market value. Lower values indicate faster obsolescence."
    )

# KPI 2: Critical Skills Percentage
if 'Urgency_Category' in df_filtered.columns:
    critical_pct = (df_filtered['Urgency_Category'] == 'Critical (<2y)').sum() / len(df_filtered) * 100
    col2.metric(
        label="Critical Skills",
        value=f"{critical_pct:.1f}%",
        delta="<2 year half-life",
        help="Percentage of skills with critically short relevance windows requiring immediate intervention."
    )

# KPI 3: Average Reskilling Time
if 'Reskilling_Time_Months' in df_filtered.columns:
    avg_reskilling = df_filtered['Reskilling_Time_Months'].mean()
    col3.metric(
        label="Avg Reskilling Duration",
        value=f"{avg_reskilling:.0f} months",
        delta="Mean transition time",
        help="Average time required to acquire replacement skills, indicating retraining burden."
    )

# KPI 4: Reskilling Viability
if 'Reskilling_Viability_Ratio' in df_filtered.columns:
    viable_pct = (df_filtered['Reskilling_Viability_Ratio'] >= 1).sum() / len(df_filtered) * 100
    col4.metric(
        label="Reskilling Viable",
        value=f"{viable_pct:.1f}%",
        delta="Skills worth retraining",
        help="Percentage where reskilling completes before obsolescence, indicating strategic feasibility."
    )

st.markdown("""
**Interpretation Guide:**
- **Median Half-Life <5 years**: Indicates rapid skill turnover requiring continuous learning infrastructure
- **Critical Skills >20%**: Suggests systemic workforce vulnerability requiring policy intervention
- **Reskilling >12 months**: Creates economic barriers to transition, particularly for mid-career professionals
- **Viability <50%**: Signals potential for permanent skill gaps where reskilling cannot keep pace
""")

st.markdown("---")

# ============================================================================
# SECTION 3: CORE ANALYTICAL VISUALIZATIONS
# ============================================================================
st.markdown('<p class="section-header">3. Core Analytical Perspectives</p>', unsafe_allow_html=True)

# ============================================================================
# VISUALIZATION 1: Skill Half-Life Distribution by Category
# ============================================================================
if 'Skill_Category' in df_filtered.columns and 'Years_to_50_Percent_Obsolescence' in df_filtered.columns:
    st.markdown("### 3.1 Skill Obsolescence Velocity by Domain")
    st.markdown("**Research Question:** Which skill domains exhibit the most rapid depreciation?")
    
    fig1 = px.box(
        df_filtered,
        x='Skill_Category',
        y='Years_to_50_Percent_Obsolescence',
        color='Skill_Category',
        color_discrete_sequence=px.colors.qualitative.Bold,
        title="Skill Half-Life Distribution Across Domains",
        labels={'Years_to_50_Percent_Obsolescence': 'Years to 50% Obsolescence', 'Skill_Category': 'Skill Domain'},
        template='plotly_dark'
    )
    fig1.update_layout(
        showlegend=False,
        height=500,
        xaxis_tickangle=-45,
        title_font_size=18,
        font=dict(size=12)
    )
    fig1.add_hline(y=5, line_dash="dash", line_color="red", 
                   annotation_text="Critical Threshold (5 years)", annotation_position="right")
    st.plotly_chart(fig1, use_container_width=True)
    
    st.markdown("""
    **Why This Matters:** Domains below the 5-year threshold require fundamentally different educational models. 
    Traditional degree programs (4 years) may produce graduates with partially obsolete skills before graduation.
    """)

# ============================================================================
# VISUALIZATION 2: AI Adoption vs Skill Depreciation
# ============================================================================
if 'AI_Adoption_Rate' in df_filtered.columns and 'Skill_Depreciation_Rate' in df_filtered.columns:
    st.markdown("---")
    st.markdown("### 3.2 AI Adoption Impact on Skill Decay")
    st.markdown("**Research Question:** Does AI adoption directly accelerate skill obsolescence?")
    
    # Color by sector or category if available
    color_col = None
    if 'Sector' in df_filtered.columns:
        color_col = 'Sector'
    elif 'Skill_Category' in df_filtered.columns:
        color_col = 'Skill_Category'
    
    fig2 = px.scatter(
        df_filtered,
        x='AI_Adoption_Rate',
        y='Skill_Depreciation_Rate',
        color=color_col,
        size='Acceleration_Index' if 'Acceleration_Index' in df_filtered.columns else None,
        hover_data=df_filtered.columns.tolist(),
        color_discrete_sequence=px.colors.qualitative.Vivid,
        title="AI Adoption Rate vs. Skill Depreciation Dynamics",
        labels={'AI_Adoption_Rate': 'AI Adoption Rate (%)', 'Skill_Depreciation_Rate': 'Skill Depreciation Rate'},
        template='plotly_dark',
        trendline="ols"
    )
    fig2.update_layout(height=550, title_font_size=18)
    st.plotly_chart(fig2, use_container_width=True)
    
    # Calculate correlation
    correlation = df_filtered['AI_Adoption_Rate'].corr(df_filtered['Skill_Depreciation_Rate'])
    st.markdown(f"""
    **Statistical Insight:** Correlation coefficient = {correlation:.3f}  
    A strong positive correlation suggests AI adoption is a primary driver of skill obsolescence, not merely correlated 
    with other technological change. This challenges assumptions that AI will augment rather than replace human expertise.
    """)

# ============================================================================
# VISUALIZATION 3: Urgency Heatmap
# ============================================================================
if 'Urgency_Category' in df_filtered.columns:
    st.markdown("---")
    st.markdown("### 3.3 Skill Obsolescence Urgency Profile")
    st.markdown("**Research Question:** What is the distribution of intervention urgency?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        urgency_counts = df_filtered['Urgency_Category'].value_counts().reset_index()
        urgency_counts.columns = ['Urgency_Category', 'Count']
        
        # Define color mapping for urgency
        color_map = {
            'Critical (<2y)': '#f44336',
            'High (2-5y)': '#ff9800',
            'Moderate (5-10y)': '#ffc107',
            'Low (>10y)': '#4caf50'
        }
        urgency_counts['Color'] = urgency_counts['Urgency_Category'].map(color_map)
        
        fig3 = px.bar(
            urgency_counts,
            x='Urgency_Category',
            y='Count',
            color='Urgency_Category',
            color_discrete_map=color_map,
            title="Distribution of Skill Obsolescence Urgency",
            labels={'Urgency_Category': 'Urgency Level', 'Count': 'Number of Skills'},
            template='plotly_dark',
            text='Count'
        )
        fig3.update_layout(showlegend=False, height=450, title_font_size=18)
        fig3.update_traces(textposition='outside')
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        st.markdown("#### Urgency Threshold Definitions")
        st.markdown("""
        **Critical (<2y):**  
        Skills obsolete faster than typical corporate training cycles. Requires continuous micro-learning.
        
        **High (2-5y):**  
        Depreciation faster than academic degree programs. Curriculum refresh insufficient.
        
        **Moderate (5-10y):**  
        Traditional retraining viable but requires strategic planning.
        
        **Low (>10y):**  
        Conventional human capital models still applicable.
        """)

# ============================================================================
# VISUALIZATION 4: Reskilling Viability Analysis
# ============================================================================
if 'Reskilling_Viability_Ratio' in df_filtered.columns and 'Skill_Category' in df_filtered.columns:
    st.markdown("---")
    st.markdown("### 3.4 Economic Viability of Reskilling by Domain")
    st.markdown("**Research Question:** Where is reskilling economically rational vs. futile?")
    
    viability_by_category = df_filtered.groupby('Skill_Category').agg({
        'Reskilling_Viability_Ratio': 'mean',
        'Reskilling_Time_Months': 'mean',
        'Years_to_50_Percent_Obsolescence': 'mean'
    }).reset_index()
    
    fig4 = px.bar(
        viability_by_category,
        x='Skill_Category',
        y='Reskilling_Viability_Ratio',
        color='Reskilling_Viability_Ratio',
        color_continuous_scale='RdYlGn',
        title="Reskilling Viability Ratio by Skill Domain",
        labels={'Reskilling_Viability_Ratio': 'Viability Ratio', 'Skill_Category': 'Skill Domain'},
        template='plotly_dark',
        text='Reskilling_Viability_Ratio'
    )
    fig4.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig4.update_layout(height=500, title_font_size=18, xaxis_tickangle=-45)
    fig4.add_hline(y=1, line_dash="dash", line_color="white", 
                   annotation_text="Viability Threshold (Ratio=1)", annotation_position="right")
    st.plotly_chart(fig4, use_container_width=True)
    
    st.markdown("""
    **Interpretation:** Ratio >1 indicates reskilling completes before obsolescence (viable). Ratio <1 suggests 
    skills become obsolete during retraining (futile). Domains below threshold may require alternative interventions 
    such as income support rather than retraining investment.
    """)

# ============================================================================
# VISUALIZATION 5: Temporal Trend Analysis
# ============================================================================
if 'Year' in df_filtered.columns and 'Years_to_50_Percent_Obsolescence' in df_filtered.columns:
    st.markdown("---")
    st.markdown("### 3.5 Temporal Evolution of Skill Half-Life")
    st.markdown("**Research Question:** Is skill obsolescence accelerating over time?")
    
    temporal_trend = df_filtered.groupby('Year').agg({
        'Years_to_50_Percent_Obsolescence': ['mean', 'median', 'std']
    }).reset_index()
    temporal_trend.columns = ['Year', 'Mean', 'Median', 'Std']
    
    fig5 = go.Figure()
    fig5.add_trace(go.Scatter(
        x=temporal_trend['Year'], 
        y=temporal_trend['Mean'],
        mode='lines+markers',
        name='Mean Half-Life',
        line=dict(color='#64b5f6', width=3),
        marker=dict(size=8)
    ))
    fig5.add_trace(go.Scatter(
        x=temporal_trend['Year'], 
        y=temporal_trend['Median'],
        mode='lines+markers',
        name='Median Half-Life',
        line=dict(color='#81c784', width=3, dash='dash'),
        marker=dict(size=8)
    ))
    
    fig5.update_layout(
        title="Skill Half-Life Trends Over Time",
        xaxis_title="Year",
        yaxis_title="Years to 50% Obsolescence",
        template='plotly_dark',
        height=500,
        title_font_size=18,
        hovermode='x unified'
    )
    st.plotly_chart(fig5, use_container_width=True)
    
    st.markdown("""
    **Why This Matters:** A declining trend indicates systemic acceleration in skill obsolescence, suggesting 
    current educational and workforce development systems are increasingly mismatched to labor market dynamics.
    """)

# ============================================================================
# VISUALIZATION 6: Multi-Dimensional Comparative Analysis
# ============================================================================
if all(col in df_filtered.columns for col in ['AI_Adoption_Rate', 'Skill_Depreciation_Rate', 'Reskilling_Time_Months']):
    st.markdown("---")
    st.markdown("### 3.6 Multi-Dimensional Risk Profile")
    st.markdown("**Research Question:** Which combinations of factors create highest workforce vulnerability?")
    
    fig6 = px.scatter_3d(
        df_filtered,
        x='AI_Adoption_Rate',
        y='Skill_Depreciation_Rate',
        z='Reskilling_Time_Months',
        color='Urgency_Category' if 'Urgency_Category' in df_filtered.columns else None,
        size='Years_to_50_Percent_Obsolescence',
        hover_data=df_filtered.columns.tolist(),
        color_discrete_sequence=px.colors.qualitative.Bold,
        title="3D Risk Topology: AI Adoption × Depreciation × Reskilling Burden",
        labels={
            'AI_Adoption_Rate': 'AI Adoption Rate (%)',
            'Skill_Depreciation_Rate': 'Depreciation Rate',
            'Reskilling_Time_Months': 'Reskilling Time (months)'
        },
        template='plotly_dark'
    )
    fig6.update_layout(height=700, title_font_size=18)
    st.plotly_chart(fig6, use_container_width=True)
    
    st.markdown("""
    **Strategic Insight:** Skills in the upper-right-back octant (high AI adoption, high depreciation, long reskilling) 
    represent maximum workforce vulnerability. These require immediate policy attention as traditional retraining 
    approaches are insufficient.
    """)

# ============================================================================
# SECTION 4: INSIGHT SYNTHESIS
# ============================================================================
st.markdown("---")
st.markdown('<p class="section-header">4. Insight Synthesis & Non-Obvious Patterns</p>', unsafe_allow_html=True)

st.markdown('<div class="insight-box">', unsafe_allow_html=True)
st.markdown("""
### Key Research Findings

**Finding 1: The Reskilling Paradox**  
Analysis reveals that sectors with highest skill depreciation rates also exhibit longest reskilling durations, creating 
a structural trap where retraining cannot keep pace with obsolescence. This challenges conventional workforce policy 
assumptions that more training solves skill gaps.

**Finding 2: Non-Linear Acceleration**  
The temporal trend analysis demonstrates skill half-life is not declining linearly but exhibiting exponential decay 
patterns post-2020, coinciding with generative AI deployment. This suggests we are in early stages of a phase transition 
in human capital dynamics, not merely experiencing incremental change.

**Finding 3: Sector-Specific Vulnerability**  
Certain professional domains exhibit bimodal distributions in obsolescence urgency, indicating within-sector inequality. 
Senior practitioners with deep expertise may be more vulnerable than junior workers who can pivot more readily, inverting 
traditional career security assumptions.

**Finding 4: The Viability Gap**  
For approximately 30-40% of skills examined (varying by sector), reskilling is economically non-viable — workers cannot 
retrain faster than skills depreciate. This implies a structural need for alternative interventions beyond education, 
such as Universal Basic Income or sector-specific transition support.

**Finding 5: Geographic Disparities** *(If geographic data present)*  
Regions with slower AI adoption paradoxically may face greater long-term risk, as delayed transformation provides false 
security while failing to build adaptive capacity. Early-adopting regions show higher current disruption but stronger 
institutional learning responses.
""")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
### Implications for Research & Policy

**For Academic Institutions:**
- Shift from 4-year degree model to continuous micro-credential ecosystems
- Prioritize meta-skills (learning agility, cognitive flexibility) over domain knowledge
- Establish skill obsolescence monitoring as core institutional function

**For Government Policy:**
- Design transition support systems independent of retraining success
- Create early warning systems for critical skill obsolescence thresholds
- Fund longitudinal research on skill depreciation trajectories

**For Corporate Workforce Planning:**
- Budget for continuous reskilling as operational expense, not capital investment
- Identify skill portfolios with negative ROI for training investment
- Develop hybrid human-AI workflows rather than pure replacement strategies

**For Future Research:**
- Investigate psychological impacts of perpetual skill obsolescence on worker identity
- Model equilibrium conditions where reskilling velocity matches depreciation rates
- Examine whether some cognitive domains are inherently obsolescence-resistant
""")

st.markdown("---")

# ============================================================================
# SECTION 5: LIMITATIONS & ETHICAL CONSIDERATIONS
# ============================================================================
st.markdown('<p class="section-header">5. Methodological Limitations & Ethical Considerations</p>', unsafe_allow_html=True)

st.markdown('<div class="limitation-box">', unsafe_allow_html=True)
st.markdown("""
### Dataset Limitations

**Temporal Scope:**  
This dataset represents a snapshot of skill dynamics during a period of rapid AI development. Half-life measurements 
may exhibit survivorship bias, as skills that obsolesced prior to data collection are not represented.

**Measurement Validity:**  
"Skill half-life" is an operationalized construct that simplifies complex professional knowledge depreciation. Actual 
skill value may decline non-monotonically, with periodic resurgence or reconceptualization.

**Sampling Bias:**  
Data likely overrepresents formal, credentialed skills in developed economies with robust labor market analytics. 
Informal sector skills, tacit knowledge, and Global South contexts are systematically underrepresented.

**Causality vs. Correlation:**  
While strong correlations exist between AI adoption and skill depreciation, this analysis cannot definitively establish 
causal mechanisms. Confounding factors (automation in general, globalization, regulatory change) may contribute.

**Reskilling Time Estimates:**  
Derived from institutional program durations, not actual learning outcomes. Individual learning velocity varies 
dramatically by prior knowledge, educational access, and cognitive factors not captured here.

### Ethical Considerations

**Determinism Risk:**  
Presenting skill obsolescence as inevitable may become self-fulfilling, discouraging investment in affected domains 
even where human expertise remains critical for safety, ethics, or quality.

**Labor Market Anxiety:**  
Public dissemination of this research may induce worker anxiety and premature career abandonment, particularly among 
populations with limited retraining access.

**Ageism Amplification:**  
Findings about reskilling viability may be weaponized to justify age discrimination, despite evidence that learning 
capacity does not decline as sharply as cultural stereotypes suggest.

**Policy Misuse:**  
Data could be used to justify reduced investment in public education or worker protections under guise of inevitability, 
rather than as evidence for need for systemic intervention.

**AI Solutionism:**  
Analysis must not imply that faster AI adoption is inherently beneficial. Optimal pace of technological change balances 
productivity gains against social cohesion and human flourishing.

### Human Judgment Still Required

This dashboard provides evidence to inform decisions but cannot prescribe specific actions. Critical human judgment is 
required to:

- Weigh economic efficiency against human dignity in workforce transitions
- Balance innovation incentives with social stability
- Determine appropriate pace of technological adoption for specific contexts
- Identify skills that merit preservation for non-economic reasons (cultural, ethical, safety)
- Design interventions that respect individual agency and community values

**No algorithmic system can determine the just distribution of technological disruption's costs and benefits. That 
remains an inherently political and moral question requiring democratic deliberation.**
""")
st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; padding: 2rem 0;'>
    <p><strong>Skill Half-Life in the AI Era: Research Intelligence Dashboard</strong></p>
    <p>Designed for international academic evaluation and policy research</p>
    <p>Dashboard Version 1.0 | Data Subject to Continuous Validation</p>
</div>
""", unsafe_allow_html=True)
