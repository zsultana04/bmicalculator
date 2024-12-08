import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height / 100) ** 2
    return round(bmi, 2)

# Function to interpret BMI
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Streamlit app layout
def main():
    st.title("BMI Calculator-by Zinnat")
    st.write("""
    This app calculates your **Body Mass Index (BMI)** based on your weight and height.
    """)

    # User input for weight and height
    weight = st.number_input("Enter your weight (in kg):", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
    height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=250.0, value=170.0, step=0.1)

    # Button to calculate BMI
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"### Your BMI: **{bmi}**")
        
        # Interpretation of BMI
        interpretation = interpret_bmi(bmi)
        st.write(f"### Interpretation: **{interpretation}**")
        
        # Provide visual feedback
        if interpretation == "Underweight":
            st.warning("You are underweight. Consider consulting a healthcare provider for guidance. 🥗")
        elif interpretation == "Normal weight":
            st.success("You have a normal weight. Keep up the healthy lifestyle! 🌟")
        elif interpretation == "Overweight":
            st.warning("You are overweight. Consider adopting healthier habits. 🏃‍♂️")
        else:
            st.error("You are in the obesity range. Consult a healthcare provider for personalized advice. 🩺")

# Run the app
if __name__ == "__main__":
    main()
