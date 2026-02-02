import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import pandas as pd
import words_list

st.set_page_config(
    page_title="Modelos Textuais",
    page_icon="📚",
    layout="wide",
)

st.markdown("""
    <style>
    [data-testid="stMetricValue"] {
        font-size: 25px;
    }
    </style>
""", unsafe_allow_html=True)

def carregar_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

carregar_css("assets/style.css")

col1, col2, col3 = st.columns(3, gap="large")

# BOTÕES DE CIMA
with col1:
    st.markdown("""
        <div style="text-align: center;">
            <button class="btn-base fiat" onclick="alert('Fiat selecionado')"></button>
        </div>
    """, unsafe_allow_html=True)

    st.space('small')
    
    sub_col1, sub_col2 = st.columns(2, border=True)

    with sub_col1:
        top_words = words_list.calcular_lift_por_marca('Fiat', 1, sort=False)
        palavra_top = top_words.index[0]
        score_top = top_words.values[0]
        
        st.metric(
            label="Palavra mais recorrente",
            value=palavra_top,
            delta=f"{score_top:.2f}",
            delta_color="normal",
            width="stretch",
        )

    with sub_col2:
        bot_words = words_list.calcular_lift_por_marca('Fiat', 1, sort=True)
        palavra_bot = bot_words.index[0]
        score_bot = bot_words.values[0]

        st.metric(
            label="Palavra menos recorrente", 
            value=palavra_bot, 
            delta=f"{score_bot:.2f}", 
            delta_color="normal",
            width="stretch",
        )

with col2:
    st.markdown("""
        <div style="text-align: center;">
            <button class="btn-base jeep" onclick="alert('Jeep selecionado')"></button>
        </div>
    """, unsafe_allow_html=True)

    st.space('small')
    
    sub_col1, sub_col2 = st.columns(2, border=True)

    with sub_col1:
        top_words = words_list.calcular_lift_por_marca('Jeep', 1, sort=False)
        palavra_top = top_words.index[0]
        score_top = top_words.values[0]
        
        st.metric(
            label="Palavra mais recorrente",
            value=palavra_top,
            delta=f"{score_top:.2f}",
            delta_color="normal",
            width="stretch",
        )

    with sub_col2:
        bot_words = words_list.calcular_lift_por_marca('Jeep', 1, sort=True)
        palavra_bot = bot_words.index[0]
        score_bot = bot_words.values[0]
        
        st.metric(
            label="Palavra menos recorrente", 
            value=palavra_bot, 
            delta=f"{score_bot:.2f}", 
            delta_color="normal",
            width="stretch",
        )

with col3:
    st.markdown("""
        <div style="text-align: center;">
            <button class="btn-base peugeot" onclick="alert('Peugeot selecionado')"></button>
        </div>
    """, unsafe_allow_html=True)

    st.space('small')
    
    sub_col1, sub_col2 = st.columns(2, border=True)

    with sub_col1:
        top_words = words_list.calcular_lift_por_marca('Peugeot', 1, sort=False)
        palavra_top = top_words.index[0]
        score_top = top_words.values[0]
        
        st.metric(
            label="Palavra mais recorrente",
            value=palavra_top,
            delta=f"{score_top:.2f}",
            delta_color="normal",
            width="stretch",
        )

    with sub_col2:
        bot_words = words_list.calcular_lift_por_marca('Peugeot', 1, sort=True)
        palavra_bot = bot_words.index[0]
        score_bot = bot_words.values[0]
        
        st.metric(
            label="Palavra menos recorrente", 
            value=palavra_bot, 
            delta=f"{score_bot:.2f}", 
            delta_color="normal",
            width="stretch",
        )

#Espaço entre botões
st.space('large')

# BOTÕES DE BAIXO
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div style="text-align: center;">
            <button class="btn-base citroen" onclick="alert('Citroën selecionado')"></button>
        <div>       
""", unsafe_allow_html=True)
    
    st.space('small')
    
    sub_col1, sub_col2 = st.columns(2, border=True)

    with sub_col1:
        top_words = words_list.calcular_lift_por_marca('Citroen', 1, sort=False)
        palavra_top = top_words.index[0]
        score_top = top_words.values[0]
        
        st.metric(
            label="Palavra mais recorrente",
            value=palavra_top,
            delta=f"{score_top:.2f}",
            delta_color="normal",
            width="stretch",
        )

    with sub_col2:
        bot_words = words_list.calcular_lift_por_marca('Citroen', 1, sort=True)
        palavra_bot = bot_words.index[0]
        score_bot = bot_words.values[0]
        
        st.metric(
            label="Palavra menos recorrente", 
            value=palavra_bot, 
            delta=f"{score_bot:.2f}", 
            delta_color="normal",
            width="stretch",
        )

with col2:
    st.markdown("""
        <div style="text-align: center;">
            <button class="btn-base ram" onclick="alert('Ram selecionado')"></button>
        <div>       
""", unsafe_allow_html=True)
    
    st.space('small')
    
    sub_col1, sub_col2 = st.columns(2, border=True)

    with sub_col1:
        top_words = words_list.calcular_lift_por_marca('RAM', 1, sort=False)
        palavra_top = top_words.index[0]
        score_top = top_words.values[0]
        
        st.metric(
            label="Palavra mais recorrente",
            value=palavra_top,
            delta=f"{score_top:.2f}",
            delta_color="normal",
            width="stretch",
        )

    with sub_col2:
        bot_words = words_list.calcular_lift_por_marca('RAM', 1, sort=True)
        palavra_bot = bot_words.index[0]
        score_bot = bot_words.values[0]
        
        st.metric(
            label="Palavra menos recorrente", 
            value=palavra_bot, 
            delta=f"{score_bot:.2f}", 
            delta_color="normal",
            width="stretch",
        )