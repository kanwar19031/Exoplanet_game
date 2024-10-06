import streamlit as st
import os

def about_us():
    # Setting a background image using CSS
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("https://c4.wallpaperflare.com/wallpaper/804/696/36/exoplanet-atmosphere-clouds-stars-moon-wallpaper-preview.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Title and introductory section
    st.title("About Us")
    st.subheader("Welcome to ExoQuest")
    st.write("""
        Welcome to **ExoQuest**, your gateway to the cosmos where exploration meets innovation. 
        At ExoQuest, we are passionate about bringing the wonders of the universe closer to you 
        through immersive content, interactive tools, and an engaging experience that blends learning with fun.
    """)

    # Mission section
    st.header("Our Mission")
    st.write("""
        Our mission is to make exoplanet exploration accessible and exciting for everyone. 
        Whether you are an aspiring astronomer, a student, or simply someone curious about the , 
        ExoQuest is here to guide you on your journey across the universe. We provide resources that 
        help you understand the mysteries and explore distant exoplanets, and listen to 
        captivating audiobooks about the vast expanse beyond earth.
    """)

    # What We Offer section
    st.header("What We Offer")
    st.write("""
        Here are some of the features and content you can explore at ExoQuest:
    """)
    st.write("- **Exo Chronicles**: Dive into our collection of audiobooks, where some of the most fascinating stories and insights about the universe come to life. From detailed accounts of space missions to inspiring science fiction, our audiobooks are designed to educate.")
    st.write("- **Exoplanet Chatbot**: Have you ever wanted to ask questions about planets beyond our solar system? Our **ExoBoT** is here to assist you. This intelligent assistant is ready to answer your questions and provide interesting facts about exoplanets and the universe, making learning interactive and engaging.")
    st.write("- **Gallery**: Explore the beauty of the exoplanet through our **Gallery** section. Here, you’ll find stunning images of galaxies, nebulae, and exoplanets that showcase the vastness and splendor of space. Let your imagination soar as you witness these incredible sights captured by powerful telescopes.")
    st.write("- **Reference Links**: Our **Reference Links** section provides a curated list of reliable resources for deeper exploration. Whether you are looking for the latest research articles, astronomy tools, or educational content, this section has got you covered.")

    # Why OrbitVerse section
    st.header("Why ExoQuest?")
    st.write("""
        At ExoQuest, we believe that everyone should have the opportunity to connect with the wonders of the Exoplanet. 
        Our platform is designed to be a hub of exploration—combining educational resources, stunning visuals, and 
        cutting-edge technology to inspire curiosity and foster learning.
    """)
    st.write("""
        Whether you're here to relax with an audiobook, engage in interactive conversations with our chatbot, or 
        simply enjoy breathtaking images from our gallery, ExoQuest has something for every space enthusiast.
    """)

    # Join Us section
    st.header("Join Us on Our Journey")
    st.write("""
        We invite you to join us on this journey beyond the stars. Stay tuned as we continue to add more features, 
        expand our audiobook library, and enhance our chatbot capabilities. Let ExoBoT be your guide as you explore the frontiers of space.
    """)
    st.write("**Discover, Learn, and Be Inspired – Welcome to ExoQuest!**")


