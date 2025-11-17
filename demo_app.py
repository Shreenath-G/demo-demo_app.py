"""
KalyanAdStudio - Interactive Demo
A working demo to showcase the platform's capabilities to investors and customers.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import time

# Page configuration
st.set_page_config(
    page_title="KalyanAdStudio - AI-Powered Ad Optimization",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'demo_started' not in st.session_state:
    st.session_state.demo_started = False
if 'optimization_running' not in st.session_state:
    st.session_state.optimization_running = False
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/200x80/1f77b4/ffffff?text=KalyanAdStudio", use_column_width=True)
    st.markdown("---")
    
    demo_mode = st.radio(
        "Choose Demo Mode:",
        ["🎬 Interactive Demo", "📊 Live Dashboard", "🤖 AI Optimization", "📈 Results Comparison"]
    )
    
    st.markdown("---")
    st.markdown("### About This Demo")
    st.info("""
    This demo showcases how KalyanAdStudio's AI automatically optimizes your advertising campaigns.
    
    **Features:**
    - Real-time optimization
    - AI-powered insights
    - Multi-platform support
    - Automated A/B testing
    """)
    
    st.markdown("---")
    st.markdown("### Contact")
    st.markdown("📧 sales@kalyankart.com")
    st.markdown("🌐 kalyankart.com")

# Main content
if demo_mode == "🎬 Interactive Demo":
    st.markdown('<div class="main-header">🚀 KalyanAdStudio</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">AI-Powered Advertising Optimization Platform</div>', unsafe_allow_html=True)
    
    # Value proposition
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2>20-40%</h2>
            <p>Better ROI</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2>24/7</h2>
            <p>Automatic Optimization</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2>90%</h2>
            <p>Cost Savings</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive demo steps
    st.markdown("## 🎯 See How It Works")
    
    if not st.session_state.demo_started:
        if st.button("▶️ Start Interactive Demo", type="primary", use_container_width=True):
            st.session_state.demo_started = True
            st.session_state.current_step = 1
            st.rerun()
    
    if st.session_state.demo_started:
        # Step 1: Connect Ad Accounts
        if st.session_state.current_step >= 1:
            st.markdown("### Step 1: Connect Your Ad Accounts")
            st.markdown('<div class="info-box">Connect your Google Ads, Facebook, or LinkedIn accounts with one click (OAuth)</div>', unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("🔗 Connect Google Ads", use_container_width=True):
                    with st.spinner("Connecting to Google Ads..."):
                        time.sleep(1)
                    st.success("✅ Connected to Google Ads!")
            with col2:
                if st.button("🔗 Connect Facebook Ads", use_container_width=True):
                    with st.spinner("Connecting to Facebook..."):
                        time.sleep(1)
                    st.success("✅ Connected to Facebook Ads!")
            with col3:
                if st.button("🔗 Connect LinkedIn Ads", use_container_width=True):
                    with st.spinner("Connecting to LinkedIn..."):
                        time.sleep(1)
                    st.success("✅ Connected to LinkedIn Ads!")
            
            if st.button("Next Step →", key="step1_next"):
                st.session_state.current_step = 2
                st.rerun()
        
        # Step 2: Import Campaigns
        if st.session_state.current_step >= 2:
            st.markdown("---")
            st.markdown("### Step 2: Import Your Campaigns")
            
            # Simulated campaign data
            campaigns_df = pd.DataFrame({
                'Campaign': ['Summer Sale 2024', 'Brand Awareness Q1', 'Product Launch', 'Retargeting Campaign'],
                'Platform': ['Google Ads', 'Facebook', 'LinkedIn', 'Google Ads'],
                'Budget': ['$5,000/mo', '$3,000/mo', '$8,000/mo', '$2,000/mo'],
                'Status': ['Active', 'Active', 'Paused', 'Active'],
                'Current ROAS': [2.3, 1.8, 3.1, 2.7]
            })
            
            st.dataframe(campaigns_df, use_container_width=True)
            
            st.markdown('<div class="success-box">✅ Found 4 campaigns. Select campaigns to optimize:</div>', unsafe_allow_html=True)
            
            selected_campaigns = st.multiselect(
                "Select campaigns:",
                campaigns_df['Campaign'].tolist(),
                default=campaigns_df['Campaign'].tolist()[:2]
            )
            
            if st.button("Next Step →", key="step2_next"):
                st.session_state.current_step = 3
                st.rerun()
        
        # Step 3: Set Optimization Goals
        if st.session_state.current_step >= 3:
            st.markdown("---")
            st.markdown("### Step 3: Set Your Optimization Goals")
            
            col1, col2 = st.columns(2)
            with col1:
                goal = st.selectbox(
                    "Primary Goal:",
                    ["Maximize ROAS", "Minimize CPA", "Maximize Conversions", "Maximize Clicks"]
                )
            with col2:
                budget_strategy = st.selectbox(
                    "Budget Strategy:",
                    ["Optimize within budget", "Flexible budget (+20%)", "Aggressive growth"]
                )
            
            st.markdown('<div class="info-box">💡 Our AI will optimize your campaigns every hour based on these goals</div>', unsafe_allow_html=True)
            
            if st.button("🚀 Start AI Optimization", type="primary", use_container_width=True):
                st.session_state.current_step = 4
                st.session_state.optimization_running = True
                st.rerun()
        
        # Step 4: AI Optimization in Progress
        if st.session_state.current_step >= 4:
            st.markdown("---")
            st.markdown("### Step 4: AI Optimization in Progress")
            
            # Simulated optimization progress
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            steps = [
                "Analyzing campaign performance...",
                "Running reinforcement learning algorithms...",
                "Calculating optimal bid adjustments...",
                "Testing creative variations...",
                "Optimizing audience targeting...",
                "Applying changes to campaigns...",
                "Optimization complete! ✅"
            ]
            
            for i, step in enumerate(steps):
                status_text.text(step)
                progress_bar.progress((i + 1) / len(steps))
                time.sleep(0.5)
            
            st.markdown('<div class="success-box">✅ AI optimization complete! Your campaigns are now being optimized automatically every hour.</div>', unsafe_allow_html=True)
            
            if st.button("View Results →", key="view_results"):
                st.session_state.current_step = 5
                st.rerun()
        
        # Step 5: Results
        if st.session_state.current_step >= 5:
            st.markdown("---")
            st.markdown("### Step 5: See the Results")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("ROAS Improvement", "+32%", "↑ 0.74 points")
            with col2:
                st.metric("CPA Reduction", "-28%", "↓ $12.50")
            with col3:
                st.metric("Conversion Rate", "+24%", "↑ 1.8%")
            with col4:
                st.metric("Cost Savings", "$4,200", "↑ This month")
            
            # Performance chart
            dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
            before_optimization = np.random.normal(2.3, 0.3, 15)
            after_optimization = np.random.normal(3.0, 0.2, 15)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=dates[:15],
                y=before_optimization,
                name='Before AI',
                line=dict(color='#ff7f0e', width=2)
            ))
            fig.add_trace(go.Scatter(
                x=dates[15:],
                y=after_optimization,
                name='After AI',
                line=dict(color='#2ca02c', width=2)
            ))
            fig.add_shape(
                type="line",
                x0=dates[14], x1=dates[14],
                y0=0, y1=1,
                yref="paper",
                line=dict(color="gray", width=2, dash="dash")
            )
            fig.add_annotation(
                x=dates[14], y=1,
                yref="paper",
                text="AI Activated",
                showarrow=False,
                yshift=10
            )
            fig.update_layout(
                title="ROAS Over Time",
                xaxis_title="Date",
                yaxis_title="ROAS",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown('<div class="success-box">🎉 Congratulations! Your campaigns are now optimized by AI and will continue to improve over time.</div>', unsafe_allow_html=True)
            
            if st.button("🔄 Restart Demo"):
                st.session_state.demo_started = False
                st.session_state.current_step = 0
                st.rerun()

elif demo_mode == "📊 Live Dashboard":
    st.markdown("## 📊 Live Campaign Dashboard")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Spend", "$18,450", "+12% vs last month")
    with col2:
        st.metric("ROAS", "3.2x", "+32% with AI")
    with col3:
        st.metric("Conversions", "1,247", "+156 this week")
    with col4:
        st.metric("CPA", "$14.80", "-28% with AI")
    
    st.markdown("---")
    
    # Campaign performance table
    st.markdown("### Active Campaigns")
    campaigns_data = pd.DataFrame({
        'Campaign': ['Summer Sale 2024', 'Brand Awareness Q1', 'Product Launch', 'Retargeting Campaign'],
        'Platform': ['Google Ads', 'Facebook', 'LinkedIn', 'Google Ads'],
        'Spend': [5234, 3120, 7890, 2206],
        'Conversions': [428, 156, 634, 189],
        'ROAS': [3.4, 2.1, 4.2, 3.8],
        'AI Status': ['✅ Optimizing', '✅ Optimizing', '✅ Optimizing', '✅ Optimizing']
    })
    st.dataframe(campaigns_data, use_container_width=True)
    
    # Performance charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Spend by platform
        platform_spend = pd.DataFrame({
            'Platform': ['Google Ads', 'Facebook', 'LinkedIn'],
            'Spend': [7440, 3120, 7890]
        })
        fig = px.pie(platform_spend, values='Spend', names='Platform', title='Spend by Platform')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Daily conversions
        dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
        conversions = np.random.poisson(40, 30)
        fig = go.Figure()
        fig.add_trace(go.Bar(x=dates, y=conversions, name='Conversions'))
        fig.update_layout(title='Daily Conversions', xaxis_title='Date', yaxis_title='Conversions')
        st.plotly_chart(fig, use_container_width=True)

elif demo_mode == "🤖 AI Optimization":
    st.markdown("## 🤖 AI Optimization Engine")
    
    st.markdown("""
    ### How Our AI Works
    
    KalyanAdStudio uses advanced machine learning to optimize your campaigns:
    """)
    
    # AI components
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 1. Multi-Agent Reinforcement Learning
        - **Bidding Agent**: Optimizes bid amounts
        - **Creative Agent**: Tests ad variations
        - **Targeting Agent**: Refines audience
        - **Budget Agent**: Allocates budget
        
        Each agent learns from every campaign and gets smarter over time.
        """)
        
        st.markdown("""
        #### 2. Causal Inference
        - Understands WHY changes work
        - Predicts impact before applying
        - Avoids false correlations
        - Makes better decisions
        """)
    
    with col2:
        st.markdown("""
        #### 3. Quantum Optimization
        - Explores millions of strategies
        - Finds optimal solutions 100x faster
        - Handles complex constraints
        - Unique competitive advantage
        """)
        
        st.markdown("""
        #### 4. LLM Creative Generation
        - Generates ad copy variations
        - Tests hundreds of messages
        - Learns what resonates
        - Always-fresh creatives
        """)
    
    st.markdown("---")
    
    # Live optimization simulation
    st.markdown("### 🔴 Live Optimization Simulation")
    
    if st.button("▶️ Run Optimization Cycle"):
        progress = st.progress(0)
        status = st.empty()
        
        optimization_steps = [
            ("Fetching campaign data from Google Ads...", 0.1),
            ("Analyzing performance metrics...", 0.2),
            ("Running RL algorithms...", 0.4),
            ("Calculating optimal bids...", 0.6),
            ("Testing creative variations...", 0.7),
            ("Optimizing audience targeting...", 0.8),
            ("Applying changes via API...", 0.9),
            ("Optimization complete! ✅", 1.0)
        ]
        
        for step, prog in optimization_steps:
            status.text(step)
            progress.progress(prog)
            time.sleep(0.5)
        
        st.success("✅ Optimization cycle complete! Changes applied to 4 campaigns.")
        
        # Show what changed
        st.markdown("#### Changes Applied:")
        changes_df = pd.DataFrame({
            'Campaign': ['Summer Sale 2024', 'Brand Awareness Q1', 'Product Launch', 'Retargeting Campaign'],
            'Change': [
                'Bid increased 15% for high-converting keywords',
                'Paused 3 underperforming ad sets',
                'Expanded audience to similar demographics',
                'Adjusted bid schedule for peak hours'
            ],
            'Expected Impact': ['+12% ROAS', '-8% CPA', '+20% reach', '+15% conversions']
        })
        st.dataframe(changes_df, use_container_width=True)

elif demo_mode == "📈 Results Comparison":
    st.markdown("## 📈 Before vs After AI Optimization")
    
    # Comparison metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Before AI")
        st.metric("ROAS", "2.3x", delta=None)
        st.metric("CPA", "$20.50", delta=None)
        st.metric("Conversion Rate", "2.4%", delta=None)
        st.metric("Monthly Spend", "$18,000", delta=None)
    
    with col2:
        st.markdown("### After AI")
        st.metric("ROAS", "3.0x", "+32%")
        st.metric("CPA", "$14.80", "-28%")
        st.metric("Conversion Rate", "3.2%", "+24%")
        st.metric("Monthly Spend", "$18,000", "Same budget")
    
    st.markdown("---")
    
    # ROI calculation
    st.markdown("### 💰 ROI Calculation")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **Before AI:**
        - Monthly spend: $18,000
        - Revenue: $41,400 (2.3x ROAS)
        - Profit: $23,400
        """)
    with col2:
        st.markdown("""
        **After AI:**
        - Monthly spend: $18,000
        - Revenue: $54,000 (3.0x ROAS)
        - Profit: $36,000
        """)
    with col3:
        st.markdown("""
        **Improvement:**
        - Additional revenue: $12,600/mo
        - Additional profit: $12,600/mo
        - Annual impact: $151,200
        """)
    
    st.markdown('<div class="success-box">💡 With KalyanAdStudio at $299/month, you save $147,612 annually compared to hiring an $80K/year ad manager, while getting better results!</div>', unsafe_allow_html=True)
    
    # Performance over time
    st.markdown("### Performance Trend")
    dates = pd.date_range(start='2024-01-01', periods=60, freq='D')
    manual_roas = np.random.normal(2.3, 0.4, 30)
    ai_roas = np.concatenate([
        np.linspace(2.3, 3.0, 15),  # Ramp up
        np.random.normal(3.0, 0.2, 15)  # Stable
    ])
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates[:30],
        y=manual_roas,
        name='Manual Optimization',
        line=dict(color='#ff7f0e', width=2),
        fill='tozeroy'
    ))
    fig.add_trace(go.Scatter(
        x=dates[30:],
        y=ai_roas,
        name='AI Optimization',
        line=dict(color='#2ca02c', width=2),
        fill='tozeroy'
    ))
    fig.add_shape(
        type="line",
        x0=dates[29], x1=dates[29],
        y0=0, y1=1,
        yref="paper",
        line=dict(color="gray", width=2, dash="dash")
    )
    fig.add_annotation(
        x=dates[29], y=1,
        yref="paper",
        text="AI Activated",
        showarrow=False,
        yshift=10
    )
    fig.update_layout(
        title="ROAS Improvement Over Time",
        xaxis_title="Date",
        yaxis_title="ROAS",
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>KalyanAdStudio</strong> - AI-Powered Advertising Optimization</p>
    <p>📧 saleso@kalyankart.com | 🌐 kalyankart.com | 📱 Schedule a demo</p>
    <p style='font-size: 0.8rem;'>This is a demonstration. Actual results may vary.</p>
</div>
""", unsafe_allow_html=True)
