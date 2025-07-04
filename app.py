import streamlit as st
import pandas as pd
import os

FILE_PATH = 'tasks.csv'

# Load tasks
def load_tasks():
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    else:
        return pd.DataFrame(columns=['Judul', 'Deskripsi', 'Deadline', 'Status'])

# Save tasks
def save_tasks(df):
    df.to_csv(FILE_PATH, index=False)

# App
st.set_page_config(page_title="Manajemen Tugas", layout="wide")
st.title("📋 Aplikasi Manajemen Tugas")

df = load_tasks()

# Tambah Tugas
with st.form("form_tugas"):
    st.subheader("Tambah Tugas Baru")
    judul = st.text_input("Judul Tugas")
    deskripsi = st.text_area("Deskripsi")
    deadline = st.date_input("Deadline")
    status = st.selectbox("Status", ["Belum Selesai", "Selesai"])
    submitted = st.form_submit_button("Simpan Tugas")

    if submitted and judul:
        df.loc[len(df)] = [judul, deskripsi, str(deadline), status]
        save_tasks(df)
        st.success("Tugas berhasil ditambahkan!")

# Tampilkan Tugas
st.subheader("📄 Daftar Tugas")

if df.empty:
    st.info("Belum ada tugas.")
else:
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
    save_tasks(edited_df)

# Hapus Semua
if st.button("🗑 Hapus Semua Tugas"):
    df = df[0:0]
    save_tasks(df)
    st.warning("Semua tugas telah dihapus!")

