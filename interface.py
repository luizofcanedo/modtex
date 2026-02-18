import streamlit as st
import words_list
from st_click_detector import click_detector
import visuals
import time

# -----------------------Configurações da página-----------------------#
st.set_page_config(
    page_title="Modelos Textuais",
    page_icon="📚",
    layout="wide",
)

# -----------------Criando meu próprio script de botão para as marcas -----------------#
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


# -----------------------------PÁGINA INICIAL-----------------------------#
marca_atual = st.session_state.get('marca_selecionada')

if not marca_atual:

    with st.spinner("Loading..."):
        time.sleep(1)

        col1, col2, col3 = st.columns(3, gap="large")

        # ---------------------BOTÕES DE CIMA-----------------------------#

        # BOTÃO FIAT
        with col1:
            is_fiat_active = botao_customizado("Fiat", "fiat")

            sub_col1, sub_col2 = st.columns(2, border=True)

            # DADOS FIAT TOP WORDS
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

            # DADOS FIAT BOT WORDS
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

        # BOTÃO JEEP
        with col2:
            is_jeep_active = botao_customizado("Jeep", "jeep")

            sub_col1, sub_col2 = st.columns(2, border=True)

            # DADOS JEEP TOP WORDS
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

            # DADOS JEEP BOT WORDS
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

        # BOTÃO PEUGEOT
        with col3:
            is_peugeot_active = botao_customizado("Peugeot", "peugeot")

            sub_col1, sub_col2 = st.columns(2, border=True)

            # DADOS PEUGEOT TOP WORDS
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

            # DADOS PEUGEOT BOT WORDS
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

        # ESPAÇO ENTRE BOTÕES
        st.space('large')
        # ESPAÇO ENTRE BOTÕES

        # BOTÕES DE BAIXO
        col1, col2 = st.columns(2, gap="large")

        # BOTÃO CITROEN
        with col1:
            is_citroen_active = botao_customizado("Citroen", "citroen")

            sub_col1, sub_col2 = st.columns(2, border=True)

            # DADOS CITROEN TOP WORDS
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

        # DADOS CITROEN BOT WORDS
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

        # BOTÅO RAM
        with col2:
            is_ram_active = botao_customizado("Ram", "ram")

            sub_col1, sub_col2 = st.columns(2, border=True)

            # DADOS RAM TOP WORDS
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

            # DADOS RAM BOT WORDS
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

    # SESSION STATE BS
    if 'pagina_atual' not in st.session_state:
        st.session_state['pagina_atual'] = 'home'
    if 'botao_selecionado' not in st.session_state:
        st.session_state['botao_selecionado'] = None
    if 'valor_botao' not in st.session_state:
        st.session_state['valor_botao'] = None


    # -------------------------CONFIG BOTAO GENÉRICO----------------------------------#
    def botao_palavra(texto):
        st.markdown(f"""
                <div class="btn-base btn-word" style="width: 100%; height: 100px; margin-bottom: 10px;">
                {texto}
            </div>
            """, unsafe_allow_html=True)


    def botao_palavra_clicavel(palavra):
        id_limpo = palavra.replace(" ", "_").lower()
        btn_id = f"btn_{id_limpo}"

        html_code = f"""
            <style>{css_content}</style>
            <div style="display: flex; justify-content: center; width: 100%;">
                <a href="#" id="{btn_id}" style="text-decoration: none; width: 100%;">
                    <div class="btn-base btn-word" style="width: 100%; height: 80px; margin: 0;">
                        {palavra}
                    </div>
                </a>
            </div>
        """

        detector_response = click_detector(html_code)
        return detector_response == btn_id


    # --------------------------DEF PAGINA SUB-DETAILS-------------------------------#
    def sub_details():

        if marca_atual == 'Ram':
            marca_atual_atualizada = 'RAM'
        else:
            marca_atual_atualizada = marca_atual

        # EVOCANDO FUNC DE CALCULAR LIFT PRO PRIMEIRO USO
        valor_botao = st.session_state['valor_botao']
        target_word = st.session_state['botao_selecionado']

        df_palavras = words_list.contagem_palavras(filter=True, target_word=target_word, sorted=True)
        palavras = df_palavras['words']

        lista_palavras = []
        for i in range(0, 9):
            palavra = palavras.values[i]
            lista_palavras.append(palavra)

        #LISTA DE PALAVRAS (E VALORES) JÁ SELECIONADAS PARA USAR NA HORA DE VOLTAR PARA A PÁGINA ANTERIOR
        if 'palavras_ja_selecionadas' not in st.session_state:
            st.session_state['palavras_ja_selecionadas'] = []
        st.session_state['palavras_ja_selecionadas'].append(st.session_state.get('botao_selecionado'))
        if 'valores_palavras_anteriores' not in st.session_state:
            st.session_state['valores_palavras_anteriores'] = []
        st.session_state['valores_palavras_anteriores'].append(st.session_state.get('valor_botao'))

        # BOTÃO VOLTAR + MOSTRA DE DADOS DA PALAVRA SELECIONADA
        col_voltar, col_home, col_marca, col_vazia, col_palavra, col_vazia = st.columns([1, 1, 1, 5, 2, 8])
        with col_voltar:
            if st.button("<-"):

                if st.session_state.get('palavras_ja_selecionadas'):
                    tamanho_lista_palavras = len(st.session_state['palavras_ja_selecionadas'])
                    palavra_anterior = st.session_state['palavras_ja_selecionadas'][tamanho_lista_palavras - 1]
                    while palavra_anterior in st.session_state['palavras_ja_selecionadas']:
                        st.session_state['palavras_ja_selecionadas'].pop()

                    if st.session_state['valores_palavras_anteriores']:
                        tamanho_lista_valores = len(st.session_state['valores_palavras_anteriores'])
                        valor_anterior = st.session_state['valores_palavras_anteriores'][tamanho_lista_valores - 1]
                        while valor_anterior in st.session_state['valores_palavras_anteriores']:
                            st.session_state['valores_palavras_anteriores'].pop()

                    if not st.session_state['palavras_ja_selecionadas']:
                        st.session_state['pagina_atual'] = 'home'
                        st.session_state['valor_botao'] = None
                        st.session_state['botao_selecionado'] = None
                        st.rerun()

                    else:
                        tamanho_lista_palavras_def = len(st.session_state['palavras_ja_selecionadas'])
                        st.session_state['botao_selecionado'] = st.session_state['palavras_ja_selecionadas'][
                            tamanho_lista_palavras_def - 1]
                        tamanho_lista_valores_def = len(st.session_state['valores_palavras_anteriores'])
                        st.session_state['valor_botao'] = st.session_state['valores_palavras_anteriores'][
                            tamanho_lista_valores_def - 1]
                        st.rerun()

                else:
                    st.session_state['pagina_atual'] = 'home'
                    st.session_state['valor_botao'] = None
                    st.session_state['botao_selecionado'] = None
                    st.rerun()
        with col_home:
            if st.button("HOME"):
                st.session_state['palavras_ja_selecionadas'].clear()
                st.session_state['valores_palavras_anteriores'].clear()
                st.session_state['marca_selecionada'] = None
                st.session_state['pagina_atual'] = 'home'
                st.session_state['valor_botao'] = None
                st.session_state['botao_selecionado'] = None
                st.rerun()
        with col_marca:
            if st.button(f"{st.session_state.get('marca_selecionada')}"):
                st.session_state['palavras_ja_selecionadas'].clear()
                st.session_state['valores_palavras_anteriores'].clear()
                st.session_state['pagina_atual'] = 'home'
                st.session_state['valor_botao'] = None
                st.session_state['botao_selecionado'] = None
                st.rerun()
        with col_vazia:
            st.empty()
        with col_palavra:
            st.metric(
                label="Palavra selecionada",
                value=target_word,
                delta=f"{valor_botao:.2f}",
                border=True
            )
        st.space("medium")

        # PALAVRAS ATRELADAS À PALAVRA ESCOLHIDA
        col1, col2, col3 = st.columns(3, border=False)

        # --- COLUNA 1 --- #
        with col1:
            sub_col1, sub_col2 = st.columns([3, 1], border=False)
            with sub_col1:
                for i in range(0, 3):
                    with st.container(height=150, width=340, border=False, vertical_alignment="center"):
                        if botao_palavra_clicavel(palavras.values[i]):
                            st.session_state['botao_selecionado'] = lista_palavras[i]
                            st.session_state['valor_botao'] = words_list.obter_score_palavra(marca_atual_atualizada,
                                                                                             lista_palavras[i])
                            st.rerun()

        lista_porcentagens = []

        with sub_col2:
            for i in range(0, 3):
                porcentagem_palavra_relativa = words_list.porcentagem_palavras(target_word=target_word, palavra_relativa=lista_palavras[i])
                lista_porcentagens.append(porcentagem_palavra_relativa)

            st.space(13)
            with st.container(border=True, height=70, width=100):
                lista_porcentagens[0]
            st.space(65)
            with st.container(border=True, height=70, width=100):
                lista_porcentagens[1]
            st.space(65)
            with st.container(border=True, height=70, width=100):
                lista_porcentagens[2]

        # --- COLUNA 2 --- #
        with col2:
            sub_col3, sub_col4 = st.columns([3, 1])
            with sub_col3:
                for i in range(3, 6):
                    with st.container(height=150, width=340, border=False, vertical_alignment="center"):
                        if botao_palavra_clicavel(palavras.values[i]):
                            st.session_state['botao_selecionado'] = lista_palavras[i]
                            st.session_state['valor_botao'] = words_list.obter_score_palavra(marca_atual_atualizada,
                                                                                             lista_palavras[i])
                            st.rerun()

            with sub_col4:
                for i in range(3, 6):
                    porcentagem_palavra_relativa = words_list.porcentagem_palavras(target_word=target_word,
                                                                                   palavra_relativa=lista_palavras[i])
                    lista_porcentagens.append(porcentagem_palavra_relativa)

                st.space(13)
                with st.container(border=True, height=70, width=100):
                    lista_porcentagens[3]
                st.space(65)
                with st.container(border=True, height=70, width=100):
                    lista_porcentagens[4]
                st.space(65)
                with st.container(border=True, height=70, width=100):
                    lista_porcentagens[5]

        # --- COLUNA 3 --- #
        with col3:
            sub_col5, sub_col6 = st.columns([3, 1], border=False)
            with sub_col5:
                for i in range(6, 9):
                    with st.container(height=150, width=340, border=False, vertical_alignment="center"):
                        if botao_palavra_clicavel(palavras.values[i]):
                            st.session_state['botao_selecionado'] = lista_palavras[i]
                            st.session_state['valor_botao'] = words_list.obter_score_palavra(marca_atual_atualizada,
                                                                                             lista_palavras[i])
                            st.rerun()

            with sub_col6:
                for i in range(6, 9):
                    porcentagem_palavra_relativa = words_list.porcentagem_palavras(target_word=target_word,
                                                                                   palavra_relativa=lista_palavras[i])
                    lista_porcentagens.append(porcentagem_palavra_relativa)

                st.space(13)
                with st.container(border=True, height=70, width=100):
                    lista_porcentagens[6]
                st.space(65)
                with st.container(border=True, height=70, width=100):
                    lista_porcentagens[7]
                st.space(65)
                with st.container(border=True, height=70, width=100):
                    lista_porcentagens[8]


    # --------------------------CONFIG PÁGINA DE DETALHES DE CADA MARCA---------------#
    with st.spinner("Loading..."):
        time.sleep(1)

        # ---------------CONFIG DA PÁGINA HOME DE DETALHES----------------------------#
        if marca_atual:
            logo = visuals.links_logos(marca_atual)
            marca_cor = visuals.coes_marcas(marca_atual)

            # RAM PRECISA SER EDITADA PORQUE O NOME DELA NA DB NÃO SEGUE O PADRÃO DE LETRA MAIÚSCULA NO INICIO
            if st.session_state['pagina_atual'] == 'home':

                if marca_atual == 'Ram':
                    marca_atual_atualizada = 'RAM'
                else:
                    marca_atual_atualizada = marca_atual

                # SETANDO BOTÃO DE VOLTAR E LOGO PRA CADA MARCA NO TOPO DA PÁGINA
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

                # espaço vazio
                st.space()
                # espaço vazio

                # SETANDO DUAS COLUNAS PRINCIPAIS
                col_top_words, col_bot_words = st.columns(2, border=False)

                # COL TOP WORDS
                with col_top_words:

                    sc1, sc2, sc3 = st.columns(3)
                    with sc1:
                        st.subheader('TOP WORDS', anchor=False, divider=marca_cor)
                    with sc2:
                        st.subheader('SCORE', anchor=False, divider=marca_cor)
                    with sc3:
                        st.subheader('KM MÉDIO', anchor=False, divider=marca_cor)

                    # EVOCANDO FUNÇÃO LIFT + CRIANDO UM LOOP QUE CRIA UM BOTÃO PRA CADA PALAVRA MAIS USADA
                    top_words = words_list.calcular_lift_por_marca(marca_atual_atualizada, 10, sort=False)

                    sub_col_words, sub_col_scores, sub_col_km_medio = st.columns(3, vertical_alignment="top",
                                                                                 border=False)
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

                # COL BOT WORDS
                with col_bot_words:

                    sc1, sc2, sc3 = st.columns(3)
                    with sc1:
                        st.subheader('BOT WORDS', anchor=False, divider=marca_cor)
                    with sc2:
                        st.subheader('SCORE', anchor=False, divider=marca_cor)
                    with sc3:
                        st.subheader('MARCAS', anchor=False, divider=marca_cor)

                    # FAZENDO O MESMO QUE FIZ EM CIMA PORÉM PRAS BOT WORDS
                    sub_col_words, sub_col_scores, sub_col_marcas = st.columns(3, vertical_alignment="top",
                                                                               border=False)
                    for i in range(10):

                        bot_words = words_list.calcular_lift_por_marca(marca_atual_atualizada, 10, sort=True)
                        palavra_bot = bot_words.index[i]
                        score_bot = bot_words.values[i]

                        with sub_col_words:
                            if st.button(label=palavra_bot):
                                st.session_state['pagina_atual'] = 'detalhes_bot'
                                st.session_state['botao_selecionado'] = palavra_bot
                                st.session_state['valor_botao'] = score_bot
                                st.rerun()

                        with sub_col_scores:
                            badge_html = visuals.html_delta(score_bot)
                            st.markdown(badge_html, unsafe_allow_html=True)
                            st.space(size="stretch")

                        with sub_col_marcas:
                            marcas_associadas = words_list.marcas_associadas(palavra_bot, marca_atual)
                            st.markdown(marcas_associadas['marca'].values[0])
                            st.space("stretch")

            # -------------------------CONFIG DA PÁGINA SUB-DETAILS--------------------------------#
            elif st.session_state['pagina_atual'] == 'detalhes':
                sub_details()

            # -----------------CONFIG DA PÁGINA SUB-DETAILS PORÉM PARA PALAVRAS BOT----------------#
            elif st.session_state['pagina_atual'] == 'detalhes_bot':
                sub_details()