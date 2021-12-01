import streamlit as st
import src.code.live_object_detection_asl as lod_asl
import src.code.live_object_detection_arabic as lod_arabic

# pylint: disable=line-too-long
def write():

    lod_asl.app_object_detection_asl()

    lod_arabic.app_object_detection_arabic()
