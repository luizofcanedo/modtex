import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy import URL
import palavras_indesejadas
import streamlit as st

url_object = URL.create(
    "postgresql+psycopg2",
    username='luizotavio',
    password='',
    host='localhost',
    port='5432',
    database='stellantis'
)
engine = create_engine(url_object)

query = """
        SELECT "ac_des_atendimento" as ordem_servico, \
               "ac_nom_marca"       as marca, \
               "os_num_km_atual"    as km_medio
        FROM public.grow_os; \
        """


@st.cache_data(ttl=3600)
def contagem_palavras(filter=False, target_word=None, marca_alvo=None, sorted=False):
    if filter == False:
        df = pd.read_sql(query, engine)

        df['ordem_servico'] = df['ordem_servico'].astype(str).str.lower()
        df_exploded = df.assign(words=df['ordem_servico'].str.split()).explode('words')
        df_exploded = df_exploded.dropna(subset=['words'])

        df_exploded['words'] = df_exploded['words'].str.replace(r'[^\w\s]', '', regex=True)
        df_exploded = df_exploded[~df_exploded['words'].str.contains(r'\d', regex=True)]
        palavras_ruins = set(palavras_indesejadas.palavras_indesejadas())
        df_clean = df_exploded[~df_exploded['words'].isin(palavras_ruins)].copy()
        df_clean = df_clean[df_clean['words'] != '']
        df_contagem = df_clean.groupby(['marca', 'words']).size().reset_index(name='contagem')

        return df_contagem

    else:
        df = pd.read_sql(query, engine)

        df_filtrado_palavra = df[df['ordem_servico'].str.contains(target_word, case=False)]

        df_filtrado_palavra['ordem_servico'] = df_filtrado_palavra['ordem_servico'].astype(str).str.lower()
        df_exploded = df_filtrado_palavra.assign(words=df_filtrado_palavra['ordem_servico'].str.split()).explode(
            'words')
        df_exploded = df_exploded.dropna(subset=['words'])
        df_exploded = df_exploded[df_exploded['words'] != target_word]

        df_exploded['words'] = df_exploded['words'].str.replace(r'[^\w\s]', '', regex=True)
        df_exploded = df_exploded[~df_exploded['words'].str.contains(r'\d', regex=True)]
        palavras_ruins = set(palavras_indesejadas.palavras_indesejadas())
        df_clean = df_exploded[~df_exploded['words'].isin(palavras_ruins)].copy()
        df_clean = df_clean[df_clean['words'] != '']
        df_contagem = df_clean.groupby(['words']).size().reset_index(name='contagem')

        if sorted == True:
            df_sorted = df_contagem.sort_values(by='contagem', ascending=False).head(10)

        return df_sorted


def calcular_lift_por_marca(marca_alvo, n, sort=bool):
    df_completo = contagem_palavras()

    matriz = df_completo.pivot_table(
        index='words',
        columns='marca',
        values='contagem',
        fill_value=0
    )

    matriz = matriz[matriz.sum(axis=1) > 50]

    smoothing = 1e-6

    freq_relativa = (matriz + smoothing).div((matriz + smoothing).sum(axis=0), axis=1)
    freq_global = freq_relativa.mean(axis=1)
    lift = freq_relativa.div(freq_global, axis=0)

    score_log = np.log(lift)

    resultado = score_log[marca_alvo].sort_values(ascending=sort).head(n)
    return resultado


def km_medio(target_word, marca_alvo):
    df = pd.read_sql(query, engine)
    df_filtrado_palavra = df[df['ordem_servico'].str.contains(target_word, case=False)]
    df_filtrado_marca = df_filtrado_palavra[df_filtrado_palavra['marca'].str.contains(marca_alvo, case=False)]
    km_medio = df_filtrado_marca['km_medio'].mean()

    return km_medio


def marcas_associadas(target_word, marca_alvo):
    df = pd.read_sql(query, engine)
    df_filtrado_palavra = df[df['ordem_servico'].str.contains(target_word, case=False)]
    df_filtrado_marca = df_filtrado_palavra[df_filtrado_palavra['marca'] != marca_alvo]
    df_counter = df_filtrado_marca.groupby(['marca']).size().reset_index(name='contagem')
    df_sorted = df_counter.sort_values(by='contagem', ascending=False)

    return df_sorted


def obter_score_palavra(marca_alvo, palavra_alvo):
    df_completo = contagem_palavras()

    matriz = df_completo.pivot_table(
        index='words',
        columns='marca',
        values='contagem',
        fill_value=0
    )

    matriz = matriz[matriz.sum(axis=1) > 50]

    smoothing = 1e-6
    freq_relativa = (matriz + smoothing).div((matriz + smoothing).sum(axis=0), axis=1)
    freq_global = freq_relativa.mean(axis=1)
    lift = freq_relativa.div(freq_global, axis=0)

    score_log = np.log(lift)

    palavra_alvo = palavra_alvo.lower()

    try:
        score = score_log.loc[palavra_alvo, marca_alvo]
        return score
    except KeyError:
        return 0.0