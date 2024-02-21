import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Persiapkan data
data_sd = {
    'Lembaga Survey': ['Poltracking', 'LSI Denny JA', 'Indikator', 'LSI'],
    'Anies-Imin': [12.9, 14.5, 16.7, 19.7],
    'Prabowo-Gibran': [45.6, 47.3, 46.9, 45.5],
    'Ganjar-Mahfud': [36.1, 29.8, 30.5, 27.7],
    'Tidak Menjawab': [5.4, 0, 6.9, 7.1]
}

data_smp = {
    'Lembaga Survey': ['Poltracking', 'LSI Denny JA', 'Indikator', 'LSI'],
    'Anies-Imin': [22.7, 26.6, 19.7, 17.5],
    'Prabowo-Gibran': [46.9, 43.3, 43.5, 36.9],
    'Ganjar-Mahfud': [28.4, 23.4, 30.5, 33.6],
    'Tidak Menjawab': [2.0, 0, 6.3, 12.0]
}

data_sma = {
    'Lembaga Survey': ['Poltracking', 'LSI Denny JA', 'Indikator', 'LSI'],
    'Anies-Imin': [25.7, 33.8, 23.9, 21.7],
    'Prabowo-Gibran': [45.1, 43.8, 49.1, 54.4],
    'Ganjar-Mahfud': [24.3, 22.4, 22.5, 17.1],
    'Tidak Menjawab': [4.9, 0, 4.5, 6.8]
}

data_kuliah = {
    'Lembaga Survey': ['Poltracking', 'LSI Denny JA', 'Indikator', 'LSI'],
    'Anies-Imin': [39.7, 35.1, 41.3, 37.2],
    'Prabowo-Gibran': [36.9, 32.1, 40.7, 37.2],
    'Ganjar-Mahfud': [19.1, 23.2, 12.3, 15.4],
    'Tidak Menjawab': [4.3, 0, 5.6, 10.2]
}

data_elektabilitas = {
    'Lembaga Survey': ['Pemilih Rasional', 'Pemilih Psikologis', 'Pemilih Sosiologis'],
    'Anies-Imin': [24.9, 18.5, 29.2],
    'Prabowo-Gibran': [44.2, 49.8, 42.9],
    'Ganjar-Mahfud': [26.9, 28.7, 22.7],
    'Tidak Menjawab': [4, 3, 5.2]
}

data_tren_elektabilitas = {
    'Bulan': ['Feb', 'Mar', 'Apr', 'Jul', 'Sep', 'Nov', 'Dec'],
    'Anies-Imin': [25.3, 22.1, 22.4, 16.9, 16.6, 26.2, 24.9],
    'Prabowo-Gibran': [26.5, 27, 39.7, 39.5, 27, 38.6, 44.2],
    'Ganjar-Mahfud': [38.4, 37.7, 27.3, 31.6, 31.6, 30.5, 26.9],
}

# Konversi data menjadi dataframe
df_sd = pd.DataFrame(data_sd)
df_smp = pd.DataFrame(data_smp)
df_sma = pd.DataFrame(data_sma)
df_kuliah = pd.DataFrame(data_kuliah)
df_elektabilitas = pd.DataFrame(data_elektabilitas)
df_tren_elektabilitas = pd.DataFrame(data_tren_elektabilitas)

# Membuat grafik interaktif dengan Plotly
def create_interactive_chart_sd(df_sd):
    fig_sd = go.Figure()

    for candidate in df_sd.columns[1:]:
        fig_sd.add_trace(go.Bar(
            x=df_sd['Lembaga Survey'],
            y=df_sd[candidate],
            name=candidate
        ))

    fig_sd.update_layout(
        barmode='group',
        title="Elektabilitas Paslon di Pemilih Lulusan SD",
        xaxis_title="Lembaga Survey",
        yaxis_title="Percentage",
        legend_title="Paslon",
        hovermode="x"
    )

    return fig_sd

def create_interactive_chart_smp(df_smp):
    fig_smp = go.Figure()

    for candidate in df_smp.columns[1:]:
        fig_smp.add_trace(go.Bar(
            x=df_smp['Lembaga Survey'],
            y=df_smp[candidate],
            name=candidate
        ))

    fig_smp.update_layout(
        barmode='group',
        title="Elektabilitas Paslon di Pemilih Lulusan SMP",
        xaxis_title="Lembaga Survey",
        yaxis_title="Percentage",
        legend_title="Paslon",
        hovermode="x"
    )

    return fig_smp

def create_interactive_chart_sma(df_sma):
    fig_sma = go.Figure()

    for candidate in df_sma.columns[1:]:
        fig_sma.add_trace(go.Bar(
            x=df_sma['Lembaga Survey'],
            y=df_sma[candidate],
            name=candidate
        ))

    fig_sma.update_layout(
        barmode='group',
        title="Elektabilitas Paslon di Pemilih Lulusan SMA",
        xaxis_title="Lembaga Survey",
        yaxis_title="Percentage",
        legend_title="Paslon",
        hovermode="x"
    )

    return fig_sma

def create_interactive_chart_kuliah(df_kuliah):
    fig_kuliah = go.Figure()

    for candidate in df_kuliah.columns[1:]:
        fig_kuliah.add_trace(go.Bar(
            x=df_kuliah['Lembaga Survey'],
            y=df_kuliah[candidate],
            name=candidate
        ))

    fig_kuliah.update_layout(
        barmode='group',
        title="Elektabilitas Paslon di Pemilih yang Kuliah",
        xaxis_title="Lembaga Survey",
        yaxis_title="Percentage",
        legend_title="Paslon",
        hovermode="x"
    )

    return fig_kuliah

def create_interactive_chart_kuliah(df_elektabilitas):
    fig_elektabilitas = go.Figure()

    for candidate in df_elektabilitas.columns[1:]:
        fig_elektabilitas.add_trace(go.Bar(
            x=df_elektabilitas['Lembaga Survey'],
            y=df_elektabilitas[candidate],
            name=candidate
        ))

    fig_elektabilitas.update_layout(
        barmode='group',
        title="Elektabilitas Paslon berdasarkan Tipologi Versi Poltracking",
        xaxis_title="Tipologi",
        yaxis_title="Percentage",
        legend_title="Paslon",
        hovermode="x"
    )

    return fig_elektabilitas

def create_smooth_line_chart(df):
    fig = px.line(df, x='Bulan', y=df.columns[1:], title="Tren Elektabilitas Paslon",
                  markers=True, line_shape='spline')

    fig.update_layout(
        yaxis=dict(range=[10, 45]),  # Set nilai maksimum sumbu y
        xaxis_title="Bulan",
        yaxis_title="Percentage",
        legend_title="Paslon"
    )

    return fig

# Menampilkan grafik interaktif menggunakan Streamlit
st.title("Tsunami Data Eaa")
fig_sd = create_interactive_chart_sd(df_sd)
fig_smp = create_interactive_chart_smp(df_smp)
fig_sma = create_interactive_chart_sma(df_sma)
fig_kuliah = create_interactive_chart_kuliah(df_kuliah)
fig_elektabilitas = create_interactive_chart_kuliah(df_elektabilitas)
fig = create_smooth_line_chart(df_tren_elektabilitas)

st.plotly_chart(fig_sd)
st.plotly_chart(fig_smp)
st.plotly_chart(fig_sma)
st.plotly_chart(fig_kuliah)
st.plotly_chart(fig_elektabilitas)
st.plotly_chart(fig)

st.markdown("<footer style='text-align: center; padding-top: 20px;'>Made by Human | <a href='https://www.datawrapper.de/_/qtKv1/'>Data Source</a></footer>", unsafe_allow_html=True)