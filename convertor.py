import streamlit as st

def length_converter(value, from_unit, to_unit):
    length_units = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    }
    
    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Invalid length unit")
    
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "kilogram": 1,
        "gram": 0.001,
        "milligram": 0.000001,
        "pound": 0.453592,
        "ounce": 0.0283495
    }
    
    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("Invalid weight unit")
    
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    
    raise ValueError("Invalid temperature unit")

st.title("Unit Converter")

option = st.selectbox(
    "Select conversion type",
    ("Length", "Weight", "Temperature")
)

value = st.number_input("Enter value to convert")

if option == "Length":
    from_unit = st.selectbox("From unit", ("meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"))
    to_unit = st.selectbox("To unit", ("meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"))
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

elif option == "Weight":
    from_unit = st.selectbox("From unit", ("kilogram", "gram", "milligram", "pound", "ounce"))
    to_unit = st.selectbox("To unit", ("kilogram", "gram", "milligram", "pound", "ounce"))
    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

elif option == "Temperature":
    from_unit = st.selectbox("From unit", ("celsius", "fahrenheit", "kelvin"))
    to_unit = st.selectbox("To unit", ("celsius", "fahrenheit", "kelvin"))
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")