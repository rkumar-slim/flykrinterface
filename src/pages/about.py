import streamlit as st
from PIL import Image
import meta

FE = """
<div style="text-align: center" class="contributors font-body text-bold">
<a class="contributor comma" href="https://www.linkedin.com/in/franciska-e-94592115a/"><h4 style='text-align: center; color: black;'>Franciska Englert</h4</a>
</div>
"""

LA = """
<div style="text-align: center" class="contributors font-body text-bold">
<a class="contributor comma" href="https://www.linkedin.com/in/layla-ibrahim/"><h4 style='text-align: center; color: black;'>Layla Ibrahim</h4</a>
</div>
"""

KW = """
<div style="text-align: center" class="contributors font-body text-bold">
<a class="contributor comma" href="https://www.linkedin.com/in/kobi-waterman-12518578/"><h4 style='text-align: center; color: black;'>Kobi Waterman</h4</a>
</div>
"""

RK = """
<div style="text-align: center" class="contributors font-body text-bold">
<a class="contributor comma" href="https://www.linkedin.com/in/rajiv-kumar-63031a9/"><h4 style='text-align: center; color: black;'>Rajiv Kumar</h4</a>
</div>
"""


# pylint: disable=line-too-long
def write():
    col1, col2, col3, col4 = st.columns([2,2,2,2])

    with col1:
        image = Image.open('images/FW.jpeg')
        st.image(image, caption='', width=200, use_column_width=True)
        st.markdown(FE, unsafe_allow_html=True)
        # st.markdown(
        #     "<h4 style='text-align: center; color: black;'>Franciska Englert</h4",
        #     unsafe_allow_html=True)

    with col2:
        image = Image.open('images/LI.jpeg')
        st.image(image, caption='', width=200, use_column_width=True)
        st.markdown(LA, unsafe_allow_html=True)


    with col3:
        image = Image.open('images/kw.jpeg')
        st.image(image, caption='', width=200, use_column_width=True)
        st.markdown(KW, unsafe_allow_html=True)

    with col4:
        image = Image.open('images/RK.jpeg')
        st.image(image, caption='', width=200, use_column_width=True)
        st.markdown(RK, unsafe_allow_html=True)
