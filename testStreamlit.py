import streamlit as st

# Define a simple chatbot logic
def chatbot_response(user_input):
    if user_input.lower() == "hello":
        return "Hi there! How can I help you today?"
    elif user_input.lower() == "how are you?":
        return "I'm just a computer program, so I don't have feelings, but thanks for asking!"
    elif user_input.lower() in ["goodbye", "see you later"]:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase your question?"

# Streamlit app
st.title("Simple Chatbot")

# User input field
user_input = st.text_input("You:", value="", key="user_input")

# Button to submit user input
if st.button('Send'):
    if user_input:
        response = chatbot_response(user_input)
        st.write(f"Bot: {response}")

# Add some initial instructions
st.write("Type your question below and click 'Send' to get a response.")