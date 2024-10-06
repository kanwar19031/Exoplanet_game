import streamlit as st
import os

def gallery():
    st.title("Gallery")
    st.write("Here are some beautiful images related to exoplanets and astronomy:")

    # Directory containing images
    image_dir = "images"

    # List of image file names and their captions
    images = [
        ("Habex-Telescope-artist_s-view.png", "HabEx Telescope - Artist's Impression"),
        ("hubble telescope.webp", "Hubble Space Telescope"),
        ("James Webb Space Telescope (JWST).webp", "James Webb Space Telescope (JWST)"),
        ("Keck observatory.webp", "Keck Observatory"),
        ("Kepler Space Telescope.webp", "Kepler Space Telescope"),
        ("Size comparison of Neptune with HAT-P-11b (gray).png", "Size Comparison: Neptune vs. Exoplanet HAT-P-11b"),
        ("SPHERE_Common_Path_Infrastructure.jpg", "SPHERE Common Path Infrastructure"),
        ("Very large Telescope (VLT).webp", "Very Large Telescope (VLT)"),
        ("Exoplanet OGLE-2007-BLG-349.webp", "Exoplanet OGLE-2007-BLG-349 - An Exoplanet Orbiting Binary Stars"),
        ("GPI (Gemini Planet Imager).webp", "Gemini Planet Imager (GPI)"),
        ("hot gas giant.jpg", "Hot Gas Giant Close to Its Star"),
        ("hubble telescope in space.webp", "Hubble Telescope in Space"),
        ("hubble telescope(1).webp", "Hubble Space Telescope - Another Perspective"),
        ("jupitertwin(1).webp", "An Artist's Impression of a Jupiter Twin Exoplanet"),
        ("jupitertwin.webp", "Jupiter-like Exoplanet in a Distant Solar System"),
        ("Large Ultraviolet Optical Infrared Surveyor.png", "Large Ultraviolet Optical Infrared Surveyor (LUVOIR) - Concept"),
        ("Nancy Grace Roman Space Telescope.webp", "Nancy Grace Roman Space Telescope"),
        ("TESS (Transiting Exoplanet Survey Satellite).webp", "Transiting Exoplanet Survey Satellite (TESS)"),
        ("The_SPHERE_instrument_attached_to_the_VLT.jpg", "The SPHERE Instrument Attached to the VLT")
    ]

    # Display images in two columns
    for i in range(0, len(images), 2):
        cols = st.columns(2)

        # Display the first image in the first column
        with cols[0]:
            image_path = os.path.join(image_dir, images[i][0])
            st.image(image_path, caption=images[i][1])

        # Check if there is a second image available and display it in the second column
        if i + 1 < len(images):
            with cols[1]:
                image_path = os.path.join(image_dir, images[i + 1][0])
                st.image(image_path, caption=images[i + 1][1])

    # Additional images from the internet with URLs
    st.write("More images from external sources:")

    # Display external images in two columns as well
    external_images = [
        ("https://cdn.esahubble.org/archives/images/screen/heic1619a.jpg", "Artist's Impression of an Exoplanet"),
        ("https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/rockcms/2024-05/240524-gliese-12-b-exoplanet-aa-115p-e29a94.jpg", "An Exoplanet with Potential Habitability"),
        ("https://exoplanets.nasa.gov/internal_resources/921/", "The Kepler Space Telescope, which Discovered Many Exoplanets")
    ]

    for i in range(0, len(external_images), 2):
        cols = st.columns(2)

        # Display the first external image in the first column
        with cols[0]:
            st.image(external_images[i][0], caption=external_images[i][1])

        # Check if there is a second external image available and display it in the second column
        if i + 1 < len(external_images):
            with cols[1]:
                st.image(external_images[i + 1][0], caption=external_images[i + 1][1])
