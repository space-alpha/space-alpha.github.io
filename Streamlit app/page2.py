#!/usr/bin/env python
# coding: utf-8

# In[2]:


# page2.py

import streamlit as st
from PIL import Image, ImageDraw
import random
import pandas as pd
import numpy as np


def page2():
    

    # Set the title and page layout
    st.title("Space Art Generator")

    # Sidebar controls
    st.sidebar.header("Art Settings")
    num_stars = st.sidebar.slider("Number of Stars", min_value=50, max_value=1000, value=300)
    star_density = st.sidebar.slider("Star Density", min_value=1, max_value=10, value=5)
    num_planets = st.sidebar.slider("Number of Planets", min_value=1, max_value=10, value=3)
    background_color = st.sidebar.color_picker("Background Color", value="#000000")
    animate = st.sidebar.checkbox("Animate", False)
    planet_size_range = st.sidebar.slider("Planet Size Range", min_value=10, max_value=100, value=(20, 50))
    add_moons = st.sidebar.checkbox("Add Moons", False)
    save_art = st.sidebar.checkbox("Save Artwork", False)

    # User customization
    st.sidebar.markdown("---")
    user_name = st.sidebar.text_input("Your Name", "Anonymous")

    # Planet customization
    planet_color = st.sidebar.color_picker("Planet Color", value="#FFA500")

        # Artwork Ratings and Comments
    st.sidebar.markdown("---")
    st.sidebar.header("Artwork Ratings and Comments")
    st.sidebar.text_input("Rate this artwork (1-5 stars)")
    user_comment = st.sidebar.text_area("Add a comment")

    # Artwork Filtering
    st.sidebar.markdown("---")
    st.sidebar.header("Artwork Filtering")
    filter_criteria = st.sidebar.selectbox("Filter Artwork By", ["Date", "Popularity", "Color Scheme"])
    if filter_criteria == "Date":
        # Implement filtering by creation date
        pass
    elif filter_criteria == "Popularity":
        # Implement filtering by popularity or user ratings
        pass
    elif filter_criteria == "Color Scheme":
        # Implement filtering by color schemes used in artwork
        pass

    # User Accounts
    st.sidebar.markdown("---")
    st.sidebar.header("User Accounts")
    if st.sidebar.button("Create Account"):
        # Implement user account creation
        st.sidebar.text("Account created!")
    if st.sidebar.button("Login"):
        # Implement user login
        st.sidebar.text("Logged in as user")

    # Artwork Challenges
    st.sidebar.markdown("---")
    st.sidebar.header("Artwork Challenges")
    if st.sidebar.button("Join Weekly Challenge"):
        # Implement joining a weekly challenge
        st.sidebar.text("You've joined this week's challenge!")

    # Background Music Selection
    st.sidebar.markdown("---")
    st.sidebar.header("Background Music")
    background_music = st.sidebar.selectbox("Background Music", ["None", "Space Ambient", "Epic Space", "Relaxing Space"])
    if background_music != "None":
        st.audio(f"{background_music}.mp3")

    # Artwork Statistics
    st.sidebar.markdown("---")
    st.sidebar.header("Artwork Statistics")
    # Implement and display statistics about the generated artwork

    # Interactive Learning
    st.sidebar.markdown("---")
    st.sidebar.header("Interactive Learning")
    if st.sidebar.button("Learn About Comets"):
        # Implement interactive learning about comets
        st.sidebar.text("Learn about comets!")

    # Multi-Language Support
    st.sidebar.markdown("---")
    st.sidebar.header("Language")
    selected_language = st.sidebar.selectbox("Select Language", ["English", "Spanish", "French", "German"])
    # Implement language selection and translation
    
    # Display the NJIT logo in the top right corner
    njit_logo = Image.open("njit_logo.png")  # Replace with the actual file path of the NJIT logo
    st.image(njit_logo, use_column_width=False, width=100)

    # Define the size of the image
    width, height = 800, 800

    # Create a function to generate space art
    def generate_space_art(num_stars, star_density, num_planets, background_color, animate, planet_size_range, add_moons, planet_color):
        img = Image.new('RGB', (width, height), background_color)
        draw = ImageDraw.Draw(img)

        # Generate stars
        def draw_stars(draw, num_stars, star_density):
            for _ in range(num_stars):
                x = random.randint(0, width)
                y = random.randint(0, height)
                size = random.randint(1, star_density)
                brightness = random.randint(200, 255)
                draw.rectangle([x, y, x + size, y + size], fill=(brightness, brightness, brightness))

        # Generate planets
        def draw_planet(draw, x, y, size, color, add_moons):
            draw.ellipse([x, y, x + size, y + size], fill=color)
            if add_moons:
                for _ in range(random.randint(0, 3)):  # Add random moons (0 to 3 moons per planet)
                    moon_size = random.randint(5, 15)
                    moon_distance = random.randint(int(size / 2), int(size * 2))
                    moon_angle = random.uniform(0, 360)
                    moon_x = x + size / 2 + moon_distance * 1.5 *                         random.cos(moon_angle)
                    moon_y = y + size / 2 + moon_distance *                         random.sin(moon_angle)
                    draw.ellipse([moon_x, moon_y, moon_x + moon_size,
                                  moon_y + moon_size], fill='gray')

        # Add stars to the image
        draw_stars(draw, num_stars, star_density)

        # Add planets to the image
        for _ in range(num_planets):
            x = random.randint(0, width)
            y = random.randint(0, height)
            size = random.randint(planet_size_range[0], planet_size_range[1])
            draw_planet(draw, x, y, size, planet_color, add_moons)

        return img

    # Generate and display the space art
    if animate:
        for i in range(10):  # Create 10 frames for animation
            space_art = generate_space_art(num_stars, star_density, num_planets, background_color, animate, planet_size_range, add_moons, planet_color)
            st.image(space_art, caption=f"Space Art - Frame {i+1}", use_column_width=True)
            time.sleep(0.5)  # Pause for 0.5 seconds between frames
    else:
        space_art = generate_space_art(num_stars, star_density, num_planets, background_color, animate, planet_size_range, add_moons, planet_color)
        st.image(space_art, caption="Space Art", use_column_width=True)

    # Save artwork
    if save_art:
        space_art.save("space_art.png")
        st.sidebar.success("Artwork saved!")

    # Instructions
    st.sidebar.markdown("---")
    st.sidebar.header("Instructions")
    st.sidebar.markdown("Adjust the settings on the left to customize your space-themed artwork for Girl Hacks 2023. You can change the number of stars, star density, planets, background color, and more. Check 'Add Moons' to include moons around planets and 'Save Artwork' to save the generated artwork.")

    # Share on social media
    st.sidebar.markdown("---")
    st.sidebar.header("Share Artwork")
    if st.sidebar.button("Share on Twitter"):
        st.sidebar.text("Artwork shared on Twitter!")
    if st.sidebar.button("Share on Instagram"):
        st.sidebar.text("Artwork shared on Instagram!")
    if st.sidebar.button("Share on Facebook"):
        st.sidebar.text("Artwork shared on Facebook!")

    # User profile
    st.sidebar.markdown("---")
    st.sidebar.header("User Profile")
    st.sidebar.text(f"Hello, {user_name}!")

    # Artwork Labels
    st.sidebar.markdown("---")
    st.sidebar.header("Artwork Labels")
    artwork_label = st.sidebar.text_input("Artwork Label", "My Space Art")
    st.sidebar.markdown(f"Artwork Label: {artwork_label}")


# In[ ]:




