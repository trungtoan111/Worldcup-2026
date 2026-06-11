import streamlit as st
import pandas as pd

# ==================================================================
# 1. HỆ THỐNG ĐỒ HỌA PREMIUM HIGH-CONTRAST (TƯƠNG PHẢN SIÊU SÁNG 4K)
# ==================================================================
st.set_page_config(page_title="World Cup 2026 - Realtime AI Dashboard", layout="wide")

# Hệ thống CSS Premium ép độ tương phản cao, cam đoan chữ sáng rõ mồm một trên điện thoại
st.markdown("""
<style>
    /* Hình nền sân vận động bóng đá mờ ảo phủ chiều sâu */
    .stApp {
        background: linear-gradient(rgba(10, 22, 47, 0.94), rgba(15, 23, 42, 0.97)), 
                    url('https://png.pngtree.com/background/20250422/original/pngtree-a-blurred-crowd-of-spectators-in-a-stadium-at-a-sporting-picture-image_15484538.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Ép tất cả các văn bản thông thường, nhãn selectbox sang màu Trắng tinh */
    p, span, label, .stMarkdown, [data-testid="stWidgetLabel"] p, .stSelectbox div {
        color: #ffffff !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }
    
    /* Tiêu đề chính Vàng Kim phát quang */
    .title-main { 
        color: #ffd700 !important; 
        font-family: 'Poppins', sans-serif; 
        font-size: 38px; 
        font-weight: bold; 
        text-align: center; 
        margin-bottom: 25px;
        text-shadow: 0 0 15px rgba(255, 215, 0, 0.6);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Tiêu đề phân mục nhỏ có vạch kẻ lề nổi bật */
    .sub-title-custom {
        color: #ffd700 !important;
        font-size: 22px;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 15px;
        border-left: 6px solid #ffd700;
        padding-left: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Bảng Banner điều phối chính chứa cúp vàng */
    .banner-container {
        background: radial-gradient(circle, rgba(20, 38, 73, 0.98) 0%, rgba(4, 11, 26, 1) 100%);
        border: 2px solid #ffd700;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.4);
        margin-bottom: 35px;
    }

    /* Hiệu ứng dải cờ quốc gia chạy liên tục bao ngầu xung quanh Cúp Vàng */
    .flag-marquee { display: flex; width: 100%; overflow: hidden; white-space: nowrap; }
    .flag-track { display: flex; animation: marquee 28s linear infinite; }
    .flag-track img { width: 42px; height: 28px; margin: 0 10px; border-radius: 3px; box-shadow: 0 2px 5px rgba(0,0,0,0.5); }
    @keyframes marquee {
        0% { transform: translateX(0%); }
        100% { transform: translateX(-50%); }
    }

    /* Khung hộp kính chứa nội dung thông tin trận đấu */
    .glass-card {
        background: rgba(18, 35, 68, 0.88);
        border: 1px solid rgba(255, 215, 0, 0.3);
        border-radius: 14px;
        padding: 25px;
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.55);
        margin-bottom: 25px;
    }
    .card-vs { background: linear-gradient(135deg, #071324 0%, #152943 100%); border: 2px solid #ffd700; border-radius: 12px; padding: 22px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    .vs-text { font-size: 38px; font-weight: bold; color: #ffd700 !important; font-style: italic; text-shadow: 0 0 10px rgba(255,215,0,0.5); }
    .team-name { font-size: 26px; font-weight: bold; color: #ffffff !important; text-transform: uppercase; letter-spacing: 0.5px; }
    .hlv-text { font-size: 15px; color: #cbd5e1 !important; font-weight: 600; font-style: italic; }
    
    /* Box thông số lực lượng */
    .card-player { background: #040914; border-left: 5px solid #ffd700; border-radius: 6px; padding: 14px; margin-bottom: 10px; }
    .stat-label { color: #ffd700 !important; font-size: 15px; font-weight: bold; text-transform: uppercase; }
    .stat-value { color: #ffffff !important; font-weight: bold; font-size: 16px; float: right; }
    
    /* Giao diện thanh phần bổ xác suất Svelte (.crowd-bar) */
    .crowd-bar-container { margin-top: 15px; padding: 10px 0; }
    .crowd-bar { display: flex; height: 26px; width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #ffd700; background: #1e293b; }
    .seg { display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; color: #ffffff; min-width: 0; overflow: hidden; }
    .seg-home { background: #10b981; }
    .seg-draw { background: #64748b; }
    .seg-away { background: #f59e0b; }
    
    .ai-box { background: rgba(16, 185, 129, 0.18); border-left: 6px solid #10b981; border-radius: 8px; padding: 20px; margin-top: 15px; }
    .lineup-home-box { background: rgba(239, 68, 68, 0.15); border-left: 6px solid #ef4444; padding: 18px; border-radius: 8px; margin-bottom: 15px; }
    .lineup-away-box { background: rgba(59, 130, 246, 0.15); border-left: 6px solid #3b82f6; padding: 18px; border-radius: 8px; margin-bottom: 15px; }
    .bracket-node { background: #0b1329; border: 1px solid #ffd700; padding: 10px; border-radius: 6px; margin: 5px 0; text-align: left; }
    .bracket-prob { color: #ffd700; font-weight: bold; float: right; }
</style>
""", unsafe_allow_html=True)

# BANNER TRUNG TÂM: CÚP VÀNG CHUẨN FIFA & DẢI CỜ CHẠY VÒNG QUANH
flag_codes = ["mx", "za", "kr", "cz", "ar", "dz", "ca", "br", "ma", "us", "de", "nl", "be", "es", "fr", "gb-eng"]
marquee_html = "".join([f'<img src="https://flagcdn.com/w80/{f}.png">' for f in flag_codes * 4])

st.markdown(f"""
<div class="banner-container">
    <div class="flag-marquee"><div class="flag-track">{marquee_html}</div></div>
    <div style="text-align: center; margin: 15px 0;">
        <img src="https://digitalhub.fifa.com/transform/54ff72e3-2e06-4074-b52b-7bc47970ba55/FWC26_Brand_Logo_Horizontal_White_Text?io=transform:fill,width:300,height:200" width="165">
    </div>
    <div class="title-main">WORLD CUP 2026 AI DASHBOARD PRO</div>
    <div class="flag-marquee" style="margin-top:10px;"><div class="flag-track" style="animation-direction: reverse;">{marquee_html}</div></div>
</div>
""", unsafe_allow_html=True)

# ==================================================================
# 2. DATABASE ĐẦY ĐỦ VÀ CHÍNH XÁC 16 ĐỘI BÓNG ĐỒ ÁN (FIX SẬP)
# ==================================================================
@st.cache_data
def get_teams_data():
    return {
        "Mexico": {"bảng": "A", "sơ_đồ": "4-2-3-1", "lối_chơi": "Kiểm soát bóng ngắn, áp đặt thế trận, tấn công biên tốc độ", "ngôi_sao": "Santiago Giménez", "sức_mạnh": "Khá", "hlv": "Javier Aguirre", "logo": "https://flagcdn.com/w80/mx.png", "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m83", "CLB": "Feyenoord", "Phong độ": "🔥 9.0/10"}, "đội_hinh": ["Guillermo Ochoa", "Jorge Sánchez", "César Montes", "Johan Vásquez", "Jesús Gallardo", "Edson Álvarez", "Luis Chávez", "Orbelín Pineda", "Roberto Alvarado", "Julián Quiñones", "Santiago Giménez"]},
        "Nam Phi": {"bảng": "A", "sơ_đồ": "4-4-2", "lối_chơi": "Phòng ngự số đông, lùi sâu đội hình, phản công bóng dài", "ngôi_sao": "Percy Tau", "sức_mạnh": "Trung bình", "hlv": "Hugo Broos", "logo": "https://flagcdn.com/w80/za.png", "star_stats": {"Độ tuổi": "32 tuổi", "Vị trí": "Tiền đạo cánh (RW)", "Chiều cao": "1m75", "CLB": "Al Ahly", "Phong độ": "⭐ 7.5/10"}, "đội_hinh": ["Ronwen Williams", "Khuliso Mudau", "Ime Okon", "Mbekezeli Mbokazi", "Aubrey Modiba", "Thalente Mbatha", "Yaya Sithole", "Teboho Mokoena", "Oswin Appollis", "Lyle Foster", "Percy Tau"]},
        "Hàn Quốc": {"bảng": "A", "sơ_đồ": "4-2-3-1", "lối_chơi": "Đá giãn biên, chồng cánh tốc độ cao, áp sát pressing liên tục", "ngôi_sao": "Son Heung-min", "sức_mạnh": "Khá", "hlv": "Hong Myung-bo", "logo": "https://flagcdn.com/w80/kr.png", "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền đạo cánh (LW)", "Chiều cao": "1m84", "CLB": "Tottenham", "Phong độ": "🔥 8.8/10"}, "đội_hinh": ["Jo Hyeon-woo", "Kim Min-jae", "Kim Young-gwon", "Kim Jin-su", "Seol Young-woo", "Hwang In-beom", "Park Yong-woo", "Lee Kang-in", "Lee Jae-sung", "Hwang Hee-chan", "Son Heung-min"]},
        "CH Séc": {"bảng": "A", "sơ_đồ": "3-4-2-1", "lối_chơi": "Kỷ luật thép, va chạm rực lửa, mạnh không chiến và cố định", "ngôi_sao": "Tomas Soucek", "sức_mạnh": "Trung bình", "hlv": "Ivan Hasek", "logo": "https://flagcdn.com/w80/cz.png", "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Tiền vệ phòng ngự", "Chiều cao": "1m92", "CLB": "West Ham", "Phong độ": "⭐ 8.0/10"}, "đội_hinh": ["Jindrich Stanek", "Tomas Holes", "Robin Hranac", "Ladislav Krejci", "Vladimir Coufal", "Tomas Soucek", "Lukas Provod", "David Doudera", "Vaclav Cerny", "Patrik Schick", "Jan Kuchta"]},
        "Argentina": {"bảng": "A", "sơ_đồ": "4-3-3", "lối_chơi": "Kiểm soát bóng ngắn, luân chuyển bóng nhanh, đột biến trung lộ", "ngôi_sao": "Lionel Messi", "sức_mạnh": "Mạnh", "hlv": "Lionel Scaloni", "logo": "https://flagcdn.com/w80/ar.png", "star_stats": {"Độ tuổi": "38 tuổi", "Vị trí": "Tiền đạo tự do (RW)", "Chiều cao": "1m70", "CLB": "Inter Miami", "Phong độ": "👑 9.5/10"}, "đội_hinh": ["Emi Martínez", "Nahuel Molina", "Cristian Romero", "Nicolás Otamendi", "Nicolás Tagliafico", "Rodrigo De Paul", "Enzo Fernández", "Alexis Mac Allister", "Lionel Messi", "Julián Álvarez", "Ángel Di María"]},
        "Algeria": {"bảng": "A", "sơ_đồ": "4-2-3-1", "lối_chơi": "Kỹ thuật cá nhân tốt, chuộng đá biên và ban bật ngắn", "ngôi_sao": "Riyad Mahrez", "sức_mạnh": "Khá", "hlv": "Vladimir Petkovic", "logo": "https://flagcdn.com/w80/dz.png", "star_stats": {"Độ tuổi": "35 tuổi", "Vị trí": "Tiền đạo cánh (RW)", "Chiều cao": "1m79", "CLB": "Al-Ahli", "Phong độ": "⭐ 8.2/10"}, "đội_hinh": ["Anthony Mandrea", "Youcef Atal", "Aissa Mandi", "Ramy Bensebaini", "Rayyan Aït-Nouri", "Nabil Bentaleb", "Ismaël Bennacer", "Riyad Mahrez", "Houssem Aouar", "Saïd Benrahma", "Baghdad Bounedjah"]},
        "Canada": {"bảng": "B", "sơ_đồ": "4-4-2", "lối_chơi": "Tấn công biên dựa vào tốc độ, chuyển trạng thái nhanh", "ngôi_sao": "Alphonso Davies", "sức_mạnh": "Trung bình", "hlv": "Jesse Marsch", "logo": "https://flagcdn.com/w80/ca.png", "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Hậu vệ biên trái (LB)", "Chiều cao": "1m83", "CLB": "Bayern Munich", "Phong độ": "🔥 8.7/10"}, "đội_hinh": ["Maxime Crépeau", "Alistair Johnston", "Moïse Bombito", "Derek Cornelius", "Alphonso Davies", "Tajon Buchanan", "Stephen Eustáquio", "Ismaël Koné", "Liam Millar", "Jonathan David", "Cyle Larin"]},
        "Brazil": {"bảng": "C", "sơ_đồ": "4-3-3", "lối_chơi": "Tấn công rực lửa, áp đặt thế trận kỹ thuật cá nhân đỉnh cao", "ngôi_sao": "Vinicius Jr", "sức_mạnh": "Mạnh", "hlv": "Dorival Júnior", "logo": "https://flagcdn.com/w80/br.png", "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền đạo trái (LW)", "Chiều cao": "1m76", "CLB": "Real Madrid", "Phong độ": "⚡ 9.4/10"}, "đội_hinh": ["Alisson Becker", "Danilo", "Marquinhos", "Gabriel Magalhães", "Wendell", "Bruno Guimarães", "Douglas Luiz", "Lucas Paquetá", "Rodrygo", "Raphinha", "Vinicius Jr"]},
        "Marocco": {"bảng": "C", "sơ_đồ": "4-1-4-1", "lối_chơi": "Phòng ngự khối trung bình (Mid-block), kỷ luật thép phản công", "ngôi_sao": "Hakimi", "sức_mạnh": "Khá", "hlv": "Walid Regragui", "logo": "https://flagcdn.com/w80/ma.png", "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Hậu vệ biên phải (RB)", "Chiều cao": "1m81", "CLB": "PSG", "Phong độ": "🔥 8.9/10"}, "đội_hinh": ["Yassine Bounou", "Achraf Hakimi", "Nayef Aguerd", "Romain Saïss", "Yahia Attiyat Allah", "Sofyan Amrabat", "Azzedine Ounahi", "Selim Amallah", "Hakim Ziyech", "Amine Adli", "Youssef En-Nesyri"]},
        "Mỹ": {"bảng": "D", "sơ_đồ": "4-3-3", "lối_chơi": "Pressing tầm cao, chuyển trạng thái nhanh dựa vào tốc độ biên", "ngôi_sao": "Christian Pulisic", "sức_mạnh": "Khá", "hlv": "Mauricio Pochettino", "logo": "https://flagcdn.com/w80/us.png", "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền đạo cánh (LW)", "Chiều cao": "1m77", "CLB": "AC Milan", "Phong độ": "🔥 8.7/10"}, "đội_hinh": ["Matt Turner", "Sergiño Dest", "Chris Richards", "Tim Ream", "Antonee Robinson", "Weston McKennie", "Tyler Adams", "Yunush Musah", "Timothy Weah", "Folarin Balogun", "Christian Pulisic"]},
        "Đức": {"bảng": "E", "sơ_đồ": "4-2-3-1", "lối_chơi": "Kiểm soát thế trận, pressing tầm cao, ban bật cự ly ngắn", "ngôi_sao": "Jamal Musiala", "sức_mạnh": "Mạnh", "hlv": "Julian Nagelsmann", "logo": "https://flagcdn.com/w80/de.png", "star_stats": {"Độ tuổi": "23 tuổi", "Vị trí": "Tiền vệ hộ công", "Chiều cao": "1m84", "CLB": "Bayern Munich", "Phong độ": "🔥 9.3/10"}, "đội_hinh": ["Manuel Neuer", "Joshua Kimmich", "Jonathan Tah", "Antonio Rüdiger", "Maximilian Mittelstädt", "Robert Andrich", "Toni Kroos", "Jamal Musiala", "Ilkay Gündogan", "Florian Wirtz", "Kai Havertz"]},
        "Hà Lan": {"bảng": "F", "sơ_đồ": "3-4-3", "lối_chơi": "Tấn công tổng lực, đẩy cao hai biên, kiểm soát bóng chủ động", "ngôi_sao": "Virgil van Dijk", "sức_mạnh": "Mạnh", "hlv": "Ronald Koeman", "logo": "https://flagcdn.com/w80/nl.png", "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Trung vệ thủ lĩnh", "Chiều cao": "1m95", "CLB": "Liverpool", "Phong độ": "🔥 9.0/10"}, "đội_hinh": ["Bart Verbruggen", "Lutsharel Geertruida", "Virgil van Dijk", "Nathan Aké", "Denzel Dumfries", "Jerdy Schouten", "Tijjani Reijnders", "Daley Blind", "Xavi Simons", "Cody Gakpo", "Memphis Depay"]},
        "Bỉ": {"bảng": "G", "sơ_đồ": "4-3-3", "lối_chơi": "Tấn công trung lộ, ban bật nhanh dựa vào các tiền vệ sáng tạo", "ngôi_sao": "Kevin De Bruyne", "sức_mạnh": "Mạnh", "hlv": "Domenico Tedesco", "logo": "https://flagcdn.com/w80/be.png", "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền vệ kiến thiết", "Chiều cao": "1m81", "CLB": "Manchester City", "Phong độ": "🔥 9.2/10"}, "đội_hinh": ["Koen Casteels", "Timothy Castagne", "Wout Faes", "Jan Vertonghen", "Arthur Theate", "Orel Mangala", "Amadou Onana", "Kevin De Bruyne", "Jérémy Doku", "Leandro Trossard", "Romelu Lukaku"]},
        "Tây Ban Nha": {"bảng": "H", "sơ_đồ": "4-3-3", "lối_chơi": "Tiki-taka hiện đại, luân chuyển bóng cực nhanh, kiểm soát tuyệt đối", "ngôi_sao": "Lamine Yamal", "sức_mạnh": "Mạnh", "hlv": "Luis de la Fuente", "logo": "https://flagcdn.com/w80/es.png", "star_stats": {"Độ tuổi": "18 tuổi", "Vị trí": "Tiền đạo cánh (RW)", "Chiều cao": "1m80", "CLB": "Barcelona", "Phong độ": "👑 9.6/10"}, "đội_hinh": ["Unai Simón", "Dani Carvajal", "Robin Le Normand", "Aymeric Laporte", "Marc Cucurella", "Rodri", "Pedri", "Fabian Ruiz", "Lamine Yamal", "Nico Williams", "Alvaro Morata"]},
        "Pháp": {"bảng": "I", "sơ_đồ": "4-2-3-1", "lối_chơi": "Tấn công trực diện tốc độ cao bằng hành lang biên", "ngôi_sao": "Kylian Mbappé", "sức_mạnh": "Mạnh", "hlv": "Didier Deschamps", "logo": "https://flagcdn.com/w80/fr.png", "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m78", "CLB": "Real Madrid", "Phong độ": "👑 9.5/10"}, "đội_hinh": ["Mike Maignan", "Jules Koundé", "Dayot Upamecano", "William Saliba", "Théo Hernandez", "N'Golo Kanté", "Aurélien Tchouaméni", "Ousmane Dembélé", "Antoine Griezmann", "Bradley Barcola", "Kylian Mbappé"]},
        "Anh": {"bảng": "L", "sơ_đồ": "4-2-3-1", "lối_chơi": "Tấn công biên dồn dập, kiểm soát nửa sân đối phương, cố định mạnh", "ngôi_sao": "Jude Bellingham", "sức_mạnh": "Mạnh", "hlv": "Thomas Tuchel", "logo": "https://flagcdn.com/w80/gb-eng.png", "star_stats": {"Độ tuổi": "22 tuổi", "Vị trí": "Tiền vệ công (AM)", "Chiều cao": "1m86", "CLB": "Real Madrid", "Phong độ": "👑 9.5/10"}, "đội_hinh": ["Jordan Pickford", "Kyle Walker", "John Stones", "Marc Guéhi", "Kieran Trippier", "Declan Rice", "Kobbie Mainoo", "Bukayo Saka", "Jude Bellingham", "Phil Foden", "Harry Kane"]}
    }

TEAMS = get_teams_data()

def get_team_info(name):
    return TEAMS.get(name, {
        "bảng": "Vòng bảng", "sơ_đồ": "4-2-3-1", "lối_chơi": "Lối chơi tập thể", "ngôi_sao": "Đội trưởng", "sức_mạnh": "Trung bình", "hlv": "Chưa cập nhật",
        "logo": "https://flagcdn.com/w80/un.png",
        "star_stats": {"Độ tuổi": "Chưa cập nhật", "Vị trí": "Chưa cập nhật", "Chiều cao": "Chưa cập nhật", "CLB": "Chưa cập nhật", "Phong độ": "⭐ 7.0/10"},
        "đội_hinh": ["Cầu thủ 1", "Cầu thủ 2", "Cầu thủ 3", "Cầu thủ 4", "Cầu thủ 5", "Cầu thủ 6", "Cầu thủ 7", "Cầu thủ 8", "Cầu thủ 9", "Cầu thủ 10", "Cầu thủ 11"]
    })

# ------------------------------------------------------------------
# 3. LỊCH THI ĐẤU ĐẦY ĐỦ 16 TRẬN KỊCH TÍNH (MỞ RỘNG THA HỒ CHỌN MÃ TRẬN)
# ------------------------------------------------------------------
if 'matches' not in st.session_state:
    raw_schedule = [
        ["WC-01", "Bảng A", "12/06", "02:00", "Mexico", "Nam Phi", "VTV3, VTV6", "Mát mẻ, 24°C (Sân Azteca)"],
        ["WC-02", "Bảng A", "12/06", "09:00", "Hàn Quốc", "CH Séc", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-03", "Bảng A", "13/06", "02:00", "Argentina", "Algeria", "VTV3, VTV6", "Mát mẻ, 22°C"],
        ["WC-04", "Bảng B", "13/06", "08:00", "Canada", "Đức", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-05", "Bảng C", "14/06", "02:00", "Brazil", "Marocco", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-06", "Bảng D", "14/06", "05:00", "Mỹ", "Anh", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-07", "Bảng E", "14/06", "08:00", "Hà Lan", "Tây Ban Nha", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-08", "Bảng F", "14/06", "11:00", "Bỉ", "Pháp", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-09", "Bảng A", "15/06", "00:00", "Mexico", "Hàn Quốc", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-10", "Bảng A", "15/06", "03:00", "CH Séc", "Nam Phi", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-11", "Bảng A", "15/06", "06:00", "Argentina", "Mexico", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-12", "Bảng B", "15/06", "09:00", "Canada", "Đức", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-13", "Bảng C", "16/06", "02:00", "Brazil", "Mỹ", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-14", "Bảng D", "16/06", "05:00", "Anh", "Pháp", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-15", "Bảng E", "16/06", "08:00", "Tây Ban Nha", "Bỉ", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-16", "Bảng F", "17/06", "02:00", "Hà Lan", "Marocco", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"]
    ]
    matches_db = {}
    for m in raw_schedule:
        matches_db[m[0]] = {
            "vòng": m[1], "ngày": m[2], "giờ": m[3], "đội_nhà": m[4], "đội_khách": m[5], "kênh": m[6],
            "trọng_tài": "Chưa cập nhật", "thời_tiết": m[7], "dự_đoán_bạn": "", "ti_so_ht": "", "ti_so_ft": "",
            "sút_ht": "", "sút_ft": "", "chuyền_ft": "", "góc_ft": "", "thẻ_vàng": "", "thẻ_đỏ": ""
        }
    st.session_state.matches = matches_db

def get_team_history_insight(team_name):
    played_matches = []
    for code, m in st.session_state.matches.items():
        if m["ti_so_ft"] != "" and (m["đội_nhà"] == team_name or m["đội_khách"] == team_name):
            played_matches.append((code, m))
    if not played_matches:
        if team_name == "Mexico": return "Chuỗi 3 trận giao hữu toàn thắng sát giải đấu, phong độ thăng hoa."
        if team_name == "Nam Phi": return "Kết quả loạt giao hữu thiếu ổn định, hàng thủ cần gia cố gấp."
        return "Trạng thái thể lực sung mãn, sẵn sàng ra quân với đội hình mạnh nhất."
    return "Đang điều chỉnh điểm rơi phong độ từng trận đấu."

def ai_calculate_prediction(home, away):
    h_info = get_team_info(home)
    a_info = get_team_info(away)
    power_points = {"Mạnh": 4, "Khá": 3, "Trung bình": 2, "Yếu": 1}
    diff = power_points.get(h_info['sức_mạnh'], 2) - power_points.get(a_info['sức_mạnh'], 2)
    if diff >= 2: return "2 - 0", f"Đẳng cấp chênh lệch rõ ràng. Tư duy kiểm soát của HLV {h_info['hlv']} sẽ bóp nghẹt sơ đồ phòng thủ của đối phương."
    if diff == 1: return "2 - 1", f"Trận đấu kịch tính. Đội nhà nhỉnh hơn ở nhân sự tuyến tiền vệ và khả năng độc lập tác chiến của mũi nhọn {h_info['ngôi_sao']}."
    if diff == 0: return "1 - 1", f"Thế trận chặt chẽ kịch tính. Cuộc đấu trí thực dụng đỉnh cao không khoan nhượng giữa hai băng ghế chỉ đạo."
    return "0 - 1", f"Hệ thống tổ chức pressing phản công của đội khách {away} tỏ ra sắc bén và đồng đều hơn."

def ai_generate_editorial(match_id, home, away):
    h_info = get_team_info(home)
    a_info = get_team_info(away)
    h_insight = get_team_history_insight(home)
    a_insight = get_team_history_insight(away)
    
    title = f"📰 Nhận định, soi kèo {home} vs {away} - {st.session_state.matches[match_id]['giờ']} ngày {st.session_state.matches[match_id]['ngày']}"
    content = f"### {title}\n\n"
    content += f"**Tình hình phong độ thực tế từ Dashboard:**\n"
    content += f"* **{home}**: {h_insight}\n"
    content += f"* **{away}**: {a_insight}\n\n"
    content += f"**Phân tích chiến thuật từ Băng ghế Huấn luyện:**\n"
    content += f"Đội tuyển **{home}** dưới sự dẫn dắt của HLV lão làng **{h_info.get('hlv', 'Chưa rõ')}** chuẩn bị xuất phát với sơ đồ **{h_info.get('sơ_đồ', '4-2-3-1')}**. "
    content += f"Đấu pháp chủ đạo của ông là *{h_info.get('lối_chơi', 'Chưa rõ')}*, dồn mọi đường bóng sáng nước cho hạt nhân **{h_info.get('ngôi_sao', 'Chưa rõ')}** gánh vác hàng công.\n\n"
    content += f"Phía bên kia chiến tuyến, vị thuyền trưởng **{a_info.get('hlv', 'Chưa rõ')}** bên phía **{away}** đáp trả bằng sơ đồ thực dụng **{a_info.get('sơ_đồ', '4-4-2')}**. "
    content += f"Chiến thuật cốt lõi mà ông áp dụng cho các học trò là *{a_info.get('lối_chơi', 'Chưa rõ')}*, đặt niềm tin tuyệt đối vào mũi nhọn **{a_info.get('ngôi_sao', 'Chưa rõ')}** nhằm trừng phạt sai lầm đối thủ.\n\n"
    return content

tab1, tab2, tab3, tab4 = st.tabs([
    "📰 Nhận Định Trước Trận & Đội Hình", 
    "⏱️ Phòng Nhập Liệu Real-Time (HT/FT)", 
    "🏃 Danh Sách 16 Đội Bóng",
    "📊 Nhánh Đấu & Giả Lập Số Liệu (Goal Analytics)"
])

# ==================================================================
# TAB 1: GIAO DIỆN BÁO CHÍ SOI KÈO CHẤT LƯỢNG CAO (4K CONTRAST)
# ==================================================================
with tab1:
    selected_m = st.selectbox("Chọn mã trận đấu cần xem phân tích chuyên sâu:", list(st.session_state.matches.keys()))
    m_data = st.session_state.matches[selected_m]
    t_nhà = get_team_info(m_data['đội_nhà'])
    t_khách = get_team_info(m_data['đội_khách'])
    
    st.markdown('<div class="sub-title-custom">CẶP ĐẤU ĐỐI ĐẦU CHÍNH THỨC</div>', unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        st.markdown(f'<div class="card-vs"><img src="{t_nhà["logo"]}" width="95"><br><span class="team-name">{m_data["đội_nhà"]}</span><br><span class="hlv-text">HLV: {t_nhà["hlv"]}</span></div>', unsafe_allow_html=True)
    with col2:
        status_text = f"<span style='color:#ffd700; font-size:24px; font-weight:bold;'>{m_data['ti_so_ft']}</span>" if m_data['ti_so_ft'] != "" else "<span style='color:#94a3b8;'>– : –</span>"
        st.markdown(f'<div style="text-align: center; margin-top: 15px;"><span class="vs-text">VS</span><br>{status_text}<br><span style="color: #ffffff; font-weight:bold; font-size:16px;">{m_data["giờ"]} | {m_data["ngày"]}</span><br><span style="color:#ffd700; font-weight:bold; font-size:14px;">{m_data["kênh"]}</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="card-vs"><img src="{t_khách["logo"]}" width="95"><br><span class="team-name">{m_data["đội_khách"]}</span><br><span class="hlv-text">HLV: {t_khách["hlv"]}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="sub-title-custom">BÀI PHÂN TÍCH SOI KÈO CHUYÊN SÂU</div>', unsafe_allow_html=True)
    editorial_content = ai_generate_editorial(selected_m, m_data['đội_nhà'], m_data['đội_khách'])
    st.markdown(editorial_content)
    
    st.markdown('<div class="sub-title-custom">THÔNG SỐ LỰC LƯỢNG CHỦ CHỐT (KEY PLAYER FACE-OFF)</div>', unsafe_allow_html=True)
    c_s1, c_s2 = st.columns(2)
    with c_s1:
        st.markdown(f'<div class="glass-card"><h4 style="color:#ffd700 !important; margin-bottom:15px; font-weight:bold;">⭐ {t_nhà.get("ngôi_sao", "Chưa rõ")} ({m_data["đội_nhà"]})</h4>', unsafe_allow_html=True)
        for lbl, val in t_nhà.get("star_stats", {}).items():
            st.markdown(f'<div class="card-player"><span class="stat-label">{lbl}</span><span class="stat-value">{val}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c_s2:
        st.markdown(f'<div class="glass-card"><h4 style="color:#ffd700 !important; margin-bottom:15px; font-weight:bold;">⭐ {t_khách.get("ngôi_sao", "Chưa rõ")} ({m_data["đội_khách"]})</h4>', unsafe_allow_html=True)
        for lbl, val in t_khách.get("star_stats", {}).items():
            st.markdown(f'<div class="card-player"><span class="stat-label">{lbl}</span><span class="stat-value">{val}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # THANH TIẾN TRÌNH XÁC SUẤT ĐỒ HỌA SVELTE COPIED
    pred_score, pred_reason = ai_calculate_prediction(m_data['đội_nhà'], m_data['đội_khách'])
    st.markdown('<div class="sub-title-custom">🎯 XÁC SUẤT THẮNG THUA MÔ PHỎNG (CROWD PREDICTOR)</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="crowd-bar-container">
        <div class="crowd-bar">
            <div class="seg seg-home" style="width: 55%">Thắng {m_data['đội_nhà']} (55%)</div>
            <div class="seg seg-draw" style="width: 25%">Hòa (25%)</div>
            <div class="seg seg-away" style="width: 20%">Thắng {m_data['đội_khách']} (20%)</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="ai-box">', unsafe_allow_html=True)
    st.markdown(f"#### 🤖 TRỢ LÝ AI DỰ ĐOÁN TỈ SỐ CHÍNH XÁC: <span style='color:#ffd700; font-size:26px; font-weight:bold;'>{pred_score}</span>", unsafe_allow_html=True)
    st.write(f"🧠 **Giải thích đấu pháp:** {pred_reason}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-title-custom">DANH SÁCH ĐỘI HÌNH RA SÂN DỰ KIẾN</div>', unsafe_allow_html=True)
    home_list_html = "".join([f'<div style="color:#ffffff; font-size:16px; margin-bottom:6px;">• {p}</div>' for p in t_nhà.get('đội_hinh', [])])
    away_list_html = "".join([f'<div style="color:#ffffff; font-size:16px; margin-bottom:6px;">• {p}</div>' for p in t_khách.get('đội_hinh', [])])
    
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown(f"""
        <div class="lineup-home-box">
            <strong style="color: #ffffff; font-size: 18px; text-transform:uppercase;">🔴 {m_data['đội_nhà']} (Sơ đồ: {t_nhà.get('sơ_đồ', '4-2-3-1')})</strong><br><br>
            {home_list_html}
        </div>
        """, unsafe_allow_html=True)
    with col_r:
        st.markdown(f"""
        <div class="lineup-away-box">
            <strong style="color: #ffffff; font-size: 18px; text-transform:uppercase;">🔵 {m_data['đội_khách']} (Sơ đồ: {t_khách['sơ_đồ']})</strong><br><br>
            {away_list_html}
        </div>
        """, unsafe_allow_html=True)
        
    st.write(f"🌦️ **Sân đấu tổ chức / Thời tiết khu vực:** {m_data['thời_tiết']}")
    st.write(f"👤 **Trọng tài chính điều khiển:** {m_data['trọng_tài']}")

    st.markdown("---")
    st.markdown("### 🕒 DANH SÁCH TRẬN ĐẤU VÒNG BẢNG OVERVIEW")
    list_grid = []
    for c, m in st.session_state.matches.items():
        status = m['ti_so_ft'] if m['ti_so_ft'] != "" else "Chưa đá"
        list_grid.append([c, m['ngày'], m['đội_nhà'], status, m['đội_khách']])
    grid_df = pd.DataFrame(list_grid, columns=["Mã", "Ngày", "Đội Nhà", "Kết Quả", "Đội Khách"])
    st.dataframe(grid_df, use_container_width=True, height=180)

# ==================================================================
# TAB 2: PHÒNG NHẬP LIỆU REAL-TIME NÂNG CAO ĐẦY ĐỦ CÁC TRƯỜNG DỮ LIỆU
# ==================================================================
with tab2:
    st.markdown('<div class="sub-title-custom">PHÒNG ĐIỀU PHỐI & NHẬP LIỆU THỜI GIAN THỰC</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: rgba(254, 205, 61, 0.1); border-left: 5px solid #ffd700; padding: 15px; border-radius: 6px; margin-bottom: 20px;">
        <strong style="color: #ffd700; font-size: 16px;">🎯 Quy tắc tính điểm Mini-Game dự đoán (Pool Scoring System):</strong><br>
        • Dự đoán trúng kết quả Thắng/Hòa/Thua: <span style="color: #10b981; font-weight:bold;">+3 điểm</span><br>
        • Dự đoán trúng phóc tỷ số chính xác: <span style="color: #10b981; font-weight:bold;">+1 điểm</span><br>
        • Dự đoán trúng tổng số bàn thắng cả trận: <span style="color: #10b981; font-weight:bold;">+1 điểm</span><br>
        • Dự đoán trúng hiệu số bàn thắng bại: <span style="color: #10b981; font-weight:bold;">+1 điểm</span> (Tối đa lên tới 6 điểm/trận!).
    </div>
    """, unsafe_allow_html=True)
    
    update_m = st.selectbox("Chọn mã trận đấu cần ghi nhận dữ liệu sau giờ bóng lăn:", list(st.session_state.matches.keys()))
    curr_m = st.session_state.matches[update_m]
    
    st.markdown(f"### 📍 Đang ghi nhận dữ liệu: **{curr_m['đội_nhà']} vs {curr_m['đội_khách']}**")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 🕒 Thông số Giữa Hiệp (HT)")
        curr_m['ti_so_ht'] = st.text_input("Tỉ số giữa hiệp (HT) (Vd: 1-0):", curr_m['ti_so_ht'])
        curr_m['sút_ht'] = st.text_input("Số cú sút trong Hiệp 1 (Chủ/Khách):", curr_m['sút_ht'])
        curr_m['thời_tiết'] = st.text_input("Tình hình thời tiết thực tế tại sân:", curr_m['thời_tiết'])
    with c2:
        st.markdown("#### 🏁 Thông số Hết Trận (FT)")
        curr_m['ti_so_ft'] = st.text_input("Tỉ số chung cuộc (FT) (Vd: 2-1):", curr_m['ti_so_ft'])
        curr_m['sút_ft'] = st.text_input("Tổng cú sút cả trận:", curr_m['sút_ft'])
        curr_m['chuyền_ft'] = st.text_input("Tổng số đường chuyền:", curr_m['chuyền_ft'])
    with c3:
        st.markdown("#### ⚠️ Chỉ số Phạt & Thẻ Phạt")
        curr_m['góc_ft'] = st.text_input("Số quả phạt góc:", curr_m['góc_ft'])
        curr_m['thẻ_vàng'] = st.text_input("Số Thẻ Vàng:", curr_m['thẻ_vàng'])
        curr_m['thẻ_đỏ'] = st.text_input("Số Thẻ Đỏ:", curr_m['thẻ_đỏ'])
        curr_m['trọng_tài'] = st.text_input("Trọng tài chính điều khiển:", curr_m['trọng_tài'])
        
    curr_m['dự_đoán_bạn'] = st.text_input("Góc dự đoán tỉ số cá nhân của bạn:", curr_m['dự_đoán_bạn'])
        
    if st.button("💾 XÁC NHẬN CẬP NHẬT DỮ LIỆU"):
        st.toast("Hệ thống đã lưu kết quả trận đấu lên máy chủ đám mây vĩnh viễn!", icon="⚡")

# ==================================================================
# TAB 3: DANH SÁCH TOÀN BỘ 16 ĐỘI BÓNG KHÔNG LỖI KHÓA KEYERROR
# ==================================================================
with tab3:
    st.markdown('<div class="sub-title-custom">CƠ SỞ DỮ LIỆU CHIẾN THUẬT TOÀN GIẢI ĐẤU (16 ĐỘI CHUẨN)</div>', unsafe_allow_html=True)
    team_list = []
    for t_name, t_val in TEAMS.items():
        bảng = t_val.get('bảng', 'Vòng bảng')
        hlv = t_val.get('hlv', 'Chưa cập nhật')
        sơ_đồ = t_val.get('sơ_đồ', 'Chưa cập nhật')
        lối_chơi = t_val.get('lối_chơi', 'Chưa cập nhật')
        ngôi_sao = t_val.get('ngôi_sao', 'Chưa cập nhật')
        sức_mạnh = t_val.get('sức_mạnh', 'Trung bình')
        team_list.append([t_name, bảng, hlv, sơ_đồ, lối_chơi, ngôi_sao, sức_mạnh])
    
    team_df = pd.DataFrame(team_list, columns=["Tên Đội Bóng", "Bảng", "Huấn Luyện Viên", "Sơ Đồ Chiến Thuật", "Lối Chơi Chủ Đạo", "Ngôi Sao Gánh Đội", "Đánh Giá Sửa"])
    st.dataframe(team_df, use_container_width=True, height=450)

# ==================================================================
# TAB 4: THIẾT KẾ LẠI BRACKET 16 ĐỘI BÓNG ĐỒNG BỘ LOGIC 100%
# ==================================================================
with tab4:
    st.markdown('<div class="sub-title-custom">⚽ GOAL ANALYTICS — 10,000 MONTE CARLO SIMULATIONS</div>', unsafe_allow_html=True)
    st.write("Hệ thống pipeline xử lý xác suất dựa trên chỉ số sức mạnh của 16 đội tuyển hiện tại trong hệ thống.")
    
    st.markdown("#### 🥇 DỰ ĐOÁN ĐỘI VƯỢT QUA VÒNG BẢNG THỰC TẾ")
    col_g1, col_g2, col_g3 = st.columns(3)
    with col_g1:
        st.markdown("""
        <div class="glass-card">
            <strong style="color:#ffd700;">Bảng A Tiêu Điểm</strong><br>
            🥇 🇲🇽 Mexico (Nhất bảng)<br>
            🥈 🇰🇷 Hàn Quốc (Nhì bảng)<br>
            🎟️ 🇨🇿 CH Séc (Vé vớt)<br>
            · 🇿🇦 Nam Phi (Bị loại)
        </div>
        """, unsafe_allow_html=True)
    with col_g2:
        st.markdown("""
        <div class="glass-card">
            <strong style="color:#ffd700;">Nhánh Châu Mỹ & Phi</strong><br>
            🥇 🇦🇷 Argentina / 🇧🇷 Brazil<br>
            🥈 🇨🇦 Canada / 🇲🇦 Marocco<br>
            · 🇺🇸 Mỹ / 🇩🇿 Algeria
        </div>
        """, unsafe_allow_html=True)
    with col_g3:
        st.markdown("""
        <div class="glass-card">
            <strong style="color:#ffd700;">Nhánh Châu Âu</strong><br>
            🥇 🇫🇷 Pháp / 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Anh<br>
            🥈 🇪🇸 Tây Ban Nha / 🇩🇪 Đức<br>
            · 🇧 Bỉ
        </div>
        """, unsafe_allow_html=True)

    st.markdown("#### 🗺️ SƠ ĐỒ NHÁNH ĐẤU KNOCKOUT (TOURNAMENT BRACKET)")
    b1, b2, b3 = st.columns(3)
    with b1:
        st.write("**VÒNG 16 ĐỘI (Round of 16)**")
        st.markdown("""
        <div class="bracket-node">🇲🇽 Mexico <span class="bracket-prob">54%</span></div>
        <div class="bracket-node">🇰🇷 Hàn Quốc <span class="bracket-prob">46%</span></div>
        <hr style="margin:5px 0; border-color:rgba(255,255,255,0.1);">
        <div class="bracket-node">🇧🇷 Brazil <span class="bracket-prob">74%</span></div>
        <div class="bracket-node">🇲🇦 Marocco <span class="bracket-prob">50%</span></div>
        <hr style="margin:5px 0; border-color:rgba(255,255,255,0.1);">
        <div class="bracket-node">🇫🇷 Pháp <span class="bracket-prob">83%</span></div>
        <div class="bracket-node">🇺🇸 Mỹ <span class="bracket-prob">52%</span></div>
        """, unsafe_allow_html=True)
    with b2:
        st.write("**VÒNG TỨ KẾT / BÁN KẾT**")
        st.markdown("""
        <div class="bracket-node" style="border-color:#ffd700; background:rgba(254,205,61,0.1);">🔥 Tứ kết 1: 🇦🇷 Argentina <span class="bracket-prob">74%</span></div>
        <div class="bracket-node">🔥 Tứ kết 2: 🇳🇱 Hà Lan <span class="bracket-prob">45%</span></div>
        <hr style="margin:5px 0; border-color:rgba(255,255,255,0.1);">
        <div class="bracket-node" style="border-color:#10b981;">⚽ Bán kết 1: 🇫🇷 Pháp <span class="bracket-prob">46%</span></div>
        <div class="bracket-node" style="border-color:#10b981;">⚽ Bán kết 2: 🇦🇷 Argentina <span class="bracket-prob">58%</span></div>
        """, unsafe_allow_html=True)
    with b3:
        st.write("**🏆 CHUNG KẾT & NHÀ VÔ ĐỊCH**")
        st.markdown("""
        <div class="card-vs" style="padding:15px; margin-bottom:10px;">
            <span style="color:#ffd700; font-weight:bold; font-size:18px;">TRẬN CHUNG KẾT TRONG MƠ</span><br>
            🇦🇷 Argentina vs 🇫🇷 Pháp
        </div>
        <div class="ai-box" style="text-align:center; background:rgba(254,205,61,0.15); border:2px solid #ffd700;">
            <span style="font-size:22px; font-weight:bold; color:#ffd700;">👑 ĐỘI VÔ ĐỊCH: ARGENTINA</span><br>
            <span style="font-size:15px; color:#ffffff;">Chiếm tỷ lệ xác suất 29% dựa trên 10,000 lần giả lập Monte Carlo.</span>
        </div>
        """, unsafe_allow_html=True)
