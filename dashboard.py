import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set_theme(style='dark')

# Define Function
def create_bycity_df(df):
    bycity_df = df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False).reset_index()
    return bycity_df

def create_bypayment_df(df):
    bypayment_df = df.groupby(by="payment_type").order_id.nunique().sort_values(ascending=False).reset_index()
    return bypayment_df

# Import Data
city_df = pd.read_csv("E:\VSC\Dicoding\olist_customers_dataset.csv")
payment_df = pd.read_csv("E:\VSC\Dicoding\olist_order_payments_dataset.csv")

# Import gambar
st.image("https://storage.googleapis.com/kaggle-datasets-images/55151/105464/d59245a7014a35a35cc7f7b721de4dae/dataset-cover.png?t=2018-09-21-16-21-21")

# Sidebar
st.sidebar.header("Dashboard Proyek Analisis Data")
st.sidebar.write("""- **Nama:** Joan Jalu Pangestu
- **Email:** m002d4ky2304@bangkit.academy
- **ID Dicoding:** joanjalup""")

# Main
bycity_df = create_bycity_df(city_df)
bypayment_df = create_bypayment_df(payment_df) 

# Add Features
st.header('Dashboard Proyek Analisis Data')

# Customer City Info
st.subheader("Customer City Info")
[col_1] = st.columns(1)
with col_1:
    fig, ax = plt.subplots(figsize=(20,10))
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    sns.barplot(
        y="customer_id",
        x="customer_city",
        data=bycity_df.head(6),
        palette=colors,
        ax=ax
    )
    ax.set_title("Number of Customer by City", loc="center", fontsize=15)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=12)
    st.pyplot(fig)
fig, ax = plt.subplots(figsize=(20, 10))
st.markdown("Dapat dilihat dari grafik di atas, mayoritas customer kita berasal dari kota Sao Paulo")


# Payment Info
st.subheader("Payment Info")
[col_1] = st.columns(1)
with col_1:
    fig, ax = plt.subplots(figsize=(20,10))
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    sns.barplot(
    y="order_id",
    x="payment_type",
    data=bypayment_df,
    palette=colors
    )
    ax.set_title("Number of Payment Type", loc="center", fontsize=15)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=12)
    st.pyplot(fig)
fig,ax = plt.subplots(figsize=(20, 10))
st.markdown("Dapat dilihat dari grafik di atas, tipe pembayaran yang paling banyak digunakan adalah Kartu kredit dan yang paling sedikit adalah pembayaran lain-lain namun yang terdefinisi adalah kartu debit.")