from os import write
from typing import Text
from altair.vegalite.v4.schema.channels import X
from numpy import save, sin
import streamlit as st
from streamlit.elements.balloons import BalloonsMixin
from streamlit.proto.Balloons_pb2 import Balloons
from streamlit.proto.Button_pb2 import Button
import flask as flask
videomp=st.image("medpost.gif")
st.title("Bienvenido a la InfVagAPP")
#APP para detectar infecciones vaginales y dar recomendaciones
st.cache()
col1,col2=st.beta_columns(2)
#Parece que en multiselect tienes que poner el orden así como esta abajo supongo que como es una lista tienes que manejarlo así como tupple :X 
with col1:
  sintomas=st.multiselect("Síntomas",("Dolor vaginal","Comezón vaginal","Dolor con las relaciones sexuales","Flujo vaginal anormal"))
  if "Dolor vaginal" in sintomas:
    st.image("medpost.gif")
  if "Comezón vaginal" in sintomas:
    st.write("Rascaste")
if "Dolor vaginal" and "Comezón vaginal" in sintomas:
    st.multiselect("Alguna enfermedad que padezcas",("Diabetes mellitus","Estoy embarazada"))