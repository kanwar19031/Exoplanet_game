import streamlit as st
from groq import Groq
import requests

# Groq API setup (with your API key)
Key = "key"
client = Groq(api_key=Key)

# Reference Links Array
reference_links = [
    {
        "topic": "discovery of exoplanets",
        "url": "https://sci.esa.int/web/exoplanets/-/60654-a-brief-introduction-to-exoplanets"
    },
    {
        "topic": "history of exoplanet discovery",
        "url": "https://www.schoolsobservatory.org/learn/astro/exoplanets/history"
    },
    {
        "topic": "introduction to exoplanets",
        "url": "https://science.nasa.gov/exoplanets/"
    },
    {
        "topic": "methods to detect exoplanets",
        "url": "https://science.nasa.gov/exoplanets/how-we-find-and-characterize/"
    },
    {
        "topic": "transit method",
        "url": "https://science.nasa.gov/exoplanets/whats-a-transit/"
    },
    {
        "topic": "direct imaging",
        "url": "https://science.nasa.gov/mission/roman-space-telescope/direct-imaging/"
    },
    {
        "topic": "gravitational microlensing",
        "url": "https://science.nasa.gov/mission/roman-space-telescope/microlensing/"
    },
    {
        "topic": "astrometry",
        "url": "https://www.planetary.org/articles/wobbly-stars-the-astrometry-method"
    },
    {
        "topic": "types of exoplanets",
        "url": "https://science.nasa.gov/exoplanets/planet-types/"
    },
    {
        "topic": "famous exoplanets",
        "url": "https://science.nasa.gov/exoplanets/immersive/strange-new-worlds/"
    }
]

def chatbot():
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("https://www.shutterstock.com/image-photo/hand-touching-digital-chatbot-provide-600nw-1639774756.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)    

    st.title("ExoBoT")
    st.write("Ask the chatbot anything about exoplanets below:")

    # Initialize session state for chat history if not already done
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert in exoplanets. Answer all questions related to exoplanets, "
                    "their discovery methods, characteristics, atmospheres, habitability, and their "
                    "importance in the study of astronomy. Provide detailed answers and, if applicable, include reference links for additional information."
                )
            }
        ]

    # Input text box for user query
    user_input = st.text_input("Enter your question about exoplanets:", placeholder="e.g., How do scientists discover exoplanets?")
    
    # Handle the chatbot response when a question is provided via text input
    if st.button("Send") and user_input.strip() != "":
        with st.spinner("Fetching response..."):
            # Append the user's message to the message history
            st.session_state.messages.append({"role": "user", "content": user_input})

            # Make a request to Groq API with the current message history
            try:
                chat_completion = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model="llama3-8b-8192",
                )
                
                # Get the response from the chatbot
                response = chat_completion.choices[0].message.content

                # Check if any reference link matches the user's query
                for ref in reference_links:
                    if ref["topic"] in user_input.lower():
                        response += f"\n\nFor more information, check this link: [Learn more about {ref['topic']}]({ref['url']})"

                # Append the chatbot's response to the message history
                st.session_state.messages.append({"role": "assistant", "content": response})

                # Display chat history
                for message in st.session_state.messages:
                    if message["role"] == "user":
                        st.write(f"**You:** {message['content']}")
                    elif message["role"] == "assistant":
                        st.write(f"**Chatbot:** {message['content']}")

            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {str(e)}")

