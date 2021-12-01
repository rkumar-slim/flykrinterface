from PIL import Image
import numpy as np
import streamlit as st
import requests
import json
import random
from typing import TypeVar
import dataclasses

HI = 1000

StateT = TypeVar('StateT')


def persistent_game_state(initial_state: StateT) -> StateT:
    session_id = st.report_thread.get_report_ctx().session_id
    session = st.server.server.Server.get_current()._get_session_info(
        session_id).session
    if not hasattr(session, '_gamestate'):
        setattr(session, '_gamestate', initial_state)
    return session._gamestate


# Function to Read and Convert Images
def load_image(img):
    im = Image.open(img)
    im = im.resize((256, 256), Image.ANTIALIAS)
    image = np.array(im)
    return image


all_signs = ["a", "b", "c", "d", 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

letter_to_guess = all_signs[random.randint(0, len(all_signs)-1)]

# st.write("Do you know the sign for " + letter_to_guess.upper() + "?")
# uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png'])

# if uploadFile is not None:
#     # Perform  Manipulations
#     img = load_image(uploadFile)
#     st.image(img)
#     st.write(":camera_with_flash: Image Uploaded Successfully !")
#     # Reshape the image
#     X = img.reshape(img.shape[0] * img.shape[1] * img.shape[2])
#     X = X.tolist()
#     X_json = json.dumps(X)
#     # Call the POST
#     url = "https://sign-lang-im-n7noas4ljq-ew.a.run.app/predict"
#     data = json.dumps({
#         "image_reshape": X_json,
#         "height": img.shape[0],
#         "width": img.shape[1],
#         "color": img.shape[2]
#     })
#     headers = {'Content-type': 'application/json'}

#     response = requests.post(url, data, headers=headers)
#     response = response.json()
#     # e.g bruschetta
#     if response['response'] == letter_to_guess.lower():
#         st.write(
#             f"Well, that was a super duper guess, this is indeed the right sign for {letter_to_guess.upper} :) So smart."
#         )
#     else:
#         st.write(
#             f"Good try, but actually, this is more like a {response['response']}. But keep on the practice!"
#         )

# else:
#     st.write("Make sure you image is in JPG/PNG Format.")

@dataclasses.dataclass
class GameState:
    number: int
    num_guesses: int = 0
    game_number: int = 0
    game_over: bool = False

# callback to update emojis in Session State
# in response to the on_click event
def random_emoji():
    st.session_state.emoji = random.choice(emojis)

# initialize emoji as a Session State variable
if "emoji" not in st.session_state:
    st.session_state.emoji = "👈"

emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "�"]


def flashcard():
    GS = GameState(random.randint(1, len(all_signs) - 1))
    state = persistent_game_state(initial_state=GS)


    if st.button(f"NEW LETTER {st.session_state.emoji}", on_click=random_emoji):
        state.number = random.randint(1, len(all_signs) - 1)
        state.num_guesses = 0
        state.game_number += 1
        state.game_over = False

    if not state.game_over:

        letter_to_guess = all_signs[state.number]
        st.write("Do you know the sign for " + letter_to_guess.upper() + "?")
        uploadFile = st.file_uploader(label="Upload your guess :) ", type=['jpg', 'png'])

        if uploadFile  is not None:
            # Perform  Manipulations
            img = load_image(uploadFile)
            st.image(img)
            st.write(":camera_with_flash: Image Uploaded Successfully !")
            # Reshape the image
            X = img.reshape(img.shape[0] * img.shape[1] * img.shape[2])
            X = X.tolist()
            X_json = json.dumps(X)
            # Call the POST
            url = "https://sign-lang-im-n7noas4ljq-ew.a.run.app/predict"
            data = json.dumps({
                "image_reshape": X_json,
                "height": img.shape[0],
                "width": img.shape[1],
                "color": img.shape[2]
            })
            headers = {'Content-type': 'application/json'}

            response = requests.post(url, data, headers=headers)
            response = response.json()
            # e.g bruschetta
            if response['response'] == letter_to_guess.lower():
                st.write(
                    f"Well, that was a super duper guess, this is indeed the right sign for {letter_to_guess.upper()} :) So smart. 🎉🎉🎉"
                )
            else:
                st.write(
                    f"Good try, but actually, this is more like a {response['response']}. But practice makes perfect 😏!"
                )

        else:
            st.write("Make sure you image is in JPG/PNG Format.")
