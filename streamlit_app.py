import streamlit as st

st.set_page_config(
    page_title="SignSight",  # => Quick reference - Streamlit
    page_icon=
    "https://emoji.slack-edge.com/T02NE0241/signsigh/7fc5f78d22bb9eb4.png",
    layout="wide",  # wide
    initial_sidebar_state="expanded")  # collapsed


from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import queue
import random
import meta
#Import for streamlit
import av
from streamlit_webrtc import (
    RTCConfiguration,
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)
from PIL import Image

#Import for Deep learning model
import tensorflow as tf
from tensorflow.keras.models import load_model

import src.pages.about
import src.pages.home
import src.pages.resources
import src.pages.vision
import src.pages.tryme

PAGES = {
    "Home": src.pages.home,
    "Mission": src.pages.vision,
    "TryMe": src.pages.tryme,
    "Resources": src.pages.resources,
    "About": src.pages.about,
}

# """Main function of the App"""
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]

with st.spinner(f"Loading {selection} ..."):
    page.write()

#Import for handling image
import cv2
from cvzone.HandTrackingModule import HandDetector


# col1, col2, col3 = st.columns([0.7,6,2])

# with col1:
#     st.write("")

# with col2:
#     image = Image.open('images/SignSight logo.png')
#     st.image(image, caption='', width=600, use_column_width=None)
#     st.markdown("<h4 style='text-align: center; color: black;'>Making sign language interpretable worldwide 🐱</h14",
#                 unsafe_allow_html=True)
#     st.markdown(meta.SIDEBAR_INFO, unsafe_allow_html=True)
#     """
#     [![Stars](https://img.shields.io/github/stars/rkumar-slim/flykrinterface)](https://github.com/rkumar-slim/flykrinterface)
#     [![Source code](https://img.shields.io/github/forks/rkumar-slim/flykr)](https://github.com/rkumar-slim/flykr)
#     """
#     with st.expander("Our Journey", expanded=True):
#         st.markdown(meta.STORY, unsafe_allow_html=True)
# image = Image.open('images/SignSight logo.png')
# # st.markdown("<br>", unsafe_allow_html=True)
# st.image(image,
#          caption='',
#          width=400,
#          use_column_width=None)
# st.header('Making sign language **interpretable** worldwide')
# """
# # Making sign language interpretable worldwide
# """

# #Create a dict for classes
# @st.cache(allow_output_mutation=True)
# def alphabet():
#     """ Generating dictionary to turn prediction into their actual labels"""
#     mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'K', 10: 'L', 11: 'M',
#                             12: 'N', 13: 'O', 14: 'P', 15: 'Q', 16: 'R', 17: 'S', 18: 'T', 19: 'U', 20: 'V', 21: 'W', 22: 'X', 23: 'Y'}
#     return mapping


# RTC_CONFIGURATION = RTCConfiguration(
#     {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
# )

# # CWD path
# HERE = Path(__file__).parent

# def display_app_header(main_txt, sub_txt, is_sidebar=False):
#     """
#     function to display major headers at user interface
#     Parameters
#     ----------
#     main_txt: str -> the major text to be displayed
#     sub_txt: str -> the minor text to be displayed
#     is_sidebar: bool -> check if its side panel or major panel
#     """

#     html_temp = f"""
#     <div style = "background.color:#3c403f  ; padding:2px">
#     <h4 style = "color:white; text_align:center;"> {main_txt} </h4>
#     <p style = "color:white; text_align:center;"> {sub_txt} </p>
#     </div>
#     """
#     if is_sidebar:
#         st.sidebar.markdown(html_temp, unsafe_allow_html=True)
#     else:
#         st.markdown(html_temp, unsafe_allow_html=True)



# main_txt = """"""
# sub_txt = ""
# display_app_header(main_txt,sub_txt,is_sidebar = False)


# callback to update emojis in Session State
# in response to the on_click event
# def random_emoji():
#     st.session_state.emoji = random.choice(emojis)


# # initialize emoji as a Session State variable
# if "emoji" not in st.session_state:
#     st.session_state.emoji = "👈"

# emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼"]

# st.button(f"Click Me {st.session_state.emoji}", on_click=random_emoji)


# #deep learning sign detector model cached
# @st.cache(allow_output_mutation=True)
# def retrieve_model():
#     """ dummy tensorflow CNN model trained on few epochs on multiclassification task (american signs) """
#     PATH_MODEL = "saved_models/asl_model.h5"
#     PATH_LABEL = "saved_models/asl_class_names.npy"

#     model = load_model(PATH_MODEL)
#     label = np.load(PATH_LABEL)
#     return model, label

# #Main intelligence of the file, class to launch a webcam, detect hands, then detect sign and output american letters
# def app_object_detection():
#     class SignPredictor(VideoProcessorBase):

#         result_queue: "queue.Queue[List[Detection]]"
#         def __init__(self) -> None:
#             # Hand detector
#             self.hand_detector = HandDetector(detectionCon=0.5, maxHands=1)
#     # Sign detector
#     self.model, self.label = retrieve_model()

#     #Queue to share information that happen within the live video thread outside the thread
#     self.result_queue = queue.Queue()

# def find_hands(self, image):

#     hands = self.hand_detector.findHands(image, draw = False)
#     # loop over all hands and print them on the video + apply predictor
#     for hand in hands:
#         # this is just an array of len 4, containing info about the bounding box
#         bbox = hand["bbox"]

#         # .rectangle needs the image, the top right, bottom left points of the rectangle,
#         # and color of the rectangle and line thickness
#         if bbox[2] > bbox[3]:
#             w = bbox[2]
#             h = bbox[2]
#     diff = int((bbox[2] - bbox[3])/2)

#     rectangle = cv2.rectangle(
#         image, (bbox[0] - 20, bbox[1] - 20 - diff),
#         (bbox[0] + bbox[2] + 20,
#         bbox[1] + bbox[3] + 20 + diff), (0, 0, 0), 2)

# else:
#     diff = int((bbox[3] - bbox[2]) / 2)
#     rectangle = cv2.rectangle(
#         image, (bbox[0] - 20 - diff, bbox[1] - 20),
#         (bbox[0] + bbox[2] + 20 + diff,
#         bbox[1] + bbox[3] + 20), (0, 0, 0), 2)

# #load model
# model, label = retrieve_model()

# # prediction
# imgage_resized = np.array(tf.image.resize(
#         (rectangle), [128, 128]) / 255)

#     prediction = model.predict(
#         np.array(tf.image.resize(
#             (rectangle), [128, 128])/ 255).reshape(-1, 128, 128, 3))

#     prediction_max = np.argmax(prediction)

#     pred = label[prediction_max]
#     #check on terminal the prediction
#     print(pred)
#     #store prediction on the queue to use them outside of the live thread
#     self.result_queue.put(pred)

#     #draw letter on images
#     cv2.putText(rectangle, pred, (bbox[0] + 30, bbox[1] - 30), cv2.FONT_ITALIC,
#                     2, (0, 0, 0), 2)

# return hands

#     def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
#         image = frame.to_ndarray(format="rgb24")
#         hands = self.find_hands(image)
#         return av.VideoFrame.from_ndarray(image, format="rgb24")

# webrtc_ctx = webrtc_streamer(
#     key="object-detection",
#     mode=WebRtcMode.SENDRECV,
#     rtc_configuration=RTC_CONFIGURATION,
#     video_processor_factory=SignPredictor,
#     media_stream_constraints={"video": True, "audio": False},
#     async_processing=True,
# )

# if st.checkbox("Show the detected labels", value=True):
#     if webrtc_ctx.state.playing:
#         labels_placeholder = st.empty()
#         # NOTE: The video transformation with object detection and
#         # this loop displaying the result labels are running
#         # in different threads asynchronously.
#         # Then the rendered video frames and the labels displayed here
#         # are not strictly synchronized.
#         while True:
#             if webrtc_ctx.video_processor:
#                 try:
#                     result = webrtc_ctx.video_processor.result_queue.get(
#                         timeout=1.0
#                     )
#                 except queue.Empty:
#                     result = None
#                 labels_placeholder.write(result)
#             else:
#                 break


# # st.markdown(
#     """All code and tutorial available [here](https://github.com/Yanka13/live-streaming-app),
# thanks to [streamlit webrtc](https://github.com/whitphx/streamlit-webrtcx) for making it possible"""
# )


############################ Sidebar + launching #################################################

# object_detection_page = "Real time sign translation"

# app_mode = st.sidebar.selectbox(
#     "Choose the app mode",
#     [
#         object_detection_page,
#     ],
# )
# st.subheader(app_mode)
# if app_mode == object_detection_page:
#     app_object_detection()
st.sidebar.title("Contribute")
st.sidebar.info(
    "This an open source project and you are very welcome to **contribute** your awesome "
    "comments, questions, resources and apps as "
    "[issues](https://github.com/rkumar-slim/flykr/issues) of or "
    "[pull requests](https://github.com/rkumar-slim/flykr/pulls) "
    "to the [source code](https://github.com/rkumar-slim/flykr). ")
st.sidebar.info("""
            Tracking down usability of the app
            [![Stars](https://img.shields.io/github/stars/rkumar-slim/flykrinterface)](https://github.com/rkumar-slim/flykrinterface)
            [![Source code](https://img.shields.io/github/forks/rkumar-slim/flykr)](https://github.com/rkumar-slim/flykr)
    """)
# with col3:
#     st.markdown("")
#     st.markdown("")
#     st.markdown("")
