import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Analisador de Dados", layout="wide")

# Título
st.title('🔍 Analisador de Dados Interativo')

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

        # Exibir dados
        st.subheader('📄 Dados da Planilha')
        st.dataframe(df)

        # Estatísticas rápidas
        st.subheader('📊 Estatísticas Descritivas')
        st.write(df.describe())

        # Seletor de coluna para gráfico
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
    st.info('👆 Aguardando você enviar um arquivo CSV ou Excel.')
