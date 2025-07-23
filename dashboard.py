



import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Influencer ROI Dashboard", layout="wide")
st.title("📊 Influencer Campaign ROI Dashboard")

# Upload section
st.sidebar.header("📂 Upload CSV Files")
inf_file = st.sidebar.file_uploader("Upload influencers.csv", type="csv")
post_file = st.sidebar.file_uploader("Upload posts.csv", type="csv")
track_file = st.sidebar.file_uploader("Upload tracking_data.csv", type="csv")
payout_file = st.sidebar.file_uploader("Upload payouts.csv", type="csv")

# Load and process data
if all([inf_file, post_file, track_file, payout_file]):
    # Read CSVs
    influencers = pd.read_csv(inf_file)
    posts = pd.read_csv(post_file)
    tracking = pd.read_csv(track_file)
    payouts = pd.read_csv(payout_file)

    # Merge datasets
    df = tracking.merge(payouts, on="influencer_id", how="left")
    df = df.merge(influencers, on="influencer_id", how="left")

    # Calculate ROAS
    df["ROAS"] = df["revenue"] / df["total_payout"]

    # Sidebar filters
    st.sidebar.header("🔍 Filter")
    platform_filter = st.sidebar.multiselect("Platform", df["platform"].unique(), default=list(df["platform"].unique()))
    gender_filter = st.sidebar.multiselect("Gender", df["gender"].unique(), default=list(df["gender"].unique()))
    category_filter = st.sidebar.multiselect("Category", df["category"].unique(), default=list(df["category"].unique()))

    filtered = df[
        (df["platform"].isin(platform_filter)) &
        (df["gender"].isin(gender_filter)) &
        (df["category"].isin(category_filter))
    ]

    # KPIs
    st.subheader("📈 Campaign Performance Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"₹{filtered['revenue'].sum():,.0f}")
    col2.metric("Total Payout", f"₹{filtered['total_payout'].sum():,.0f}")
    col3.metric("Average ROAS", f"{filtered['ROAS'].mean():.2f}x")

    # Influencer Table
    st.subheader("📋 Influencer Performance Table")
    perf_cols = ["influencer_id", "name", "platform", "category", "gender", "revenue", "total_payout", "ROAS"]
    st.dataframe(filtered[perf_cols].sort_values("ROAS", ascending=False), use_container_width=True)

    # ROAS Chart
    st.subheader("🏆 Top 10 Influencers by ROAS")
    top10 = filtered.sort_values("ROAS", ascending=False).head(10)
    st.bar_chart(top10.set_index("name")["ROAS"])

    # Export
    st.subheader("📤 Export")
    csv = filtered[perf_cols].to_csv(index=False).encode('utf-8')
    st.download_button("Download Performance CSV", data=csv, file_name="influencer_performance.csv", mime="text/csv")

else:
    st.warning("👈 Please upload all 4 required CSV files to see the dashboard.")
