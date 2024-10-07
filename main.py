import streamlit as st
from about_us import about_us
from gallery import gallery
#from chatbot import chatbot
from Exo_Chronicles import Exo
from reference_links import reference_links
from our_team import our_team  # Import the new page

# Set Streamlit page configuration with favicon
st.set_page_config(
    page_title="ExoQuest",
    page_icon="images/Comet KIDS.png",  # Path to the uploaded favicon image
    layout="wide"  # Set the layout to wide for more space
)

# Sidebar navigation
st.sidebar.title("Quick Access")
page = st.sidebar.radio("Go to", ["About Us", "Exo Chronicles", "Gallery", "Exoplanet Chatbot", "Reference Links", "Our Team"])

# Render the selected page
if page == "About Us":
    about_us()
elif page == "Gallery":
    gallery()
elif page == "Exo Chronicles":
    Exo()
#elif page == "Exoplanet Chatbot":
    #chatbot()
elif page == "Reference Links":
    reference_links()
elif page == "Our Team":
    our_team()
