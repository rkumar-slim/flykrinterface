"""Home page shown when the user enters the application"""
import streamlit as st
from PIL import Image
import meta



# pylint: disable=line-too-long
def write():
    #     """Used to write the page in the app.py file"""
    #     with st.spinner("Loading Home ..."):
    #         # ast.shared.components.title_awesome("")
    #         st.write("""
    # [Streamlit](https://streamlit.io/) is [announced](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace) as being **The fastest way to build custom Machine Learning tools** but I believe it has the potential to become much more awesome than that.
    # I believe Streamlit has the **potential to become the Iphone of Data Science Apps**. And maybe it can even become the Iphone of Technical Writing, Code, Micro Apps and Python.
    # The **purpose** of the **Awesome Streamlit Project** is to share knowledge on how Awesome Streamlit is and can become.
    # This application provides
    # - A list of awesome Streamlit **resources**.
    # - A **gallery** of awesome streamlit applications.
    # - A **vision** on how awesome Streamlit can be.
    # ## The Magic of Streamlit
    # The only way to truly understand how magical Streamlit is to play around with it.
    # But if you need to be convinced first, then here is the **4 minute introduction** to Streamlit!
    # Afterwards you can explore examples in the Gallery and go to the [Streamlit docs](https://streamlit.io/docs/) to get started.
    #     """)
    # ast.shared.components.video_youtube(
    #     src="https://www.youtube.com/embed/B2iAodr0fOo")
    col1, col2, col3 = st.columns([0.7, 6, 2])


    with col1:
        st.write("")

    with col2:
        image = Image.open('images/SignSight logo.png')
        st.image(image, caption='', width=600, use_column_width=None)
        st.markdown(
            "<h4 style='text-align: center; color: black;'>Making sign language interpretable worldwide 🌎</h14",
            unsafe_allow_html=True)
        st.write("##")
        st.markdown(
            """SignSight’s mission is to make the communication, translation, and
learning of any Sign-language just as seamless and easy as any
spoken languages. SignSight is driven by the core principle of
democratising communication, and our goal is to make every Sign-
language accessible to every age group in a fun, stimulating
manner.""")


    with col3:
        st.write("")
