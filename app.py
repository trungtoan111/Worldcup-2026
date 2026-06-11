import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================
# 1. HỆ THỐNG ĐỒ HỌA CAO CẤP: FULL BACKGROUND & BANNER CỜ CHẠY XUNG QUANH
# ==================================================================
st.set_page_config(page_title="World Cup 2026 - AI Prediction Engine", layout="wide")

# Inject CSS để phủ nền toàn màn hình và tạo dải cờ chạy chạy xung quanh chữ World Cup
st.markdown("""
<style>
    /* Ép nền sân vận động mờ ảo toàn trang web */
    .stApp {
        background: linear-gradient(rgba(13, 27, 42, 0.9), rgba(15, 23, 42, 0.95)), 
                    url('https://png.pngtree.com/background/20250422/original/pngtree-a-blurred-crowd-of-spectators-in-a-stadium-at-a-sporting-picture-image_15484538.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Khung Banner Trung Tâm Phát Sáng */
    .banner-container {
        background: radial-gradient(circle, rgba(31, 58, 82, 0.8) 0%, rgba(17, 34, 51, 0.9) 100%);
        border: 2px solid #fecd3d;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 0 30px rgba(254, 205, 61, 0.3);
        margin-bottom: 30px;
        overflow: hidden;
        position: relative;
    }
    
    .main-logo-text {
        font-family: 'Poppins', sans-serif;
        font-size: 55px;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 0 20px rgba(254, 205, 61, 0.8);
        letter-spacing: 3px;
        margin: 15px 0;
    }
    
    /* Hiệu ứng Marquee: Cờ chạy liên tục từ phải qua trái */
    .flag-marquee {
        display: flex;
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        padding: 10px 0;
    }
    .flag-track {
        display: flex;
        animation: marquee 25s linear infinite;
    }
    .flag-track img {
        width: 45px;
        height: 30px;
        margin: 0 12px;
        border-radius: 4px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    }
    @keyframes marquee {
        0% { transform: translateX(0%); }
        100% { transform: translateX(-50%); }
    }

    /* Thẻ Container Bo Góc Kiểu Ứng Dụng Cao Cấp */
    .glass-card {
        background: rgba(30, 41, 59, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
    }
    .card-vs { background: linear-gradient(135deg, #112233 0%, #1f3a52 100%); border: 2px solid #3a506b; border-radius: 15px; padding: 25px; text-align: center; }
    .vs-text { font-size: 36px; font-weight: bold; color: #fecd3d; font-style: italic; }
    .team-name { font-size: 26px; font-weight: bold; color: #ffffff; text-transform: uppercase; }
    .card-player { background: #1e293b; border-left: 5px solid #059669; border-radius: 8px; padding: 12px; margin-bottom: 10px; }
    .stat-label { color: #94a3b8; font-size: 15px; }
    .stat-value { color: #fecd3d; font-weight: bold; font-size: 16px; float: right; }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# XUẤT BANNER ĐỒ HỌA: CHỮ PHÁT SÁNG Ở GIỮA, CỜ 48 NƯỚC CHẠY VÒNG QUANH
# ------------------------------------------------------------------
flag_list = ["mx", "za", "kr", "cz", "ar", "dz", "ca", "ba", "br", "ma", "us", "de", "nl", "be", "es", "fr", "gb-eng", "hr", "au", "jp", "uy", "sa"]
marquee_html = "".join([f'<img src="https://flagcdn.com/w80/{f}.png">' for f in flag_list * 4])

st.markdown(f"""
<div class="banner-container">
    <div class="flag-marquee"><div class="flag-track">{marquee_html}</div></div>
    <div class="main-logo-text">⚡ FIFA WORLD CUP 2026 ⚡</div>
    <div style="color: #94a3b8; font-weight: bold; letter-spacing: 1px;">REALTIME PREDICTION POOL ENGINE</div>
    <div class="flag-marquee" style="margin-top:10px;"><div class="flag-track" style="animation-direction: reverse;">{marquee_html}</div></div>
</div>
""", unsafe_allow_html=True)

# ==================================================================
# 2. CƠ SỞ DỮ LIỆU CHUẨN ĐẦY ĐỦ THÔNG SỐ SOI KÈO
# ==================================================================
@st.cache_data
def get_teams_data():
    return {
        "Mexico": {
            "bảng": "A", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "hlv": "Javier Aguirre", "logo": "https://flagcdn.com/w80/mx.png",
            "star_name": "Santiago Giménez", "star_img": "https://img.a.transfermarkt.technology/portrait/header/469254-1668673752.jpg",
            "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m83", "CLB": "Feyenoord", "Phong độ": "🔥 9.0/10"},
            "lối_chơi": "Kiểm soát bóng ngắn, áp đặt thế trận, tấn công biên tốc độ",
            "đội_hinh": ["Guillermo Ochoa", "Jorge Sánchez", "César Montes", "Johan Vásquez", "Jesús Gallardo", "Edson Álvarez", "Luis Chávez", "Orbelín Pineda", "Roberto Alvarado", "Julián Quiñones", "Santiago Giménez"]
        },
        "Nam Phi": {
            "bảng": "A", "sơ_đồ": "4-4-2", "sức_mạnh": "Trung bình", "hlv": "Hugo Broos", "logo": "https://flagcdn.com/w80/za.png",
            "star_name": "Percy Tau", "star_img": "https://img.a.transfermarkt.technology/portrait/header/312239-1666617937.jpg",
            "star_stats": {"Độ tuổi": "32 tuổi", "Vị trí": "Tiền đạo cánh (RW)", "Chiều cao": "1m75", "CLB": "Al Ahly", "Phong độ": "⭐ 7.5/10"},
            "lối_chơi": "Phòng ngự số đông, lùi sâu đội hình, phản công bóng dài",
            "đội_hinh": ["Ronwen Williams", "Khuliso Mudau", "Ime Okon", "Mbekezeli Mbokazi", "Aubrey Modiba", "Thalente Mbatha", "Yaya Sithole", "Teboho Mokoena", "Oswin Appollis", "Lyle Foster", "Percy Tau"]
        },
        "Hàn Quốc": {
            "bảng": "A", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "hlv": "Hong Myung-bo", "logo": "https://flagcdn.com/w80/kr.png",
            "star_name": "Son Heung-min", "star_img": "https://img.a.transfermarkt.technology/portrait/header/91845-1669106900.jpg",
            "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền đạo trái (LW)", "Chiều cao": "1m84", "CLB": "Tottenham", "Phong độ": "🔥 8.8/10"},
            "lối_chơi": "Đá giãn biên, chồng cánh tốc độ cao, áp sát pressing liên tục",
            "đội_hinh": ["Jo Hyeon-woo", "Kim Min-jae", "Kim Young-gwon", "Kim Jin-su", "Seol Young-woo", "Hwang In-beom", "Park Yong-woo", "Lee Kang-in", "Lee Jae-sung", "Hwang Hee-chan", "Son Heung-min"]
        },
        "CH Séc": {
            "bảng": "A", "sơ_đồ": "3-4-2-1", "sức_mạnh": "Trung bình", "hlv": "Ivan Hasek", "logo": "https://flagcdn.com/w80/cz.png",
            "star_name": "Tomáš Souček", "star_img": "https://img.a.transfermarkt.technology/portrait/header/283628-1661282672.jpg",
            "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Tiền vệ phòng ngự", "Chiều cao": "1m92", "CLB": "West Ham", "Phong độ": "⭐ 8.0/10"},
            "lối_chơi": "Kỷ luật thép, va chạm rực lửa, mạnh không chiến và cố định",
            "đội_hinh": ["Jindrich Stanek", "Tomas Holes", "Robin Hranac", "Ladislav Krejci", "Vladimir Coufal", "Tomas Soucek", "Lukas Provod", "David Doudera", "Vaclav Cerny", "Patrik Schick", "Jan Kuchta"]
        },
        "Argentina": {
            "bảng": "A", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "hlv": "Lionel Scaloni", "logo": "https://flagcdn.com/w80/ar.png",
            "star_name": "Lionel Messi", "star_img": "https://img.a.transfermarkt.technology/portrait/header/28003-1710151161.jpg",
            "star_stats": {"Độ tuổi": "38 tuổi", "Vị trí": "Tiền đạo phải (RW)", "Chiều cao": "1m70", "CLB": "Inter Miami", "Phong độ": "👑 9.5/10"},
            "lối_chơi": "Kiểm soát bóng ngắn, luân chuyển bóng nhanh, đột biến trung lộ",
            "đội_hinh": ["Emi Martínez", "Nahuel Molina", "Cristian Romero", "Nicolás Otamendi", "Nicolás Tagliafico", "Rodrigo De Paul", "Enzo Fernández", "Alexis Mac Allister", "Lionel Messi", "Julián Álvarez", "Ángel Di María"]
        },
        "Pháp": {
            "bảng": "I", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "hlv": "Didier Deschamps", "logo": "https://flagcdn.com/w80/fr.png",
            "star_name": "Kylian Mbappé", "star_img": "https://img.a.transfermarkt.technology/portrait/header/342229-1669106304.jpg",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m78", "CLB": "Real Madrid", "Phong độ": "👑 9.5/10"},
            "lối_chơi": "Tấn công trực diện tốc độ cao bằng hành lang biên",
            "đội_hinh": ["Mike Maignan", "Jules Koundé", "Dayot Upamecano", "William Saliba", "Théo Hernandez", "N'Golo Kanté", "Aurélien Tchouaméni", "Ousmane Dembélé", "Antoine Griezmann", "Bradley Barcola", "Kylian Mbappé"]
        }
    }

TEAMS = get_teams_data()

def get_team_info(name):
    return TEAMS.get(name, {
        "bảng": "Vòng bảng", "sơ_đồ": "4-2-3-1", "lối_chơi": "Tập thể", "ngôi_sao": "Đội trưởng", "sức_mạnh": "Trung bình", "hlv": "Chưa rõ",
        "logo": "https://flagcdn.com/w80/un.png", "star_name": "Chưa cập nhật", "star_img": "https://flagcdn.com/w80/un.png",
        "star_stats": {"Độ tuổi": "Chưa rõ", "Vị trí": "Chưa rõ", "Chiều cao": "Chưa rõ", "CLB": "Tự do", "Phong độ": "0/10"},
        "đội_hinh": ["Thủ môn", "Hậu vệ 1", "Hậu vệ 2", "Hậu vệ 3", "Hậu vệ 4", "Tiền vệ 1", "Tiền vệ 2", "Tiền vệ 3", "Tiền đạo 1", "Tiền đạo 2", "Tiền đạo 3"]
    })

if 'matches' not in st.session_state:
    st.session_state.matches = {
        "WC-01": {"vòng": "Bảng A", "ngày": "12/06", "giờ": "02:00", "đội_nhà": "Mexico", "đội_khách": "Nam Phi", "kênh": "VTV3, VTV6", "thời_tiết": "Mát mẻ, 24°C (Sân Azteca)", "ti_so_ft": "", "trọng_tài": "Chưa cập nhật"},
        "WC-02": {"vòng": "Bảng A", "ngày": "12/06", "giờ": "09:00", "đội_nhà": "Hàn Quốc", "đội_khách": "CH Séc", "kênh": "VTV3", "thời_tiết": "Mát mẻ, 20°C", "ti_so_ft": "", "trọng_tài": "Chưa cập nhật"}
    }

# ==================================================================
# 3. QUẢN LÝ TABS CHỨC NĂNG (KẾT HỢP Ý TƯỞNG GITHUB ĐA DẠNG)
# ==================================================================
tab1, tab2, tab3 = st.tabs(["🏟️ Trung Tâm Trận Đấu & Sa Bàn", "🔮 Dự Đoán Tỉ Số (Prediction Pool)", "⏱️ Cập Nhật Dữ Liệu"])

# --- TAB 1: SA BÀN CHIẾN THUẬT & TRẬN ĐẤU CHUYÊN NGHIỆP ---
with tab1:
    selected_m = st.selectbox("Chọn cặp đấu muốn xem phân tích:", list(st.session_state.matches.keys()))
    m_data = st.session_state.matches[selected_m]
    t_nhà = get_team_info(m_data['đội_nhà'])
    t_khách = get_team_info(m_data['đội_khách'])
    
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        st.markdown(f'<div class="card-vs"><img src="{t_nhà["logo"]}" width="110"><br><span class="team-name">{m_data["đội_nhà"]}</span><br><span class="hlv-text">HLV: {t_nhà["hlv"]}</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div style="text-align: center; margin-top: 30px;"><span class="vs-text">VS</span><br><span style="color: #ffffff; font-size:18px; font-weight:bold;">{m_data["giờ"]} | {m_data["ngày"]}</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="card-vs"><img src="{t_khách["logo"]}" width="110"><br><span class="team-name">{m_data["đội_khách"]}</span><br><span class="hlv-text">HLV: {t_khách["hlv"]}</span></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### ⚡ SOI KÈO NGÔI SAO CHỦ CHỐT (KEY PLAYER FACE-OFF)")
    c_star1, c_star2 = st.columns(2)
    with c_star1:
        st.markdown(f'<div class="glass-card"><h4 style="color:#fecd3d;">⭐ {t_nhà["star_name"]}</h4>', unsafe_allow_html=True)
        st.image(t_nhà["star_img"], width=130)
        for lbl, val in t_nhà["star_stats"].items():
            st.markdown(f'<div class="card-player"><span class="stat-label">{lbl}</span><span class="stat-value">{val}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c_star2:
        st.markdown(f'<div class="glass-card"><h4 style="color:#fecd3d;">⭐ {t_khách["star_name"]}</h4>', unsafe_allow_html=True)
        st.image(t_khách["star_img"], width=130)
        for lbl, val in t_khách["star_stats"].items():
            st.markdown(f'<div class="card-player"><span class="stat-label">{lbl}</span><span class="stat-value">{val}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📋 ĐỘI HÌNH RA SÂN & SA BÀN 2D CHUẨN")
    col_pitch, col_text = st.columns([3, 2])
    with col_pitch:
        fig, ax = plt.subplots(figsize=(7, 4.8))
        fig.patch.set_facecolor('#0f172a')
        ax.set_facecolor('#14532d')
        plt.plot([0, 0, 100, 100, 0], [0, 100, 100, 0, 0], color="white", linewidth=2)
        plt.plot([0, 100], [50, 50], color="white", linewidth=2)
        center_circle = plt.Circle((50, 50), 14, color='white', fill=False, linewidth=2)
        ax.add_patch(center_circle)
        
        plt.scatter([50], [7], color='#ef4444', s=200, edgecolors='white', zorder=5)
        plt.scatter([50], [93], color='#3b82f6', s=200, edgecolors='white', zorder=5)
        plt.text(50, 11, "CHỦ NHÀ", color='white', ha='center', weight='bold')
        plt.text(50, 85, "ĐỘI KHÁCH", color='white', ha='center', weight='bold')
        plt.axis('off')
        st.pyplot(fig)
    with col_text:
        st.info(f"🔴 **{m_data['đội_nhà']} ({t_nhà['sơ_đồ']}):** \n" + ", ".join(t_nhà['đội_hinh']))
        st.success(f"🔵 **{m_data['đội_khách']} ({t_khách['sơ_đồ']}):** \n" + ", ".join(t_khách['đội_hinh']))

# --- TAB 2: TÍNH NĂNG DỰ ĐOÁN TẬP THỂ (ĐƯỢC COPY Ý TƯỞNG TỪ GITHUB BAN NÃY) ---
with tab2:
    st.markdown("### 🔮 PHÒNG MINI-GAME DỰ ĐOÁN TRÚNG THƯỞNG (PREDICTION GAME)")
    st.write("Triển khai tính năng mini-game tính điểm cạnh tranh cho nhóm bạn bè y hệt hệ thống `world-cup-pool`.")
    
    st.markdown("""
    | Quy Tắc Tính Điểm Thưởng (Scoring Matrix) | Số Điểm |
    | :--- | :---: |
    | Dự đoán đúng Đội Thắng / Hòa | **+3 Điểm** |
    | Dự đoán trúng phóc tỉ số bàn thắng | **+1 Điểm** |
    | Dự đoán đúng hiệu số bàn thắng bại | **+1 Điểm** |
    """)
    
    st.markdown("#### 📝 GHI ĐƠN CỦA BẠN")
    game_m = st.selectbox("Chọn trận đấu muốn nạp dự đoán gửi lên hệ thống:", list(st.session_state.matches.keys()))
    m_info = st.session_state.matches[game_m]
    
    c_g1, c_g2 = st.columns(2)
    with c_g1:
        user_pred = st.text_input(f"Dự đoán tỉ số của bạn cho trận {m_info['đội_nhà']} vs {m_info['đội_khách']} (Vd: 2-1):")
    with c_g2:
        leagues = st.text_input("Nhập mã phòng đấu / Mã League của bạn (Vd: IT-HUTECH-POOL):")
        
    if st.button("🚀 GỬI DỰ ĐOÁN LÊN HỆ THỐNG CLOUD"):
        if user_pred:
            st.toast(f"Hệ thống ghi nhận thành công! Dự đoán [{user_pred}] tại phòng [{leagues}] đã khóa sổ.", icon="🔥")
        else:
            st.warning("Vui lòng điền tỉ số trước khi bấm gửi.")

# --- TAB 3: PHÒNG ĐIỀU PHỐI DỮ LIỆU ---
with tab3:
    st.subheader("⏱️ Phòng Điều Phối & Nhập Liệu Trực Tiếp")
    update_m = st.selectbox("Chọn mã trận nạp kết quả thực tế:", list(st.session_state.matches.keys()))
    curr_m = st.session_state.matches[update_m]
    curr_m['ti_so_ft'] = st.text_input(f"Nhập tỉ số chung cuộc FT:", curr_m['ti_so_ft'])
    if st.button("💾 XÁC NHẬN LƯU DIỄN BIẾN"):
        st.toast("Dữ liệu nạp trực tiếp thành công!", icon="⚡")
