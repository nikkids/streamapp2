import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv("day.csv")


day_df['dteday'] = pd.to_datetime(day_df['dteday'])


st.title("Dashboard Bike Sharing")


st.sidebar.header("Filter")
selected_year = st.sidebar.selectbox("Pilih Tahun", day_df['dteday'].dt.year.unique())


data_filtered = day_df[day_df['dteday'].dt.year == selected_year]

st.subheader("PERTANYAAN BISNIS 1")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=data_filtered, x=data_filtered['dteday'].dt.strftime('%B'), y='registered', color='blue', label='Registered', errorbar=None)
sns.barplot(data=data_filtered, x=data_filtered['dteday'].dt.strftime('%B'), y='casual', color='orange', label='Casual', errorbar=None)
plt.xticks(rotation=45)
plt.xlabel("Bulan")
plt.ylabel("Total User")
plt.legend()
st.pyplot(fig)


Periode = data_filtered.copy()
Periode.set_index('dteday', inplace=True)
Periode_monthly = Periode.resample('M').mean().reset_index()

st.subheader("PERTANYAAN BISNIS 2")
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.scatterplot(x='dteday', y='registered', data=Periode_monthly, s=100, color='blue')
sns.lineplot(x='dteday', y='registered', data=Periode_monthly, linestyle='-')
plt.title('Rata-Rata Registrasi Tiap Bulan', fontsize=14)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Jumlah Registrasi Rata-Rata', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
st.pyplot(fig2)
