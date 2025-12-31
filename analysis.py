# src/analysis.py - YOUR PRODUCTION CODE
import pandas as pd
from .risk_engine import get_risk_level, is_unsafe_day

def load_cpcb_data(file_path):
    """Load CPCB city_day.csv → clean 4 cities"""
    df = pd.read_csv(file_path)
    df_clean = df[df['City'].isin(['Delhi', 'Mumbai', 'Kolkata', 'Bengaluru'])].copy()
    df_clean['Date'] = pd.to_datetime(df_clean['Date'])
    df_clean['AQI'] = pd.to_numeric(df_clean['AQI'], errors='coerce')
    df_clean = df_clean.dropna(subset=['Date', 'AQI'])
    return df_clean[['City', 'Date', 'AQI']].rename(columns={'City': 'city', 'Date': 'date', 'AQI': 'aqi'})

def calculate_unsafe_days(df):
    """SIGNATURE: city/month/persona → unsafe_days"""
    df = df.copy()
    df['year_month'] = df['date'].dt.to_period('M')
    df['month'] = df['date'].dt.month_name()
    
    results = []
    for persona in ["children", "elderly", "outdoor_workers"]:
        persona_df = df.copy()
        persona_df['unsafe'] = df['aqi'].apply(lambda x: is_unsafe_day(x, persona))
        
        monthly_counts = (persona_df
            .groupby(['city', 'year_month', 'month'])['unsafe']
            .sum()
            .reset_index()
            .rename(columns={'unsafe': 'unsafe_days'})
        )
        monthly_counts['persona'] = persona
        results.append(monthly_counts)
    
    return pd.concat(results, ignore_index=True)
