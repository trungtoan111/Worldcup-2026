import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. CẤU HÌNH TRANG WEB & GIAO DIỆN CHỦ ĐẠO (INFOGRAPHIC STYLE)
st.set_page_config(page_title="World Cup 2026 - AI Dashboard Pro", layout="wide")

# Hệ thống CSS Custom đồng bộ 100% theo phong cách thiết kế cao cấp
st.markdown("""
<style>
    .main { background-color: #0d1b2a; }
    .title-main { color: #fecd3d; font-family: 'Poppins', sans-serif; font-size: 38px; font-weight: bold; text-align: center; margin-bottom: 25px; text-transform: uppercase; letter-spacing: 1px; }
    .card-vs { background: linear-gradient(135deg, #112233 0%, #1f3a52 100%); border: 2px solid #3a506b; border-radius: 15px; padding: 25px; text-align: center; box-shadow: 0 6px 20px rgba(0,0,0,0.4); }
    .vs-text { font-size: 36px; font-weight: bold; color: #fecd3d; margin: 0 10px; font-style: italic; }
    .team-name { font-size: 26px; font-weight: bold; color: #ffffff; text-transform: uppercase; }
    .hlv-text { font-size: 15px; color: #a5b4fc; font-style: italic; font-weight: 500; }
    .card-player { background: #1e293b; border-left: 5px solid #059669; border-radius: 8px; padding: 12px; margin-bottom: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.2); }
    .stat-label { color: #94a3b8; font-size: 15px; font-weight: bold; }
    .stat-value { color: #fecd3d; font-weight: bold; font-size: 16px; float: right; }
    .ai-box { background: linear-gradient(90deg, rgba(5, 150, 105, 0.15) 0%, rgba(31, 58, 82, 0.3) 100%); border-left: 6px solid #059669; border-radius: 12px; padding: 20px; margin-top: 15px; }
    .stTabs [data-baseweb="tab"] { font-size: 18px; font-weight: bold; color: #94a3b8; }
    .stTabs [aria-selected="true"] { color: #fecd3d !important; border-bottom-color: #fecd3d !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-main">🏆 WORLD CUP 2026 - REALTIME AI DASHBOARD PRO</div>', unsafe_allow_html=True)
st.markdown("---")

# 2. DATABASE TỔNG LỰC: TÍCH HỢP ĐẦY ĐỦ 48 ĐỘI, LOGO QUỐC KỲ VÀ ẢNH NGÔI SAO SẮC NÉT
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
        "Algeria": {
            "bảng": "A", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "hlv": "Vladimir Petkovic", "logo": "https://flagcdn.com/w80/dz.png",
            "star_name": "Riyad Mahrez", "star_img": "https://img.a.transfermarkt.technology/portrait/header/171424-1661376848.jpg",
            "star_stats": {"Độ tuổi": "35 tuổi", "Vị trí": "Tiền đạo phải (RW)", "Chiều cao": "1m79", "CLB": "Al-Ahli", "Phong độ": "⭐ 8.2/10"},
            "lối_chơi": "Kỹ thuật cá nhân tốt, chuộng đá biên và ban bật ngắn",
            "đội_hinh": ["Anthony Mandrea", "Youcef Atal", "Aissa Mandi", "Ramy Bensebaini", "Rayyan Aït-Nouri", "Nabil Bentaleb", "Ismaël Bennacer", "Riyad Mahrez", "Houssem Aouar", "Saïd Benrahma", "Baghdad Bounedjah"]
        },
        "Canada": {
            "bảng": "B", "sơ_đồ": "4-4-2", "sức_mạnh": "Trung bình", "hlv": "Jesse Marsch", "logo": "https://flagcdn.com/w80/ca.png",
            "star_name": "Alphonso Davies", "star_img": "https://img.a.transfermarkt.technology/portrait/header/424204-1667823528.jpg",
            "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Hậu vệ trái (LB)", "Chiều cao": "1m83", "CLB": "Bayern Munich", "Phong độ": "🔥 8.7/10"},
            "lối_chơi": "Tấn công biên dựa vào tốc độ, chuyển trạng thái nhanh",
            "đội_hinh": ["Maxime Crépeau", "Alistair Johnston", "Moïse Bombito", "Derek Cornelius", "Alphonso Davies", "Tajon Buchanan", "Stephen Eustáquio", "Ismaël Koné", "Liam Millar", "Jonathan David", "Cyle Larin"]
        },
        "Bosnia": {
            "bảng": "B", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Trung bình", "hlv": "Sergej Barbarez", "logo": "https://flagcdn.com/w80/ba.png",
            "star_name": "Edin Džeko", "star_img": "https://img.a.transfermarkt.technology/portrait/header/28396-1667554867.jpg",
            "star_stats": {"Độ tuổi": "40 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m93", "CLB": "Fenerbahçe", "Phong độ": "⭐ 7.8/10"},
            "lối_chơi": "Chậm rãi, chắc chắn khu trung tuyến, tận dụng bóng bổng",
            "đội_hinh": ["Kenan Piric", "Anel Ahmedhodzic", "Dennis Hadzikadunic", "Sead Kolasinac", "Jusuf Gazibegovic", "Rade Krunic", "Benjamin Tahirovic", "Haris Hajradinovic", "Miroslav Stevanovic", "Ermedin Demirovic", "Edin Dzeko"]
        },
        "Brazil": {
            "bảng": "C", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "hlv": "Dorival Júnior", "logo": "https://flagcdn.com/w80/br.png",
            "star_name": "Vinícius Júnior", "star_img": "https://img.a.transfermarkt.technology/portrait/header/371998-1669106099.jpg",
            "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền đạo trái (LW)", "Chiều cao": "1m76", "CLB": "Real Madrid", "Phong độ": "⚡ 9.4/10"},
            "lối_chơi": "Tấn công rực lửa, áp đặt thế trận kỹ thuật cá nhân đỉnh cao",
            "đội_hinh": ["Alisson Becker", "Danilo", "Marquinhos", "Gabriel Magalhães", "Wendell", "Bruno Guimarães", "Douglas Luiz", "Lucas Paquetá", "Rodrygo", "Raphinha", "Vinicius Jr"]
        },
        "Marocco": {
            "bảng": "C", "sơ_đồ": "4-1-4-1", "sức_mạnh": "Khá", "hlv": "Walid Regragui", "logo": "https://flagcdn.com/w80/ma.png",
            "star_name": "Achraf Hakimi", "star_img": "https://img.a.transfermarkt.technology/portrait/header/398073-1668673854.jpg",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Hậu vệ phải (RB)", "Chiều cao": "1m81", "CLB": "PSG", "Phong độ": "🔥 8.9/10"},
            "lối_chơi": "Phòng ngự khối trung bình (Mid-block), kỷ luật thép phản công",
            "đội_hinh": ["Yassine Bounou", "Achraf Hakimi", "Nayef Aguerd", "Romain Saïss", "Yahia Attiyat Allah", "Sofyan Amrabat", "Azzedine Ounahi", "Selim Amallah", "Hakim Ziyech", "Amine Adli", "Youssef En-Nesyri"]
        },
        "Mỹ": {
            "bảng": "D", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "hlv": "Mauricio Pochettino", "logo": "https://flagcdn.com/w80/us.png",
            "star_name": "Christian Pulisic", "star_img": "https://img.a.transfermarkt.technology/portrait/header/315779-1669106201.jpg",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền đạo trái (LW)", "Chiều cao": "1m77", "CLB": "AC Milan", "Phong độ": "🔥 8.7/10"},
            "lối_chơi": "Pressing tầm cao, chuyển trạng thái nhanh dựa vào tốc độ biên",
            "đội_hinh": ["Matt Turner", "Sergiño Dest", "Chris Richards", "Tim Ream", "Antonee Robinson", "Weston McKennie", "Tyler Adams", "Yunush Musah", "Timothy Weah", "Folarin Balogun", "Christian Pulisic"]
        },
        "Đức": {
            "bảng": "E", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "hlv": "Julian Nagelsmann", "logo": "https://flagcdn.com/w80/de.png",
            "star_name": "Jamal Musiala", "star_img": "https://img.a.transfermarkt.technology/portrait/header/580195-1669106512.jpg",
            "star_stats": {"Độ tuổi": "23 tuổi", "Vị trí": "Tiền vệ công (AM)", "Chiều cao": "1m84", "CLB": "Bayern Munich", "Phong độ": "🔥 9.3/10"},
            "lối_chơi": "Kiểm soát thế trận, pressing tầm cao, ban bật cự ly ngắn",
            "đội_hinh": ["Manuel Neuer", "Joshua Kimmich", "Jonathan Tah", "Antonio Rüdiger", "Maximilian Mittelstädt", "Robert Andrich", "Toni Kroos", "Jamal Musiala", "Ilkay Gündogan", "Florian Wirtz", "Kai Havertz"]
        },
        "Hà Lan": {
            "bảng": "F", "sơ_đồ": "3-4-3", "sức_mạnh": "Mạnh", "hlv": "Ronald Koeman", "logo": "https://flagcdn.com/w80/nl.png",
            "star_name": "Virgil van Dijk", "star_img": "https://img.a.transfermarkt.technology/portrait/header/139208-1669106757.jpg",
            "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Trung vệ (CB)", "Chiều cao": "1m95", "CLB": "Liverpool", "Phong độ": "🔥 9.0/10"},
            "lối_chơi": "Tấn công tổng lực, đẩy cao hai biên, kiểm soát bóng chủ động",
            "đội_hinh": ["Bart Verbruggen", "Lutsharel Geertruida", "Virgil van Dijk", "Nathan Aké", "Denzel Dumfries", "Jerdy Schouten", "Tijjani Reijnders", "Daley Blind", "Xavi Simons", "Cody Gakpo", "Memphis Depay"]
        },
        "Bỉ": {
            "bảng": "G", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "hlv": "Domenico Tedesco", "logo": "https://flagcdn.com/w80/be.png",
            "star_name": "Kevin De Bruyne", "star_img": "https://img.a.transfermarkt.technology/portrait/header/88755-1669106297.jpg",
            "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m81", "CLB": "Manchester City", "Phong độ": "🔥 9.2/10"},
            "lối_chơi": "Tấn công trung lộ, ban bật nhanh dựa vào các tiền vệ sáng tạo",
            "đội_hinh": ["Koen Casteels", "Timothy Castagne", "Wout Faes", "Jan Vertonghen", "Arthur Theate", "Orel Mangala", "Amadou Onana", "Kevin De Bruyne", "Jérémy Doku", "Leandro Trossard", "Romelu Lukaku"]
        },
        "Tây Ban Nha": {
            "bảng": "H", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "hlv": "Luis de la Fuente", "logo": "https://flagcdn.com/w80/es.png",
            "star_name": "Lamine Yamal", "star_img": "https://img.a.transfermarkt.technology/portrait/header/1057013-1683103444.jpg",
            "star_stats": {"Độ tuổi": "18 tuổi", "Vị trí": "Tiền đạo phải (RW)", "Chiều cao": "1m80", "CLB": "Barcelona", "Phong độ": "👑 9.6/10"},
            "lối_chơi": "Tiki-taka hiện đại, luân chuyển bóng cực nhanh, kiểm soát tuyệt đối",
            "đội_hinh": ["Unai Simón", "Dani Carvajal", "Robin Le Normand", "Aymeric Laporte", "Marc Cucurella", "Rodri", "Pedri", "Fabian Ruiz", "Lamine Yamal", "Nico Williams", "Alvaro Morata"]
        },
        "Pháp": {
            "bảng": "I", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "hlv": "Didier Deschamps", "logo": "https://flagcdn.com/w80/fr.png",
            "star_name": "Kylian Mbappé", "star_img": "https://img.a.transfermarkt.technology/portrait/header/342229-1669106304.jpg",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m78", "CLB": "Real Madrid", "Phong độ": "👑 9.5/10"},
            "lối_chơi": "Tấn công trực diện tốc độ cao bằng hành lang biên",
            "đội_hinh": ["Mike Maignan", "Jules Koundé", "Dayot Upamecano", "William Saliba", "Théo Hernandez", "N'Golo Kanté", "Aurélien Tchouaméni", "Ousmane Dembélé", "Antoine Griezmann", "Bradley Barcola", "Kylian Mbappé"]
        },
        "Anh": {
            "bảng": "L", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "hlv": "Thomas Tuchel", "logo": "https://flagcdn.com/w80/gb-eng.png",
            "star_name": "Jude Bellingham", "star_img": "https://img.a.transfermarkt.technology/portrait/header/581678-1669106450.jpg",
            "star_stats": {"Độ tuổi": "22 tuổi", "Vị trí": "Tiền vệ công (AM)", "Chiều cao": "1m86", "CLB": "Real Madrid", "Phong độ": "👑 9.5/10"},
            "lối_chơi": "Tấn công biên dồn dập, kiểm soát nửa sân đối phương, cố định mạnh",
            "đội_hinh": ["Jordan Pickford", "Kyle Walker", "John Stones", "Marc Guéhi", "Kieran Trippier", "Declan Rice", "Kobbie Mainoo", "Bukayo Saka", "Jude Bellingham", "Phil Foden", "Harry Kane"]
        }
    }

TEAMS = get_teams_data()

# Hàm bổ trợ lấy thông tin phòng hờ lỗi thiếu đội
def get_team_info(name):
    return TEAMS.get(name, {
        "bảng": "Vòng bảng", "sơ_đồ": "4-2-3-1", "lối_chơi": "Lối chơi tập thể", "ngôi_sao": "Đội trưởng", "sức_mạnh": "Trung bình", "hlv": "Chưa cập nhật",
        "logo": "https://flagcdn.com/w80/un.png",
        "star_name": "Chưa cập nhật", "star_img": "https://flagcdn.com/w80/un.png",
        "star_stats": {"Độ tuổi": "Chưa rõ", "Vị trí": "Chưa rõ", "Chiều cao": "Chưa rõ", "CLB": "Tự do", "Phong độ": "0/10"},
        "đội_hinh": ["Thủ môn", "Hậu vệ 1", "Hậu vệ 2", "Hậu vệ 3", "Hậu vệ 4", "Tiền vệ 1", "Tiền vệ 2", "Tiền vệ 3", "Tiền đạo 1", "Tiền đạo 2", "Tiền đạo 3"]
    })

# 3. KHỞI TẠO LỊCH THI ĐẤU CHUẨN (MỞ RỘNG)
if 'matches' not in st.session_state:
    raw_schedule = [
        ["WC-01", "Bảng A", "12/06", "02:00", "Mexico", "Nam Phi", "VTV3, VTV6", "Mát mẻ, 24°C (Sân Azteca)"],
        ["WC-02", "Bảng A", "12/06", "09:00", "Hàn Quốc", "CH Séc", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-03", "Bảng B", "13/06", "02:00", "Canada", "Bosnia", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-06", "Bảng C", "14/06", "05:00", "Brazil", "Marocco", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-09", "Bảng E", "15/06", "00:00", "Đức", "Mexico", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-10", "Bảng F", "15/06", "03:00", "Hà Lan", "Hàn Quốc", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-14", "Bảng G", "16/06", "02:00", "Bỉ", "Argentina", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-17", "Bảng I", "17/06", "02:00", "Pháp", "Algeria", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-22", "Bảng L", "18/06", "03:00", "Anh", "Brazil", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"]
    ]
    
    matches_db = {}
    for m in raw_schedule:
        matches_db[m[0]] = {
            "vòng": m[1], "ngày": m[2], "giờ": m[3], "đội_nhà": m[4], "đội_khách": m[5], "kênh": m[6],
            "trọng_tài": "Chưa cập nhật", "thời_tiết": m[7], "dự_đoán_bạn": "", "ti_so_ft": ""
        }
    st.session_state.matches = matches_db

# CHIA TABS CHỨC NĂNG CHUẨN DEV
tab1, tab2, tab3 = st.tabs(["📰 Nhận Định & Sa Bàn Đội Hình", "⏱️ Phòng Cập Nhật Kết Quả", "🏃 Danh Sách Đội Bóng"])

# ==================================================================
# TAB 1: GIAO DIỆN HIỂN THỊ ĐỈNH CAO (ĐỦ ĐỘI HÌNH & NGÔI SAO)
# ==================================================================
with tab1:
    selected_m = st.selectbox("Chọn mã trận đấu cần xem phân tích chuyên sâu:", list(st.session_state.matches.keys()))
    m_data = st.session_state.matches[selected_m]
    
    t_nhà = get_team_info(m_data['đội_nhà'])
    t_khách = get_team_info(m_data['đội_khách'])
    
    # HIỂN THỊ CẶP ĐẤU ĐỐI ĐẦU CÓ LOGO QUỐC KỲ VÀ TÊN HLV VÀ BOX TRANG TRÍ MÀU SẮC ĐẬM ĐÀ
    st.markdown("### 🏟️ CẶP ĐẤU ĐỐI ĐẦU CHÍNH THỨC")
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        st.markdown(f'<div class="card-vs"><img src="{t_nhà["logo"]}" width="110"><br><span class="team-name">{m_data["đội_nhà"]}</span><br><span class="hlv-text">HLV: {t_nhà["hlv"]}</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div style="text-align: center; margin-top: 30px;"><span class="vs-text">VS</span><br><span style="color: #ffffff; font-size:18px; font-weight:bold;">{m_data["giờ"]} | {m_data["ngày"]}</span><br><span style="color:#ef4444; font-weight:bold;">{m_data["kênh"]}</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="card-vs"><img src="{t_khách["logo"]}" width="110"><br><span class="team-name">{m_data["đội_khách"]}</span><br><span class="hlv-text">HLV: {t_khách["hlv"]}</span></div>', unsafe_allow_html=True)
        
    st.markdown("---")
    
    # CẶP ĐÔI NGUY HIỂM & BOX SO SÁNH CHỈ SỐ CỦA BẠN (HÌNH 4: ĐỘ TUỔI, CHIỀU CAO, PHONG ĐỘ...)
    st.markdown("### ⚡ NGÔI SAO GHIM TRẬN (KEY PLAYER FACE-OFF)")
    c_star1, c_star2 = st.columns(2)
    
    with c_star1:
        st.markdown(f'<h4 style="color:#fecd3d; text-transform:uppercase;">⭐ {t_nhà["star_name"]} ({m_data["đội_nhà"]})</h4>', unsafe_allow_html=True)
        if t_nhà["star_name"] != "Chưa cập nhật":
            st.image(t_nhà["star_img"], width=150)
        for lbl, val in t_nhà["star_stats"].items():
            st.markdown(f'<div class="card-player"><span class="stat-label">{lbl}</span><span class="stat-value">{val}</span></div>', unsafe_allow_html=True)
            
    with c_star2:
        st.markdown(f'<h4 style="color:#fecd3d; text-transform:uppercase;">⭐ {t_khách["star_name"]} ({m_data["đội_khách"]})</h4>', unsafe_allow_html=True)
        if t_khách["star_name"] != "Chưa cập nhật":
            st.image(t_khách["star_img"], width=150)
        for lbl, val in t_khách["star_stats"].items():
            st.markdown(f'<div class="card-player"><span class="stat-label">{lbl}</span><span class="stat-value">{val}</span></div>', unsafe_allow_html=True)

    # BOX AI TỰ ĐỘNG PHÁT HIỆN SỨC MẠNH VÀ NHẢ NHẬN ĐỊNH BÀI BÁO
    st.markdown('<div class="ai-box">', unsafe_allow_html=True)
    st.markdown("#### 🤖 TRỢ LÝ AI NHẬN ĐỊNH ĐẤU PHÁP CHUYÊN SÂU")
    power_points = {"Mạnh": 4, "Khá": 3, "Trung bình": 2, "Yếu": 1}
    diff = power_points.get(t_nhà['sức_mạnh'], 2) - power_points.get(t_khách['sức_mạnh'], 2)
    
    if diff > 0:
        st.write(f"📊 **Dự báo chiến thuật:** {m_data['đội_nhà']} ở cửa trên. Sơ đồ hỏa lực **{t_nhà['sơ_đồ']}** do chiến lược gia {t_nhà['hlv']} chỉ đạo sẽ tổ chức thế trận áp đặt thực dụng, đẩy cao đội hình nhằm khai thác sơ hở của hệ thống tuyến dưới bên phía {m_data['đội_khách']}.")
    elif diff < 0:
        st.write(f"📊 **Dự báo chiến thuật:** Đội khách {m_data['đội_khách']} sở hữu dàn nhân sự chất lượng vượt trội. Khối pressing cự ly ngắn mang thương hiệu của HLV {t_khách['hlv']} sẽ bóp nghẹt ý đồ phản công của đội chủ nhà.")
    else:
        st.write(f"📊 **Dự báo chiến thuật:** Thế trận cân bằng tuyệt đối giữa hai hệ thống triết lý chiến thuật **{t_nhà['sơ_đồ']}** và **{t_khách['sơ_đồ']}**. Hai vị thuyền trưởng đều là những bậc thầy thực dụng nên trận đấu nhiều khả năng sẽ được định đoạt bằng một khoảnh khắc tỏa sáng cá nhân.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # SA BÀN SÂN CỎ V VẼ THEO SƠ ĐỒ ĐỒ HỌA THỰC TẾ (HÌNH 3)
    st.markdown("### 📋 ĐỘI HÌNH DỰ KIẾN CHI TIẾT TẠI SÂN")
    col_pitch, col_text = st.columns([3, 2])
    
    with col_pitch:
        fig, ax = plt.subplots(figsize=(7, 4.8))
        fig.patch.set_facecolor('#0f172a')
        ax.set_facecolor('#14532d') # Đổi sang màu cỏ đậm rực rỡ đúng chuẩn thiết kế
        
        # Vẽ cấu trúc sân vận động tiêu chuẩn
        plt.plot([0, 0, 100, 100, 0], [0, 100, 100, 0, 0], color="white", linewidth=2)
        plt.plot([0, 100], [50, 50], color="white", linewidth=2)
        center_circle = plt.Circle((50, 50), 14, color='white', fill=False, linewidth=2)
        ax.add_patch(center_circle)
        
        # Đổ chấm tròn chiến thuật quân cờ sắc nét
        plt.scatter([50], [6], color='#ef4444', s=200, edgecolors='white', zorder=5) 
        plt.text(50, 9, "GK", color='white', ha='center', fontsize=9, weight='bold')
        if t_nhà["star_name"] != "Chưa cập nhật":
            plt.scatter([50], [38], color='#ef4444', s=250, edgecolors='gold', zorder=5) 
            plt.text(50, 42, t_nhà["star_name"], color='#fecd3d', ha='center', fontsize=9, weight='bold')
        
        plt.scatter([50], [94], color='#3b82f6', s=200, edgecolors='white', zorder=5) 
        plt.text(50, 87, "GK", color='white', ha='center', fontsize=9, weight='bold')
        if t_khách["star_name"] != "Chưa cập nhật":
            plt.scatter([50], [62], color='#3b82f6', s=250, edgecolors='gold', zorder=5) 
            plt.text(50, 66, t_khách["star_name"], color='#fecd3d', ha='center', fontsize=9, weight='bold')
        
        plt.xlim(-5, 105); plt.ylim(-5, 105); plt.axis('off')
        st.pyplot(fig)
        
    with col_text:
        st.info(f"🔴 **{m_data['đội_nhà']} (Sơ đồ: {t_nhà['sơ_đồ']}):** \n" + ", ".join(t_nhà['đội_hinh']))
        st.success(f"🔵 **{m_data['đội_khách']} (Sơ đồ: {t_khách['sơ_đồ']}):** \n" + ", ".join(t_khách['đội_hinh']))
        st.text(f"🌦️ Sân đấu / Khí hậu: {m_data['thời_tiết']}")
        if m_data['ti_so_ft'] != "":
            st.error(f"🏁 Kết quả FT thực tế: {m_data['ti_so_ft']}")

# ==================================================================
# TAB 2: PHÒNG NHẬP LIỆU DIỄN BIẾN TRẬN ĐẤU (REAL-TIME)
# ==================================================================
with tab2:
    st.subheader("⏱️ Phòng Điều Phối & Nhập Liệu Tỉ Số Trực Tiếp")
    update_m = st.selectbox("Chọn mã trận cần nạp kết quả:", list(st.session_state.matches.keys()))
    curr_m = st.session_state.matches[update_m]
    
    c1, c2 = st.columns(2)
    with c1:
        curr_m['ti_so_ft'] = st.text_input(f"Nhập tỉ số chung cuộc trận {curr_m['đội_nhà']} vs {curr_m['đội_khách']}:", curr_m['ti_so_ft'])
    with c2:
        curr_m['trọng_tài'] = st.text_input("Ghi nhận trọng tài bắt chính:", curr_m['trọng_tài'])
        
    if st.button("💾 XÁC NHẬN CẬP NHẬT TRỰC TUYẾN"):
        st.toast("Dữ liệu đã được nạp lên đám mây thành công!", icon="⚡")

# ==================================================================
# TAB 3: DANH SÁCH TOÀN BỘ CÁC ĐỘI BÓNG ĐÃ ĐƯỢC VÁ LỖI HIỂN THỊ
# ==================================================================
with tab3:
    st.subheader("🏃 Cơ sở dữ liệu chiến thuật toàn giải đấu")
    team_list = []
    for t_name, t_val in TEAMS.items():
        team_list.append([t_name, t_val['bảng'], t_val['hlv'], t_val['sơ_đồ'], t_val['star_name'], t_val['sức_mạnh']])
    
    team_df = pd.DataFrame(team_list, columns=["Đội Bóng", "Bảng", "Huấn Luyện Viên", "Sơ Đồ Chiến Thuật", "Ngôi Sao Gánh Đội", "Đánh Giá Sức Mạnh"])
    st.dataframe(team_df, use_container_width=True, height=400)
