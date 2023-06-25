import streamlit as st
def add_custom_css():
    st.markdown('<link rel="stylesheet" href="assets/styles.css">', unsafe_allow_html=True)

# Memanggil fungsi untuk menambahkan CSS kustom
add_custom_css()
def app():
    st.title('Congratulation Anikmatillah Trisnayanti, S.EI. 💖')
    st.write('Selamat atas kelulusan sidangnya ayang, maaf aku gak bisa kasih apa-apa ke ayang, cuman bisa buat kayak gini. Aku harap ayang happy setelah lihat halaman ini, halaman website ini khusus aku buat untuk ayang yang memuat video ucapan selamat atas kelulusan sidangnya ayang. Untuk melihat videonya klik tombol lihat video!')
    if st.button('lihat video'):
        st.subheader('Video ini aku persembahkan buat ayang')
        video_file = open('sayang.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes, format="video/mp4")
        from streamlit_extras.let_it_rain import rain

        rain(
            emoji="💝",
            font_size=54,
            falling_speed=5,
            animation_length="infinite",
        )
