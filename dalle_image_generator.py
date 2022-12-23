import openai
import urllib.request
from PIL import Image
import streamlit as st

openai.api_key = "Use your api key here."

def generate_image(image_description, image_quantity):
    response = openai.Image.create(
    prompt=image_description,
    n=image_quantity,
    size="512x512"
    )
    images = []
    img_urls = response['data']
    for i in range(len(img_urls)):
        urllib.request.urlretrieve(img_urls[i]['url'], f'img{i}.png')
        img = Image.open(f"img{i}.png")
        images.append(img)
    return images


#page tile
st.title('Dall.E - Image Generator - Web App')

#text input box for image recognition
img_desc = st.text_input("Image Description")

#number input box for image quantity
image_quantity = st.number_input("Number of Images", min_value=1, max_value=5, step=1)

if st.button("Generate Image"):
    generate_img =  generate_image(img_desc, image_quantity)
    st.image(generate_img, use_column_width=True)
