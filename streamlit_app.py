import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://thumbs.dreamstime.com/b/back-to-school-seamless-background-blackboard-physics-chemistry-can-be-used-wallpaper-pattern-fills-textile-web-page-58597956.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .block-container {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 15px;
        max-width: 829px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

R = 0.0821  # L.atm/mol.K

# FUNGSI PERHITUNGAN
def hitung_tekanan(n, V, T):
    return (n * R * T) / V

def hitung_volume(P, n, T):
    return (n * R * T) / P

def hitung_mol(P, V, T):
    return (P * V) / (R * T)

def hitung_suhu(P, V, n):
    return (P * V) / (n * R)

if "halaman" not in st.session_state:
    st.session_state.halaman = "menu"
    
# STREAMLIT UI
if st.session_state.halaman == "menu":
    st.title("⚗️KALKULATOR HUKUM GAS IDEAL⚗️")
    st.write("Persamaan Gas Ideal: **PV = nRT**")
    st.write("Satuan yang digunakan: atm, L, mol, K")
    st.write(f"Konstanta gas: **R = {R} L.atm/mol.K**")

    menu = st.selectbox(
        "Pilih Menu Perhitungan:",
        ["Hitung Tekanan (P)", "Hitung Volume (V)", "Hitung Mol (n)", "Hitung Suhu (T)", "Simulasi Perubahan (%)"]
    )

    if st.button("Lanjut"):
        st.session_state.menu = menu
        st.session_state.halaman = "input"

elif st.session_state.halaman == "input":

    menu = st.session_state.menu

# MENU HITUNG P 
    if menu == "Hitung Tekanan (P)":
        st.subheader("Hitung Tekanan (P)")
        n = st.number_input("Masukkan mol (n) [mol]", min_value=0.0001, step=0.1)
        V = st.number_input("Masukkan volume (V) [L]", min_value=0.0001, step=0.1)
        T = st.number_input("Masukkan suhu (T) [K]", min_value=0.0001, step=1.0)

        if st.button("Hitung P"):
            P = hitung_tekanan(n, V, T)
            st.success(f"Tekanan (P) = {P:.4f} atm")

# MENU HITUNG V
    elif menu == "Hitung Volume (V)":
        st.subheader("Hitung Volume (V)")
        P = st.number_input("Masukkan tekanan (P) [atm]", min_value=0.0001, step=0.1)
        n = st.number_input("Masukkan mol (n) [mol]", min_value=0.0001, step=0.1)
        T = st.number_input("Masukkan suhu (T) [K]", min_value=0.0001, step=1.0)

        if st.button("Hitung V"):
        V = hitung_volume(P, n, T)
        st.success(f"Volume (V) = {V:.4f} L")

# MENU HITUNG n 
    elif menu == "Hitung Mol (n)":
        st.subheader("Hitung Mol (n)")
        P = st.number_input("Masukkan tekanan (P) [atm]", min_value=0.0001, step=0.1)
        V = st.number_input("Masukkan volume (V) [L]", min_value=0.0001, step=0.1)
        T = st.number_input("Masukkan suhu (T) [K]", min_value=0.0001, step=1.0)

        if st.button("Hitung n"):
            n = hitung_mol(P, V, T)
            st.success(f"Jumlah mol (n) = {n:.4f} mol")

# MENU HITUNG T
    elif menu == "Hitung Suhu (T)":
        st.subheader("Hitung Suhu (T)")
        P = st.number_input("Masukkan tekanan (P) [atm]", min_value=0.0001, step=0.1)
        V = st.number_input("Masukkan volume (V) [L]", min_value=0.0001, step=0.1)
        n = st.number_input("Masukkan mol (n) [mol]", min_value=0.0001, step=0.1)

        if st.button("Hitung T"):
        T = hitung_suhu(P, V, n)
        st.success(f"Suhu (T) = {T:.4f} K")

# MENU SIMULASI
    elif menu == "Simulasi Perubahan (%)":
        st.subheader("Simulasi Perubahan Variabel (%)")
        st.write("Masukkan kondisi awal gas:")

        P1 = st.number_input("Tekanan awal P1 [atm]", min_value=0.0001, step=0.1)
        V1 = st.number_input("Volume awal V1 [L]", min_value=0.0001, step=0.1)
        n1 = st.number_input("Mol awal n1 [mol]", min_value=0.0001, step=0.1)
        T1 = st.number_input("Suhu awal T1 [K]", min_value=0.0001, step=1.0)

        st.divider()

        variabel = st.selectbox("Pilih variabel yang diubah:", ["Tekanan (P)", "Volume (V)", "Mol (n)", "Suhu (T)"])
        persen = st.number_input("Masukkan persen perubahan (%) (boleh negatif untuk turun)", value=10.0, step=1.0)

        faktor = 1 + (persen / 100)

        if st.button("Simulasikan"):
            if faktor <= 0:
                st.error("Persen perubahan terlalu besar sehingga nilai menjadi 0 atau negatif.")
            else:
                if variabel == "Tekanan (P)":
                    P2 = P1 * faktor
                    V2 = hitung_volume(P2, n1, T1)
                    st.success(f"P baru = {P2:.4f} atm")
                    st.success(f"V baru = {V2:.4f} L")
                    st.info("Kesimpulan: Jika P naik, maka V turun (berbanding terbalik).")

                elif variabel == "Volume (V)":
                    V2 = V1 * faktor
                    P2 = hitung_tekanan(n1, V2, T1)
                    st.success(f"V baru = {V2:.4f} L")
                    st.success(f"P baru = {P2:.4f} atm")
                    st.info("Kesimpulan: Jika V naik, maka P turun (berbanding terbalik).")

                elif variabel == "Mol (n)":
                    n2 = n1 * faktor
                    P2 = hitung_tekanan(n2, V1, T1)
                    st.success(f"n baru = {n2:.4f} mol")
                    st.success(f"P baru = {P2:.4f} atm")
                    st.info("Kesimpulan: Jika n naik, maka P naik (berbanding lurus).")

                elif variabel == "Suhu (T)":
                    T2 = T1 * faktor
                    P2 = hitung_tekanan(n1, V1, T2)
                    st.success(f"T baru = {T2:.4f} K")
                    st.success(f"P baru = {P2:.4f} atm")
                    st.info("Kesimpulan: Jika T naik, maka P naik (berbanding lurus).")

if st.button("Kembali ke Menu"):
        st.session_state.halaman = "menu"
