import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from datetime import date

st.title("Pertemuan 10: Interaksi Streamlit dan Yahoo Finance")

kamus_ticker = {
    'GOOGL' : 'Google',
    'AAPL' : 'Apple Inc',
    'MCD' : "McDonald's Corp",
    'META' : "Meta Platforms Inc",
    'TLKM.JK' : 'Telkom Indonesia (Persero) Tbk PT',
    'BBNI.JK' : 'Bank Negara Indonesia (Persero) Tbk PT',
    'BMRI.JK' : 'Bank Mandiri (Persero) Tbk PT',
    'BBRI.JK' : 'Bank Rakyat Indonesia (Persero) Tbk PT',
    'NESN' : 'Nestle SA'
}

ticker_symbol = st.selectbox(
    'Silahkan pilih kode perusahaan: ',
    sorted( kamus_ticker.keys())
    # ['AAPL', 'GOOGL', 'META', ] -- sudah ga kepake, karena pake sorted kamus_ticker
)

#st.write(ticker_symbol)  --- bisa dipake untuk mengecek
#ticker_symbol ='GOOGL' -- sudah ga kepake, karena sudah pake selectbox
#ticker_symbol = 'AAPL' -- sudah ga kepake, karena sudah pake selectbox

ticker_data = yf.Ticker( ticker_symbol ) # mengambil data dari internet NASDAQ
pilihan_periode =st.selectbox(
    'Pilih Periode:',
    ['1d','5d','1mo','3mo','6mo','1y','2y']
)
tgl_mulai = st.date_input(
    'Mulai tanggal',
    value = date.today()
)
tgl_akhir = st.date_input(
    'Sampai tanggal',
    value = date.today()
)

df_ticker = ticker_data.history( # membuat data frame
    # period = '1d', -- sudah ga kepake, karena sudah pake selectbox date
    # start = '2024-11-01', -- sudah ga kepake, karena sudah pake selectbox date
    # end = '2024-11-08'  -- sudah ga kepake, karena sudah pake selectbox date
    period = pilihan_periode,
    start = str(tgl_mulai),
    end = str(tgl_akhir)
)

pilihan_tampil_tabel = st.checkbox('Tampilkan Tabel') # membuat checkbox dan disimpan di varibael 'pilihan_tampil_tabel'
# st.write(pilihan_tampil_tabel) --- bisa dipake untuk mengecek

if pilihan_tampil_tabel == True :
    st.write('## Lima Data Awal')
    st.write( df_ticker.head() ) # menampilkan head dari df_ticker

st.write(f'## Visualisasi Pergerakan Saham {kamus_ticker[ticker_symbol]}')

pilihan_atribut = st.multiselect(
    'Silahkan pilih atribut yang akan ditampilkan:',
    ['Low','High','Open','Close','Volume']
)

#st.write(pilihan_atribut) --- bisa dipake untuk mengecek
grafik = px.line( # membuat visualisasi line
    df_ticker, # data diambil dari df_ticker
    #y = ['Open', 'Close'], # x nya tanggal karena time series & nama string y sesuai kolom --- y sudah ga kepake, karena pake multiselect
    y = pilihan_atribut,
    #title = 'Harga Saham',
    title = f'Harga Saham {kamus_ticker[ticker_symbol]}'
)    
st.plotly_chart( grafik ) # menampilkan visualisasi



#gifthub.com
#share.streamlit.io
#git-scm.com
