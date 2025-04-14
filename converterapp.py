import streamlit as st

# Conversion logic
def convert_length(value, from_unit, to_unit):
    factors = {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    factors = {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15)
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15)
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32)

# Streamlit UI
st.title("🔁 Unit Converter App")

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

if category == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter Value", format="%.4f")
    result = convert_length(value, from_unit, to_unit)
elif category == "Weight":
    units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter Value", format="%.4f")
    result = convert_weight(value, from_unit, to_unit)
else:  # Temperature
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter Value", format="%.2f")
    result = convert_temperature(value, from_unit, to_unit)

st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
