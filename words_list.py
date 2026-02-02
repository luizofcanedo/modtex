import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy import URL
import palavras_indesejadas

url_object = URL.create(
    "postgresql+psycopg2",
    username='luizotavio',
    password='',
    host='localhost',
    port='5432',
    database='stellantis'
)
engine = create_engine(url_object)

def contagem_palavras():
    query = """
        SELECT
            "ac_des_atendimento" as ordem_servico, "ac_nom_marca" as marca
        FROM
            public.grow_os;
    """

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

def calcular_lift_por_marca(marca_alvo, n, sort=bool):
    df_completo = contagem_palavras()

    matriz = df_completo.pivot_table(
        index='words',
        columns='marca', 
        values='contagem', 
        fill_value=0
    )
    
    matriz = matriz[matriz.sum(axis=1) > 5]

    smoothing = 1e-6
    
    freq_relativa = (matriz+smoothing).div((matriz+smoothing).sum(axis=0), axis=1)
    freq_global = freq_relativa.mean(axis=1)
    lift = freq_relativa.div(freq_global, axis=0)
    
    score_log = np.log(lift)

    resultado = score_log[marca_alvo].sort_values(ascending=sort).head(n)
    return resultado