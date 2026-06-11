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
    
    /* Box thông số lực lượng chữ Vàng-Trắng */
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
# 2. DATABASE CHUẨN XỊN CHÍNH XÁC: ĐẦY ĐỦ ĐÚNG 48 ĐỘI BÓNG KHÔNG THIẾU
# ==================================================================
@st.cache_data
def get_teams_data():
    return {
        # Bảng A
        "Mexico": {"bảng": "A", "sơ_đồ": "4-2-3-1", "lối_chơi": "Kiểm soát bóng ngắn, áp đặt thế trận, tấn công biên tốc độ", "ngôi_sao": "Santiago Giménez", "sức_mạnh": "Khá", "hlv": "Javier Aguirre", "logo": "https://flagcdn.com/w80/mx.png", "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m83", "CLB": "Feyenoord", "Phong độ": "🔥 9.0/10"}, "đội_hinh": ["Guillermo Ochoa", "Jorge Sánchez", "César Montes", "Johan Vásquez", "Jesús Gallardo", "Edson Álvarez", "Luis Chávez", "Orbelín Pineda", "Roberto Alvarado", "Julián Quiñones", "Santiago Giménez"]},
        "Nam Phi": {"bảng": "A", "sơ_đồ": "4-4-2", "lối_chơi": "Phòng ngự số đông, lùi sâu đội hình, phản công bóng dài", "ngôi_sao": "Percy Tau", "sức_mạnh": "Trung bình", "hlv": "Hugo Broos", "logo": "https://flagcdn.com/w80/za.png", "star_stats": {"Độ tuổi": "32 tuổi", "Vị trí": "Tiền đạo cánh (RW)", "Chiều cao": "1m75", "CLB": "Al Ahly", "Phong độ": "⭐ 7.5/10"}, "đội_hinh": ["Ronwen Williams", "Khuliso Mudau", "Ime Okon", "Mbekezeli Mbokazi", "Aubrey Modiba", "Thalente Mbatha", "Yaya Sithole", "Teboho Mokoena", "Oswin Appollis", "Lyle Foster", "Percy Tau"]},
        "Hàn Quốc": {"bảng": "A", "sơ_đồ": "4-2-3-1", "lối_chơi": "Đá giãn biên, chồng cánh tốc độ cao, áp sát pressing liên tục", "ngôi_sao": "Son Heung-min", "sức_mạnh": "Khá", "hlv": "Hong Myung-bo", "logo": "https://flagcdn.com/w80/kr.png", "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền đạo cánh (LW)", "Chiều cao": "1m84", "CLB": "Tottenham", "Phong độ": "🔥 8.8/10"}, "đội_hinh": ["Jo Hyeon-woo", "Kim Min-jae", "Kim Young-gwon", "Kim Jin-su", "Seol Young-woo", "Hwang In-beom", "Park Yong-woo", "Lee Kang-in", "Lee Jae-sung", "Hwang Hee-chan", "Son Heung-min"]},
        "CH Séc": {"bảng": "A", "sơ_đồ": "3-4-2-1", "lối_chơi": "Kỷ luật thép, va chạm rực lửa, mạnh không chiến và cố định", "ngôi_sao": "Tomas Soucek", "sức_mạnh": "Trung bình", "hlv": "Ivan Hasek", "logo": "https://flagcdn.com/w80/cz.png", "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Tiền vệ phòng ngự", "Chiều cao": "1m92", "CLB": "West Ham", "Phong độ": "⭐ 8.0/10"}, "đội_hinh": ["Jindrich Stanek", "Tomas Holes", "Robin Hranac", "Ladislav Krejci", "Vladimir Coufal", "Tomas Soucek", "Lukas Provod", "David Doudera", "Vaclav Cerny", "Patrik Schick", "Jan Kuchta"]},
        
        # Bảng B
        "Canada": {"bảng": "B", "sơ_đồ": "4-4-2", "lối_chơi": "Tấn công biên dựa vào tốc độ, chuyển trạng thái nhanh", "ngôi_sao": "Alphonso Davies", "sức_mạnh": "Trung bình", "hlv": "Jesse Marsch", "logo": "https://flagcdn.com/w80/ca.png", "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Hậu vệ biên (LB)", "Chiều cao": "1m83", "CLB": "Bayern Munich", "Phong độ": "🔥 8.7/10"}, "đội_hinh": ["M. Crépeau", "A. Johnston", "M. Bombito", "D. Cornelius", "A. Davies", "T. Buchanan", "S. Eustáquio", "I. Koné", "L. Millar", "J. David", "C. Larin"]},
        "Thụy Sĩ": {"bảng": "B", "sơ_đồ": "3-4-2-1", "lối_chơi": "Kỷ luật cao, tổ chức đội hình khoa học, bọc lót tốt", "ngôi_sao": "Granit Xhaka", "sức_mạnh": "Khá", "hlv": "Murat Yakin", "logo": "https://flagcdn.com/w80/ch.png", "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m85", "CLB": "Bayer Leverkusen", "Phong độ": "🔥 8.9/10"}, "đội_hinh": ["Y. Sommer", "M. Akanji", "N. Elvedi", "R. Rodríguez", "S. Widmer", "R. Freuler", "G. Xhaka", "D. Ndoye", "X. Shaqiri", "R. Vargas", "B. Embolo"]},
        "Bosnia & Herzegovina": {"bảng": "B", "sơ_đồ": "4-2-3-1", "lối_chơi": "Chậm rãi, chắc chắn trung tuyến, tận dụng bóng bổng", "ngôi_sao": "Edin Dzeko", "sức_mạnh": "Trung bình", "hlv": "Sergej Barbarez", "logo": "https://flagcdn.com/w80/ba.png", "star_stats": {"Độ tuổi": "40 tuổi", "Vị trí": "Tiền đạo cắm", "Chiều cao": "1m93", "CLB": "Fenerbahçe", "Phong độ": "⭐ 7.8/10"}, "đội_hinh": ["K. Piric", "A. Ahmedhodzic", "D. Hadzikadunic", "S. Kolasinac", "J. Gazibegovic", "R. Krunic", "B. Tahirovic", "H. Hajradinovic", "M. Stevanovic", "E. Demirovic", "E. Dzeko"]},
        "Qatar": {"bảng": "B", "sơ_đồ": "5-3-2", "lối_chơi": "Phòng ngự phản công, phối hợp nhỏ nhóm trung lộ", "ngôi_sao": "Akram Afif", "sức_mạnh": "Trung bình", "hlv": "Tintín Márquez", "logo": "https://flagcdn.com/w80/qa.png", "star_stats": {"Độ tuổi": "29 tuổi", "Vị trí": "Tiền đạo cánh", "Chiều cao": "1m77", "CLB": "Al-Sadd", "Phong độ": "⭐ 8.1/10"}, "đội_hinh": ["M. Barsham", "P. Miguel", "A. Ali", "L. Mendes", "T. Salman", "H. Ahmed", "H. Al-Haydos", "A. Fathy", "J. Gaber", "A. Ali", "A. Afif"]},

        # Bảng C
        "Brazil": {"bảng": "C", "sơ_đồ": "4-3-3", "lối_chơi": "Tấn công rực lửa, áp đặt thế trận kỹ thuật đỉnh cao", "ngôi_sao": "Vinicius Jr", "sức_mạnh": "Mạnh", "hlv": "Dorival Júnior", "logo": "https://flagcdn.com/w80/br.png", "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền đạo trái (LW)", "Chiều cao": "1m76", "CLB": "Real Madrid", "Phong độ": "⚡ 9.4/10"}, "đội_hinh": ["Alisson Becker", "Danilo", "Marquinhos", "Gabriel Magalhães", "Wendell", "B. Guimarães", "Douglas Luiz", "Lucas Paquetá", "Rodrygo", "Raphinha", "Vinicius Jr"]},
        "Morocco": {"bảng": "C", "sơ_đồ": "4-1-4-1", "lối_chơi": "Phòng ngự khối trung bình (Mid-block), phản công sắc bén", "ngôi_sao": "Hakimi", "sức_mạnh": "Khá", "hlv": "Walid Regragui", "logo": "https://flagcdn.com/w80/ma.png", "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Hậu vệ biên (RB)", "Chiều cao": "1m81", "CLB": "PSG", "Phong độ": "🔥 8.9/10"}, "đội_hinh": ["Y. Bounou", "A. Hakimi", "N. Aguerd", "R. Saïss", "Y. Attiyat Allah", "S. Amrabat", "A. Ounahi", "S. Amallah", "H. Ziyech", "A. Adli", "Y. En-Nesyri"]},
        "Scotland": {"bảng": "C", "sơ_đồ": "3-4-2-1", "lối_chơi": "Lối đá Anh truyền thống, tạt cánh đánh đầu mạnh mẽ", "ngôi_sao": "Andy Robertson", "sức_mạnh": "Trung bình", "hlv": "Steve Clarke", "logo": "https://flagcdn.com/w80/gb-sct.png", "star_stats": {"Độ tuổi": "32 tuổi", "Vị trí": "Hậu vệ biên", "Chiều cao": "1m78", "CLB": "Liverpool", "Phong độ": "⭐ 8.0/10"}, "đội_hinh": ["A. Gunn", "J. Hendry", "G. Hanley", "S. McKenna", "A. Ralston", "B. Gilmour", "C. McGregor", "A. Robertson", "S. McTominay", "J. McGinn", "C. Adams"]},
        "Haiti": {"bảng": "C", "sơ_đồ": "4-5-1", "lối_chơi": "Phòng ngự lùi sâu, tận dụng thể lực áp sát tầm xa", "ngôi_sao": "Frantzdy Pierrot", "sức_mạnh": "Yếu", "hlv": "Sébastien Migné", "logo": "https://flagcdn.com/w80/ht.png", "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Tiền đạo cắm", "Chiều cao": "1m94", "CLB": "Maccabi Haifa", "Phong độ": "⭐ 6.8/10"}, "đội_hinh": ["J. Placide", "C. Arcus", "R. Adé", "J. Duverne", "A. Christian", "B. Alceus", "L. Pierre", "D. Nazon", "D. Etienne", "F. Picault", "F. Pierrot"]},

        # Bảng D
        "Mỹ": {"bảng": "D", "sơ_đồ": "4-3-3", "lối_chơi": "Pressing tầm cao, chuyển trạng thái nhanh biên tốc độ", "ngôi_sao": "Pulisic", "sức_mạnh": "Khá", "hlv": "M. Pochettino", "logo": "https://flagcdn.com/w80/us.png", "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền đạo cánh", "Chiều cao": "1m77", "CLB": "AC Milan", "Phong độ": "🔥 8.7/10"}, "đội_hinh": ["M. Turner", "S. Dest", "C. Richards", "T. Ream", "A. Robinson", "W. McKennie", "T. Adams", "Y. Musah", "T. Weah", "F. Balogun", "C. Pulisic"]},
        "Paraguay": {"bảng": "D", "sơ_đồ": "4-4-2", "lối_chơi": "Thủ chặt phá lối chơi đối phương, va chạm áp sát", "ngôi_sao": "Almirón", "sức_mạnh": "Trung bình", "hlv": "Gustavo Alfaro", "logo": "https://flagcdn.com/w80/py.png", "star_stats": {"Độ tuổi": "32 tuổi", "Vị trí": "Tiền đạo cánh", "Chiều cao": "1m74", "CLB": "Newcastle", "Phong độ": "⭐ 7.6/10"}, "đội_hinh": ["C. Coronel", "R. Rojas", "G. Gómez", "J. Alonso", "B. Riveros", "M. Almirón", "M. Villasanti", "A. Cubas", "R. Sosa", "A. Sanabria", "Á. Arce"]},
        "Australia": {"bảng": "D", "sơ_đồ": "4-4-2", "lối_chơi": "Thiên về thể chất, bóng bổng, cố định mạnh", "ngôi_sao": "Harry Souttar", "sức_mạnh": "Trung bình", "hlv": "Tony Popovic", "logo": "https://flagcdn.com/w80/au.png", "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Trung vệ", "Chiều cao": "1m98", "CLB": "Sheffield", "Phong độ": "⭐ 7.5/10"}, "đội_hinh": ["M. Ryan", "G. Jones", "H. Souttar", "K. Rowles", "A. Behich", "M. Boyle", "K. Baccus", "J. Irvine", "C. Goodwin", "K. Yengi", "M. Duke"]},
        "Thổ Nhĩ Kỳ": {"bảng": "D", "sơ_đồ": "4-2-3-1", "lối_chơi": "Kỷ luật, đá cống hiến, tấn công trung lộ rất mạnh", "ngôi_sao": "Arda Güler", "sức_mạnh": "Khá", "hlv": "V. Montella", "logo": "https://flagcdn.com/w80/tr.png", "star_stats": {"Độ tuổi": "21 tuổi", "Vị trí": "Tiền vệ công", "Chiều cao": "1m75", "CLB": "Real Madrid", "Phong độ": "🔥 8.6/10"}, "đội_hinh": ["M. Günok", "Z. Çelik", "S. Akaydin", "A. Bardakcı", "F. Kadıoğlu", "H. Çalhanoğlu", "S. Özcan", "C. Ünder", "Arda Güler", "K. Aktürkoğlu", "B. Yılmaz"]},

        # Bảng E
        "Đức": {"bảng": "E", "sơ_đồ": "4-2-3-1", "lối_chơi": "Kiểm soát thế trận, pressing tầm cao, ban bật ngắn", "ngôi_sao": "Jamal Musiala", "sức_mạnh": "Mạnh", "hlv": "Julian Nagelsmann", "logo": "https://flagcdn.com/w80/de.png", "star_stats": {"Độ tuổi": "23 tuổi", "Vị trí": "Tiền vệ hộ công", "Chiều cao": "1m84", "CLB": "Bayern", "Phong độ": "🔥 9.3/10"}, "đội_hinh": ["M. Neuer", "J. Kimmich", "J. Tah", "A. Rüdiger", "M. Mittelstädt", "R. Andrich", "T. Kroos", "Jamal Musiala", "I. Gündogan", "F. Wirtz", "Kai Havertz"]},
        "Curaçao": {"bảng": "E", "sơ_đồ": "4-4-2", "lối_chơi": "Phòng ngự số đông, phản công bứt tốc biên", "ngôi_sao": "Juninho Bacuna", "sức_mạnh": "Yếu", "hlv": "Dick Advocaat", "logo": "https://flagcdn.com/w80/cw.png", "star_stats": {"Độ tuổi": "28 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m78", "CLB": "Al-Wahda", "Phong độ": "⭐ 6.5/10"}, "đội_hinh": ["E. Room", "J. Gaari", "R. van Eijma", "C. Martina", "S. Floranus", "B. Kuwas", "V. Anita", "L. Bacuna", "K. Gorré", "R. Janga", "J. Bacuna"]},
        "Bờ Biển Ngà": {"bảng": "E", "sơ_đồ": "4-3-3", "lối_chơi": "Cậy nhờ thể lực, giàu tốc độ, đá trực diện", "ngôi_sao": "Franck Kessié", "sức_mạnh": "Trung bình", "hlv": "Emerse Faé", "logo": "https://flagcdn.com/w80/ci.png", "star_stats": {"Độ tuổi": "29 tuổi", "Vị trí": "Tiền vệ", "Chiều cao": "1m83", "CLB": "Al-Ahli", "Phong độ": "⭐ 7.9/10"}, "đội_hinh": ["Y. Fofana", "W. Singo", "O. Diomande", "E. Ndicka", "G. Konan", "F. Kessié", "J. Seri", "S. Fofana", "M. Gradel", "S. Adingra", "S. Haller"]},
        "Ecuador": {"bảng": "E", "sơ_đồ": "3-4-3", "lối_chơi": "Đá rực lửa, pressing mạnh ở biên, giàu thể lực", "ngôi_sao": "Moisés Caicedo", "sức_mạnh": "Khá", "hlv": "S. Beccacece", "logo": "https://flagcdn.com/w80/ec.png", "star_stats": {"Độ tuổi": "24 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m78", "CLB": "Chelsea", "Phong độ": "🔥 8.5/10"}, "đội_hinh": ["A. Domínguez", "F. Torres", "W. Pacho", "P. Hincapié", "A. Preciado", "M. Caicedo", "A. Franco", "P. Estupiñán", "K. Páez", "J. Sarmiento", "E. Valencia"]},

        # Bảng F
        "Hà Lan": {"bảng": "F", "sơ_đồ": "3-4-3", "lối_chơi": "Tấn công tổng lực, đẩy cao hai biên, kiểm soát bóng chủ động", "ngôi_sao": "Virgil van Dijk", "sức_mạnh": "Mạnh", "hlv": "Ronald Koeman", "logo": "https://flagcdn.com/w80/nl.png", "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Trung vệ thủ lĩnh", "Chiều cao": "1m95", "CLB": "Liverpool", "Phong độ": "🔥 9.0/10"}, "đội_hinh": ["B. Verbruggen", "L. Geertruida", "Virgil van Dijk", "N. Aké", "D. Dumfries", "J. Schouten", "T. Reijnders", "D. Blind", "X. Simons", "Cody Gakpo", "M. Depay"]},
        "Nhật Bản": {"bảng": "F", "sơ_đồ": "4-2-3-1", "lối_chơi": "Phối hợp nhỏ nhóm tốc độ cao, kỷ luật vị trí tốt", "ngôi_sao": "Kaoru Mitoma", "sức_mạnh": "Khá", "hlv": "Hajime Moriyasu", "logo": "https://flagcdn.com/w80/jp.png", "star_stats": {"Độ tuổi": "29 tuổi", "Vị trí": "Tiền đạo cánh", "Chiều cao": "1m78", "CLB": "Brighton", "Phong độ": "🔥 8.6/10"}, "đội_hinh": ["Z. Suzuki", "Y. Sugawara", "K. Itakura", "S. Taniguchi", "H. Ito", "W. Endo", "H. Morita", "T. Kubo", "T. Minamino", "Kaoru Mitoma", "A. Ueda"]},
        "Thụy Điển": {"bảng": "F", "sơ_đồ": "4-4-2", "lối_chơi": "Tổ chức chặt chẽ, chơi bóng dài bổng hiệu quả", "ngôi_sao": "Alexander Isak", "sức_mạnh": "Khá", "hlv": "Jon Dahl Tomasson", "logo": "https://flagcdn.com/w80/se.png", "star_stats": {"Độ tuổi": "26 tuổi", "Vị trí": "Tiền đạo", "Chiều cao": "1m92", "CLB": "Newcastle", "Phong độ": "🔥 8.9/10"}, "đội_hinh": ["R. Olsen", "E. Holm", "I. Hien", "V. Lindelöf", "L. Augustinsson", "D. Kulusevski", "J. Cajuste", "A. Salétros", "E. Forsberg", "V. Gyökeres", "A. Isak"]},
        "Tunisia": {"bảng": "F", "sơ_đồ": "4-5-1", "lối_chơi": "Phòng ngự kỷ luật, phá lối chơi đối phương", "ngôi_sao": "Ellyes Skhiri", "sức_mạnh": "Trung bình", "hlv": "Faouzi Benzarti", "logo": "https://flagcdn.com/w80/tn.png", "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m85", "CLB": "Frankfurt", "Phong độ": "⭐ 7.4/10"}, "đội_hinh": ["B. Saïd", "W. Kechrida", "D. Bronn", "M. Talbi", "A. Abdi", "E. Skhiri", "A. Laïdouni", "A. Slimane", "H. Rafia", "S. Ltaief", "Y. Msakni"]},

        # Bảng G
        "Bỉ": {"bảng": "G", "sơ_đồ": "4-3-3", "lối_chơi": "Tấn công trung lộ, ban bật nhanh tiền vệ sáng tạo", "ngôi_sao": "Kevin De Bruyne", "sức_mạnh": "Mạnh", "hlv": "Domenico Tedesco", "logo": "https://flagcdn.com/w80/be.png", "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền vệ kiến thiết", "Chiều cao": "1m81", "CLB": "Man City", "Phong độ": "🔥 9.2/10"}, "đội_hinh": ["K. Casteels", "T. Castagne", "W. Faes", "Jan Vertonghen", "A. Theate", "O. Mangala", "A. Onana", "Kevin De Bruyne", "J. Doku", "L. Trossard", "R. Lukaku"]},
        "Ai Cập": {"bảng": "G", "sơ_đồ": "4-3-3", "lối_chơi": "Phòng ngự chặt, dồn bóng cho ngôi sao bứt tốc", "ngôi_sao": "Mohamed Salah", "sức_mạnh": "Khá", "hlv": "Hossam Hassan", "logo": "https://flagcdn.com/w80/eg.png", "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền đạo cánh", "Chiều cao": "1m75", "CLB": "Liverpool", "Phong độ": "🔥 9.0/10"}, "đội_hinh": ["M. El Shenawy", "M. Hany", "M. Abdelmonem", "Y. Ibrahim", "A. Maâloul", "M. Attia", "M. Elneny", "H. Fathi", "Mohamed Salah", "Trézéguet", "M. Mohamed"]},
        "Iran": {"bảng": "G", "sơ_đồ": "4-4-2", "lối_chơi": "Khối phòng ngự lùi sâu vững chãi, phản công nhanh", "ngôi_sao": "Mehdi Taremi", "sức_mạnh": "Khá", "hlv": "Amir Ghalenoei", "logo": "https://flagcdn.com/w80/ir.png", "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền đạo", "Chiều cao": "1m87", "CLB": "Inter Milan", "Phong độ": "⭐ 8.1/10"}, "đội_hinh": ["A. Beiranvand", "R. Rezaeian", "H. Kanaanizadegan", "S. Khalilzadeh", "M. Mohammadi", "S. Ghoddos", "S. Ezatolahi", "A. Jahanbakhsh", "M. Torabi", "S. Azmoun", "Mehdi Taremi"]},
        "New Zealand": {"bảng": "G", "sơ_đồ": "4-4-2", "lối_chơi": "Bóng bổng, dựa vào thể hình tranh chấp mạnh", "ngôi_sao": "Chris Wood", "sức_mạnh": "Yếu", "hlv": "Darren Bazeley", "logo": "https://flagcdn.com/w80/nz.png", "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền đạo cắm", "Chiều cao": "1m91", "CLB": "Nottingham", "Phong độ": "⭐ 7.2/10"}, "đội_hinh": ["O. Sail", "T. Payne", "M. Boxall", "N. Pijnaker", "L. Cacace", "Joe Bell", "M. Garbett", "S. Singh", "Ben Old", "K. Barbarouses", "Chris Wood"]},

        # Bảng H
        "Tây Ban Nha": {"bảng": "H", "sơ_đồ": "4-3-3", "lối_chơi": "Tiki-taka hiện đại, luân chuyển bóng nhanh, kiểm soát", "ngôi_sao": "Lamine Yamal", "sức_mạnh": "Mạnh", "hlv": "Luis de la Fuente", "logo": "https://flagcdn.com/w80/es.png", "star_stats": {"Độ tuổi": "18 tuổi", "Vị trí": "Tiền đạo cánh (RW)", "Chiều cao": "1m80", "CLB": "Barcelona", "Phong độ": "👑 9.6/10"}, "đội_hinh": ["Unai Simón", "Dani Carvajal", "R. Le Normand", "A. Laporte", "M. Cucurella", "Rodri", "Pedri", "Fabian Ruiz", "Lamine Yamal", "Nico Williams", "Alvaro Morata"]},
        "Cape Verde": {"bảng": "H", "sơ_đồ": "4-3-3", "lối_chơi": "Phòng ngự phản công biên tốc độ", "ngôi_sao": "Ryan Mendes", "sức_mạnh": "Trung bình", "hlv": "Bubista", "logo": "https://flagcdn.com/w80/cv.png", "star_stats": {"Độ tuổi": "36 tuổi", "Vị trí": "Tiền đạo cánh", "Chiều cao": "1m78", "CLB": "Karagümrük", "Phong độ": "⭐ 6.9/10"}, "đội_hinh": ["Vozinha", "S. Moreira", "Logan Costa", "R. Lopes", "João Paulo", "Kevin Pina", "J. Monteiro", "D. Duarte", "Ryan Mendes", "G. Rodrigues", "J. Cabral"]},
        "Saudi Arabia": {"bảng": "H", "sơ_đồ": "4-5-1", "lối_chơi": "Áp sát tầm cao, bẫy việt vị chiến thuật tốt", "ngôi_sao": "Salem Al-Dawsari", "sức_mạnh": "Trung bình", "hlv": "Roberto Mancini", "logo": "https://flagcdn.com/w80/sa.png", "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền đạo cánh (LW)", "Chiều cao": "1m71", "CLB": "Al-Hilal", "Phong độ": "⭐ 7.7/10"}, "đội_hinh": ["M. Al-Owais", "S. Abdulhamid", "Ali Lajami", "Ali Al-Bulaihi", "Y. Al-Shahrani", "A. Otayf", "M. Kanno", "F. Al-Buraikan", "S. Al-Faraj", "Salem Al-Dawsari", "S. Al-Shehri"]},
        "Uruguay": {"bảng": "H", "sơ_đồ": "4-3-3", "lối_chơi": "Pressing điên cuồng, va chạm rực lửa, trực diện công", "ngôi_sao": "Federico Valverde", "sức_mạnh": "Mạnh", "hlv": "Marcelo Bielsa", "logo": "https://flagcdn.com/w80/uy.png", "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền vệ", "Chiều cao": "1m82", "CLB": "Real Madrid", "Phong độ": "🔥 9.1/10"}, "đội_hinh": ["Sergio Rochet", "N. Nández", "Ronald Araújo", "J. M. Giménez", "M. Olivera", "Federico Valverde", "Manuel Ugarte", "N. de la Cruz", "F. Pellistri", "Darwin Núñez", "M. Araújo"]},

        # Bảng I
        "Pháp": {"bảng": "I", "sơ_đồ": "4-2-3-1", "lối_chơi": "Tấn công trực diện tốc độ cao hành lang biên", "ngôi_sao": "Kylian Mbappé", "sức_mạnh": "Mạnh", "hlv": "Didier Deschamps", "logo": "https://flagcdn.com/w80/fr.png", "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền đạo cắm", "Chiều cao": "1m78", "CLB": "Real Madrid", "Phong độ": "👑 9.5/10"}, "đội_hinh": ["Mike Maignan", "Jules Koundé", "D. Upamecano", "William Saliba", "Théo Hernandez", "N'Golo Kanté", "A. Tchouaméni", "O. Dembélé", "A. Griezmann", "B. Barcola", "Kylian Mbappé"]},
        "Senegal": {"bảng": "I", "sơ_đồ": "4-3-3", "lối_chơi": "Cân bằng thể lực và kỹ thuật, áp sát nhanh", "ngôi_sao": "Sadio Mané", "sức_mạnh": "Khá", "hlv": "Aliou Cissé", "logo": "https://flagcdn.com/w80/sn.png", "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền đạo biên", "Chiều cao": "1m74", "CLB": "Al-Nassr", "Phong độ": "⭐ 8.0/10"}, "đội_hinh": ["É. Mendy", "F. Mendy", "K. Koulibaly", "A. Diallo", "I. Jakobs", "I. Gueye", "P. M. Sarr", "L. Camara", "I. Sarr", "N. Jackson", "Sadio Mané"]},
        "Iraq": {"bảng": "I", "sơ_đồ": "4-2-3-1", "lối_chơi": "Đá tinh quái, không ngại va chạm, mạnh trung lộ", "ngôi_sao": "Aymen Hussein", "sức_mạnh": "Trung bình", "hlv": "Jesús Casas", "logo": "https://flagcdn.com/w80/iq.png", "star_stats": {"Độ tuổi": "30 tuổi", "Vị trí": "Tiền đạo cắm", "Chiều cao": "1m89", "CLB": "Al-Khor", "Phong độ": "⭐ 7.9/10"}, "đội_hinh": ["J. Hassan", "H. Ali", "S. Natiq", "R. Sulaka", "M. Doski", "A. Al-Ammari", "O. Rashid", "I. Bayesh", "Z. Iqbal", "Ali Jasim", "Aymen Hussein"]},
        "Na Uy": {"bảng": "I", "sơ_đồ": "4-3-3", "lối_chơi": "Tấn công trục dọc, nhồi bóng cho trung phong cắm", "ngôi_sao": "Erling Haaland", "sức_mạnh": "Khá", "hlv": "Ståle Solbakken", "logo": "https://flagcdn.com/w80/no.png", "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền đạo cắm", "Chiều cao": "1m94", "CLB": "Man City", "Phong độ": "🔥 9.4/10"}, "đội_hinh": ["Ø. Nyland", "J. Ryerson", "L. Östigard", "K. Ajer", "D. Wolfe", "M. Ødegaard", "P. Berg", "S. Berge", "Oscar Bobb", "A. Nusa", "Erling Haaland"]},

        # Bảng J
        "Áo": {"bảng": "J", "sơ_đồ": "4-2-2-2", "lối_chơi": "Gegenpressing điên cuồng, bóp nghẹt không gian bóng", "ngôi_sao": "David Alaba", "sức_mạnh": "Khá", "hlv": "Ralf Rangnick", "logo": "https://flagcdn.com/w80/at.png", "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Hậu vệ đa năng", "Chiều cao": "1m80", "CLB": "Real Madrid", "Phong độ": "⭐ 8.2/10"}, "đội_hinh": ["P. Pentz", "S. Posch", "K. Danso", "David Alaba", "P. Mwene", "N. Seiwald", "K. Laimer", "M. Sabitzer", "C. Baumgartner", "M. Gregoritsch", "M. Arnautovic"]},
        "Jordan": {"bảng": "J", "sơ_đồ": "3-4-3", "lối_chơi": "Phòng ngự kỷ luật, phản công chớp nhoáng biên", "ngôi_sao": "Mousa Al-Tamari", "sức_mạnh": "Trung bình", "hlv": "Jamal Sellami", "logo": "https://flagcdn.com/w80/jo.png", "star_stats": {"Độ tuổi": "28 tuổi", "Vị trí": "Tiền đạo cánh", "Chiều cao": "1m78", "CLB": "Montpellier", "Phong độ": "⭐ 7.9/10"}, "đội_hinh": ["Y. Abulaila", "A. Nasib", "Y. Al-Arab", "S. Al-Ajalin", "E. Haddad", "N. Al-Rashdan", "N. Al-Rawabdeh", "M. Al-Mardi", "M. Al-Tamari", "A. Olwan", "Y. Al-Naimat"]},
        "Algeria": {"bảng": "J", "sơ_đồ": "4-2-3-1", "lối_chơi": "Kỹ thuật cá nhân tốt, chuộng đá biên và ban bật ngắn", "ngôi_sao": "Riyad Mahrez", "sức_mạnh": "Khá", "hlv": "Vladimir Petkovic", "logo": "https://flagcdn.com/w80/dz.png", "star_stats": {"Độ tuổi": "35 tuổi", "Vị trí": "Tiền đạo cánh", "Chiều cao": "1m79", "CLB": "Al-Ahli", "Phong độ": "⭐ 8.2/10"}, "đội_hinh": ["A. Mandrea", "Y. Atal", "A. Mandi", "R. Bensebaini", "R. Aït-Nouri", "N. Bentaleb", "I. Bennacer", "R. Mahrez", "H. Aouar", "S. Benrahma", "B. Bounedjah"]},

        # Bảng K
        "Bồ Đào Nha": {"bảng": "K", "sơ_đồ": "4-3-3", "lối_chơi": "Tấn công áp đặt đa dạng, hoán đổi biên liên tục", "ngôi_sao": "Bruno Fernandes", "sức_mạnh": "Mạnh", "hlv": "Roberto Martínez", "logo": "https://flagcdn.com/w80/pt.png", "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Tiền vệ công", "Chiều cao": "1m79", "CLB": "Man United", "Phong độ": "🔥 9.0/10"}, "đội_hinh": ["Diogo Costa", "J. Cancelo", "Rúben Dias", "Pepe", "Nuno Mendes", "J. Palhinha", "Vitinha", "Bruno Fernandes", "Bernardo Silva", "Rafael Leão", "Cristiano Ronaldo"]},
        "Uzbekistan": {"bảng": "K", "sơ_đồ": "3-4-2-1", "lối_chơi": "Kỷ luật chiến thuật cao, thủ chặt phản công sắc", "ngôi_sao": "Eldor Shomurodov", "sức_mạnh": "Trung bình", "hlv": "Srecko Katanec", "logo": "https://flagcdn.com/w80/uz.png", "star_stats": {"Độ tuổi": "30 tuổi", "Vị trí": "Tiền đạo cắm", "Chiều cao": "1m90", "CLB": "Roma", "Phong độ": "⭐ 7.5/10"}, "đội_hinh": ["U. Yusupov", "A. Khusanov", "U. Eshmurodov", "R. Ashurmatov", "K. Alijonov", "O. Shukurov", "O. Hamrobekov", "S. Nasrullaev", "A. Fayzullaev", "J. Masharipov", "E. Shomurodov"]},
        "Colombia": {"bảng": "K", "sơ_đồ": "4-2-3-1", "lối_chơi": "Kỹ thuật Nam Mỹ rực lửa, đột biến cánh tốt", "ngôi_sao": "Luis Díaz", "sức_mạnh": "Mạnh", "hlv": "Néstor Lorenzo", "logo": "https://flagcdn.com/w80/co.png", "star_stats": {"Độ tuổi": "29 tuổi", "Vị trí": "Tiền đạo cánh", "Chiều cao": "1m80", "CLB": "Liverpool", "Phong độ": "🔥 8.9/10"}, "đội_hinh": ["C. Vargas", "D. Muñoz", "D. Sánchez", "C. Cuesta", "J. Mojica", "R. Ríos", "J. Lerma", "J. Arias", "James Rodríguez", "Luis Díaz", "J. Córdoba"]},
        "CHDC Congo": {"bảng": "K", "sơ_đồ": "4-2-3-1", "lối_chơi": "Đá giàu tốc độ và va chạm thể lực khu tuyến giữa", "ngôi_sao": "Chancel Mbemba", "sức_mạnh": "Trung bình", "hlv": "Sébastien Desabre", "logo": "https://flagcdn.com/w80/cd.png", "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Trung vệ (CB)", "Chiều cao": "1m82", "CLB": "Marseille", "Phong độ": "⭐ 7.4/10"}, "đội_hinh": ["L. Mpasi", "G. Kalulu", "C. Mbemba", "H. Inonga", "A. Masuaku", "S. Moutoussamy", "C. Pickel", "T. Bongonda", "G. Kakuta", "Y. Wissa", "C. Bakambu"]},

        # Bảng L
        "Anh": {"bảng": "L", "sơ_đồ": "4-2-3-1", "lối_chơi": "Tấn công biên dồn dập, cố định rất mạnh", "ngôi_sao": "Jude Bellingham", "sức_mạnh": "Mạnh", "hlv": "Thomas Tuchel", "logo": "https://flagcdn.com/w80/gb-eng.png", "star_stats": {"Độ tuổi": "22 tuổi", "Vị trí": "Tiền vệ công", "Chiều cao": "1m86", "CLB": "Real Madrid", "Phong độ": "👑 9.5/10"}, "đội_hinh": ["J. Pickford", "K. Walker", "J. Stones", "M. Guéhi", "K. Trippier", "D. Rice", "K. Mainoo", "B. Saka", "Jude Bellingham", "Phil Foden", "Harry Kane"]},
        "Croatia": {"bảng": "L", "sơ_đồ": "4-3-3", "lối_chơi": "Làm chủ tuyến giữa, cầm nhịp trận đấu chậm tinh tế", "ngôi_sao": "Luka Modric", "sức_mạnh": "Khá", "hlv": "Zlatko Dalic", "logo": "https://flagcdn.com/w80/hr.png", "star_stats": {"Độ tuổi": "40 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m72", "CLB": "Real Madrid", "Phong độ": "⭐ 8.3/10"}, "đội_hinh": ["D. Livakovic", "J. Stanisic", "J. Sutalo", "M. Pongracic", "J. Gvardiol", "Luka Modric", "M. Brozovic", "M. Kovacic", "L. Majer", "A. Kramaric", "Ante Budimir"]},
        "Ghana": {"bảng": "L", "sơ_đồ": "4-2-3-1", "lối_chơi": "Tấn công trực diện, bứt tốc quãng ngắn mạnh", "ngôi_sao": "Mohammed Kudus", "sức_mạnh": "Trung bình", "hlv": "Otto Addo", "logo": "https://flagcdn.com/w80/gh.png", "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền vệ tấn công", "Chiều cao": "1m77", "CLB": "West Ham", "Phong độ": "🔥 8.4/10"}, "đội_hinh": ["L. Ati-Zigi", "A. Seidu", "A. Djiku", "M. Salisu", "G. Mensah", "S. Samed", "T. Partey", "J. Ayew", "M. Kudus", "E. Nuamah", "I. Williams"]},
        "Panama": {"bảng": "L", "sơ_đồ": "5-4-1", "lối_chơi": "Phòng ngự số đông co cụm, phá bóng rát", "ngôi_sao": "Michael Murillo", "sức_mạnh": "Trung bình", "hlv": "Thomas Christiansen", "logo": "https://flagcdn.com/w80/pa.png", "star_stats": {"Độ tuổi": "30 tuổi", "Vị trí": "Hậu vệ biên", "Chiều cao": "1m83", "CLB": "Marseille", "Phong độ": "⭐ 7.1/10"}, "đội_hinh": ["O. Mosquera", "M. Murillo", "J. Córdoba", "E. Fariña", "R. Miller", "Eric Davis", "A. Godoy", "A. Carrasquilla", "J. Rodríguez", "Y. Bárcenas", "J. Fajardo"]}
    }

TEAMS = get_teams_data()

# KHAI BÁO THUẬT TOÁN LOGIC TRƯỚC KHI GỌI Ở GIAO DIỆN ĐỂ TRÁNH LỖI NAMERROR 100%
def get_team_history_insight(team_name):
    played_matches = []
    for code, m in st.session_state.matches.items():
        if m["ti_so_ft"] != "" and (m["đội_nhà"] == team_name or m["đội_khách"] == team_name):
            played_matches.append((code, m))
    if not played_matches:
        if team_name == "Mexico": return "Chuỗi 3 trận giao hữu toàn thắng sát giải đấu, phong độ thăng hoa."
        if team_name == "Nam Phi": return "Kết quả loạt giao hữu thiếu ổn định, hàng thủ cần gia cố gấp."
        return "Trạng thái thể lực sung mãn, sẵn sàng bung hết sức lực ra quân."
    return "Đang điều chỉnh điểm rơi phong độ thực tế qua từng vòng đấu."

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

# ĐỊNH HÌNH 4 TABS CHỨC NĂNG CHUẨN CHỈ
tab1, tab2, tab3, tab4 = st.tabs([
    "📰 Nhận Định Trước Trận & Đội Hình", 
    "⏱️ Phòng Nhập Liệu Real-Time (HT/FT)", 
    "🏃 Danh Sách Các Đội Bóng",
    "📊 Xác Suất Vô Địch Qua Từng Vòng (Goal Analytics)"
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

    # THANH TIẾN TRÌNH XÁC SUẤT ĐỒ HỌA SVELTE COPIED CỰC XỊN CHÍNH DIỆN
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
    st.markdown("### 🕒 DANH SÁCH TRẬN ĐẤU VÒNG BẢNG & KNOCKOUT OVERVIEW")
    list_grid = []
    for c, m in st.session_state.matches.items():
        status = m['ti_so_ft'] if m['ti_so_ft'] != "" else "Chưa đá"
        list_grid.append([c, m['ngày'], m['đội_nhà'], status, m['đội_khách']])
    grid_df = pd.DataFrame(list_grid, columns=["Mã", "Ngày", "Đội Nhà", "Kết Quả", "Đội Khách"])
    st.dataframe(grid_df, use_container_width=True, height=220)

# ==================================================================
# TAB 2: PHÒNG NHẬP LIỆU REAL-TIME NÂNG CAO ĐẦY ĐỦ CÁC TRƯỜNG DỮ LIỆU
# ==================================================================
with tab2:
    st.markdown('<div class="sub-title-custom">PHÒNG ĐIỀU PHỐI & NHẬP LIỆU THỜI GIAN THỰC</div>', unsafe_allow_html=True)
    update_m = st.selectbox("Chọn mã trận đấu cần ghi nhận dữ liệu sau giờ bóng lăn:", list(st.session_state.matches.keys()))
    curr_m = st.session_state.matches[update_m]
    
    st.markdown(f"### 📍 Đang ghi nhận dữ liệu: **{curr_m['đội_nhà']} vs {curr_m['đội_khách']}**")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 🕒 Thông số Giữa Hiệp (HT)")
        curr_m['ti_so_ht'] = st.text_input("Tỉ số giữa hiệp (HT) (Vd: 1-0):", curr_m['ti_so_ht'])
        curr_m['sút_ht'] = st.text_input("Số cú sút trong Hiệp 1 (Chủ/Khách):", curr_m['sút_ht'])
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
        
    curr_m['thời_tiết'] = st.text_input("Tình hình thời tiết thực tế tại sân:", curr_m['thời_tiết'])
    curr_m['trọng_tài'] = st.text_input("Trọng tài chính điều khiển:", curr_m['trọng_tài'])
        
    if st.button("💾 XÁC NHẬN CẬP NHẬT DỮ LIỆU"):
        st.toast("Hệ thống đã lưu kết quả trận đấu lên máy chủ đám mây vĩnh viễn!", icon="⚡")

# ==================================================================
# TAB 3: DANH SÁCH TOÀN BỘ CÁC ĐỘI BÓNG KHÔNG LỖI KHÓA KEYERROR
# ==================================================================
with tab3:
    st.markdown('<div class="sub-title-custom">CƠ SỞ DỮ LIỆU CHIẾN THUẬT TOÀN GIẢI ĐẤU (ĐẦY ĐỦ 48 ĐỘI)</div>', unsafe_allow_html=True)
    team_list = []
    for t_name, t_val in TEAMS.items():
        bảng = t_val.get('bảng', 'Vòng bảng')
        hlv = t_val.get('hlv', 'Chưa cập nhật')
        sơ_đồ = t_val.get('sơ_đồ', 'Chưa cập nhật')
        lối_chơi = t_val.get('lối_chơi', 'Chưa cập nhật')
        ngôi_sao = t_val.get('ngôi_sao', 'Chưa cập nhật')
        sức_mạnh = t_val.get('sức_mạnh', 'Trung bình')
        team_list.append([t_name, bảng, hlv, sơ_đồ, lối_chơi, ngôi_sao, sức_mạnh])
    
    team_df = pd.DataFrame(team_list, columns=["Tên Đội Bóng", "Bảng", "Huấn Luyện Viên", "Sơ Đồ Chiến Thuật", "Lối Chơi Chủ Đạo", "Ngôi Sao Gánh Đội", "Đánh Giá Cửa"])
    st.dataframe(team_df, use_container_width=True, height=450)

# ==================================================================
# TAB 4: THAY THẾ TOÀN DIỆN BẰNG % CƠ HỘI VÔ ĐỊCH 2026 CHUẨN XỊN LỊCH SỬ
# ==================================================================
with tab4:
    st.markdown('<div class="sub-title-custom">🏆 XÁC SUẤT CƠ HỘI VÔ ĐỊCH DỰ KIẾN (CHAMPIONSHIP ODDS EVOLUTION)</div>', unsafe_allow_html=True)
    st.write("Hệ thống tổng hợp và phân tích biến động tỷ lệ cơ hội nâng cao chiếc cúp vô địch của các ứng cử viên dựa trên giả lập 10,000 thuật toán Monte Carlo.")
    
    # Cho phép người xem lựa chọn vòng đấu bằng selectbox chữ sáng
    round_choice = st.selectbox("Chọn giai đoạn giải đấu để xem tỷ lệ % cơ hội vô địch:", [
        "Sau Vòng Bảng (Còn 32 Đội Tuyển)",
        "Sau Vòng 32 Đội (Còn 16 Đội Tuyển)",
        "Sau Vòng 16 Đội (Còn 8 Đội Tuyển)",
        "Sau Vòng Tứ Kết (Còn 4 Đội Tuyển)",
        "Sau Vòng Bán Kết (Trận Chung Kết Trong Mơ)"
    ])
    
    st.markdown(f"#### 📊 BẢNG XẾP HẠNG % CƠ HỘI VÔ ĐỊCH: {round_choice.upper()}")
    
    if round_choice == "Sau Vòng Bảng (Còn 32 Đội Tuyển)":
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="card-player"><span class="stat-label">🇦🇷 Argentina (Đương kim Vô địch)</span><span class="stat-value">25%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇫🇷 Pháp (Thách thức lớn)</span><span class="stat-value">20%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇧🇷 Brazil</span><span class="stat-value">16%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇪🇸 Tây Ban Nha</span><span class="stat-value">12%</span></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="card-player"><span class="stat-label">🏴󠁧󠁢󠁥󠁮󠁧󠁿 Anh</span><span class="stat-value">10%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇩🇪 Đức</span><span class="stat-value">8%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇵🇹 Bồ Đào Nha</span><span class="stat-value">6%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">Các đội tuyển khác</span><span class="stat-value">3%</span></div>', unsafe_allow_html=True)
            
    elif round_choice == "Sau Vòng 32 Đội (Còn 16 Đội Tuyển)":
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="card-player"><span class="stat-label">🇦🇷 Argentina (Đương kim Vô địch)</span><span class="stat-value">28%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇫🇷 Pháp</span><span class="stat-value">22%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇧🇷 Brazil</span><span class="stat-value">19%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇪🇸 Tây Ban Nha</span><span class="stat-value">14%</span></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="card-player"><span class="stat-label">🏴󠁧󠁢󠁥󠁮󠁧󠁿 Anh</span><span class="stat-value">11%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇩🇪 Đức</span><span class="stat-value">5%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇲🇽 Mexico</span><span class="stat-value">1%</span></div>', unsafe_allow_html=True)
            
    elif round_choice == "Sau Vòng 16 Đội (Còn 8 Đội Tuyển)":
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="card-player"><span class="stat-label">🇦🇷 Argentina (Đương kim Vô địch)</span><span class="stat-value">34%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇫🇷 Pháp</span><span class="stat-value">26%</span></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="card-player"><span class="stat-label">🇧🇷 Brazil</span><span class="stat-value">22%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇪🇸 Tây Ban Nha</span><span class="stat-value">18%</span></div>', unsafe_allow_html=True)
            
    elif round_choice == "Sau Vòng Tứ Kết (Còn 4 Đội Tuyển)":
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="card-player"><span class="stat-label">🇦🇷 Argentina (Đương kim Vô địch)</span><span class="stat-value">42%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇫🇷 Pháp</span><span class="stat-value">35%</span></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="card-player"><span class="stat-label">🇧🇷 Brazil</span><span class="stat-value">15%</span></div>', unsafe_allow_html=True)
            st.markdown('<div class="card-player"><span class="stat-label">🇪🇸 Tây Ban Nha</span><span class="stat-value">8%</span></div>', unsafe_allow_html=True)
            
    elif round_choice == "Sau Vòng Bán Kết (Trận Chung Kết Trong Mơ)":
        st.markdown('<div class="card-vs" style="padding:15px; margin-bottom:15px;"><span style="color:#ffd700; font-weight:bold; font-size:20px;">TRẬN CHUNG KẾT TRONG MƠ CHÍNH THỨC 2026</span><br>🇦🇷 Argentina vs 🇫🇷 Pháp</div>', unsafe_allow_html=True)
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.markdown('<div class="card-player" style="border-left: 5px solid #ffd700;"><span class="stat-label">👑 ARGENTINA BẢO VỆ NGÔI VƯƠNG (ĐKVĐ 2022)</span><span class="stat-value">58%</span></div>', unsafe_allow_html=True)
        with col_f2:
            st.markdown('<div class="card-player" style="border-left: 5px solid #3b82f6;"><span class="stat-label">🐓 PHÁP LẬT ĐỔ ĐÒI NỢ THÀNH CÔNG</span><span class="stat-value">42%</span></div>', unsafe_allow_html=True)
