import streamlit as st
from groq import Groq
import requests

# Groq API setup (with your API key)
Key = "Key"
client = Groq(api_key=Key)

# Set Streamlit page configuration
st.set_page_config(layout="wide")  # Set the layout to wide for more space

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Us", "Gallery", "Exoplanet Chatbot", "Reference Links"])

# Page 1: About Us
if page == "About Us":
    # Add CSS for background image
    st.markdown(
        """
        <style>
        .about-us-page {
            background-image: url('https://exoplanets.nasa.gov/system/stellar_items/image_files/3135_kepler-16b-illustration.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            padding: 3rem;
            color: white;
        }
        .about-us-content {
            background: rgba(0, 0, 0, 0.5); /* Darken the content background for better readability */
            padding: 2rem;
            border-radius: 10px;
            max-width: 800px;
            margin: auto;
        }
        </style>
        <div class="about-us-page">
            <div class="about-us-content">
                <h1>About Us</h1>
                <p>
                Welcome to the Exoplanet Learning Platform! This is an interactive learning tool designed to educate you about the fascinating
                world of exoplanets—planets that orbit stars outside our own solar system.
                </p>
                <p>
                Our platform is dedicated to providing rich resources about the discoveries, characteristics, and importance of exoplanets.
                Through our engaging materials, interactive gallery, and chatbot, we aim to make learning about exoplanets an enjoyable experience.
                </p>
                <p>
                Feel free to explore the gallery to see some amazing visuals, chat with our AI-powered chatbot, or refer to our carefully curated
                learning links to dive deeper into the subject!
                </p>
                <h2>What is an Exoplanet?</h2>
                <p>
                An <strong>exoplanet</strong> (or extrasolar planet) is a planet that orbits a star outside our solar system. These planets 
                can vary greatly in size, composition, and habitability, and discovering them helps scientists learn about the formation 
                and diversity of planetary systems in the universe.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Audio file definition and playback
    audio_file_path = "exoplanet_definition.mp3"  # Specify the path to your audio file
    try:
        # Display the audio player
        st.audio(audio_file_path, format="audio/mp3")
    except FileNotFoundError:
        st.error("Audio file not found. Please ensure the file is located at './assets/exoplanet_definition.mp3'")


# Page 2: Gallery
elif page == "Gallery":
    st.title("Gallery")
    st.write("Here are some beautiful images related to exoplanets and astronomy:")

    # Display images (you can add your own URLs or local images)
    st.image("https://cdn.esahubble.org/archives/images/screen/heic1619a.jpg", caption="Artist's impression of an exoplanet.")
    st.image("https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/rockcms/2024-05/240524-gliese-12-b-exoplanet-aa-115p-e29a94.jpg", caption="An exoplanet with potential habitability.")
    st.image("https://exoplanets.nasa.gov/internal_resources/921/", caption="The Kepler space telescope, which discovered many exoplanets.")

# Page 3: Exoplanet Chatbot
elif page == "Exoplanet Chatbot":
    st.title("Exoplanet Chatbot")
    st.write("Ask the chatbot anything about exoplanets below:")

    # Initialize session state for chat history if not already done
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert in exoplanets. Answer all questions related to exoplanets, "
                    "their discovery methods, characteristics, atmospheres, habitability, and their "
                    "importance in the study of astronomy. Stay focused on exoplanets and related astronomy topics."
                )
            }
        ]

    # Input text box for user query
    user_input = st.text_input("Enter your question about exoplanets:", placeholder="e.g., How do scientists discover exoplanets?")

    # Handle the chatbot response
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

# Page 4: Reference Links
elif page == "Reference Links":
    st.title("Exoplanet Reference Links")
    st.write("""
    Here are some useful links for learning more about exoplanets:
    - [NASA Exoplanet Exploration](https://exoplanets.nasa.gov/): Explore NASA's dedicated portal for information on exoplanets, their discovery, and the missions involved.
    - [Wikipedia: Exoplanet](https://en.wikipedia.org/wiki/Exoplanet): A comprehensive overview of exoplanets, their types, detection methods, and characteristics.
    - [The Habitable Exoplanet Catalog](https://phl.upr.edu/projects/habitable-exoplanets-catalog): Browse through a catalog of potentially habitable exoplanets.
    - [Kepler and Exoplanet Discovery](https://www.nasa.gov/mission_pages/kepler/main/index.html): Learn more about NASA's Kepler mission and how it revolutionized exoplanet discovery.
    - [What are Exoplanets?](https://science.nasa.gov/astrophysics/focus-areas/exoplanet-exploration): Understand what makes exoplanets unique and why scientists are so interested in studying them.
    """)

