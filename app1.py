import streamlit as st
import google.generativeai as genai

# 🔑 Configure Gemini API
genai.configure(api_key="AIzaSyCvS2kPyLYyKQYuhJalrpFZsJmJyldqcGo")  # <-- Replace with your key
model = genai.GenerativeModel("gemini-1.5-flash")

# 💡 Streamlit UI
st.set_page_config(page_title="Child Nutrition AI Agent", page_icon="🍽️")
st.title("🍽️ Food Recommendation Agent for Malnourished Children")

# 📥 Input Form
with st.form("nutrition_form"):
    name = st.text_input("Child's Name", value="")
    age = st.slider("Age (in years)", 1, 10, 3)
    weight = st.number_input("Weight (in kg)", min_value=5.0, max_value=30.0, value=10.0)
    location = st.text_input("Location (State/Region)", value="")
    health_issue = st.selectbox("Health Issue", ["Underweight", "Stunted", "Normal"])
    local_foods = st.text_area("Available Local Foods (comma-separated)", 
                               value="")
    submitted = st.form_submit_button("Get Nutrition Plan")

# 🤖 Call Gemini on Submit
if submitted:
    with st.spinner("Generating personalized food plan..."):
        prompt = f"""
        You are a child nutrition expert. Recommend a daily meal plan for a malnourished child.

        Child Info:
        - Name: {name}
        - Age: {age} years
        - Weight: {weight} kg
        - Location: {location}
        - Health issue: {health_issue}
        - Available foods: {local_foods}

        Give:
        1. Meal plan (Breakfast, Lunch, Snack, Dinner)
        2. Simple nutrition tips for caregiver
        3. Why these foods are helpful
        """
        try:
            response = model.generate_content(prompt)
            st.success("✅ Nutrition Plan Generated!")
            st.markdown("### 🍽️ Personalized Meal Plan")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error generating content: {e}")
