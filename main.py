import streamlit as st
import os
import openai
import dotenv

dotenv.load_dotenv(".env")
env_vars = dotenv.dotenv_values()
for key in env_vars:
    os.environ[key] = env_vars[key]

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

# Define the options for image size and number of images
image_sizes = ["1024x1024", "1024x1792", "1792x1024"]
num_images_options = [1, 2, 3, 4, 5]

# Create a Streamlit app
st.title("RG - Image Generation App")
user_prompt = "Generate an image of Thar vehicle from Mahindra and Mahindra. The color should be red. The background should be the mountains in Ladakh. The image should be realistic. It should be an evening shot with the sun shining on the car."

# Create a form to input parameters
with st.form("Image Generation Form"):
    
    # Add a text input for the image prompt
    image_prompt = st.text_area("Image Prompt", value=user_prompt, height=3)

    # Add a select box for image size
    image_size = st.selectbox("Image Size", image_sizes)

    # Add a select box for the number of images
    num_images = st.selectbox("Number of Images", num_images_options)

    # Add a submit button
    submit_button = st.form_submit_button("Generate Images")

# Check if the form is submitted
if submit_button:
    # You can use the selected parameters to call OpenAI's API for image generation.
    

    response = openai.Image.create(
        prompt=image_prompt,
        model="dall-e-3",
        n=1,
        size=image_size,
        quality="standard", 
    )

    st.write("Generating Images with the following parameters:")
    st.write("Image Prompt:", image_prompt)
    st.write("Image Size:", image_size)
    st.write("Number of Images:", num_images)

    # Iterate through the response to display multiple images
    for i, item in enumerate(response['data']):
        image_url = item['url']
        st.image(image_url, caption=f"Generated Image {i+1}", use_column_width=True)
