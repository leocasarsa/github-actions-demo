import streamlit as st

# Set the app title
st.title("GitHub Actions")
# Add a welcome message
st.write("Demo app!")
# Create a text input
user_input = st.text_input("Enter a custom message:", "CI/CD")
# Display the customized message
st.write("Customized Message:", user_input)
