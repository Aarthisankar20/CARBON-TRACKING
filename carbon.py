
import streamlit as st
import matplotlib.pyplot as plt

st.title("🌍 Individual Carbon Footprint Dashboard")

# Input widgets
electricity = st.number_input("Monthly Electricity Usage (kWh)", min_value=0.0, value=120.0)
lpg = st.number_input("Monthly LPG Usage (kg)", min_value=0.0, value=15.0)
petrol = st.number_input("Monthly Petrol/Diesel Usage (liters)", min_value=0.0, value=25.0)
public_transport = st.number_input("Monthly Public Transport Usage (km)", min_value=0.0, value=100.0)
flights = st.number_input("One-way Flights per Year", min_value=0.0, value=2.0)
non_veg_meals = st.number_input("Non-Veg Meals per Week", min_value=0.0, value=5.0)
plastic_waste = st.number_input("Plastic Waste per Month (kg)", min_value=0.0, value=3.0)

# Emission factors
emission_factors = {
    "Electricity": 0.82,
    "LPG": 2.98,
    "Petrol/Diesel": 2.31,
    "Public Transport": 0.1,
    "Flights": 250 / 12,
    "Non-Veg Meals": 2.5 * 4.33,
    "Plastic Waste": 6
}

# Calculate emissions
emissions = {
    "Electricity": electricity * emission_factors["Electricity"],
    "LPG": lpg * emission_factors["LPG"],
    "Petrol/Diesel": petrol * emission_factors["Petrol/Diesel"],
    "Public Transport": public_transport * emission_factors["Public Transport"],
    "Flights": flights * emission_factors["Flights"],
    "Non-Veg Meals": non_veg_meals * emission_factors["Non-Veg Meals"],
    "Plastic Waste": plastic_waste * emission_factors["Plastic Waste"]
}

total_emission = sum(emissions.values())
annual_emission = total_emission * 12

benchmark_monthly = 83

# Display results
st.subheader("Monthly Carbon Footprint (kg CO₂e)")
for category, value in emissions.items():
    st.write(f"**{category}:** {value:.2f} kg CO₂e")

st.markdown(f"### Total Monthly Carbon Footprint: {total_emission:.2f} kg CO₂e")
st.markdown(f"### Estimated Annual Carbon Footprint: {annual_emission:.2f} kg CO₂e")

if total_emission > benchmark_monthly:
    st.error("⚠️ Your monthly carbon footprint is ABOVE the average benchmark for India.")
else:
    st.success("✅ Your monthly carbon footprint is within the average range. Good job!")

# Plotting with matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10,6))
categories = list(emissions.keys())
values = list(emissions.values())
bars = ax.bar(categories, values, color='skyblue')
ax.axhline(benchmark_monthly, color='red', linestyle='--', label='Average Indian Monthly Footprint (83 kg)')
ax.set_ylabel('Carbon Emission (kg CO₂e)')
ax.set_title('Individual Monthly Carbon Footprint Breakdown')
ax.legend()
plt.xticks(rotation=45)

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

st.pyplot(fig)

