import os
import google.generativeai as genai
import streamlit as st

# Configure the API key
genai.configure(api_key='AIzaSyDCDYwWt-5rVtQvvZkqMIH_-HL_pg7_b1E')

# Create the model configuration
generation_config = {
    "temperature": 0.7,  # Lowered temperature for more focused and fact-based responses
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 1024,  # Adjusted for more relevant output length
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Initialize or get chat session history
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit UI
st.title("Exoplanet Explorer Chatbot")

# Introduction for users
st.write("Welcome to the Exoplanet Explorer Chatbot! Feel free to ask questions about exoplanets, "
         "such as their characteristics, discovery methods, potential for life, and recent research findings.")

# User input
user_input = st.text_input("Enter your exoplanet-related question:", key="input")

# Handle input and send message
if st.button("Send"):
    if user_input:
        # Structured prompt to focus on exoplanets
        structured_prompt = (
            "You are an astrophysics expert specializing in exoplanets. Provide informative, "
            "detailed, and scientifically accurate answers to questions about exoplanets, including topics like:\n"
            "- Methods of detecting exoplanets (e.g., radial velocity, transit method)\n"
            "- Characteristics of known exoplanets (e.g., size, atmosphere, temperature)\n"
            "- Potential habitability of exoplanets and recent discoveries\n"
            "- Differences between exoplanet types (e.g., gas giants, super-Earths, terrestrial planets)\n\n"
            f"User's question: {user_input}\n"
            "Your answer should be educational, clear, and concise."
        )

        # Add user message to the session state
        st.session_state.messages.append({"user": "user", "text": user_input})

        # Send the structured prompt to the model and get a response
        response = st.session_state.chat_session.send_message(structured_prompt)

        # Add bot response to the session state
        st.session_state.messages.append({"user": "bot", "text": response.text})

# Display previous messages
for message in st.session_state.messages:
    if message["user"] == "user":
        st.write(f"**You:** {message['text']}")
    else:
        st.write(f"**Bot:** {message['text']}")
