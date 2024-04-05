import streamlit as st
import pandas as pd
import pickle

def main():
    # Title
    st.title("Prediksi Rating Cokelat")


        # Load model KNN dari berkas .pkl
    @st.cache(allow_output_mutation=True)
    def load_model():
        with open('knn1.pkl', 'rb') as f:
            model = pickle.load(f)
        return model

    # Fungsi untuk membuat prediksi
    def predict_rating(cocoa_percent, selected_ingredients):
        knn_model = load_model()
        # Buat DataFrame dari data input
        data = {'cocoa_percent': [cocoa_percent]}
        all_ingredients = [
                'ingredients_1- B', 'ingredients_2- B,C', 'ingredients_2- B,S',
                'ingredients_2- B,S*', 'ingredients_3- B,S*,C', 'ingredients_3- B,S*,Sa',
                'ingredients_3- B,S,C', 'ingredients_3- B,S,L', 'ingredients_3- B,S,V',
                'ingredients_4- B,S*,C,L', 'ingredients_4- B,S*,C,Sa', 'ingredients_4- B,S*,C,V',
                'ingredients_4- B,S*,V,L', 'ingredients_4- B,S,C,L', 'ingredients_4- B,S,C,Sa',
                'ingredients_4- B,S,C,V', 'ingredients_4- B,S,V,L', 'ingredients_5- B,S,C,L,Sa',
                'ingredients_5- B,S,C,V,L', 'ingredients_5- B,S,C,V,Sa', 'ingredients_6- B,S,C,V,L,Sa'
            ]
        for ingredient in all_ingredients:
            data[ingredient] = 0  # Set nilai awal semua fitur menjadi 0
        for ingredient in selected_ingredients:
            data[ingredient] = 1  # Set nilai fitur yang dipilih menjadi 1
        input_data = pd.DataFrame(data)
            
        # Memasukkan kolom rating
        input_data['rating'] = 0  # Tentukan nilai awal rating
            
        # Lakukan prediksi menggunakan model
        predicted_rating = knn_model.predict(input_data)
        return predicted_rating[0]

        # Masukan dari pengguna
    cocoa_percent = st.slider("Masukkan Persentase Kakao:", min_value=0, max_value=100, step=1)

        # Dropdown untuk memilih bahan-bahan
    with st.form("my_form"):
        selected_ingredients = st.multiselect("Pilih Bahan:", [
                'ingredients_1- B', 'ingredients_2- B,C', 'ingredients_2- B,S',
                'ingredients_2- B,S*', 'ingredients_3- B,S*,C', 'ingredients_3- B,S*,Sa',
                'ingredients_3- B,S,C', 'ingredients_3- B,S,L', 'ingredients_3- B,S,V',
                'ingredients_4- B,S*,C,L', 'ingredients_4- B,S*,C,Sa', 'ingredients_4- B,S*,C,V',
                'ingredients_4- B,S*,V,L', 'ingredients_4- B,S,C,L', 'ingredients_4- B,S,C,Sa',
                'ingredients_4- B,S,C,V', 'ingredients_4- B,S,V,L', 'ingredients_5- B,S,C,L,Sa',
                'ingredients_5- B,S,C,V,L', 'ingredients_5- B,S,C,V,Sa', 'ingredients_6- B,S,C,V,L,Sa'
        ], format_func=lambda x: ' '.join(x.split('-')[-1].split(',')))
        submitted = st.form_submit_button("Prediksi")

        # Tombol untuk membuat prediksi
    if submitted:
        rating = predict_rating(cocoa_percent, selected_ingredients)
        if rating == 1:
            st.write("Berdasarkan kedua bahan tersebut, prediksi rating coklat adalah : Tinggi")
        else:
            st.write("Berdasarkan kedua bahan tersebut, prediksi rating coklat adalah : Rendah")
