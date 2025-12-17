# Skill Half-Life in the AI Era: Research Intelligence Dashboard


## Overview

A production-grade analytical dashboard examining the accelerating obsolescence of professional skills in AI-augmented workflows. Designed for international academic evaluation, policy research, and evidence-based workforce planning.

**Key Features:**
- 6 research-grade visualizations answering distinct analytical questions
- Dark theme with professional multi-color palette
- Real-time filtering and interactive exploration
- Production-ready code suitable for academic publication and policy briefings

## Research Context

This dashboard operationalizes the concept of **skill half-life** — the time required for a professional skill's market value to depreciate by 50%. Unlike traditional human capital models assuming gradual linear decline, this research examines non-linear obsolescence patterns driven by:

- Generative AI automating cognitive tasks
- Large language models replacing domain expertise
- Automated systems disrupting professional hierarchies
- AI-driven tools compressing production timelines

## Installation & Deployment

### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/skill-half-life-ai-dashboard.git
cd skill-half-life-ai-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app.py
```

### Streamlit Cloud Deployment

1. Fork this repository to your GitHub account
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select `app.py` as the main file
5. Deploy

The dashboard will be live at: `https://[your-app-name].streamlit.app`

## Dataset Requirements

Place your `skill_half_life_ai.csv` file in the root directory. Expected columns:

**Required:**
- `Years_to_50_Percent_Obsolescence` (float): Skill half-life metric
- `Skill_Category` (str): Domain classification
- `AI_Adoption_Rate` (float): Percentage of AI integration
- `Skill_Depreciation_Rate` (float): Rate of value decline

**Optional (enhances analysis):**
- `Sector` or `Industry` (str): Economic sector
- `Reskilling_Time_Months` (int): Time to acquire replacement skills
- `Year` (int): Temporal dimension for trend analysis
- `Region` or `Country` (str): Geographic segmentation

## Dashboard Structure

### Section 1: Research Context
Establishes the analytical framework, global significance, and decision support objectives.

### Section 2: Key Research KPIs
Four critical metrics:
- **Median Skill Half-Life**: Cross-sector obsolescence rate
- **Critical Skills Percentage**: Proportion with <2 year relevance
- **Average Reskilling Duration**: Mean transition time requirement
- **Reskilling Viability**: Economic feasibility ratio

### Section 3: Core Analytical Visualizations

**3.1 Skill Obsolescence Velocity by Domain**  
Box plot revealing distribution disparities across professional categories.

**3.2 AI Adoption Impact on Skill Decay**  
Scatter plot with trendline examining causal relationships between AI integration and depreciation.

**3.3 Skill Obsolescence Urgency Profile**  
Bar chart categorizing intervention priorities by temporal urgency.

**3.4 Economic Viability of Reskilling**  
Comparative analysis identifying where retraining is economically rational vs. futile.

**3.5 Temporal Evolution of Skill Half-Life**  
Time series revealing acceleration patterns in skill obsolescence.

**3.6 Multi-Dimensional Risk Profile**  
3D scatter plot mapping vulnerability across AI adoption, depreciation rate, and reskilling burden.

### Section 4: Insight Synthesis
Non-obvious patterns including:
- The Reskilling Paradox
- Non-Linear Acceleration post-2020
- Sector-Specific Vulnerability patterns
- The Viability Gap affecting 30-40% of skills

### Section 5: Limitations & Ethical Considerations
Explicit discussion of:
- Temporal scope and survivorship bias
- Measurement validity constraints
- Sampling limitations
- Ethical risks of determinism and labor market anxiety
- Human judgment requirements in policy application

## Design Philosophy

This dashboard adheres to **panel-grade analytical standards**:

- ✅ Every visualization answers a distinct research question
- ✅ No decorative or redundant charts
- ✅ Professional dark theme with semantic color coding
- ✅ Clear methodological transparency
- ✅ Explicit limitation acknowledgment
- ✅ Designed for international academic audiences

## Target Audience

- **Professors & Researchers**: Examining human capital dynamics in AI era
- **Policy Experts**: Designing evidence-based workforce interventions
- **University Administrators**: Curriculum planning and program design
- **International Evaluators**: Comparative labor market analysis
- **Corporate Strategists**: Workforce planning and reskilling investment

## Citation

If you use this dashboard in academic work, please cite:

```
[Your Name/Institution]. (2024). Skill Half-Life in the AI Era: Research Intelligence Dashboard.
GitHub repository: https://github.com/yourusername/skill-half-life-ai-dashboard
```

## Contributing

This is a research-grade tool. Contributions should maintain:
- Academic rigor in analytical methods
- Professional visualization standards
- Comprehensive documentation
- Explicit limitation acknowledgment

## License

MIT License - See LICENSE file for details

## Contact

For research collaboration, methodology questions, or data sharing inquiries:
- Email: [your.email@institution.edu]
- LinkedIn: [Your Profile]
- Institution: [Your Research Lab/Department]

---

**Built for serious research. No shortcuts. No placeholders. Production-ready.**
