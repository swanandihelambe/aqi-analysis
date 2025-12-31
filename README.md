# 🛡️ Human-Centric AQI Health Risk Intelligence System

From **AQI Numbers → Human Health Risk → Actionable Insights**
![Hero Image](dashboard.png)
---

## 📌 Overview

Most air-quality dashboards stop at showing AQI values.  
This project goes further by converting AQI data into **human health risk intelligence**.

It forecasts air quality for major Indian cities and translates predictions into **persona-specific risk insights** for **children, elderly citizens, and outdoor workers**, using a simple but powerful concept: **Unsafe Air Days**.

The goal is not just prediction — but **interpretability, impact, and decision support**.

---

### This project focuses on interpretable data science and human-centric risk modeling, and is designed to scale to real-time AQI and policy-level decision systems.

---

## 🚀 Features

- 🏙️ City-wise AQI analysis for major Indian metros  
- 🧍 Persona-based health risk modeling  
  - Children  
  - Elderly  
  - Outdoor Workers  
- ⚠️ **Unsafe Air Days** metric *(signature feature)*  
- 🔮 Time-series forecasting  
  - Prophet (selected model)  
  - ARIMA (baseline comparison)  
- 📊 Interactive Streamlit dashboard  
- 📈 Monthly & seasonal pollution trend analysis  

---

## 🛠 Tech Stack

- 🐍 **Python**
- 📊 **Pandas, NumPy**
- 📈 **Matplotlib, Seaborn, Plotly**
- 🔮 **Prophet, Statsmodels (ARIMA)**
- 🎛 **Streamlit**
- 💾 **CPCB Air Quality Data**

---

## 📈 Outcome

- Identified city-wise pollution severity using unsafe-day counts  
- Forecasted AQI and health risk trends for upcoming periods  
- Highlighted vulnerable population exposure across cities  
- Transformed raw AQI data into **clear, human-centric insights**

---
## 🚀 Live Dashboard Features

### 🔥 Tab 1: Risk Intelligence

- City selector: Delhi / Mumbai / Kolkata / Bengaluru  
- Persona selector: Children / Elderly / Outdoor Workers  
- Heatmap of unsafe days per month  
- Multi-city trend comparison  
- Live risk metrics table  

---

### 🔮 Tab 2: Forecasting & Prediction

- 90-day AQI forecast using Prophet  
- Next 30-day risk table by persona  
- Real-time unsafe day counts  
- AQI confidence intervals  

**Run the dashboard locally:**
```bash
streamlit run streamlit_app.py


