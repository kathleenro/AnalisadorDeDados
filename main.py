import streamlit as st
import pandas as pd
import plotly.express as px

# ================== 🎨 Estilo e Layout ==================
st.set_page_config(page_title="Analisador de Dados", layout="wide")

# Estilo CSS personalizado
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f9f9f9;
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Banner ou logo (se quiser usar uma imagem, insira o link direto dela)
st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Placeholder.png/800px-Placeholder.png', width=200)

# Título estilizado
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🔍 Analisador de Dados Interativo</h1>",
    unsafe_allow_html=True
)

# Descrição / Boas-vindas
st.markdown(
    """
    <div style='text-align: center;'>
        <h4>📊 Suba sua planilha (.csv ou .xlsx) e gere insights instantâneos!</h4>
        <p>Veja dados, estatísticas e gráficos em poucos cliques.</p>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("---")


# ================== 🚀 Funcionalidade ==================
# Upload do arquivo
st.subheader('📥 Faça upload da sua planilha (.csv ou .xlsx)')
arquivo = st.file_uploader("Escolha o arquivo", type=['csv', 'xlsx'])

if arquivo is not None:
    try:
        # Leitura da planilha
        if arquivo.name.endswith('.csv'):
            df = pd.read_csv(arquivo)
        else:
            df = pd.read_excel(arquivo)

        st.success('✅ Arquivo carregado com sucesso!')

        # ================== 📄 Exibir dados ==================
        st.subheader('📄 Dados da Planilha')
        st.dataframe(df)

        # ================== 📊 Estatísticas ==================
        st.subheader('📊 Estatísticas Descritivas')
        st.write(df.describe())

        # ================== 📈 Gráficos ==================
        st.subheader('📈 Gerador de Gráficos')

        coluna = st.selectbox('Selecione uma coluna para visualizar:', df.columns)

        tipo_grafico = st.selectbox('Escolha o tipo de gráfico:', ['Histograma', 'Barras', 'Pizza'])

        if tipo_grafico == 'Histograma':
            fig = px.histogram(df, x=coluna)
            st.plotly_chart(fig)

        elif tipo_grafico == 'Barras':
            contagem = df[coluna].value_counts().reset_index()
            contagem.columns = [coluna, 'Contagem']
            fig = px.bar(contagem, x=coluna, y='Contagem')
            st.plotly_chart(fig)

        elif tipo_grafico == 'Pizza':
            contagem = df[coluna].value_counts().reset_index()
            contagem.columns = [coluna, 'Contagem']
            fig = px.pie(contagem, names=coluna, values='Contagem')
            st.plotly_chart(fig)

    except Exception as e:
        st.error(f'❌ Erro ao ler o arquivo: {e}')

else:
    st.info('ℹ️ Aguardando você enviar um arquivo CSV ou Excel.')
