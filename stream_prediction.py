import pickle
import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler

# Membaca model dan scaler yang telah dilatih
prediction_model = pickle.load(open('prediksi_cuaca_model.sav', 'rb'))
scaler = pickle.load(open('prediksi_cuaca_scaler.sav', 'rb'))

# Judul halaman web
st.title('Prediksi Cuaca')

# Membagi kolom untuk input data
col1, col2 = st.columns(2)

# Input data numerik
with col1:
    precipitation = st.number_input('Input Nilai Presipitasi', min_value=0.0, step=0.1)
    temp_max = st.number_input('Input Suhu Maksimum', min_value=-100.0, max_value=50.0)

with col2:
    temp_min = st.number_input('Input Suhu Minimum', min_value=-100.0, max_value=50.0)
    wind = st.number_input('Input Kecepatan Angin', min_value=0.0, step=0.1)

# Variabel untuk menyimpan hasil prediksi
weather_message = ''

# Tombol untuk melakukan prediksi
if st.button('Lihat Hasil Prediksi'):
    # Standarisasi data input
    input_data = np.array([[precipitation, temp_max, temp_min, wind]])
    std_data = scaler.transform(input_data)

    # Prediksi cuaca berdasarkan input data
    weather_prediction = prediction_model.predict(std_data)

    # Interpretasi hasil prgitediksi
    if weather_prediction[0] == 0:
        weather_message = 'Cuaca cerah, aman untuk keluar rumah.'
    elif weather_prediction[0] == 1:
        weather_message = 'Cuaca mendung, aman untuk keluar rumah.'
    else:
        weather_message = 'Cuaca tidak aman untuk keluar rumah.'

    # Menampilkan hasil prediksi
    st.success(weather_message)
