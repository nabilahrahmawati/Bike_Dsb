# ✨ Bikesharing Analysis and Dashboard

## -- Analisis menggunakan Colab Notebook -- 

### Detail hasil visualisasi ada di [notebook](https://github.com/nabilahrahmawati/Bike_Dashboard/blob/main/Projek_Bikesharing.ipynb))

### Pertanyaan
1. Bagaimana tren jumlah pengguna sepeda dalam beberapa tahun terakhir?
2. Apakah cuaca berpengaruh terhadap jumlah pengguna sepeda?
3. Musim apa yang memiliki intensitas penggunaan sepeda yang tinggi?
4. Bagaimana kondisi yang terlihat saat sepeda digunakan pada workingday holiday, dan weekday
5. Apakah ada korelasi temprature dan atemprature (suhu yang terasa) terhadap kondisi saat penggunaan sepeda sedang tinggi?

### Insights dan Kesimpulan
1. Tahun 2012 menjadi tahun yang paling banyak dalam penyewaan sepeda. Setiap tahun menunjukkan tren yang sama. Pertengahan tahun terjadi kenaikan jumlah sewa, sedangkan akhir tahun terjadi penurunan. Adapun terjadi perbedaan bulan puncak penyewaan sepeda di tiap tahunnya. Puncak penyewaan sepeda tahun 2011 terjadi di bulan Juni lalu menurun hingga Desember. Sedangkan penyewaan sepeda tersepi berada di bulan Januari 2011. Tahun 2012, puncak penyewaan sepeda terjadi pada bulan September lalu menurun hingga bulan Desember 2012. Sedangkan penyewaan sepi terjadi di bulan Januari 2012.

2. Ya, berpengaruh. Kondisi cuaca saat sedang clear/few/partly cloudy menjadi kondisi yang paling diminati sehingga jumlah penyewa sepwda menjadi tinggi dan ketika cuaca heavy rain/ice pallets/fog menjadi yang paling sedikit diminati.

3. Sewa sepeda tertinggi berada di musim panas (Summer Season) dan terendah berada di musim dingin (Winter).

4. Jumlah penyewa lebih banyak di hari kerja dibanding akhir pekan/hari libur. Berdasakan hari biasa, hari Kamis menjadi posisi pertama sebagai hari dengan penyewa sepeda terbanyak, sedangkan jumlah penyewa sepeda paling sedikit berada di hari Minggu.

5. temp dan atemp memiliki korelasi positif dengan count, sehingga jika temperatur (temp dan atemp) meningkat, maka pengguna sepeda juga cenderung meningkat. Maka, pada musim dingin dengan temperatur rendah dan dingin memiliki jumlah sewa sepeda yang lebih sedikit. Sedangkan pada musim panas dengan temperatur tinggi dan panas memiliki jumlah sewa sepeda yang banyak juga.

#### Setup Environment
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install pandas matplotlib seaborn streamlit
```

#### Run Streamlit app
```bash
cd dashboard
streamlit run bike_rent.py
```
Streamlit dapat dilihat di [link](https://bikedashboard-j6dckywxgyzy9xacbyx8aa.streamlit.app/) berikut
