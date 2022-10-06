
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # Gráficos interativos
import streamlit as st  # 🎈 data web app desenvolvimento
import mysql.connector


@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])


@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


conn = init_connection()


def estadosLista(x, tabela):
    query = run_query(f"SELECT {x} FROM {tabela}")
    result = []
    for item in query:
        result.append(str(item)[2:-3])

    return result
st.header("Modelagem de Dados - Dw Pedido")
pagina = st.sidebar.selectbox("Escolha das Páginas: ",("Questão1","Questão2","Questão3","Questão4","Questão5"))


def questao_1() :
    x = st.selectbox(
    "campos de consulta Geral: ",
    ("categoria_produto", "tipo_pagamento", "estado_sigla", "cidade", "nota_avaliacao","data_de_compra", "ano_numero", "mes_texto", 'mes_numero', 'mes_numero_ano' ,'dia_semana' , 'dia_semana_numero'
,'semana_numero_ano', 'dia_numero_mes', 'dia_numero_ano', 'semana_nome', 'dia_ehdiautil', 'semestre_texto' , 'semestre_numero', 'semestre_numero_ano', 'trimestre_texto', 'trimestre_numero', 'trimestre_numero_ano'),
)
    y = 'valorPedido'
    tabela = ''
    key = ''
    chaveTabela = 'key'
    if x == "categoria_produto":
        tabela = "dimproduto"
        key = "dimProduto_key"
    elif x == "nota_avaliacao":
        tabela = "dimavaliacao"
        key = "dimAvaliacao_key"
    elif x == 'tipo_pagamento':
        tabela = 'dimpagamento'
        key = "dimPagamento_key"
    elif x == 'cidade' or x == 'estado_sigla':
        tabela = 'dimlocalizacao'
        key = "dimLocalizacao_key"
    elif x == 'data_de_compra' or x == 'ano_numero' or x == 'mes_texto' or x == 'mes_numero' or x == 'mes_numero_ano' or x == 'dia_semana' or x == 'dia_semana_numero' or x == 'semana_numero_ano' or x == 'dia_numero_mes' or x == 'dia_numero_ano' or x == 'semana_nome' or x == 'dia_ehdiautil' or x == 'semestre_texto' or x == 'semestre_numero' or x == 'semestre_numero_ano' or x == 'trimestre_texto' or x == 'trimestre_numero' or x == 'trimestre_numero_ano':
        tabela = 'dimtempo'
        key = "dimAtempo_key"
        chaveTabela = 'key_data'
    query = run_query(
""" SELECT 
        COUNT({y}) AS quantidade_pedido  
        , t.{x} 
        , dt.dia_semana
    FROM fatopedido fp 
    LEFT JOIN {tabela} t ON t.{chaveTabela} = fp.{key} 
    LEFT JOIN dimtempo dt ON dt.key_data = fp.dimATempo_key
    GROUP BY 3,2
    ORDER BY 1 DESC;
""".format(
    x=x,
    y=y,
    tabela=tabela,
    chaveTabela=chaveTabela,
    key=key
)) 
    qtd,temp1,dia = [],[],[]
    for quantidade_pedido,temp,dia_semana in query:
        qtd.append(str(quantidade_pedido))
        temp1.append(str(temp))
        dia.append(str(dia_semana))
    df = pd.DataFrame(zip(qtd,temp1,dia), columns=['quantidade_pedido',x,'dia_semana'])
    st.markdown("Qual a quantidade de pedidos por campo selecionado, realizados de acordo com os dias da semana ou final de semana?")
    st.markdown("###  Bar Chart")
    fig1 =  px.bar(df,'dia_semana','quantidade_pedido',color = x) 
    st.write(fig1)

    st.markdown("### Scatter Chart")
    fig2 =  px.scatter(df,'quantidade_pedido', x,color = 'dia_semana',hover_name= x) 
    st.write(fig2)

    st.markdown("###  Data Frame")
    st.write(df)
    

def questao_2() :
    x = st.selectbox(
    "campos de consulta Geral: ",
    ("categoria_produto", "tipo_pagamento", "estado_sigla", "cidade", "nota_avaliacao","data_de_compra", "ano_numero", "mes_texto", 'mes_numero', 'mes_numero_ano' ,'dia_semana' , 'dia_semana_numero'
,'semana_numero_ano', 'dia_numero_mes', 'dia_numero_ano', 'semana_nome', 'dia_ehdiautil', 'semestre_texto' , 'semestre_numero', 'semestre_numero_ano', 'trimestre_texto', 'trimestre_numero', 'trimestre_numero_ano'),
)
    y = 'valorPedido'
    tabela = ''
    key = ''
    chaveTabela = 'key'
    if x == "categoria_produto":
        tabela = "dimproduto"
        key = "dimProduto_key"
    elif x == "nota_avaliacao":
        tabela = "dimavaliacao"
        key = "dimAvaliacao_key"
    elif x == 'tipo_pagamento':
        tabela = 'dimpagamento'
        key = "dimPagamento_key"
    elif x == 'cidade' or x == 'estado_sigla':
        tabela = 'dimlocalizacao'
        key = "dimLocalizacao_key"
    elif x == 'data_de_compra' or x == 'ano_numero' or x == 'mes_texto' or x == 'mes_numero' or x == 'mes_numero_ano' or x == 'dia_semana' or x == 'dia_semana_numero' or x == 'semana_numero_ano' or x == 'dia_numero_mes' or x == 'dia_numero_ano' or x == 'semana_nome' or x == 'dia_ehdiautil' or x == 'semestre_texto' or x == 'semestre_numero' or x == 'semestre_numero_ano' or x == 'trimestre_texto' or x == 'trimestre_numero' or x == 'trimestre_numero_ano':
        tabela = 'dimtempo'
        key = "dimAtempo_key"
        chaveTabela = 'key_data'
    query = run_query(
""" SELECT 
        COUNT(fp.{y}) AS quantidade_pedido
        , t.{x} 
        , dt.dia_ehdiautil
    FROM fatopedido fp
    LEFT JOIN {tabela} t ON t.{chaveTabela} = fp.{key} 
    LEFT JOIN dimtempo dt ON dt.key_data = fp.dimATempo_key
    GROUP BY 2,3
    ORDER BY 1 DESC;
""".format(
    x=x,
    y=y,
    tabela=tabela,
    chaveTabela=chaveTabela,
    key=key
)) 
 
    qtd,temp1,dia = [],[],[]
    for quantidade_pedido,temp,dia_semana in query:
        qtd.append(str(quantidade_pedido))
        temp1.append(str(temp))
        dia.append(str(dia_semana))
    df = pd.DataFrame(zip(qtd,temp1,dia), columns=['quantidade_pedido',x,'dia_ehdiautil'])

    st.markdown("Os períodos que ocorrem maior quantidade vendas por item selecionado no filtro estão relacionados a datas comemorativas?")

    st.markdown("###  Bar Chart")
    fig = px.bar(df, x=x, y='quantidade_pedido', color='dia_ehdiautil')
    st.write(fig)
    st.markdown("###  Scatter Chart")
    fig2 = px.scatter(df, x='quantidade_pedido', y=x, color='dia_ehdiautil')
    st.write(fig2)
    st.markdown("###  Data Frame")
    st.write(df)
    
    
def questao_3() :
    x = st.selectbox(
    "campos de consulta Geral: ",
    ("categoria_produto", "tipo_pagamento", "estado_sigla", "cidade", "nota_avaliacao","data_de_compra", "ano_numero", "mes_texto", 'mes_numero', 'mes_numero_ano' ,'dia_semana' , 'dia_semana_numero'
,'semana_numero_ano', 'dia_numero_mes', 'dia_numero_ano', 'semana_nome', 'dia_ehdiautil', 'semestre_texto' , 'semestre_numero', 'semestre_numero_ano', 'trimestre_texto', 'trimestre_numero', 'trimestre_numero_ano'),
)
    y = 'valorPedido'
    tabela = ''
    key = ''
    chaveTabela = 'key'
    if x == "categoria_produto":
        tabela = "dimproduto"
        key = "dimProduto_key"
    elif x == "nota_avaliacao":
        tabela = "dimavaliacao"
        key = "dimAvaliacao_key"
    elif x == 'tipo_pagamento':
        tabela = 'dimpagamento'
        key = "dimPagamento_key"
    elif x == 'cidade' or x == 'estado_sigla':
        tabela = 'dimlocalizacao'
        key = "dimLocalizacao_key"
    elif x == 'data_de_compra' or x == 'ano_numero' or x == 'mes_texto' or x == 'mes_numero' or x == 'mes_numero_ano' or x == 'dia_semana' or x == 'dia_semana_numero' or x == 'semana_numero_ano' or x == 'dia_numero_mes' or x == 'dia_numero_ano' or x == 'semana_nome' or x == 'dia_ehdiautil' or x == 'semestre_texto' or x == 'semestre_numero' or x == 'semestre_numero_ano' or x == 'trimestre_texto' or x == 'trimestre_numero' or x == 'trimestre_numero_ano':
        tabela = 'dimtempo'
        key = "dimAtempo_key"
        chaveTabela = 'key_data'
    query = run_query(
""" SELECT 
        COUNT(fp.{y}) AS quantidade_pedido
        , ROUND(AVG(da.nota_avaliacao),2) AS media_nota_avaliacao
        , dp.{x}
    FROM fatopedido fp
    LEFT JOIN dimavaliacao da ON da.key = fp.dimAvaliacao_key
    LEFT JOIN {tabela} dp ON dp.{chaveTabela} = fp.{key}
    GROUP BY 3
    ORDER BY 2 ;
""".format(
    x=x,
    y=y,
    tabela=tabela,
    chaveTabela=chaveTabela,
    key=key
)) 

    qtd,temp1,dia = [],[],[]
    for quantidade_pedido,temp,dia_semana in query:
        qtd.append(str(quantidade_pedido))
        temp1.append(str(temp))
        dia.append(str(dia_semana))

    df = pd.DataFrame(zip(qtd,temp1,dia), columns=['quantidade_pedido','media_nota_avaliacao', x])    
    
    st.write("Qual a média de avaliação dos pedidos por tipo selecionado")
    fig3_a = px.scatter(df, x=df.media_nota_avaliacao, y=df[x],size_max=100, color=df.media_nota_avaliacao)
    st.write(fig3_a)

    fig3_b = px.pie(df, values=df.media_nota_avaliacao, names=df[x])
    fig3_b.update_traces(textposition='inside')
    fig3_b.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    st.write(fig3_b)

    st.markdown("###  Data Frame")
    st.write(df)
    
    

def questao_4() :
    x = st.selectbox(
    "campos de consulta Geral: ",
    ("categoria_produto", "tipo_pagamento", "nota_avaliacao","data_de_compra", "ano_numero", "mes_texto", 'mes_numero', 'mes_numero_ano' ,'dia_semana' , 'dia_semana_numero'
,'semana_numero_ano', 'dia_numero_mes', 'dia_numero_ano', 'semana_nome', 'dia_ehdiautil', 'semestre_texto' , 'semestre_numero', 'semestre_numero_ano', 'trimestre_texto', 'trimestre_numero', 'trimestre_numero_ano'),
)
    y = 'valorPedido'
    tabela = ''
    key = ''
    chaveTabela = 'key'
    if x == "categoria_produto":
        tabela = "dimproduto"
        key = "dimProduto_key"
    elif x == "nota_avaliacao":
        tabela = "dimavaliacao"
        key = "dimAvaliacao_key"
    elif x == 'tipo_pagamento':
        tabela = 'dimpagamento'
        key = "dimPagamento_key"
    elif x == 'data_de_compra' or x == 'ano_numero' or x == 'mes_texto' or x == 'mes_numero' or x == 'mes_numero_ano' or x == 'dia_semana' or x == 'dia_semana_numero' or x == 'semana_numero_ano' or x == 'dia_numero_mes' or x == 'dia_numero_ano' or x == 'semana_nome' or x == 'dia_ehdiautil' or x == 'semestre_texto' or x == 'semestre_numero' or x == 'semestre_numero_ano' or x == 'trimestre_texto' or x == 'trimestre_numero' or x == 'trimestre_numero_ano':
        tabela = 'dimtempo'
        key = "dimAtempo_key"
        chaveTabela = 'key_data'
    query = run_query(
    """ SELECT 
            COUNT(fp.{y}) AS quantidade_pedido
            , dl.estado_sigla
            , dp.{x}
        FROM fatopedido fp
        LEFT JOIN dimlocalizacao dl ON dl.key = fp.dimLocalizacao_key
        LEFT JOIN {tabela} dp ON dp.{chaveTabela} = fp.{key}
        GROUP BY 2,3
        ORDER BY 1 DESC;
    """.format(
        x=x,
        y=y,
        tabela=tabela,
        chaveTabela=chaveTabela,
        key=key
)) 

    qtd,temp1,dia = [],[],[]
    for quantidade_pedido,temp,dia_semana in query:
        qtd.append(str(quantidade_pedido))
        temp1.append(str(temp))
        dia.append(str(dia_semana))
    df = pd.DataFrame(zip(qtd,temp1,dia), columns=['quantidade_pedido',  'estado_sigla', x])    
    st.markdown("Qual a quantidade de pedidos realizados por consulta de acordo com cada variável do filtro?")
    st.markdown("###  Bar Chart")
    fig4 =  px.histogram(df,'estado_sigla','quantidade_pedido', color=x) 
    st.write(fig4)
    st.markdown("###  Bar Scatter")
    fig41 =  px.scatter(df,'estado_sigla' ,'quantidade_pedido', color= x) 
    st.write(fig41)
    st.markdown("###  Data Frame")
    st.write(df)

def questao_5() :
    x = st.selectbox(
    "campos de consulta Geral: ",
    ("categoria_produto", "tipo_pagamento", "estado_sigla", "cidade", "nota_avaliacao"),
)
    y = 'valorPedido'
    tabela = ''
    key = ''
    chaveTabela = 'key'
    if x == "categoria_produto":
        tabela = "dimproduto"
        key = "dimProduto_key"
    elif x == "nota_avaliacao":
        tabela = "dimavaliacao"
        key = "dimAvaliacao_key"
    elif x == 'tipo_pagamento':
        tabela = 'dimpagamento'
        key = "dimPagamento_key"
    elif x == 'cidade' or x == 'estado_sigla':
        tabela = 'dimlocalizacao'
        key = "dimLocalizacao_key"
    query = run_query(
    """ 
    SELECT 
        COUNT(fp.{y}) AS quantidade_pedido
        , dp.{x}
        , CASE 
            WHEN DATE_FORMAT(data_de_compra, "%d/%m") >= '20/03' AND DATE_FORMAT(data_de_compra, "%d/%m") < '20/06'  THEN 'outono'
            WHEN DATE_FORMAT(data_de_compra, "%d/%m") >= '20/06' AND DATE_FORMAT(data_de_compra, "%d/%m") < '22/09'  THEN 'inverno'
            WHEN DATE_FORMAT(data_de_compra, "%d/%m") >= '22/09' AND DATE_FORMAT(data_de_compra, "%d/%m") < '21/12'  THEN 'primavera'
            ELSE 'verão' 
        END AS estacoes
    FROM fatopedido fp
    LEFT JOIN {tabela} dp ON dp.{chaveTabela} = fp.{key}
    LEFT JOIN dimtempo dt ON dt.key_data = fp.dimATempo_key
    GROUP BY 2, 3
    ORDER BY 1 DESC
    """.format(
        x=x,
        y=y,
        tabela=tabela,
        chaveTabela=chaveTabela,
        key=key
)) 

    qtd,temp1,dia = [],[],[]
    for quantidade_pedido,temp,dia_semana in query:
        qtd.append(str(quantidade_pedido))
        temp1.append(str(temp))
        dia.append(str(dia_semana))
    df = pd.DataFrame(zip(qtd,temp1,dia), columns=['quantidade_pedido',x,'estações'])
    st.markdown("Qual a quantidade de pedidos realizados de acordo com as estações do ano?")
    st.markdown("###  Bar Chart")
    fig = px.bar(df, x=x, y='quantidade_pedido', color='estações')
    st.write(fig)
    st.markdown("###  Scatter Chart")
    fig2 = px.scatter(df, x='quantidade_pedido', y=x, color="estações")
    st.write(fig2)
    st.markdown("###  Data Frame")
    st.write(df)

    

if pagina == "Questão1":
    st.write(questao_1())
    
elif pagina == "Questão2":
    st.write(questao_2())

elif pagina == "Questão3":
    st.write(questao_3())

elif pagina == "Questão4":
    st.write(questao_4())

elif pagina == "Questão5": 
   st.write(questao_5())

else:
    st.write("Página não encontrada")


