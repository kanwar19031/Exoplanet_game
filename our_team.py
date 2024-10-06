import streamlit as st



def our_team():
    # Set the background image with custom CSS
    st.markdown(
        """
        <style>
        .stApp {
            background-image: path("images/Comet KIDS.png");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Team Page Content
    st.title("Comet Kids")
    st.header("Meet Our Team")

    # Kanwar
    st.subheader("Kanwar: Website and Chatbot Developer")
    st.write("Kanwar is responsible for developing and maintaining the website as well as designing the chatbot that facilitates interactions with users. With strong skills in web technologies and AI, Kanwar ensures a seamless user experience.")

    # Vaishnavi
    st.subheader("Vaishnavi: Information Gathering Specialist")
    st.write("Vaishnavi plays a key role in researching and gathering information for the project. Her expertise in finding accurate and relevant data helps keep our content informative and up-to-date.")

    # Vishnu
    st.subheader("Vishnu: Audiobook Creator")
    st.write("Vishnu specializes in creating engaging audiobooks for our users. With a knack for storytelling and audio production, Vishnu ensures our content is accessible and captivating in audio format.")

    # Krity
    st.subheader("Krity: Logo and Presentation Designer")
    st.write("Krity is the creative mind behind the visuals of the project. She has designed our logo and creates presentations that effectively communicate our ideas, ensuring a visually appealing experience.")

    # Veron
    st.subheader("Veron: Visual Content Curator")
    st.write("Veron is responsible for curating the best visuals for our gallery. With a keen eye for design, Veron ensures that our gallery provides an inspiring and beautiful experience for our audience.")

    # Divyanshi
    st.subheader("Divyanshi: Figure-it-out Specialist")
    st.write("Divyanshi brings a versatile approach to the team by taking on tasks that need innovative solutions. She is always up for the challenge of figuring out new and creative ways to contribute.")

