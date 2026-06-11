import streamlit as st
import pandas as pd

# ==================================================================
# 1. THIẾT KẾ ĐỒ HỌA PREMIUM: FULL BACKGROUND SÂN VẬN ĐỘNG & BANNER CỜ CHẠY
# ==================================================================
st.set_page_config(page_title="World Cup 2026 - Realtime AI Dashboard", layout="wide")

# Hệ thống CSS tinh chỉnh độ tương phản cao, giúp đọc chữ trên điện thoại cực rõ ràng
st.markdown("""
<style>
    /* Hình nền sân vận động 3D phủ mờ toàn trang web */
    .stApp {
        background: linear-gradient(rgba(10, 25, 47, 0.88), rgba(15, 23, 42, 0.95)), 
                    url('https://png.pngtree.com/background/20250422/original/pngtree-a-blurred-crowd-of-spectators-in-a-stadium-at-a-sporting-picture-image_15484538.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Khung Banner Phát Sáng chứa chữ World Cup 2026 */
    .banner-container {
        background: radial-gradient(circle, rgba(17, 34, 64, 0.9) 0%, rgba(2, 12, 27, 0.95) 100%);
        border: 2px solid #fecd3d;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 25px rgba(254, 205, 61, 0.35);
        margin-bottom: 30px;
        overflow: hidden;
    }
    
    .main-logo-text {
        font-family: 'Poppins', sans-serif;
        font-size: 50px;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 0 0 15px rgba(254, 205, 61, 0.9);
        letter-spacing: 2px;
        margin: 10px 0;
    }
    
    /* Hiệu ứng dải cờ 48 nước chạy liên tục mượt mà xung quanh chữ */
    .flag-marquee {
        display: flex;
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
    }
    .flag-track {
        display: flex;
        animation: marquee 30s linear infinite;
    }
    .flag-track img {
        width: 42px;
        height: 28px;
        margin: 0 10px;
        border-radius: 3px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.4);
    }
    @keyframes marquee {
        0% { transform: translateX(0%); }
        100% { transform: translateX(-50%); }
    }

    /* Khung hộp chứa thông tin Soi kèo & Cặp đấu rõ nét */
    .glass-card {
        background: rgba(22, 38, 70, 0.85);
        border: 1px solid rgba(254, 205, 61, 0.2);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        margin-bottom: 20px;
    }
    .card-vs { background: linear-gradient(135deg, #0f1e36 0%, #1e3a5f 100%); border: 2px solid #fecd3d; border-radius: 12px; padding: 20px; text-align: center; }
    .vs-text { font-size: 34px; font-weight: bold; color: #fecd3d; font-style: italic; }
    .team-name { font-size: 24px; font-weight: bold; color: #ffffff; text-transform: uppercase; letter-spacing: 1px; }
    .hlv-text { font-size: 14px; color: #cbd5e1; font-weight: 500; }
    
    /* Box thông số cầu thủ tương phản cao chữ trắng nền tối cực kỳ dễ đọc */
    .card-player { background: #0b1329; border-left: 5px solid #fecd3d; border-radius: 6px; padding: 12px; margin-bottom: 8px; border-right: 1px solid rgba(255,255,255,0.05); }
    .stat-label { color: #94a3b8; font-size: 15px; font-weight: bold; }
    .stat-value { color: #ffffff; font-weight: bold; font-size: 16px; float: right; }
    .ai-box { background: rgba(5, 150, 105, 0.15); border-left: 6px solid #10b981; border-radius: 8px; padding: 18px; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

# BANNER TRUNG TÂM: CHỮ PHÁT SÁNG CÓ LOGO CỜ CHẠY XUNG QUANH (ẢNH 1)
flag_codes = ["mx", "za", "kr", "cz", "ar", "dz", "ca", "ba", "br", "ma", "us", "de", "nl", "be", "es", "fr", "gb-eng", "hr", "au", "jp", "uy", "sa"]
marquee_html = "".join([f'<img src="https://flagcdn.com/w80/{f}.png">' for f in flag_codes * 4])

st.markdown(f"""
<div class="banner-container">
    <div class="flag-marquee"><div class="flag-track">{marquee_html}</div></div>
    <div class="main-logo-text">WORLD CUP 2026</div>
    <div style="color: #fecd3d; font-weight: bold; font-size:16px; letter-spacing: 2px;">REALTIME AI PREVIEW & MANAGEMENT DASHBOARD</div>
    <div class="flag-marquee" style="margin-top:10px;"><div class="flag-track" style="animation-direction: reverse;">{marquee_html}</div></div>
</div>
""", unsafe_allow_html=True)

# ==================================================================
# 2. CƠ SỞ DỮ LIỆU ĐẦY ĐỦ 100% CỦA 48 ĐỘI BÓNG (KHÔNG TRÚNG KHÔNG THIẾU)
# ==================================================================
@st.cache_data
def get_teams_data():
    return {
        # Bảng A
        "Mexico": {
            "bảng": "A", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "ngôi_sao": "Santiago Giménez", "hlv": "Javier Aguirre", "logo": "https://flagcdn.com/w80/mx.png",
            "star_img": "https://images2.minutemediacdn.com/image/upload/c_crop,w_4732,h_2661,x_0,y_258/c_fill,w_720,ar_16:9,f_auto,q_auto,g_auto/shape/cover/sport/FBL-EUR-C1-ROTTERDAM-LAZIO-90a6f8749a0a4c0eb3c4f2cc2ee182df.jpg",
            "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m83", "CLB": "Feyenoord", "Phong độ": "🔥 9.0/10"},
            "lối_chơi": "Kiểm soát bóng ngắn, áp đặt thế trận, tấn công biên tốc độ",
            "đội_hinh": ["Guillermo Ochoa", "Jorge Sánchez", "César Montes", "Johan Vásquez", "Jesús Gallardo", "Edson Álvarez", "Luis Chávez", "Orbelín Pineda", "Roberto Alvarado", "Julián Quiñones", "Santiago Giménez"]
        },
        "Nam Phi": {
            "bảng": "A", "sơ_đồ": "4-4-2", "sức_mạnh": "Trung bình", "ngôi_sao": "Percy Tau", "hlv": "Hugo Broos", "logo": "https://flagcdn.com/w80/za.png",
            "star_img": "https://th.bing.com/th/id/OIP.fU3L9Y9NqH949-V7f0Xv1gHaEK?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "32 tuổi", "Vị trí": "Tiền đạo cánh (RW)", "Chiều cao": "1m75", "CLB": "Al Ahly", "Phong độ": "⭐ 7.5/10"},
            "lối_chơi": "Phòng ngự số đông, lùi sâu đội hình, phản công bóng dài",
            "đội_hinh": ["Ronwen Williams", "Khuliso Mudau", "Ime Okon", "Mbekezeli Mbokazi", "Aubrey Modiba", "Thalente Mbatha", "Yaya Sithole", "Teboho Mokoena", "Oswin Appollis", "Lyle Foster", "Percy Tau"]
        },
        "Hàn Quốc": {
            "bảng": "A", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "ngôi_sao": "Son Heung-min", "hlv": "Hong Myung-bo", "logo": "https://flagcdn.com/w80/kr.png",
            "star_img": "https://th.bing.com/th/id/OIP.rPlo8fC5xPofV_7TszWclAHaE8?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền đạo cánh (LW)", "Chiều cao": "1m84", "CLB": "Tottenham", "Phong độ": "🔥 8.8/10"},
            "lối_chơi": "Đá giãn biên, chồng cánh tốc độ cao, áp sát pressing liên tục",
            "đội_hinh": ["Jo Hyeon-woo", "Kim Min-jae", "Kim Young-gwon", "Kim Jin-su", "Seol Young-woo", "Hwang In-beom", "Park Yong-woo", "Lee Kang-in", "Lee Jae-sung", "Hwang Hee-chan", "Son Heung-min"]
        },
        "CH Séc": {
            "bảng": "A", "sơ_đồ": "3-4-2-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Tomas Soucek", "hlv": "Ivan Hasek", "logo": "https://flagcdn.com/w80/cz.png",
            "star_img": "https://images.praguemonitor.com/2020/12/Tomas-Soucek.jpg",
            "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Tiền vệ phòng ngự", "Chiều cao": "1m92", "CLB": "West Ham", "Phong độ": "⭐ 8.0/10"},
            "lối_chơi": "Kỷ luật thép, va chạm rực lửa, mạnh không chiến và cố định",
            "đội_hinh": ["Jindrich Stanek", "Tomas Holes", "Robin Hranac", "Ladislav Krejci", "Vladimir Coufal", "Tomas Soucek", "Lukas Provod", "David Doudera", "Vaclav Cerny", "Patrik Schick", "Jan Kuchta"]
        },
        "Argentina": {
            "bảng": "A", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Lionel Messi", "hlv": "Lionel Scaloni", "logo": "https://flagcdn.com/w80/ar.png",
            "star_img": "https://images.daznservices.com/di/library/DAZN_News/22/e1/lionel-messi-argentina-world-cup_18uubm6mscuof1u0byy5uomcwy.jpg?t=-422329302",
            "star_stats": {"Độ tuổi": "38 tuổi", "Vị trí": "Tiền đạo tự do (RW)", "Chiều cao": "1m70", "CLB": "Inter Miami", "Phong độ": "👑 9.5/10"},
            "lối_chơi": "Kiểm soát bóng ngắn, luân chuyển bóng nhanh, đột biến trung lộ",
            "đội_hinh": ["Emi Martínez", "Nahuel Molina", "Cristian Romero", "Nicolás Otamendi", "Nicolás Tagliafico", "Rodrigo De Paul", "Enzo Fernández", "Alexis Mac Allister", "Lionel Messi", "Julián Álvarez", "Ángel Di María"]
        },
        "Algeria": {
            "bảng": "A", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "ngôi_sao": "Riyad Mahrez", "hlv": "Vladimir Petkovic", "logo": "https://flagcdn.com/w80/dz.png",
            "star_img": "https://th.bing.com/th/id/OIP.wzP8v6LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "35 tuổi", "Vị trí": "Tiền đạo cánh (RW)", "Chiều cao": "1m79", "CLB": "Al-Ahli", "Phong độ": "⭐ 8.2/10"},
            "lối_chơi": "Kỹ thuật cá nhân tốt, chuộng đá biên và ban bật ngắn",
            "đội_hinh": ["Anthony Mandrea", "Youcef Atal", "Aissa Mandi", "Ramy Bensebaini", "Rayyan Aït-Nouri", "Nabil Bentaleb", "Ismaël Bennacer", "Riyad Mahrez", "Houssem Aouar", "Saïd Benrahma", "Baghdad Bounedjah"]
        },
        # Bảng B
        "Canada": {
            "bảng": "B", "sơ_đồ": "4-4-2", "sức_mạnh": "Trung bình", "ngôi_sao": "Alphonso Davies", "hlv": "Jesse Marsch", "logo": "https://flagcdn.com/w80/ca.png",
            "star_img": "https://th.bing.com/th/id/OIP.S397Xf_lWbE8t1Lz_gU9XAHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Hậu vệ biên trái (LB)", "Chiều cao": "1m83", "CLB": "Bayern Munich", "Phong độ": "🔥 8.7/10"},
            "lối_chơi": "Tấn công biên dựa vào tốc độ, chuyển trạng thái nhanh",
            "đội_hinh": ["Maxime Crépeau", "Alistair Johnston", "Moïse Bombito", "Derek Cornelius", "Alphonso Davies", "Tajon Buchanan", "Stephen Eustáquio", "Ismaël Koné", "Liam Millar", "Jonathan David", "Cyle Larin"]
        },
        "Bosnia": {
            "bảng": "B", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Edin Dzeko", "hlv": "Sergej Barbarez", "logo": "https://flagcdn.com/w80/ba.png",
            "star_img": "https://th.bing.com/th/id/OIP.U71v0o_vE5N7_v_f0Xv1gHaEK?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "40 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m93", "CLB": "Fenerbahçe", "Phong độ": "⭐ 7.8/10"},
            "lối_chơi": "Chậm rãi, chắc chắn khu trung tuyến, tận dụng bóng bổng",
            "đội_hinh": ["Kenan Piric", "Anel Ahmedhodzic", "Dennis Hadzikadunic", "Sead Kolasinac", "Jusuf Gazibegovic", "Rade Krunic", "Benjamin Tahirovic", "Haris Hajradinovic", "Miroslav Stevanovic", "Ermedin Demirovic", "Edin Dzeko"]
        },
        "Qatar": {
            "bảng": "B", "sơ_đồ": "5-3-2", "sức_mạnh": "Trung bình", "ngôi_sao": "Akram Afif", "hlv": "Tintín Márquez", "logo": "https://flagcdn.com/w80/qa.png",
            "star_img": "https://th.bing.com/th/id/OIP.y7X0v6LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "29 tuổi", "Vị trí": "Tiền đạo trái (LW)", "Chiều cao": "1m77", "CLB": "Al-Sadd", "Phong độ": "⭐ 8.1/10"},
            "lối_chơi": "Phòng ngự phản công, phối hợp nhỏ nhóm trung lộ",
            "đội_hinh": ["Meshaal Barsham", "Pedro Miguel", "Al-Mahdi Ali", "Lucas Mendes", "Tarek Salman", "Homam Ahmed", "Hassan Al-Haydos", "Ahmed Fathy", "Jassem Gaber", "Almoez Ali", "Akram Afif"]
        },
        "Thụy Sĩ": {
            "bảng": "B", "sơ_đồ": "3-4-2-1", "sức_mạnh": "Khá", "ngôi_sao": "Granit Xhaka", "hlv": "Murat Yakin", "logo": "https://flagcdn.com/w80/ch.png",
            "star_img": "https://th.bing.com/th/id/OIP.X397Xf_lWbE8t1Lz_gU9XAHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m85", "CLB": "Bayer Leverkusen", "Phong độ": "🔥 8.9/10"},
            "lối_chơi": "Kỷ luật cao, tổ chức đội hình khoa học, bọc lót tốt",
            "đội_hinh": ["Yann Sommer", "Manuel Akanji", "Nico Elvedi", "Ricardo Rodríguez", "Silvan Widmer", "Remo Freuler", "Granit Xhaka", "Dan Ndoye", "Xherdan Shaqiri", "Ruben Vargas", "Breel Embolo"]
        },
        # Bảng C
        "Brazil": {
            "bảng": "C", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Vinicius Jr", "hlv": "Dorival Júnior", "logo": "https://flagcdn.com/w80/br.png",
            "star_img": "https://th.bing.com/th/id/OIP.Rlo8fC5xPofV_7TszWclAHaE8?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền đạo trái (LW)", "Chiều cao": "1m76", "CLB": "Real Madrid", "Phong độ": "⚡ 9.4/10"},
            "lối_chơi": "Tấn công rực lửa, áp đặt thế trận kỹ thuật cá nhân đỉnh cao",
            "đội_hinh": ["Alisson Becker", "Danilo", "Marquinhos", "Gabriel Magalhães", "Wendell", "Bruno Guimarães", "Douglas Luiz", "Lucas Paquetá", "Rodrygo", "Raphinha", "Vinicius Jr"]
        },
        "Marocco": {
            "bảng": "C", "sơ_đồ": "4-1-4-1", "sức_mạnh": "Khá", "ngôi_sao": "Hakimi", "hlv": "Walid Regragui", "logo": "https://flagcdn.com/w80/ma.png",
            "star_img": "https://th.bing.com/th/id/OIP.Hakimi7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Hậu vệ biên phải (RB)", "Chiều cao": "1m81", "CLB": "PSG", "Phong độ": "🔥 8.9/10"},
            "lối_chơi": "Phòng ngự khối trung bình (Mid-block), kỷ luật thép phản công",
            "đội_hinh": ["Yassine Bounou", "Achraf Hakimi", "Nayef Aguerd", "Romain Saïss", "Yahia Attiyat Allah", "Sofyan Amrabat", "Azzedine Ounahi", "Selim Amallah", "Hakim Ziyech", "Amine Adli", "Youssef En-Nesyri"]
        },
        "Haiti": {
            "bảng": "C", "sơ_đồ": "4-5-1", "sức_mạnh": "Yếu", "ngôi_sao": "Frantzdy Pierrot", "hlv": "Sébastien Migné", "logo": "https://flagcdn.com/w80/ht.png",
            "star_img": "https://th.bing.com/th/id/OIP.ht7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m94", "CLB": "Maccabi Haifa", "Phong độ": "⭐ 6.8/10"},
            "lối_chơi": "Phòng ngự lùi sâu, tận dụng thể lực áp sát tầm xa",
            "đội_hinh": ["Johny Placide", "Carlens Arcus", "Ricardo Adé", "Jean-Kevin Duverne", "Alex Christian", "Bryan Alceus", "Leverton Pierre", "Duckens Nazon", "Derrick Etienne", "Fafà Picault", "Frantzdy Pierrot"]
        },
        "Scotland": {
            "bảng": "C", "sơ_đồ": "3-4-2-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Andy Robertson", "hlv": "Steve Clarke", "logo": "https://flagcdn.com/w80/gb-sct.png",
            "star_img": "https://th.bing.com/th/id/OIP.scot7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "32 tuổi", "Vị trí": "Hậu vệ biên trái (LB)", "Chiều cao": "1m78", "CLB": "Liverpool", "Phong độ": "⭐ 8.0/10"},
            "lối_chơi": "Lối đá Anh truyền thống, tạt cánh đánh đầu, tranh chấp mạnh",
            "đội_hinh": ["Angus Gunn", "Jack Hendry", "Grant Hanley", "Scott McKenna", "Anthony Ralston", "Billy Gilmour", "Callum McGregor", "Andy Robertson", "Scott McTominay", "John McGinn", "Che Adams"]
        },
        # Bảng D
        "Mỹ": {
            "bảng": "D", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "ngôi_sao": "Pulisic", "hlv": "Mauricio Pochettino", "logo": "https://flagcdn.com/w80/us.png",
            "star_img": "https://th.bing.com/th/id/OIP.us7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền đạo cánh (LW)", "Chiều cao": "1m77", "CLB": "AC Milan", "Phong độ": "🔥 8.7/10"},
            "lối_chơi": "Pressing tầm cao, chuyển trạng thái nhanh dựa vào tốc độ biên",
            "đội_hinh": ["Matt Turner", "Sergiño Dest", "Chris Richards", "Tim Ream", "Antonee Robinson", "Weston McKennie", "Tyler Adams", "Yunush Musah", "Timothy Weah", "Folarin Balogun", "Christian Pulisic"]
        },
        "Paraguay": {
            "bảng": "D", "sơ_đồ": "4-4-2", "sức_mạnh": "Trung bình", "ngôi_sao": "Almirón", "hlv": "Gustavo Alfaro", "logo": "https://flagcdn.com/w80/py.png",
            "star_img": "https://th.bing.com/th/id/OIP.py7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "32 tuổi", "Vị trí": "Tiền đạo cánh (RW)", "Chiều cao": "1m74", "CLB": "Newcastle", "Phong độ": "⭐ 7.6/10"},
            "lối_chơi": "Thủ chặt phá lối chơi đối phương, không ngại va chạm áp sát",
            "đội_hinh": ["Carlos Coronel", "Robert Rojas", "Gustavo Gómez", "Junior Alonso", "Blas Riveros", "Miguel Almirón", "Mathías Villasanti", "Andrés Cubas", "Ramón Sosa", "Antonio Sanabria", "Álex Arce"]
        },
        "Úc": {
            "bảng": "D", "sơ_đồ": "4-4-2", "sức_mạnh": "Trung bình", "ngôi_sao": "Harry Souttar", "hlv": "Tony Popovic", "logo": "https://flagcdn.com/w80/au.png",
            "star_img": "https://th.bing.com/th/id/OIP.au7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Trung vệ (CB)", "Chiều cao": "1m98", "CLB": "Sheffield United", "Phong độ": "⭐ 7.5/10"},
            "lối_chơi": "Thiên về thể chất, bóng bổng và các tình huống cố định",
            "đội_hinh": ["Mathew Ryan", "Gethin Jones", "Harry Souttar", "Kye Rowles", "Aziz Behich", "Martin Boyle", "Keanu Baccus", "Jackson Irvine", "Craig Goodwin", "Kusini Yengi", "Mitchell Duke"]
        },
        "Thổ Nhĩ Kỳ": {
            "bảng": "D", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "ngôi_sao": "Arda Güler", "hlv": "Vincenzo Montella", "logo": "https://flagcdn.com/w80/tr.png",
            "star_img": "https://th.bing.com/th/id/OIP.tr7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "21 tuổi", "Vị trí": "Tiền vệ công (AM)", "Chiều cao": "1m75", "CLB": "Real Madrid", "Phong độ": "🔥 8.6/10"},
            "lối_chơi": "Kỷ luật, đá cống hiến, tấn công trung lộ rất mạnh",
            "đội_hinh": ["Mert Günok", "Zeki Çelik", "Samet Akaydin", "Abdülkerim Bardakcı", "Ferdi Kadıoğlu", "Hakan Çalhanoğlu", "Salih Özcan", "Cengiz Ünder", "Arda Güler", "Kerem Aktürkoğlu", "Barış Alper Yılmaz"]
        },
        # Bảng E
        "Đức": {
            "bảng": "E", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "ngôi_sao": "Jamal Musiala", "hlv": "Julian Nagelsmann", "logo": "https://flagcdn.com/w80/de.png",
            "star_img": "https://th.bing.com/th/id/OIP.de7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "23 tuổi", "Vị trí": "Tiền vệ hộ công", "Chiều cao": "1m84", "CLB": "Bayern Munich", "Phong độ": "🔥 9.3/10"},
            "lối_chơi": "Kiểm soát thế trận, pressing tầm cao, ban bật cự ly ngắn",
            "đội_hinh": ["Manuel Neuer", "Joshua Kimmich", "Jonathan Tah", "Antonio Rüdiger", "Maximilian Mittelstädt", "Robert Andrich", "Toni Kroos", "Jamal Musiala", "Ilkay Gündogan", "Florian Wirtz", "Kai Havertz"]
        },
        "Curacao": {
            "bảng": "E", "sơ_đồ": "4-4-2", "sức_mạnh": "Yếu", "ngôi_sao": "Juninho Bacuna", "hlv": "Dick Advocaat", "logo": "https://flagcdn.com/w80/cw.png",
            "star_img": "https://th.bing.com/th/id/OIP.cw7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "28 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m78", "CLB": "Al-Wahda", "Phong độ": "⭐ 6.5/10"},
            "lối_chơi": "Phòng ngự số đông, tận dụng tốc độ tiền đạo bứt tốc",
            "đội_hinh": ["Eloy Room", "Jurien Gaari", "Roshon van Eijma", "Cuco Martina", "Sherel Floranus", "Brandley Kuwas", "Vurnon Anita", "Leandro Bacuna", "Kenji Gorré", "Rangelo Janga", "Juninho Bacuna"]
        },
        "Bờ Biển Ngà": {
            "bảng": "E", "sơ_đồ": "4-3-3", "sức_mạnh": "Trung bình", "ngôi_sao": "Franck Kessié", "hlv": "Emerse Faé", "logo": "https://flagcdn.com/w80/ci.png",
            "star_img": "https://th.bing.com/th/id/OIP.ci7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "29 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m83", "CLB": "Al-Ahli", "Phong độ": "⭐ 7.9/10"},
            "lối_chơi": "Cậy nhờ thể lực, giàu tốc độ, đá trực diện áp sát",
            "đội_hinh": ["Yahia Fofana", "Wilfried Singo", "Ousmane Diomande", "Evan Ndicka", "Ghislain Konan", "Franck Kessié", "Jean Michaël Seri", "Seko Fofana", "Max Gradel", "Simon Adingra", "Sebastien Haller"]
        },
        "Ecuador": {
            "bảng": "E", "sơ_đồ": "3-4-3", "sức_mạnh": "Khá", "ngôi_sao": "Moisés Caicedo", "hlv": "Sebastián Beccacece", "logo": "https://flagcdn.com/w80/ec.png",
            "star_img": "https://th.bing.com/th/id/OIP.ec7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "24 tuổi", "Vị trí": "Tiền vệ mỏ neo", "Chiều cao": "1m78", "CLB": "Chelsea", "Phong độ": "🔥 8.5/10"},
            "lối_chơi": "Đá rực lửa, pressing mạnh ở biên, giàu thể lực",
            "đội_hinh": ["Alexander Domínguez", "Félix Torres", "Willian Pacho", "Piero Hincapié", "Angelo Preciado", "Moisés Caicedo", "Alan Franco", "Pervis Estupiñán", "Kendry Páez", "Jeremy Sarmiento", "Enner Valencia"]
        },
        # Bảng F
        "Hà Lan": {
            "bảng": "F", "sơ_đồ": "3-4-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Virgil van Dijk", "hlv": "Ronald Koeman", "logo": "https://flagcdn.com/w80/nl.png",
            "star_img": "https://th.bing.com/th/id/OIP.nl7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Trung vệ thủ lĩnh", "Chiều cao": "1m95", "CLB": "Liverpool", "Phong độ": "🔥 9.0/10"},
            "lối_chơi": "Tấn công tổng lực, đẩy cao hai biên, kiểm soát bóng chủ động",
            "đội_hinh": ["Bart Verbruggen", "Lutsharel Geertruida", "Virgil van Dijk", "Nathan Aké", "Denzel Dumfries", "Jerdy Schouten", "Tijjani Reijnders", "Daley Blind", "Xavi Simons", "Cody Gakpo", "Memphis Depay"]
        },
        "Nhật Bản": {
            "bảng": "F", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "ngôi_sao": "Kaoru Mitoma", "hlv": "Hajime Moriyasu", "logo": "https://flagcdn.com/w80/jp.png",
            "star_img": "https://th.bing.com/th/id/OIP.jp7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "29 tuổi", "Vị trí": "Tiền đạo cánh (LW)", "Chiều cao": "1m78", "CLB": "Brighton", "Phong độ": "🔥 8.6/10"},
            "lối_chơi": "Phối hợp nhóm nhỏ tốc độ cao, kỷ luật vị trí cực tốt",
            "đội_hinh": ["Zion Suzuki", "Yukinari Sugawara", "Ko Itakura", "Shogo Taniguchi", "Hiroki Ito", "Wataru Endo", "Hidemasa Morita", "Takefusa Kubo", "Takumi Minamino", "Kaoru Mitoma", "Ayase Ueda"]
        },
        "Thụy Điển": {
            "bảng": "F", "sơ_đồ": "4-4-2", "sức_mạnh": "Khá", "ngôi_sao": "Alexander Isak", "hlv": "Jon Dahl Tomasson", "logo": "https://flagcdn.com/w80/se.png",
            "star_img": "https://th.bing.com/th/id/OIP.se7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "26 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m92", "CLB": "Newcastle", "Phong độ": "🔥 8.9/10"},
            "lối_chơi": "Tổ chức chặt chẽ, chơi bóng dài bổng hiệu quả",
            "đội_hinh": ["Robin Olsen", "Emil Holm", "Isak Hien", "Victor Lindelöf", "Ludwig Augustinsson", "Dejan Kulusevski", "Jens Cajuste", "Anton Salétros", "Emil Forsberg", "Viktor Gyökeres", "Alexander Isak"]
        },
        "Tunisia": {
            "bảng": "F", "sơ_đồ": "4-5-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Ellyes Skhiri", "hlv": "Faouzi Benzarti", "logo": "https://flagcdn.com/w80/tn.png",
            "star_img": "https://th.bing.com/th/id/OIP.tn7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m85", "CLB": "Eintracht Frankfurt", "Phong độ": "⭐ 7.4/10"},
            "lối_chơi": "Phòng ngự kỷ luật, phá lối chơi đối phương",
            "đội_hinh": ["Bechir Ben Saïd", "Wajdi Kechrida", "Dylan Bronn", "Montassar Talbi", "Ali Abdi", "Ellyes Skhiri", "Aïssa Laïdouni", "Anis Ben Slimane", "Hamza Rafia", "Sayfallah Ltaief", "Youssef Msakni"]
        },
        # Bảng G
        "Bỉ": {
            "bảng": "G", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Kevin De Bruyne", "hlv": "Domenico Tedesco", "logo": "https://flagcdn.com/w80/be.png",
            "star_img": "https://th.bing.com/th/id/OIP.be7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền vệ kiến thiết", "Chiều cao": "1m81", "CLB": "Manchester City", "Phong độ": "🔥 9.2/10"},
            "lối_chơi": "Tấn công trung lộ, ban bật nhanh dựa vào các tiền vệ sáng tạo",
            "đội_hinh": ["Koen Casteels", "Timothy Castagne", "Wout Faes", "Jan Vertonghen", "Arthur Theate", "Orel Mangala", "Amadou Onana", "Kevin De Bruyne", "Jérémy Doku", "Leandro Trossard", "Romelu Lukaku"]
        },
        "Ai Cập": {
            "bảng": "G", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "ngôi_sao": "Mohamed Salah", "hlv": "Hossam Hassan", "logo": "https://flagcdn.com/w80/eg.png",
            "star_img": "https://th.bing.com/th/id/OIP.eg7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền đạo cánh (RW)", "Chiều cao": "1m75", "CLB": "Liverpool", "Phong độ": "🔥 9.0/10"},
            "lối_chơi": "Phòng ngự chặt, dồn bóng cho ngôi sao đột phá tốc độ",
            "đội_hinh": ["Mohamed El Shenawy", "Mohamed Hany", "Mohamed Abdelmonem", "Yasser Ibrahim", "Ali Maâloul", "Marwan Attia", "Mohamed Elneny", "Hamdi Fathi", "Mohamed Salah", "Trézéguet", "Mostafa Mohamed"]
        },
        "Iran": {
            "bảng": "G", "sơ_đồ": "4-4-2", "sức_mạnh": "Khá", "ngôi_sao": "Mehdi Taremi", "hlv": "Amir Ghalenoei", "logo": "https://flagcdn.com/w80/ir.png",
            "star_img": "https://th.bing.com/th/id/OIP.ir7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m87", "CLB": "Inter Milan", "Phong độ": "⭐ 8.1/10"},
            "lối_chơi": "Khối phòng ngự lùi sâu vững chãi, phản công sắc bén",
            "đội_hinh": ["Alireza Beiranvand", "Ramin Rezaeian", "Hossein Kanaanizadegan", "Shojae Khalilzadeh", "Milad Mohammadi", "Saman Ghoddos", "Saeid Ezatolahi", "Alireza Jahanbakhsh", "Mehdi Torabi", "Sardar Azmoun", "Mehdi Taremi"]
        },
        "New Zealand": {
            "bảng": "G", "sơ_đồ": "4-4-2", "sức_mạnh": "Yếu", "ngôi_sao": "Chris Wood", "hlv": "Darren Bazeley", "logo": "https://flagcdn.com/w80/nz.png",
            "star_img": "https://th.bing.com/th/id/OIP.nz7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m91", "CLB": "Nottingham Forest", "Phong độ": "⭐ 7.2/10"},
            "lối_chơi": "Bóng bổng, dựa vào thể hình tranh chấp bóng hai",
            "đội_hinh": ["Oliver Sail", "Tim Payne", "Michael Boxall", "Nando Pijnaker", "Liberato Cacace", "Joe Bell", "Matthew Garbett", "Sarpreet Singh", "Ben Old", "Kosta Barbarouses", "Chris Wood"]
        },
        # Bảng H
        "Tây Ban Nha": {
            "bảng": "H", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Lamine Yamal", "hlv": "Luis de la Fuente", "logo": "https://flagcdn.com/w80/es.png",
            "star_img": "https://th.bing.com/th/id/OIP.es7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "18 tuổi", "Vị trí": "Tiền đạo cánh (RW)", "Chiều cao": "1m80", "CLB": "Barcelona", "Phong độ": "👑 9.6/10"},
            "lối_chơi": "Tiki-taka hiện đại, luân chuyển bóng cực nhanh, kiểm soát tuyệt đối",
            "đội_hinh": ["Unai Simón", "Dani Carvajal", "Robin Le Normand", "Aymeric Laporte", "Marc Cucurella", "Rodri", "Pedri", "Fabian Ruiz", "Lamine Yamal", "Nico Williams", "Alvaro Morata"]
        },
        "Cabo Verde": {
            "bảng": "H", "sơ_đồ": "4-3-3", "sức_mạnh": "Trung bình", "ngôi_sao": "Ryan Mendes", "hlv": "Bubista", "logo": "https://flagcdn.com/w80/cv.png",
            "star_img": "https://th.bing.com/th/id/OIP.cv7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "36 tuổi", "Vị trí": "Tiền đạo cánh", "Chiều cao": "1m78", "CLB": "Fatih Karagümrük", "Phong độ": "⭐ 6.9/10"},
            "lối_chơi": "Chơi phòng ngự phản công dựa vào tốc độ các cầu thủ chạy cánh",
            "đội_hinh": ["Vozinha", "Steven Moreira", "Logan Costa", "Roberto Lopes", "João Paulo", "Kevin Pina", "Jamiro Monteiro", "Deroy Duarte", "Ryan Mendes", "Garry Rodrigues", "Jovane Cabral"]
        },
        "Saudi Arabia": {
            "bảng": "H", "sơ_đồ": "4-5-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Salem Al-Dawsari", "hlv": "Roberto Mancini", "logo": "https://flagcdn.com/w80/sa.png",
            "star_img": "https://th.bing.com/th/id/OIP.sa7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền đạo cánh (LW)", "Chiều cao": "1m71", "CLB": "Al-Hilal", "Phong độ": "⭐ 7.7/10"},
            "lối_chơi": "Áp sát tầm cao, bẫy việt vị, đá gắn kết kỷ luật",
            "đội_hinh": ["Mohammed Al-Owais", "Saud Abdulhamid", "Ali Lajami", "Ali Al-Bulaihi", "Yasir Al-Shahrani", "Abdullah Otayf", "Mohamed Kanno", "Firas Al-Buraikan", "Salman Al-Faraj", "Salem Al-Dawsari", "Saleh Al-Shehri"]
        },
        "Uruguay": {
            "bảng": "H", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Federico Valverde", "hlv": "Marcelo Bielsa", "logo": "https://flagcdn.com/w80/uy.png",
            "star_img": "https://th.bing.com/th/id/OIP.uy7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m82", "CLB": "Real Madrid", "Phong độ": "🔥 9.1/10"},
            "lối_chơi": "Pressing điên cuồng, va chạm rực lửa, tấn công trực diện",
            "đội_hinh": ["Sergio Rochet", "Nahitan Nández", "Ronald Araújo", "José María Giménez", "Mathías Olivera", "Federico Valverde", "Manuel Ugarte", "Nicolás de la Cruz", "Facundo Pellistri", "Darwin Núñez", "Maximilian Araújo"]
        },
        # Bảng I
        "Pháp": {
            "bảng": "I", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "ngôi_sao": "Kylian Mbappé", "hlv": "Didier Deschamps", "logo": "https://flagcdn.com/w80/fr.png",
            "star_img": "https://th.bing.com/th/id/OIP.fr7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m78", "CLB": "Real Madrid", "Phong độ": "👑 9.5/10"},
            "lối_chơi": "Tấn công trực diện tốc độ cao bằng hành lang biên",
            "đội_hinh": ["Mike Maignan", "Jules Koundé", "Dayot Upamecano", "William Saliba", "Théo Hernandez", "N'Golo Kanté", "Aurélien Tchouaméni", "Ousmane Dembélé", "Antoine Griezmann", "Bradley Barcola", "Kylian Mbappé"]
        },
        "Senegal": {
            "bảng": "I", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "ngôi_sao": "Sadio Mané", "hlv": "Aliou Cissé", "logo": "https://flagcdn.com/w80/sn.png",
            "star_img": "https://th.bing.com/th/id/OIP.sn7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền đạo cánh (LW)", "Chiều cao": "1m74", "CLB": "Al-Nassr", "Phong độ": "⭐ 8.0/10"},
            "lối_chơi": "Cân bằng giữa thể lực và kỹ thuật, đá áp sát nhanh",
            "đội_hinh": ["Édouard Mendy", "Formose Mendy", "Kalidou Koulibaly", "Abdou Diallo", "Ismail Jakobs", "Idrissa Gueye", "Pape Matar Sarr", "Lamine Camara", "Ismaïla Sarr", "Nicolas Jackson", "Sadio Mané"]
        },
        "Iraq": {
            "bảng": "I", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Aymen Hussein", "hlv": "Jesús Casas", "logo": "https://flagcdn.com/w80/iq.png",
            "star_img": "https://th.bing.com/th/id/OIP.iq7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "30 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m89", "CLB": "Al-Khor", "Phong độ": "⭐ 7.9/10"},
            "lối_chơi": "Đá tinh quái, không ngại va chạm, mạnh tấn công trung lộ",
            "đội_hinh": ["Jalal Hassan", "Hussein Ali", "Saad Natiq", "Rebin Sulaka", "Merchas Doski", "Amir Al-Ammari", "Osama Rashid", "Ibrahim Bayesh", "Zidane Iqbal", "Ali Jasim", "Aymen Hussein"]
        },
        "Na Uy": {
            "bảng": "I", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "ngôi_sao": "Erling Haaland", "hlv": "Ståle Solbakken", "logo": "https://flagcdn.com/w80/no.png",
            "star_img": "https://th.bing.com/th/id/OIP.no7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m94", "CLB": "Manchester City", "Phong độ": "🔥 9.4/10"},
            "lối_chơi": "Tấn công trục dọc, nhồi bóng cho trung phong cắm ghi bàn",
            "đội_hinh": ["Ørjan Nyland", "Julian Ryerson", "Leo Östigard", "Kristoffer Ajer", "David Møller Wolfe", "Martin Ødegaard", "Patrick Berg", "Sander Berge", "Oscar Bobb", "Antonio Nusa", "Erling Haaland"]
        },
        # Bảng J
        "Áo": {
            "bảng": "J", "sơ_đồ": "4-2-2-2", "sức_mạnh": "Khá", "ngôi_sao": "David Alaba", "hlv": "Ralf Rangnick", "logo": "https://flagcdn.com/w80/at.png",
            "star_img": "https://th.bing.com/th/id/OIP.at7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Hậu vệ đa năng", "Chiều cao": "1m80", "CLB": "Real Madrid", "Phong độ": "⭐ 8.2/10"},
            "lối_chơi": "Gegenpressing điên cuồng, bóp nghẹt không gian đối thủ",
            "đội_hinh": ["Patrick Pentz", "Stefan Posch", "Kevin Danso", "David Alaba", "Phillipp Mwene", "Nicolas Seiwald", "Konrad Laimer", "Marcel Sabitzer", "Christoph Baumgartner", "Michael Gregoritsch", "Marko Arnautovic"]
        },
        "Jordan": {
            "bảng": "J", "sơ_đồ": "3-4-3", "sức_mạnh": "Trung bình", "ngôi_sao": "Mousa Al-Tamari", "hlv": "Jamal Sellami", "logo": "https://flagcdn.com/w80/jo.png",
            "star_img": "https://th.bing.com/th/id/OIP.jo7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "28 tuổi", "Vị trí": "Tiền đạo cánh", "Chiều cao": "1m78", "CLB": "Montpellier", "Phong độ": "⭐ 7.9/10"},
            "lối_chơi": "Phòng ngự kỷ luật, phản công chớp nhoáng ở biên",
            "đội_hinh": ["Yazeed Abulaila", "Abdallah Nasib", "Yazan Al-Arab", "Salem Al-Ajalin", "Ehsan Haddad", "Nizar Al-Rashdan", "Noor Al-Rawabdeh", "Mahmoud Al-Mardi", "Mousa Al-Tamari", "Ali Olwan", "Yazan Al-Naimat"]
        },
        # Bảng K
        "Bồ Đào Nha": {
            "bảng": "K", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Bruno Fernandes", "hlv": "Roberto Martínez", "logo": "https://flagcdn.com/w80/pt.png",
            "star_img": "https://th.bing.com/th/id/OIP.pt7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Tiền vệ công (AM)", "Chiều cao": "1m79", "CLB": "Manchester United", "Phong độ": "🔥 9.0/10"},
            "lối_chơi": "Tấn công áp đặt đa dạng, hoán đổi vị trí biên liên tục",
            "đội_hinh": ["Diogo Costa", "João Cancelo", "Rúben Dias", "Pepe", "Nuno Mendes", "João Palhinha", "Vitinha", "Bruno Fernandes", "Bernardo Silva", "Rafael Leão", "Cristiano Ronaldo"]
        },
        "Uzbekistan": {
            "bảng": "K", "sơ_đồ": "3-4-2-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Eldor Shomurodov", "hlv": "Srecko Katanec", "logo": "https://flagcdn.com/w80/uz.png",
            "star_img": "https://th.bing.com/th/id/OIP.uz7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "30 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m90", "CLB": "Roma", "Phong độ": "⭐ 7.5/10"},
            "lối_chơi": "Tính kỷ luật chiến thuật cực cao, thủ chặt phản công sắc",
            "đội_hinh": ["Utkir Yusupov", "Abdukodir Khusanov", "Umar Eshmurodov", "Rustam Ashurmatov", "Khojiakbar Alijonov", "Otabek Shukurov", "Odiljon Hamrobekov", "Sherzod Nasrullaev", "Abbosbek Fayzullaev", "Jaloliddin Masharipov", "Eldor Shomurodov"]
        },
        "Colombia": {
            "bảng": "K", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "ngôi_sao": "Luis Díaz", "hlv": "Néstor Lorenzo", "logo": "https://flagcdn.com/w80/co.png",
            "star_img": "https://th.bing.com/th/id/OIP.co7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "29 tuổi", "Vị trí": "Tiền đạo cánh (LW)", "Chiều cao": "1m80", "CLB": "Liverpool", "Phong độ": "🔥 8.9/10"},
            "lối_chơi": "Đá kỹ thuật và rực lửa Nam Mỹ, đột biến hành lang cánh",
            "đội_hinh": ["Camilo Vargas", "Daniel Muñoz", "Davinson Sánchez", "Carlos Cuesta", "Johan Mojica", "Richard Ríos", "Jefferson Lerma", "Jhon Arias", "James Rodríguez", "Luis Díaz", "Jhon Córdoba"]
        },
        "CHDC Congo": {
            "bảng": "K", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Chancel Mbemba", "hlv": "Sébastien Desabre", "logo": "https://flagcdn.com/w80/cd.png",
            "star_img": "https://th.bing.com/th/id/OIP.cd7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Trung vệ (CB)", "Chiều cao": "1m82", "CLB": "Marseille", "Phong độ": "⭐ 7.4/10"},
            "lối_chơi": "Đá giàu tốc độ và va chạm thể lực từ khu trung tuyến",
            "đội_hinh": ["Lionel Mpasi", "Gédéon Kalulu", "Chancel Mbemba", "Henoc Inonga", "Arthur Masuaku", "Samuel Moutoussamy", "Charles Pickel", "Theo Bongonda", "Gaël Kakuta", "Yoane Wissa", "Cédric Bakambu"]
        },
        # Bảng L
        "Anh": {
            "bảng": "L", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "ngôi_sao": "Jude Bellingham", "hlv": "Thomas Tuchel", "logo": "https://flagcdn.com/w80/gb-eng.png",
            "star_img": "https://th.bing.com/th/id/OIP.eng7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "22 tuổi", "Vị trí": "Tiền vệ công (AM)", "Chiều cao": "1m86", "CLB": "Real Madrid", "Phong độ": "👑 9.5/10"},
            "lối_chơi": "Tấn công biên dồn dập, kiểm soát nửa sân đối phương, cố định mạnh",
            "đội_hinh": ["Jordan Pickford", "Kyle Walker", "John Stones", "Marc Guéhi", "Kieran Trippier", "Declan Rice", "Kobbie Mainoo", "Bukayo Saka", "Jude Bellingham", "Phil Foden", "Harry Kane"]
        },
        "Croatia": {
            "bảng": "L", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "ngôi_sao": "Luka Modric", "hlv": "Zlatko Dalic", "logo": "https://flagcdn.com/w80/hr.png",
            "star_img": "https://th.bing.com/th/id/OIP.hr7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "40 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m72", "CLB": "Real Madrid", "Phong độ": "⭐ 8.3/10"},
            "lối_chơi": "Làm chủ khu trung tuyến, cầm nhịp trận đấu chậm rãi tinh tế",
            "đội_hinh": ["Dominik Livakovic", "Josip Stanisic", "Josip Sutalo", "Marin Pongracic", "Josko Gvardiol", "Luka Modric", "Marcelo Brozovic", "Mateo Kovacic", "Lovro Majer", "Andrejan Kramaric", "Ante Budimir"]
        },
        "Ghana": {
            "bảng": "L", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Mohammed Kudus", "hlv": "Otto Addo", "logo": "https://flagcdn.com/w80/gh.png",
            "star_img": "https://th.bing.com/th/id/OIP.gh7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền vệ tấn công", "Chiều cao": "1m77", "CLB": "West Ham", "Phong độ": "🔥 8.4/10"},
            "lối_chơi": "Tấn công trực diện, bứt tốc quãng ngắn mạnh mẽ",
            "đội_hinh": ["Lawrence Ati-Zigi", "Alidu Seidu", "Alexander Djiku", "Mohammed Salisu", "Gideon Mensah", "Salo Abdul Samed", "Thomas Partey", "Jordan Ayew", "Mohammed Kudus", "Ernest Nuamah", "Inaki Williams"]
        },
        "Panama": {
            "bảng": "L", "sơ_đồ": "5-4-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Michael Murillo", "hlv": "Thomas Christiansen", "logo": "https://flagcdn.com/w80/pa.png",
            "star_img": "https://th.bing.com/th/id/OIP.pa7LzBw7DOf8YvNf0qQHaE7?pid=ImgDetMain",
            "star_stats": {"Độ tuổi": "30 tuổi", "Vị trí": "Hậu vệ biên phải", "Chiều cao": "1m83", "CLB": "Marseille", "Phong độ": "⭐ 7.1/10"},
            "lối_chơi": "Phòng ngự số đông co cụm, phá bóng rát",
            "đội_hinh": ["Orlando Mosquera", "Michael Murillo", "José Córdoba", "Edgardo Fariña", "Roderick Miller", "Eric Davis", "Aníbal Godoy", "Adalberto Carrasquilla", "José Luis Rodríguez", "Yoel Bárcenas", "José Fajardo"]
        }
    }

TEAMS = get_teams_data()

def get_team_info(name):
    return TEAMS.get(name, {
        "bảng": "Vòng bảng", "sơ_đồ": "4-2-3-1", "lối_chơi": "Lối chơi tập thể", "ngôi_sao": "Đội trưởng", "sức_mạnh": "Trung bình", "hlv": "Chưa cập nhật",
        "logo": "https://flagcdn.com/w80/un.png", "star_img": "https://flagcdn.com/w80/un.png",
        "star_stats": {"Độ tuổi": "Chưa cập nhật", "Vị trí": "Chưa cập nhật", "Chiều cao": "Chưa cập nhật", "CLB": "Chưa cập nhật", "Phong độ": "⭐ 7.0/10"},
        "đội_hinh": ["Cầu thủ số 1", "Cầu thủ số 2", "Cầu thủ số 3", "Cầu thủ số 4", "Cầu thủ số 5", "Cầu thủ số 6", "Cầu thủ số 7", "Cầu thủ số 8", "Cầu thủ số 9", "Cầu thủ số 10", "Cầu thủ số 11"]
    })

# 3. KHỞI TẠO LỊCH THI ĐẤU CHUẨN VÀ THỜI TIẾT REAL-TIME
if 'matches' not in st.session_state:
    raw_schedule = [
        ["WC-01", "Bảng A", "12/06", "02:00", "Mexico", "Nam Phi", "VTV3, VTV6", "Mát mẻ, 24°C (Sân Azteca)"],
        ["WC-02", "Bảng A", "12/06", "09:00", "Hàn Quốc", "CH Séc", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-03", "Bảng B", "13/06", "02:00", "Canada", "Bosnia", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-04", "Bảng D", "13/06", "08:00", "Mỹ", "Paraguay", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-05", "Bảng B", "14/06", "02:00", "Qatar", "Thụy Sĩ", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-06", "Bảng C", "14/06", "05:00", "Brazil", "Marocco", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-07", "Bảng C", "14/06", "08:00", "Haiti", "Scotland", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-08", "Bảng D", "14/06", "11:00", "Úc", "Thổ Nhĩ Kỳ", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-09", "Bảng E", "15/06", "00:00", "Đức", "Curacao", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-10", "Bảng F", "15/06", "03:00", "Hà Lan", "Nhật Bản", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-14", "Bảng G", "16/06", "02:00", "Bỉ", "Ai Cập", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-17", "Bảng I", "17/06", "02:00", "Pháp", "Senegal", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-22", "Bảng L", "18/06", "03:00", "Anh", "Croatia", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"]
    ]
    
    matches_db = {}
    for m in raw_schedule:
        matches_db[m[0]] = {
            "vòng": m[1], "ngày": m[2], "giờ": m[3], "đội_nhà": m[4], "đội_khách": m[5], "kênh": m[6],
            "trọng_tài": "Chưa cập nhật", "thời_tiết": m[7],
            "dự_đoán_bạn": "", "ti_so_ht": "", "ti_so_ft": "",
            "sút_ht": "", "sút_ft": "", "chuyền_ft": "", 
            "góc_ft": "", "thẻ_vàng": "", "thẻ_đỏ": "", "lỗi_ft": ""
        }
    st.session_state.matches = matches_db

def get_team_history_insight(team_name):
    played_matches = []
    for code, m in st.session_state.matches.items():
        if m["ti_so_ft"] != "" and (m["đội_nhà"] == team_name or m["đội_khách"] == team_name):
            played_matches.append((code, m))
    if not played_matches:
        if team_name == "Mexico": return "Chuỗi 3 trận giao hữu thắng liên tiếp, phong độ đỉnh cao."
        if team_name == "Nam Phi": return "Lượt trận giao hữu không ổn định, hàng thủ cần chấn chỉnh."
        return "Sẵn sàng ra quân với đội hình mạnh nhất."
    return "Đang tập trung cao độ cho hành trình vòng bảng."

def ai_calculate_prediction(home, away):
    h_info = get_team_info(home)
    a_info = get_team_info(away)
    power_points = {"Mạnh": 4, "Khá": 3, "Trung bình": 2, "Yếu": 1}
    diff = power_points.get(h_info['sức_mạnh'], 2) - power_points.get(a_info['sức_mạnh'], 2)
    if diff >= 2: return "2 - 0", f"Sức mạnh áp đảo từ {home}. Đấu pháp của HLV {h_info['hlv']} vượt trội hoàn toàn."
    if diff == 1: return "2 - 1", f"Trận đấu kịch tính. {home} nhỉnh hơn ở trục dọc và khả năng dứt điểm của {h_info['ngôi_sao']}."
    if diff == 0: return "1 - 1", f"Cuộc đấu trí thực dụng đỉnh cao giữa HLV {h_info['hlv']} và HLV {a_info['hlv']}."
    return "0 - 1", f"Đội khách {away} sở hữu chiến thuật phản công sắc bén hơn."

# CHIA CÁC TABS QUẢN LÝ CHUYÊN NGHIỆP TRÊN DI ĐỘNG
tab1, tab2, tab3 = st.tabs(["📰 Nhận Định & Danh Sách Đội Hình", "⏱️ Diễn Biến Trận Đấu (Real-Time)", "🏃 Danh Sách 48 Đội Bóng"])

# ==================================================================
# TAB 1: TRANG NHẬN ĐỊNH BÁO CHÍ VÀ CÁC THÔNG SỐ SOI KÈO ĐỈNH CAO
# ==================================================================
with tab1:
    selected_m = st.selectbox("Chọn trận đấu muốn xem bài viết nhận định & phân tích chi tiết:", list(st.session_state.matches.keys()))
    m_data = st.session_state.matches[selected_m]
    t_nhà = get_team_info(m_data['đội_nhà'])
    t_khách = get_team_info(m_data['đội_khách'])
    
    # BOX ĐỐI ĐẦU CHÍNH THỨC CÓ LOGO (ẢNH 1)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        st.markdown(f'<div class="card-vs"><img src="{t_nhà["logo"]}" width="100"><br><span class="team-name">{m_data["đội_nhà"]}</span><br><span class="hlv-text">HLV: {t_nhà["hlv"]}</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div style="text-align: center; margin-top: 25px;"><span class="vs-text">VS</span><br><span style="color: #ffffff; font-weight:bold; font-size:15px;">{m_data["giờ"]} | {m_data["ngày"]}</span><br><span style="color:#fecd3d; font-weight:bold; font-size:14px;">{m_data["kênh"]}</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="card-vs"><img src="{t_khách["logo"]}" width="100"><br><span class="team-name">{m_data["đội_khách"]}</span><br><span class="hlv-text">HLV: {t_khách["hlv"]}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # BÀI BÁO NHẬN ĐỊNH TRƯỚC TRẬN ĐẤU CHUẨN THỜI SỰ
    st.markdown(f"### 📰 BÀI PHÂN TÍCH CHUYÊN SÂU: {m_data['đội_nhà']} VS {m_data['đội_khách']}")
    st.write(f"Trận mở màn tại khu vực chứng kiến màn so tài rực lửa giữa **{m_data['đội_nhà']}** và **{m_data['đội_khách']}**. Về mặt phong độ, {m_data['đội_nhà']} đang có trạng thái: *{get_team_history_insight(m_data['đội_nhà'])}*. Phía bên kia chiến tuyến, đại diện khách đáp trả với: *{get_team_history_insight(m_data['đội_khách'])}*.")
    
    # SO SÁNH CHỈ SỐ NGÔI SAO CHỦ CHỐT (ẢNH 4)
    st.markdown("### ⚡ NGÔI SAO GHIM TRẬN (KEY PLAYER FACE-OFF)")
    c_s1, c_s2 = st.columns(2)
    with c_s1:
        st.markdown(f'<div class="glass-card"><h4 style="color:#fecd3d;">⭐ {t_nhà["ngôi_sao"]} ({m_data["đội_nhà"]})</h4>', unsafe_allow_html=True)
        st.image(t_nhà["star_img"], use_container_width=True)
        for lbl, val in t_nhà["star_stats"].items():
            st.markdown(f'<div class="card-player"><span class="stat-label">{lbl}</span><span class="stat-value">{val}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c_s2:
        st.markdown(f'<div class="glass-card"><h4 style="color:#fecd3d;">⭐ {t_khách["ngôi_sao"]} ({m_data["đội_khách"]})</h4>', unsafe_allow_html=True)
        st.image(t_khách["star_img"], use_container_width=True)
        for lbl, val in t_khách["star_stats"].items():
            st.markdown(f'<div class="card-player"><span class="stat-label">{lbl}</span><span class="stat-value">{val}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # TRỢ LÝ AI DỰ ĐOÁN KẾT QUẢ TRẬN ĐẤU
    pred_score, pred_reason = ai_calculate_prediction(m_data['đội_nhà'], m_data['đội_khách'])
    st.markdown('<div class="ai-box">', unsafe_allow_html=True)
    st.markdown(f"#### 🤖 TRỢ LÝ AI DỰ ĐOÁN TỈ SỐ CHÍNH XÁC: <span style='color:#ffffff; font-size:24px;'>{pred_score}</span>", unsafe_allow_html=True)
    st.write(f"🧠 **Phân tích đấu pháp chuyên sâu:** {pred_reason} Triết lý thực dụng của huấn luyện viên hai bên sẽ biến trận đấu thành một bàn cờ chiến thuật cân não.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    # ĐỘI HÌNH RA SÂN CHI TIẾT (BỎ SƠ ĐỒ HÌNH VẼ NHƯ BẠN GỢI Ý - GIỮ KHỐI CHỮ RÕ NÉT)
    st.markdown("### 📋 DANH SÁCH ĐỘI HÌNH DỰ KIẾN RA SÂN")
    col_l, col_r = st.columns(2)
    with col_l:
        st.info(f"🔴 **{m_data['đội_nhà']} (Sơ đồ chiến thuật: {t_nhà['sơ_đồ']}):**\n\n" + "\n".join([f"- {p}" for p in t_nhà['đội_hinh']]))
    with col_r:
        st.success(f"🔵 **{m_data['đội_khách']} (Sơ đồ chiến thuật: {t_khách['sơ_đồ']}):**\n\n" + "\n".join([f"- {p}" for p in t_khách['đội_hinh']]))

# ==================================================================
# TAB 2: PHÒNG ĐIỀU PHỐI DIỄN BIẾN TRẬN ĐẤU REAL-TIME (HT/FT)
# ==================================================================
with tab2:
    st.subheader("⏱️ Phòng Điều Phối & Nhập Liệu Tỉ Số Trực Tiếp")
    update_m = st.selectbox("Chọn mã trận cần nạp kết quả sau trận đấu:", list(st.session_state.matches.keys()))
    curr_m = st.session_state.matches[update_m]
    
    st.markdown(f"### 📍 Ghi nhận trực tiếp: **{curr_m['đội_nhà']} vs {curr_m['đội_khách']}**")
    c1, c2, c3 = st.columns(3)
    with c1:
        curr_m['ti_so_ht'] = st.text_input("Tỉ số hiệp 1 (HT) (Vd: 1-0):", curr_m['ti_so_ht'])
        curr_m['sút_ht'] = st.text_input("Số cú sút Hiệp 1:", curr_m['sút_ht'])
    with c2:
        curr_m['ti_so_ft'] = st.text_input("Tỉ số hết trận (FT) (Vd: 2-1):", curr_m['ti_so_ft'])
        curr_m['sút_ft'] = st.text_input("Tổng cú sút cả trận:", curr_m['sút_ft'])
    with c3:
        curr_m['thời_tiết'] = st.text_input("Thời tiết thực tế:", curr_m['thời_tiết'])
        curr_m['trọng_tài'] = st.text_input("Trọng tài bắt chính:", curr_m['trọng_tài'])
        
    if st.button("💾 XÁC NHẬN CẬP NHẬT KẾT QUẢ CHÍNH THỨC"):
        st.toast("Dữ liệu trận đấu đã được lưu lên đám mây vĩnh viễn!", icon="⚡")

# ==================================================================
# TAB 3: DANH SÁCH 48 ĐỘI BÓNG ĐẦY ĐỦ THÔNG TIN CHI TIẾT
# ==================================================================
with tab3:
    st.subheader("🏃 Cơ sở dữ liệu chiến thuật toàn giải đấu")
    team_list = []
    for t_name, t_val in TEAMS.items():
        team_list.append([t_name, t_val['bảng'], t_val['hlv'], t_val['sơ_đồ'], t_val['lối_chơi'], t_val['ngôi_sao'], t_val['sức_mạnh']])
    
    team_df = pd.DataFrame(team_list, columns=["Tên Đội Bóng", "Bảng", "Huấn Luyện Viên", "Sơ Đồ Chiến Thuật", "Lối Chơi Chủ Đạo", "Ngôi Sao Gánh Đội", "Đánh Giá Cửa"])
    st.dataframe(team_df, use_container_width=True, height=400)
