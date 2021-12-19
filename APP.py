import streamlit as st
from streamlit.elements.balloons import BalloonsMixin
from streamlit.proto.Balloons_pb2 import Balloons
videomp=st.image("medpost.gif")
st.title("Bienvenido a la InfVagAPP")
#APP para detectar infecciones vaginales y dar recomendaciones

sint=st.multiselect("Selecciona de los siguientes opciones la que se aproxime más a tus síntomas",("Dolor con las relaciones sexuales","Salida de líquido vaginal","Mal olor vaginal","Comezón en región vaginal"))
if sint== "Salida de líquido vaginal":
    BalloonsMixin