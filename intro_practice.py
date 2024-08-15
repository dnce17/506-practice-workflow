import pandas as pd
import numpy as np

season = "Summer"
month = 8
seasonal_fruits = ["Watermelon", "Honeydew Melon", "Berries"]

patient_info = {
    "name": "Bobby Lin",
    "age": 34,
    "birth_date": "1990-01-01", 
    "allergies": ["dust mites", "pollen", "nuts"],
    "past_appt": {
        "dust mites": "mild",
        "pollen": "moderate",
        "nuts": "severe",
    }
}

def temperature_converter(temp_val, desired_scale):
    # Convert to F if scale is C and vice versa
    if desired_scale == "C":
        converted_temp = (float(temp_val) - 32) / (9/5)
    else:
        converted_temp = float(temp_val) * (9/5) + 32
    
    return f"{round(converted_temp, 1)} {desired_scale}"

print(season)
print(month)
print(seasonal_fruits)
print(patient_info)

converted_temp = temperature_converter(40, 'F')
print(f"The converted temperature is {converted_temp}")

