# HealthKart

 📊 Influencer Campaign ROI Dashboard

This is an open-source Streamlit dashboard that tracks and visualizes the **ROI of influencer marketing campaigns** across platforms like Instagram, YouTube, and Twitter. It is designed to help HealthKart (or any brand) evaluate campaign performance, influencer efficiency, and payout effectiveness in real time.



 🧠 Key Features

- 📂 Upload influencer, post, tracking, and payout data
- 📈 Track ROAS (Return on Ad Spend) and revenue vs. payout
- 🧍 Filter by platform, gender, and category
- 💡 Identify top influencers and poor ROAS performers
- 📤 Export filtered performance data as CSV



 🗂️ Data Model (CSV Schema)

You’ll need 4 CSV files with the following structures:

 1. `influencers.csv`

| Column         | Type   | Description                          |
|----------------|--------|--------------------------------------|
| influencer_id  | int    | Unique ID for each influencer        |
| name           | string | Influencer’s full name               |
| category       | string | Niche/genre (e.g., fitness, beauty)  |
| gender         | string | Male/Female/Other                    |
| follower_count | int    | Number of followers                  |
| platform       | string | Instagram, YouTube, Twitter, etc.    |



 2. `posts.csv`

| Column        | Type   | Description                          |
|---------------|--------|--------------------------------------|
| influencer_id | int    | Links to influencer                  |
| platform      | string | Where the post was made              |
| date          | date   | Post date                            |
| URL           | string | Link to post                         |
| caption       | string | Post caption                         |
| reach         | int    | People reached                       |
| likes         | int    | Number of likes                      |
| comments      | int    | Number of comments                   |



3. `tracking_data.csv`

| Column        | Type   | Description                          |
|---------------|--------|--------------------------------------|
| source        | string | Source of traffic                    |
| campaign      | string | Campaign name                        |
| influencer_id | int    | Linked influencer                    |
| user_id       | int    | Buyer ID                             |
| product       | string | Product name                         |
| date          | date   | Order date                           |
| orders        | int    | Order count                          |
| revenue       | float  | Total revenue from orders            |



 4. `payouts.csv`

| Column        | Type   | Description                          |
|---------------|--------|--------------------------------------|
| influencer_id | int    | Linked influencer                    |
| basis         | string | post or order                        |
| rate          | float  | Payout per post or per order         |
| orders        | int    | Total orders (if per-order basis)    |
| total_payout  | float  | Total payout to influencer           |



🚀 How to Run It Locally

 🔧 Prerequisites

- Python 3.8+
- `pip` installed
- Recommended: VS Code or Jupyter



 📦 Install Required Packages

Run this in your terminal:

```bash
pip install streamlit pandas
```



 ▶️ Launch the Dashboard

```bash
streamlit run dashboard.py
```

This will open the dashboard in your default browser.



🧠 Assumptions

- ROAS = `Revenue / Total Payout` (assumes all revenue is directly attributable)
- Tracking data is pre-aggregated by influencer & product
- All 4 CSV files must be uploaded to run the dashboard


 📌 Screenshots

> ![Main Dashboard](assets/dashboard_home.png)
> !


 📤 Exportable Outputs

- Download filtered influencer performance CSV
- (Optional) Export insights as PDF



 📈 Sample Insights (from mock data)

- **Top ROAS Influencer**: Aarti Yadav on Instagram with ROAS of 7.3x  
- **Best Platform**: YouTube has average ROAS of 5.4x  
- **Category Trends**: Fitness > Lifestyle > Parenting  
- **High Payout, Low ROI Influencers**: Flag for review



 🛠️ Future Improvements

- Add incrementality model support
- Visualize time-based trends (e.g., ROAS over weeks)
- Compare campaigns by product or brand
- Automate CSV ingestion from Google Sheets



 🤝 License

This project is open-source and free to use under the MIT license.



 🙌 Author

Built by [Tejasri Nagireddi] — feel free to fork, contribute, or reuse.
