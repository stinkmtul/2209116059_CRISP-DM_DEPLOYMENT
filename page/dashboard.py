import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
from PIL import Image

df = pd.read_csv("chocolate.csv")
df2 = pd.read_csv("Data_Cleaned.csv")

def main():
    # Baca data cokelat
    df = pd.read_csv("chocolate.csv")

    # Sidebar untuk memilih jumlah top ingredients
    st.sidebar.title("Menu")
    num_top = st.sidebar.selectbox("Kategori Top", [5, 10])

    # Sidebar untuk memilih menu
    menu = st.sidebar.radio("Pilih Menu", ["Rata-rata bahan", "Rata-rata rating", "Rata-rata kakao"])

    # Tampilkan berdasarkan menu yang dipilih
    if menu == "Rata-rata bahan":
        st.title(f'Top {num_top} Bahan Pembuatan Cokelat')

        # Menambahkan CSS untuk efek paralaks
        st.markdown(
            """
            <style>
            .parallax {
                /* The image used */
                background-image: url('https://wallpapers.com/images/hd/chocolate-background-6t6z4elybq6269dl.jpg');

                /* Set height untuk menyesuaikan dengan kebutuhan Anda */
                height: 200px;

                /* Create the parallax scrolling effect */
                background-attachment: fixed;
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Menampilkan efek paralaks
        st.markdown('<div class="parallax"></div>', unsafe_allow_html=True)

        # Menggabungkan semua entri dalam kolom "ingredients" menjadi satu string
        all_ingredients = ', '.join(df['ingredients'].dropna())

        # Membuat DataFrame dari kata-kata dalam kolom "ingredients"
        ingredients_df = pd.DataFrame(all_ingredients.split(', '), columns=['Ingredient'])

        # Menghitung jumlah kemunculan setiap bahan
        ingredient_counts = ingredients_df['Ingredient'].value_counts().sort_values(ascending=False)

        st.subheader("")
        st.subheader(f'Data Top {num_top} Bahan Pembuatan Cokelat')

        # Mengambil bahan teratas
        top_ingredients = ingredient_counts.head(num_top)

        # Menampilkan DataFrame dengan tata letak yang lebih baik
        st.dataframe(top_ingredients.reset_index().rename(columns={'index': 'Bahan', 'Ingredient': 'Bahan-Bahan'}), width=600)

        # Menambahkan judul untuk visualisasi
        st.subheader(f'Visualisasi Top {num_top} Bahan Pembuatan Cokelat')

        # Visualisasi dengan pie chart menggunakan Plotly Express
        fig = px.pie(top_ingredients, values=top_ingredients.values, names=top_ingredients.index,
                     color_discrete_sequence=px.colors.sequential.Aggrnyl)  # Menggunakan palet warna Aggrnyl
        st.plotly_chart(fig)

        # Menambahkan teks dalam format markdown
        # Menambahkan teks dalam format markdown
        st.markdown("### Bahan-bahan")
        st.markdown("- **B**: Biji Kakao\n- **S**: Gula\n- **S***: Pemanis selain gula tebu atau gula bit\n- **C**: Mentega Kakao\n- **V**: Vanilla\n- **L**: Lesitin\n- **Sa**: Garam")
        
        st.subheader("Interpretasi:")
        st.write("- Rata-rata bahan yang digunakan dalam pembuatan cokelat menunjukkan preferensi konsumen terhadap komposisi cokelat tertentu. Bahan-bahan seperti cokelat, gula, dan mentega kakao mendominasi daftar top 10, menandakan bahwa konsumen cenderung menyukai cokelat dengan rasa yang kaya dan manis.")

        # Saran tindak lanjut yang lebih terperinci
        st.subheader("Actionable Insight:")
        st.write("- Produsen dapat memanfaatkan informasi ini dengan memfokuskan upaya pengembangan produk pada kombinasi bahan yang paling populer, seperti mengeksplorasi variasi rasa dan kualitas bahan untuk meningkatkan daya tarik produk.")

    elif menu == "Rata-rata rating":
        st.title(f'Rata rata rating bahan top {num_top}')

        # Menambahkan CSS untuk efek paralaks
        st.markdown(
            """
            <style>
            .parallax {
                /* The image used */
                background-image: url('https://wallpapers.com/images/hd/chocolate-background-6t6z4elybq6269dl.jpg');

                /* Set height untuk menyesuaikan dengan kebutuhan Anda */
                height: 200px;

                /* Create the parallax scrolling effect */
                background-attachment: fixed;
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Menampilkan efek paralaks
        st.markdown('<div class="parallax"></div>', unsafe_allow_html=True)

        # Menggabungkan semua entri dalam kolom "ingredients" menjadi satu string
        all_ingredients = ', '.join(df['ingredients'].dropna())

        # Membuat DataFrame dari kata-kata dalam kolom "ingredients"
        ingredients_df = pd.DataFrame(all_ingredients.split(', '), columns=['Ingredient'])

        # Menggabungkan DataFrame ingredients_df dengan DataFrame df untuk mendapatkan rating setiap bahan
        ingredients_df['Rating'] = df['rating']

        # Menghitung jumlah kemunculan setiap bahan
        ingredient_counts = ingredients_df['Ingredient'].value_counts().sort_values(ascending=False)

        # Mengambil top bahan sesuai dengan nilai num_top
        top_ingredients = ingredient_counts.head(num_top).index.tolist()

        # Dropdown untuk memilih bahan
        st.subheader("")
        st.subheader(f'Visualisasi rata rata rating bahan Top {num_top}')
        selected_ingredient = st.selectbox(f"Select Ingredient (Top {num_top})", top_ingredients)

        # Filter dataframe berdasarkan bahan yang dipilih
        filtered_df = ingredients_df[ingredients_df['Ingredient'] == selected_ingredient]

        # Hitung rata-rata rating untuk bahan yang dipilih
        avg_rating = filtered_df['Rating'].mean()

        # Tampilkan rata-rata rating
        st.write(f"Rata rata rating dari bahan {selected_ingredient} : {avg_rating:.2f}")


        # Definisikan palet warna bluegreen yang mirip dengan Aggrnyl
        bluegreen_palette = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

        # Buat visualisasi histogram dengan menggunakan palet warna bluegreen
        hist = alt.Chart(filtered_df).mark_bar(color=bluegreen_palette[0]).encode(
            x=alt.X('Rating', bin=True, title='Rating'),
            y=alt.Y('count()', title='Count')
        ).properties(
            width=500,
            height=300
        )

        st.altair_chart(hist)

        # Interpretasi
        st.subheader("Interpretasi:")
        st.write(f"- Rata-rata rating dari produk cokelat yang menggunakan bahan-bahan top {num_top} merupakan gambaran keseluruhan tentang bagaimana konsumen menilai kualitas dan kenikmatan dari produk tersebut.")

        # Actionable Insight
        st.subheader("Actionable Insight:")
        st.write(f"- Data rating memberikan wawasan berharga tentang faktor-faktor yang memengaruhi kepuasan pelanggan, seperti komposisi bahan, sehingga memungkinkan kita untuk membuat keputusan yang lebih baik dalam pengembangan produk..")

    elif menu == 'Rata-rata kakao':
        st.title(f"Top {num_top} Persentase Kakao yang Sering Digunakan")
        
        # Menambahkan CSS untuk efek paralaks
        st.markdown(
            """
            <style>
            .parallax {
                /* The image used */
                background-image: url('https://wallpapers.com/images/hd/chocolate-background-6t6z4elybq6269dl.jpg');

                /* Set height untuk menyesuaikan dengan kebutuhan Anda */
                height: 200px;

                /* Create the parallax scrolling effect */
                background-attachment: fixed;
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Menampilkan efek paralaks
        st.markdown('<div class="parallax"></div>', unsafe_allow_html=True)
        
        cocoa_counts = df2['cocoa_percent'].value_counts().sort_index(ascending=False)

        st.subheader("")
        st.subheader(f'Data rata rata persen kakao yang digunakan')
        top_10_cocoa = cocoa_counts.head(num_top)
        
        st.dataframe(top_10_cocoa.reset_index().rename(columns={'index': 'Persentase Kakao', 'cocoa_percent': 'Persen Kakao (%)'}))
        
        fig = px.pie(top_10_cocoa, 
                values=top_10_cocoa.values, 
                names=top_10_cocoa.index, 
                title=(f'Visualisasi top {num_top} persen kakao yang sering digunakan'),
                labels={'index': 'Persentase Kakao'},
                color_discrete_sequence=px.colors.sequential.Aggrnyl)
        st.plotly_chart(fig)

        st.subheader("Interpretasi:")
        st.write("- Distribusi persentase kakao yang sering digunakan menunjukkan bahwa mayoritas produsen cenderung menggunakan kandungan kakao antara 84% hingga 100%. Persentase ini mungkin dianggap sebagai standar industri dalam pembuatan cokelat.")

        # Saran tindak lanjut yang lebih terperinci
        st.subheader("Actionable Insight:")
        st.write("- Perusahaan dapat fokus pada produk dengan kandungan kakao yang tinggi untuk memenuhi permintaan pasar yang dominan.")


if __name__ == "__main__":
    main()
