import streamlit as st # type: ignore
import dialogue as d
from tkinter import PhotoImage
import Data as data






































# Title and Description
st.title("Vexora - Your Digital Healthcare Assistant")
st.write("Enter your symptoms below to get initial diagnosis suggestions and health advice.")

# Input Section
symptoms = st.text_input("Describe your symptoms (e.g., fever, headache, fatigue):")

# Process Symptoms
if st.button("Get Diagnosis"):
    if symptoms:
        # Placeholder logic
        st.write(f"Analyzing symptoms: {symptoms}")
        # Example Output
        st.success("Suggested diagnosis: Common Cold")
        st.info("Advice: Rest, stay hydrated, and monitor your symptoms.")
    else:
        st.warning("Please enter your symptoms to proceed.")

# Footer
st.write("---")
st.write("**Disclaimer:** This tool does not replace professional medical advice.")

















