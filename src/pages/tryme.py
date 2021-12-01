import streamlit as st
import src.code.live_object_detection_asl as lod_asl
import src.code.live_object_detection_arabic as lod_arabic
import src.code.app_flashcard as fcard
# pylint: disable=line-too-long

ASL = """
<div style="text-align: center" class="contributors font-body text-bold">
<a class="contributor comma" href="https://www.linkedin.com/in/franciska-e-94592115a/"><h4 style='text-align: center; color: black;'>Franciska Englert</h4</a>
</div>
"""


def write():

    options = st.selectbox("Choose what you want to test today",
                           index=0,
                           options=[
                               "Live demo with American sign",
                               "Live demo with Arabic sign", "Knowledge Test w/ Flashcards"
                           ])

    if options=="Live demo with American sign":
        st.write("##")
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Click on the start button to activate the webcam</h4",
                    unsafe_allow_html=True)
        st.write("##")
        lod_asl.app_object_detection_asl()
    elif options=="Live demo with Arabic sign":
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Click on the start button to activate the webcam</h4",
            unsafe_allow_html=True)
        st.write("##")
        lod_arabic.app_object_detection_arabic()
    elif options=="Knowledge Test w/ Flashcards":
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Upload an image to test your knowledge about sign language</h4",
            unsafe_allow_html=True)
        st.write("##")
        fcard.flashcard()
        # # lod_arabic.app_object_detection_arabic()
        # flash_card = fcard.GameState()
