import streamlit as st
from streamlit.elements.balloons import BalloonsMixin
from streamlit.proto.Balloons_pb2 import Balloons
from streamlit.proto.Button_pb2 import Button
videomp=st.image("medpost.gif")
st.title("Bienvenido a la InfVagAPP")
#APP para detectar infecciones vaginales y dar recomendaciones

st.subheader("Esta es una aplicación de autocuestionamiento para orientación médica, no se registrará ningún dato que se ingresé y no se pedirá la identificación del usuario de ninguna manera (Nombre, Id, etc).")
dolorvag="Dolor vaginal"
Sintomas=st.multiselect("Selecciona de los siguientes opciones la que se aproxime más a tus síntomas",[dolorvag,"Dolor con las relaciones sexuales","Salida de líquido vaginal","Mal olor vaginal","Comezón en región vaginal"])
if Sintomas == dolorvag:
    st.markdown("Duele")