import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
from streamlit_option_menu import option_menu
from st_social_media_links import SocialMediaIcons


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_tec = load_lottieurl("https://lottie.host/f01a21a4-3e85-4a93-b86f-c65634d56171/ynBOws9BSV.json")
image_im = Image.open("images/photo_2025-05-31_09-57-01.jpg")
vice_im = Image.open("images/photo_2025-05-31_09-55-47.jpg")




st.set_page_config(page_title="Mayura Silva", layout="wide")
st.subheader("Hi, My name is Mayura Silva")
st.title("I am ,Millwright Fitter Trainne @ CGTTI")
st.write("As a Millwright Fitter i cover areas like Hydraulic, Pneumatics, Water Pump, Auto mobile, Lathe and Milling etc.")

with st.container():
    st.write("---")
    left_column, right_coloum = st.columns(2)
    with left_column:
        st.header("Education")
        st.write("##")
        st.write("De Mazenod College-Kandana(2008-2022)\n\nCeylon German Technical Training Institute(2022-present)")

with right_coloum:
    st_lottie(lottie_tec, height=300)


with st.container():
    st.write("---")
    left_column, right_coloum = st.columns(2)
    with left_column:
        st.header("Experiance")
        st.write("##")
        st.subheader("2025/01-2025/06\n\nInternship at Michelin Lanka PLC")
        st.write("-Predictive Maintanance\n\n-Hydraulic systems\n\n-Mig and Arc welding\n\n-Gearbox Mill and Mixxer overhauling")
    with right_coloum:
        st.subheader("Socials")
        social_media_links = [
            "https://www.linkedin.com/in/mayura-silva-a9717022a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
            "https://github.com/ggitsmomo",
            "https://www.instagram.com/_mayura_silva_?utm_source=qr&igsh=MWRmZHIyNXpkNjVoeQ=="
        ]
        social_media_icons = SocialMediaIcons(social_media_links)

        social_media_icons.render()
    



with st.container():
    st.write("---")
    st.header("Media")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with text_column:
        st.subheader("Working on a Electro Pneumatic Training Module")
        st.write("In here i'm wiring a cascade circuit.")

    with image_column:
        st.image(image_im)

#with st.container():
   # image_column, text_column = st.columns((1, 2))
    #with image_column:
        #st.video("images/video_2025-05-31_10-31-15.mp4")
   # with text_column:
        #st.subheader("Practicing on a Bobcat Skid loader")
       # st.write("Leveling the ground with a BOBCAT skid loader.")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(vice_im)
    with text_column:
        st.subheader("This vice was made by me with hand tools and a bench drill.")
        st.write("This vice was made as a project to trade selection exam\n\nAs for tools hacksaw, files, tapset, rivetpuncher and bench drill used.")

with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

    contac_form = """<form action="https://formsubmit.co/mayurachamod00@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder= "your email" required>
     <textarea name="message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
</form>"""

left_column, right_coloum =st.columns(2)
with left_column:
    st.markdown(contac_form, unsafe_allow_html=True)
with right_coloum:
    st.empty()


