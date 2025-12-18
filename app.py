import streamlit as st
import pandas as pd

# Load emission factors
df = pd.read_csv("emission_factors.csv")
factors = dict(zip(df.activity, df.co2_factor))

st.title("🌱 AI Carbon Footprint Calculator")

st.write("Calculate your monthly carbon footprint")

electricity = st.number_input("Electricity usage (kWh/month)", 0)
petrol = st.number_input("Petrol used (litres/month)", 0)
lpg = st.number_input("LPG cylinders used/month", 0)
bus = st.number_input("Bus travel (km/month)", 0)

total_co2 = (
    electricity * factors["electricity_kwh"] +
    petrol * factors["petrol_litre"] +
    lpg * factors["lpg_cylinder"] +
    bus * factors["bus_km"]
)

st.subheader("🌍 Total Carbon Footprint")
st.success(f"{total_co2:.2f} kg CO₂ per month")

st.subheader("🤖 AI Sustainability Tips")

if total_co2 > 300:
    st.warning("High carbon footprint detected!")
    st.write("""
    • Use LED lights  
    • Reduce private vehicle usage  
    • Switch to renewable energy  
    • Use public transport  
    """)
else:
    st.success("Good job! Your footprint is moderate.")
