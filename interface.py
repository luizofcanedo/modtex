import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import pandas as pd
import words_list
from st_click_detector import click_detector
import visuals
import time

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

with open("assets/style.css") as f:
    css_content = f.read()
st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)

def botao_customizado(nome_marca, css_class):
    btn_id = f"btn_{css_class}"
    
    html_code = f"""
        <style>
            {css_content}
        </style>
        
        <div style="display: flex; justify-content: center; margin-bottom: 10px;">
            <a href="#" id="{btn_id}" style="text-decoration: none;">
                <div class="btn-base {css_class}"></div>
            </a>
        </div>
    """

    detector_response = click_detector(html_code)
    
    if detector_response == btn_id:
        if st.session_state.get('marca_selecionada') != nome_marca:
            st.session_state['marca_selecionada'] = nome_marca
            st.rerun()
            return True
    return st.session_state.get('marca_selecionada') == nome_marca

marca_atual = st.session_state.get('marca_selecionada')

if not marca_atual:

    with st.spinner("Loading..."):
        time.sleep(1)

        col1, col2, col3 = st.columns(3, gap="large")

        # BOTÕES DE CIMA
        with col1:

            is_fiat_active = botao_customizado("Fiat", "fiat")
        
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
        
            is_jeep_active = botao_customizado("Jeep", "jeep")
        
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
        
            is_peugeot_active = botao_customizado("Peugeot", "peugeot")
        
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
        
            is_citroen_active = botao_customizado("Citroen", "citroen")
        
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
        
            is_ram_active = botao_customizado("Ram", "ram")
        
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

else:

    with st.spinner("Loading..."):
        time.sleep(1)

        if 'pagina_atual' not in st.session_state:
            st.session_state['pagina_atual'] = 'home'
        if 'botao_selecionado' not in st.session_state:
            st.session_state['botao_selecionado'] = None
        if 'valor_botao' not in st.session_state:
            st.session_state['valor_botao'] = None

        if marca_atual:
            logo = visuals.links_logos(marca_atual)
            marca_cor = visuals.coes_marcas(marca_atual)

            if st.session_state['pagina_atual'] == 'home':

                if marca_atual == 'Ram':
                    marca_atual_atualizada = 'RAM'
                else:
                    marca_atual_atualizada = marca_atual
                
                col_voltar, col_vazia, col_logo, col_vazia = st.columns([1, 3, 1, 4], border=False)
                with col_voltar:
                    if st.button("<-"):
                        st.session_state['marca_selecionada'] = None
                        st.rerun()
                with col_logo:
                    if marca_atual == 'Peugeot':
                        st.image(logo, width=110)
                    elif marca_atual == 'Ram':
                        st.image(logo, width=250)
                    elif marca_atual == 'Jeep':
                        st.image(logo, width=200)
                    else:
                        st.image(logo, width=150)
                with col_vazia:
                    st.empty()

                st.space()

                col_top_words, col_bot_words = st.columns(2, border=False)
                with col_top_words:
                    
                    sc1, sc2, sc3 = st.columns(3)
                    with sc1:
                        st.subheader('TOP WORDS', anchor=False, divider=marca_cor)
                    with sc2:
                        st.subheader('SCORE', anchor=False, divider=marca_cor)
                    with sc3:
                        st.subheader('KM MÉDIO', anchor=False, divider=marca_cor)

                    top_words = words_list.calcular_lift_por_marca(marca_atual_atualizada, 10, sort=False)

                    sub_col_words, sub_col_scores, sub_col_km_medio = st.columns(3, vertical_alignment="top", border=False)
                    for i in range(10):

                        palavra_top = top_words.index[i]
                        score_top = top_words.values[i]
                    
                        with sub_col_words:
                            if st.button(label=palavra_top):
                                st.session_state['pagina_atual'] = 'detalhes'
                                st.session_state['botao_selecionado'] = palavra_top
                                st.session_state['valor_botao'] = score_top
                                st.rerun()
                    
                        with sub_col_scores:
                            badge_html = visuals.html_delta(score_top)
                            st.markdown(badge_html, unsafe_allow_html=True)
                            st.space(size="stretch")
                        
                        with sub_col_km_medio:
                            km_medio = words_list.km_medio(target_word=palavra_top, marca_alvo=marca_atual)
                            st.markdown(f"{km_medio:.0f}")
                            st.space(size="stretch")

                with col_bot_words:

                    sc1, sc2, sc3 = st.columns(3)
                    with sc1:
                        st.subheader('BOT WORDS', anchor=False, divider=marca_cor)
                    with sc2:
                        st.subheader('SCORE', anchor=False, divider=marca_cor)
                    with sc3:
                        st.subheader('MARCAS', anchor=False, divider=marca_cor)
                    
                    sub_col_words, sub_col_scores, sub_col_marcas = st.columns(3, vertical_alignment="top", border=False)
                    for i in range(10):
                        
                        bot_words = words_list.calcular_lift_por_marca(marca_atual_atualizada, 10, sort=True)
                        palavra_bot = bot_words.index[i]
                        score_bot = bot_words.values[i]
                    
                        with sub_col_words:
                            if st.button(label=palavra_bot):
                                st.write("Em construção")
                    
                        with sub_col_scores:
                            badge_html = visuals.html_delta(score_bot)
                            st.markdown(badge_html, unsafe_allow_html=True)
                            st.space(size="stretch")

                        with sub_col_marcas:
                            marcas_associadas = words_list.marcas_associadas(palavra_bot, marca_atual)
                            st.markdown(marcas_associadas['marca'].values[0])
                            st.space("stretch")

            elif st.session_state['pagina_atual'] == 'detalhes':
                botao = st.session_state['botao_selecionado']
                valor_botao = st.session_state['valor_botao']

                if marca_atual == 'Ram':
                    marca_atual_atualizada = 'RAM'
                else:
                    marca_atual_atualizada = marca_atual

                top_words = words_list.calcular_lift_por_marca(marca_atual_atualizada, 12, sort=False)

                col_voltar, col_vazia, col_palavra, col_vazia = st.columns([1, 3, 1, 4])
                with col_voltar:
                    if st.button("<-"):
                        st.session_state['pagina_atual'] = 'home'
                        st.session_state['botao_selecionado'] = None
                        st.session_state['valor_botao'] = None
                        st.rerun()
                with col_vazia:
                    st.empty()
                with col_palavra:
                    st.metric(
                        label="Palavra selecionada",
                        value=botao,
                        delta=f"{valor_botao:.2f}",
                        border=True
                    )
                st.space("medium")

                col1, col2, col3 = st.columns(3)
                with col1:
                    for i in range(0, 4):
                        with st.container(border=True):
                            palavra_relacionada = top_words.index[i]
                            st.subheader(f"{palavra_relacionada}", width="stretch")
                            st.space("stretch")
                with col2:
                    for i in range(4, 8):
                        with st.container(border=True):
                            palavra_relacionada = top_words.index[i]
                            st.subheader(f"{palavra_relacionada}", width="stretch")
                            st.space("stretch")
                with col3:
                    for i in range(8, 12):
                        with st.container(border=True):
                            palavra_relacionada = top_words.index[i]
                            st.subheader(f"{palavra_relacionada}", width="stretch")
                            st.space("stretch")