import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


day_df = pd.read_csv("dashboard/day.csv")
hour_df = pd.read_csv("dashboard/hour.csv")


st.title("Bikesharing")


st.header("Dataset Overview")
st.write("Sample data harian")
st.dataframe(day_df.head())
st.write("Sample data per jam")
st.dataframe(hour_df.head())


st.subheader("Missing Value")
st.write(day_df.isna().sum())
st.write(hour_df.isna().sum())
st.write("Tidak ada missing value")



st.header("Tren User Seiring Waktu")
st.write("Per Tahun")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
selected_year = st.slider("Pilih Tahun", 2011, 2012)
filtered_data = day_df[day_df['dteday'].dt.year == selected_year]
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='dteday', y='cnt', data=filtered_data, ax=ax)
ax.set_ylabel("Total User per Hari")
st.pyplot(fig)

st.header("Tren User Seiring Waktu")
st.write("Per Bulan")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
selected_month = st.selectbox("Pilih Bulan", list(range(1, 13)))
filtered_data = day_df[(day_df['dteday'].dt.year == selected_year) & (day_df['dteday'].dt.month == selected_month)]
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='dteday', y='cnt', data=filtered_data, ax=ax)
ax.set_ylabel("Total user per Hari")
st.pyplot(fig)


st.header("User Casual vs User Registered")
fig, ax = plt.subplots()
day_df[['casual', 'registered']].sum().plot(kind='bar', ax=ax, color=['blue', 'green'])
ax.set_ylabel("Total User")
st.pyplot(fig)




st.header("Fitur Korelasi Heatmap")
if st.checkbox("Tampilkan Correlation Matrix"):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(day_df.corr(), cmap='coolwarm', ax=ax)
    st.pyplot(fig)