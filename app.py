import sys
import os

# allow dashboard to import backend modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

from backend.scraper import scrape_top10
from backend.preprocessing import preprocess
from backend.volatility_model import compute_garch_volatility
from backend.regime_model import compute_regime_switching
from backend.volatility_explosion import detect_volatility_spikes
from backend.risk_heatmap import compute_risk_heatmap
from backend.ai_risk_agent import generate_risk_insight


# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="Crypto Risk Dashboard",
    layout="wide"
)

st.title("📊 Cryptocurrency Risk Monitoring Dashboard")
st.write("AI-driven volatility and regime-switching analysis")

st.divider()

# -----------------------------
# Update Data
# -----------------------------

st.subheader("🔄 Fetch Latest Market Data")

if st.button("Update Market Data"):
    scrape_top10()
    st.success("Market data updated successfully")

# -----------------------------
# Load Data
# -----------------------------

df = preprocess()

st.subheader("📁 Dataset Preview")
st.dataframe(df.tail(20))

# -----------------------------
# Coin Selection
# -----------------------------

coin_list = df["Coin"].unique()

selected_coin = st.selectbox(
    "Select Cryptocurrency",
    coin_list
)

coin_df = df[df["Coin"] == selected_coin]

# -----------------------------
# Current Risk Indicator
# -----------------------------

st.subheader("⚠ Market Risk Indicator")

latest_volatility = coin_df["Volatility"].dropna().iloc[-1]

if latest_volatility > 0.05:
    risk_level = "HIGH"
elif latest_volatility > 0.02:
    risk_level = "MEDIUM"
else:
    risk_level = "LOW"

col1, col2 = st.columns(2)

with col1:
    st.metric("Current Volatility", round(latest_volatility,5))

with col2:
    st.metric("Risk Level", risk_level)

# -----------------------------
# Price Trend
# -----------------------------

st.subheader("📈 Price Trend")

fig_price = px.line(
    coin_df,
    x="Date",
    y="Price",
    title=f"{selected_coin} Price Movement"
)

st.plotly_chart(fig_price, use_container_width=True)

# -----------------------------
# Rolling Volatility
# -----------------------------

st.subheader("📉 Rolling Volatility")

fig_vol = px.line(
    coin_df,
    x="Date",
    y="Volatility",
    title=f"{selected_coin} Rolling Volatility"
)

st.plotly_chart(fig_vol, use_container_width=True)

# -----------------------------
# GARCH Volatility Model
# -----------------------------

st.subheader("⚡ GARCH Volatility Model")

garch_df = compute_garch_volatility(df, selected_coin)

fig_garch = px.line(
    garch_df,
    x="Date",
    y="GARCH_volatility",
    title="GARCH Conditional Volatility"
)

st.plotly_chart(fig_garch, use_container_width=True)

# -----------------------------
# Regime Switching Model
# -----------------------------

st.subheader("🔄 Markov Regime Switching")

regime_df = compute_regime_switching(df, selected_coin)

fig_regime = px.line(
    regime_df,
    x="Date",
    y="Regime",
    title="Regime Probability (High Volatility State)"
)

st.plotly_chart(fig_regime, use_container_width=True)

# -----------------------------
# Volatility Explosion
# -----------------------------

st.subheader("💥 Volatility Explosion Detection")

explosion_df = detect_volatility_spikes(df)

spikes = explosion_df[explosion_df["Volatility_Explosion"] == True]

st.write("Recent extreme volatility events:")

st.dataframe(spikes.tail(10))

# -----------------------------
# Risk Heatmap
# -----------------------------

st.subheader("🔥 Top 10 Crypto Risk Heatmap")

risk_table = compute_risk_heatmap(df)

fig, ax = plt.subplots()

heatmap_data = risk_table.pivot_table(
    values="RiskScore",
    index="Coin"
)

sns.heatmap(
    heatmap_data,
    annot=True,
    cmap="Reds",
    ax=ax
)

st.pyplot(fig)

# -----------------------------
# AI Risk Insight
# -----------------------------

st.subheader("🤖 AI Market Risk Insight")

latest_regime = regime_df["Regime"].iloc[-1]

insight = generate_risk_insight(
    latest_volatility,
    latest_regime
)

st.success(insight)

st.divider()

st.write("Built for Cryptocurrency Risk & Volatility Analytics Project")