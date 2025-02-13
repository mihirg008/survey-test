import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("path/to/your/firebase-key.json")  # Replace with your Firebase key path
    firebase_admin.initialize_app(cred)
db = firestore.client()

# Title and Introduction
st.title("The Ultimate Gamer Survey 🎮🔥")
st.write("Hey there, legend! 👾 Answer honestly, and we promise no lag, just pure insights. Let’s roll! 🚀")

# Collect User Input
form = {}
form["ign"] = st.text_input("What’s your IGN (In-Game Name)? (Optional)")
form["age"] = st.selectbox("How old are you?", ["Under 18", "18-24", "25-34", "35+"])
form["gender"] = st.radio("What’s your power level (gender)?", ["Male", "Female", "Non-binary", "Prefer not to say"])
form["city"] = st.text_input("Where do you respawn IRL? (City/State)")
form["occupation"] = st.text_input("What do you do when you’re not gaming? (Occupation/Student/Other)")
form["gamingYears"] = st.selectbox("When did you first start gaming?", ["Less than a year ago", "1-3 years ago", "3-5 years ago", "More than 5 years ago"])
form["firstGame"] = st.text_area("What was the first video game that made you fall in love with gaming?")
form["balanceLife"] = st.text_area("How do you balance gaming with other aspects of your life?")

# Platforms Selection
form["platforms"] = st.multiselect("Which platform(s) do you play on?", ["Mobile", "PC", "Console"])

# Submit Button
if st.button("Submit Survey"):
    try:
        db.collection("gamer-survey").add(form)
        st.success("Survey submitted successfully! GGWP! 🎉")
    except Exception as e:
        st.error(f"Error submitting survey: {e}")

# Instructions to Set Up Streamlit + Firebase
st.sidebar.header("Setup Instructions")
st.sidebar.markdown("""
### Steps to Run This Survey:

1. Install dependencies:  
   ```sh
   pip install streamlit firebase-admin
   ```
2. Set up Firebase Firestore:  
   - Go to [Firebase Console](https://console.firebase.google.com/)
   - Create a Firestore database
   - Generate a service account key (JSON) and replace `path/to/your/firebase-key.json` in the code.
3. Run Streamlit app:  
   ```sh
   streamlit run your_script.py
   ```

Your survey is now live! 🚀
""")
