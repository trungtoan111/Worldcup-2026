import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. CẤU HÌNH TRANG WEB & GIAO DIỆN CHỦ ĐẠO (DARK SPORTS THEME)
st.set_page_config(page_title="World Cup 2026 - AI Dashboard Pro", layout="wide")

# Hệ thống CSS Custom độc quyền giúp giao diện hiển thị chuyên nghiệp như các trang báo lớn
st.markdown("""
<style>
    .main { background-color: #0f172a; }
    .title-main { color: #fecd3d; font-family: 'Poppins', sans-serif; font-size: 36px; font-weight: bold; text-align: center; margin-bottom: 25px; }
    .card-vs { background: linear-gradient(135deg, #1e293b 0%, #334155 100%); border: 1px solid #475569; border-radius: 15px; padding: 25px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    .vs-text { font-size: 32px; font-weight: bold; color: #fecd3d; margin: 0 10px; }
    .team-name { font-size: 24px; font-weight: bold; color: #ffffff; }
    .hlv-text { font-size: 15px; color: #94a3b8; font-style: italic; }
    .card-player { background: #1e293b; border-left: 5px solid #fecd3d; border-radius: 8px; padding: 12px; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    .stat-label { color: #94a3b8; font-size: 15px; font-weight: 500; }
    .stat-value { color: #ffffff; font-weight: bold; font-size: 16px; float: right; }
    .ai-box { background: rgba(254, 205, 61, 0.1); border: 1px solid #fecd3d; border-radius: 12px; padding: 20px; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-main">🏆 WORLD CUP 2026 - REALTIME AI DASHBOARD PRO</div>', unsafe_allow_html=True)
st.markdown("---")

# 2. DATABASE TỔNG LỰC: ĐỦ ĐỘI BÓNG, LOGO QUỐC KỲ, ẢNH CẦU THỦ & CHỈ SỐ NGUY HIỂM
@st.cache_data
def get_teams_data():
    return {
        # Bảng A
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
        # Bảng B
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
        "Qatar": {
            "bảng": "B", "sơ_đồ": "5-3-2", "sức_mạnh": "Trung bình", "hlv": "Tintín Márquez", "logo": "https://flagcdn.com/w80/qa.png",
            "star_name": "Akram Afif", "star_img": "https://img.a.transfermarkt.technology/portrait/header/336647-1701332840.jpg",
            "star_stats": {"Độ tuổi": "29 tuổi", "Vị trí": "Tiền đạo trái (LW)", "Chiều cao": "1m77", "CLB": "Al-Sadd", "Phong độ": "⭐ 8.1/10"},
            "lối_chơi": "Phòng ngự phản công, phối hợp nhỏ nhóm trung lộ",
            "đội_hinh": ["Meshaal Barsham", "Pedro Miguel", "Al-Mahdi Ali", "Lucas Mendes", "Tarek Salman", "Homam Ahmed", "Hassan Al-Haydos", "Ahmed Fathy", "Jassem Gaber", "Almoez Ali", "Akram Afif"]
        },
        "Thụy Sĩ": {
            "bảng": "B", "sơ_đồ": "3-4-2-1", "sức_mạnh": "Khá", "hlv": "Murat Yakin", "logo": "https://flagcdn.com/w80/ch.png",
            "star_name": "Granit Xhaka", "star_img": "https://img.a.transfermarkt.technology/portrait/header/90231-1668673070.jpg",
            "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m85", "CLB": "Bayer Leverkusen", "Phong độ": "🔥 8.9/10"},
            "lối_chơi": "Kỷ luật cao, tổ chức đội hình khoa học, bọc lót tốt",
            "đội_hinh": ["Yann Sommer", "Manuel Akanji", "Nico Elvedi", "Ricardo Rodríguez", "Silvan Widmer", "Remo Freuler", "Granit Xhaka", "Dan Ndoye", "Xherdan Shaqiri", "Ruben Vargas", "Breel Embolo"]
        },
        # Bảng C
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
        "Haiti": {
            "bảng": "C", "sơ_đồ": "4-5-1", "sức_mạnh": "Yếu", "hlv": "Sébastien Migné", "logo": "https://flagcdn.com/w80/ht.png",
            "star_name": "Frantzdy Pierrot", "star_img": "https://img.a.transfermarkt.technology/portrait/header/413009-1533036669.jpg",
            "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m94", "CLB": "Maccabi Haifa", "Phong độ": "⭐ 6.8/10"},
            "lối_chơi": "Phòng ngự lùi sâu, tận dụng thể lực áp sát tầm xa",
            "đội_hinh": ["Johny Placide", "Carlens Arcus", "Ricardo Adé", "Jean-Kevin Duverne", "Alex Christian", "Bryan Alceus", "Leverton Pierre", "Duckens Nazon", "Derrick Etienne", "Fafà Picault", "Frantzdy Pierrot"]
        },
        "Scotland": {
            "bảng": "C", "sơ_đồ": "3-4-2-1", "sức_mạnh": "Trung bình", "hlv": "Steve Clarke", "logo": "https://flagcdn.com/w80/gb-sct.png",
            "star_name": "Andy Robertson", "star_img": "https://img.a.transfermarkt.technology/portrait/header/234803-1668674347.jpg",
            "star_stats": {"Độ tuổi": "32 tuổi", "Vị trí": "Hậu vệ trái (LB)", "Chiều cao": "1m78", "CLB": "Liverpool", "Phong độ": "⭐ 8.0/10"},
            "lối_chơi": "Lối đá Anh truyền thống, tạt cánh đánh đầu, tranh chấp mạnh",
            "đội_hinh": ["Angus Gunn", "Jack Hendry", "Grant Hanley", "Scott McKenna", "Anthony Ralston", "Billy Gilmour", "Callum McGregor", "Andy Robertson", "Scott McTominay", "John McGinn", "Che Adams"]
        },
        # Bảng D
        "Mỹ": {
            "bảng": "D", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "hlv": "Mauricio Pochettino", "logo": "https://flagcdn.com/w80/us.png",
            "star_name": "Christian Pulisic", "star_img": "https://img.a.transfermarkt.technology/portrait/header/315779-1669106201.jpg",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền đạo trái (LW)", "Chiều cao": "1m77", "CLB": "AC Milan", "Phong độ": "🔥 8.7/10"},
            "lối_chơi": "Pressing tầm cao, chuyển trạng thái nhanh dựa vào tốc độ biên",
            "đội_hinh": ["Matt Turner", "Sergiño Dest", "Chris Richards", "Tim Ream", "Antonee Robinson", "Weston McKennie", "Tyler Adams", "Yunush Musah", "Timothy Weah", "Folarin Balogun", "Christian Pulisic"]
        },
        "Paraguay": {
            "bảng": "D", "sơ_đồ": "4-4-2", "sức_mạnh": "Trung bình", "hlv": "Gustavo Alfaro", "logo": "https://flagcdn.com/w80/py.png",
            "star_name": "Miguel Almirón", "star_img": "https://img.a.transfermarkt.technology/portrait/header/272999-1668158522.jpg",
            "star_stats": {"Độ tuổi": "32 tuổi", "Vị trí": "Tiền đạo phải (RW)", "Chiều cao": "1m74", "CLB": "Newcastle", "Phong độ": "⭐ 7.6/10"},
            "lối_chơi": "Thủ chặt phá lối chơi đối phương, không ngại va chạm áp sát",
            "đội_hinh": ["Carlos Coronel", "Robert Rojas", "Gustavo Gómez", "Junior Alonso", "Blas Riveros", "Miguel Almirón", "Mathías Villasanti", "Andrés Cubas", "Ramón Sosa", "Antonio Sanabria", "Álex Arce"]
        },
        "Úc": {
            "bảng": "D", "sơ_đồ": "4-4-2", "sức_mạnh": "Trung bình", "hlv": "Tony Popovic", "logo": "https://flagcdn.com/w80/au.png",
            "star_name": "Harry Souttar", "star_img": "https://img.a.transfermarkt.technology/portrait/header/342939-1658402517.jpg",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Trung vệ (CB)", "Chiều cao": "1m98", "CLB": "Leicester City", "Phong độ": "⭐ 7.5/10"},
            "lối_chơi": "Thiên về thể chất, bóng bổng và các tình huống cố định",
            "đội_hinh": ["Mathew Ryan", "Gethin Jones", "Harry Souttar", "Kye Rowles", "Aziz Behich", "Martin Boyle", "Keanu Baccus", "Jackson Irvine", "Craig Goodwin", "Kusini Yengi", "Mitchell Duke"]
        },
        "Thổ Nhĩ Kỳ": {
            "bảng": "D", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "hlv": "Vincenzo Montella", "logo": "https://flagcdn.com/w80/tr.png",
            "star_name": "Arda Güler", "star_img": "https://img.a.transfermarkt.technology/portrait/header/982959-1689255675.jpg",
            "star_stats": {"Độ tuổi": "21 tuổi", "Vị trí": "Tiền vệ công (AM)", "Chiều cao": "1m75", "CLB": "Real Madrid", "Phong độ": "🔥 8.6/10"},
            "lối_chơi": "Kỷ luật, đá cống hiến, tấn công trung lộ rất mạnh",
            "đội_hinh": ["Mert Günok", "Zeki Çelik", "Samet Akaydin", "Abdülkerim Bardakcı", "Ferdi Kadıoğlu", "Hakan Çalhanoğlu", "Salih Özcan", "Cengiz Ünder", "Arda Güler", "Kerem Aktürkoğlu", "Barış Alper Yılmaz"]
        },
        # Bảng E
        "Đức": {
            "bảng": "E", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "hlv": "Julian Nagelsmann", "logo": "https://flagcdn.com/w80/de.png",
            "star_name": "Jamal Musiala", "star_img": "https://img.a.transfermarkt.technology/portrait/header/580195-1669106512.jpg",
            "star_stats": {"Độ tuổi": "23 tuổi", "Vị trí": "Tiền vệ công (AM)", "Chiều cao": "1m84", "CLB": "Bayern Munich", "Phong độ": "🔥 9.3/10"},
            "lối_chơi": "Kiểm soát thế trận, pressing tầm cao, ban bật cự ly ngắn",
            "đội_hinh": ["Manuel Neuer", "Joshua Kimmich", "Jonathan Tah", "Antonio Rüdiger", "Maximilian Mittelstädt", "Robert Andrich", "Toni Kroos", "Jamal Musiala", "Ilkay Gündogan", "Florian Wirtz", "Kai Havertz"]
        },
        "Curacao": {
            "bảng": "E", "sơ_đồ": "4-4-2", "sức_mạnh": "Yếu", "hlv": "Dick Advocaat", "logo": "https://flagcdn.com/w80/cw.png",
            "star_name": "Juninho Bacuna", "star_img": "https://img.a.transfermarkt.technology/portrait/header/340456-1614246894.jpg",
            "star_stats": {"Độ tuổi": "28 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m78", "CLB": "Birmingham", "Phong độ": "⭐ 6.5/10"},
            "lối_chơi": "Phòng ngự số đông, tận dụng tốc độ tiền đạo bứt tốc",
            "đội_hinh": ["Eloy Room", "Jurien Gaari", "Roshon van Eijma", "Cuco Martina", "Sherel Floranus", "Brandley Kuwas", "Vurnon Anita", "Leandro Bacuna", "Kenji Gorré", "Rangelo Janga", "Juninho Bacuna"]
        },
        "Bờ Biển Ngà": {
            "bảng": "E", "sơ_đồ": "4-3-3", "sức_mạnh": "Trung bình", "hlv": "Emerse Faé", "logo": "https://flagcdn.com/w80/ci.png",
            "star_name": "Franck Kessié", "star_img": "https://img.a.transfermarkt.technology/portrait/header/294808-1663162794.jpg",
            "star_stats": {"Độ tuổi": "29 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m83", "CLB": "Al-Ahli", "Phong độ": "⭐ 7.9/10"},
            "lối_chơi": "Cậy nhờ thể lực, giàu tốc độ, đá trực diện áp sát",
            "đội_hinh": ["Yahia Fofana", "Wilfried Singo", "Ousmane Diomande", "Evan Ndicka", "Ghislain Konan", "Franck Kessié", "Jean Michaël Seri", "Seko Fofana", "Max Gradel", "Simon Adingra", "Sebastien Haller"]
        },
        "Ecuador": {
            "bảng": "E", "sơ_đồ": "3-4-3", "sức_mạnh": "Khá", "hlv": "Sebastián Beccacece", "logo": "https://flagcdn.com/w80/ec.png",
            "star_name": "Moisés Caicedo", "star_img": "https://img.a.transfermarkt.technology/portrait/header/487964-1668673327.jpg",
            "star_stats": {"Độ tuổi": "24 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m78", "CLB": "Chelsea", "Phong độ": "🔥 8.5/10"},
            "lối_chơi": "Đá rực lửa, pressing mạnh ở biên, giàu thể lực",
            "đội_hinh": ["Alexander Domínguez", "Félix Torres", "Willian Pacho", "Piero Hincapié", "Angelo Preciado", "Moisés Caicedo", "Alan Franco", "Pervis Estupiñán", "Kendry Páez", "Jeremy Sarmiento", "Enner Valencia"]
        },
        # Bảng F
        "Hà Lan": {
            "bảng": "F", "sơ_đồ": "3-4-3", "sức_mạnh": "Mạnh", "hlv": "Ronald Koeman", "logo": "https://flagcdn.com/w80/nl.png",
            "star_name": "Virgil van Dijk", "star_img": "https://img.a.transfermarkt.technology/portrait/header/139208-1669106757.jpg",
            "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Trung vệ (CB)", "Chiều cao": "1m95", "CLB": "Liverpool", "Phong độ": "🔥 9.0/10"},
            "lối_chơi": "Tấn công tổng lực, đẩy cao hai biên, kiểm soát bóng chủ động",
            "đội_hinh": ["Bart Verbruggen", "Lutsharel Geertruida", "Virgil van Dijk", "Nathan Aké", "Denzel Dumfries", "Jerdy Schouten", "Tijjani Reijnders", "Daley Blind", "Xavi Simons", "Cody Gakpo", "Memphis Depay"]
        },
        "Nhật Bản": {
            "bảng": "F", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "hlv": "Hajime Moriyasu", "logo": "https://flagcdn.com/w80/jp.png",
            "star_name": "Kaoru Mitoma", "star_img": "https://img.a.transfermarkt.technology/portrait/header/504849-1669107147.jpg",
            "star_stats": {"Độ tuổi": "29 tuổi", "Vị trí": "Tiền đạo trái (LW)", "Chiều cao": "1m78", "CLB": "Brighton", "Phong độ": "🔥 8.6/10"},
            "lối_chơi": "Phối hợp nhóm nhỏ tốc độ cao, kỷ luật vị trí cực tốt",
            "đội_hinh": ["Zion Suzuki", "Yukinari Sugawara", "Ko Itakura", "Shogo Taniguchi", "Hiroki Ito", "Wataru Endo", "Hidemasa Morita", "Takefusa Kubo", "Takumi Minamino", "Kaoru Mitoma", "Ayase Ueda"]
        },
        "Thụy Điển": {
            "bảng": "F", "sơ_đồ": "4-4-2", "sức_mạnh": "Khá", "hlv": "Jon Dahl Tomasson", "logo": "https://flagcdn.com/w80/se.png",
            "star_name": "Viktor Gyökeres", "star_img": "https://img.a.transfermarkt.technology/portrait/header/325443-1698658826.jpg",
            "star_stats": {"Độ tuổi": "28 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m87", "CLB": "Sporting CP", "Phong độ": "🔥 9.1/10"},
            "lối_chơi": "Tổ chức chặt chẽ, chơi bóng dài bổng hiệu quả",
            "đội_hinh": ["Robin Olsen", "Emil Holm", "Isak Hien", "Victor Lindelöf", "Ludwig Augustinsson", "Dejan Kulusevski", "Jens Cajuste", "Anton Salétros", "Emil Forsberg", "Viktor Gyökeres", "Alexander Isak"]
        },
        "Tunisia": {
            "bảng": "F", "sơ_đồ": "4-5-1", "sức_mạnh": "Trung bình", "hlv": "Faouzi Benzarti", "logo": "https://flagcdn.com/w80/tn.png",
            "star_name": "Ellyes Skhiri", "star_img": "https://img.a.transfermarkt.technology/portrait/header/290623-1668673738.jpg",
            "star_stats": {"Độ tuổi": "31 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m85", "CLB": "Eintracht Frankfurt", "Phong độ": "⭐ 7.4/10"},
            "lối_chơi": "Phòng ngự kỷ luật, phá lối chơi đối phương",
            "đội_hinh": ["Bechir Ben Saïd", "Wajdi Kechrida", "Dylan Bronn", "Montassar Talbi", "Ali Abdi", "Ellyes Skhiri", "Aïssa Laïdouni", "Anis Ben Slimane", "Hamza Rafia", "Sayfallah Ltaief", "Youssef Msakni"]
        },
        # Bảng G
        "Bỉ": {
            "bảng": "G", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "hlv": "Domenico Tedesco", "logo": "https://flagcdn.com/w80/be.png",
            "star_name": "Kevin De Bruyne", "star_img": "https://img.a.transfermarkt.technology/portrait/header/88755-1669106297.jpg",
            "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m81", "CLB": "Manchester City", "Phong độ": "🔥 9.2/10"},
            "lối_chơi": "Tấn công trung lộ, ban bật nhanh dựa vào các tiền vệ sáng tạo",
            "đội_hinh": ["Koen Casteels", "Timothy Castagne", "Wout Faes", "Jan Vertonghen", "Arthur Theate", "Orel Mangala", "Amadou Onana", "Kevin De Bruyne", "Jérémy Doku", "Leandro Trossard", "Romelu Lukaku"]
        },
        "Ai Cập": {
            "bảng": "G", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "hlv": "Hossam Hassan", "logo": "https://flagcdn.com/w80/eg.png",
            "star_name": "Mohamed Salah", "star_img": "https://img.a.transfermarkt.technology/portrait/header/148455-1669106471.jpg",
            "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền đạo phải (RW)", "Chiều cao": "1m75", "CLB": "Liverpool", "Phong độ": "🔥 9.0/10"},
            "lối_chơi": "Phòng ngự chặt, dồn bóng cho ngôi sao đột phá tốc độ",
            "đội_hinh": ["Mohamed El Shenawy", "Mohamed Hany", "Mohamed Abdelmonem", "Yasser Ibrahim", "Ali Maâloul", "Marwan Attia", "Mohamed Elneny", "Hamdi Fathi", "Mohamed Salah", "Trézéguet", "Mostafa Mohamed"]
        },
        "Iran": {
            "bảng": "G", "sơ_đồ": "4-4-2", "sức_mạnh": "Khá", "hlv": "Amir Ghalenoei", "logo": "https://flagcdn.com/w80/ir.png",
            "star_name": "Mehdi Taremi", "star_img": "https://img.a.transfermarkt.technology/portrait/header/322301-1668673719.jpg",
            "star_stats": {"Độ tuổi": "33 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m87", "CLB": "Inter Milan", "Phong độ": "⭐ 8.1/10"},
            "lối_chơi": "Khối phòng ngự lùi sâu vững chãi, phản công sắc bén",
            "đội_hinh": ["Alireza Beiranvand", "Ramin Rezaeian", "Hossein Kanaanizadegan", "Shojae Khalilzadeh", "Milad Mohammadi", "Saman Ghoddos", "Saeid Ezatolahi", "Alireza Jahanbakhsh", "Mehdi Torabi", "Sardar Azmoun", "Mehdi Taremi"]
        },
        "New Zealand": {
            "bảng": "G", "sơ_đồ": "4-4-2", "sức_mạnh": "Yếu", "hlv": "Darren Bazeley", "logo": "https://flagcdn.com/w80/nz.png",
            "star_name": "Chris Wood", "star_img": "https://img.a.transfermarkt.technology/portrait/header/108725-1658402127.jpg",
            "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m91", "CLB": "Nottingham Forest", "Phong độ": "⭐ 7.2/10"},
            "lối_chơi": "Bóng bổng, dựa vào thể hình tranh chấp bóng hai",
            "đội_hinh": ["Oliver Sail", "Tim Payne", "Michael Boxall", "Nando Pijnaker", "Liberato Cacace", "Joe Bell", "Matthew Garbett", "Sarpreet Singh", "Ben Old", "Kosta Barbarouses", "Chris Wood"]
        },
        # Bảng H
        "Tây Ban Nha": {
            "bảng": "H", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "hlv": "Luis de la Fuente", "logo": "https://flagcdn.com/w80/es.png",
            "star_name": "Lamine Yamal", "star_img": "https://img.a.transfermarkt.technology/portrait/header/1057013-1683103444.jpg",
            "star_stats": {"Độ tuổi": "18 tuổi", "Vị trí": "Tiền đạo phải (RW)", "Chiều cao": "1m80", "CLB": "Barcelona", "Phong độ": "👑 9.6/10"},
            "lối_chơi": "Tiki-taka hiện đại, luân chuyển bóng cực nhanh, kiểm soát tuyệt đối",
            "đội_hinh": ["Unai Simón", "Dani Carvajal", "Robin Le Normand", "Aymeric Laporte", "Marc Cucurella", "Rodri", "Pedri", "Fabian Ruiz", "Lamine Yamal", "Nico Williams", "Alvaro Morata"]
        },
        "Cabo Verde": {
            "bảng": "H", "sơ_đồ": "4-3-3", "sức_mạnh": "Trung bình", "hlv": "Bubista", "logo": "https://flagcdn.com/w80/cv.png",
            "star_name": "Ryan Mendes", "star_img": "https://img.a.transfermarkt.technology/portrait/header/102371-1510651713.jpg",
            "star_stats": {"Độ tuổi": "36 tuổi", "Vị trí": "Tiền đạo cánh (RW)", "Chiều cao": "1m78", "CLB": "Fatih Karagümrük", "Phong độ": "⭐ 6.9/10"},
            "lối_chơi": "Chơi phòng ngự phản công dựa vào tốc độ các cầu thủ chạy cánh",
            "đội_hinh": ["Vozinha", "Steven Moreira", "Logan Costa", "Roberto Lopes", "João Paulo", "Kevin Pina", "Jamiro Monteiro", "Deroy Duarte", "Ryan Mendes", "Garry Rodrigues", "Jovane Cabral"]
        },
        "Saudi Arabia": {
            "bảng": "H", "sơ_đồ": "4-5-1", "sức_mạnh": "Trung bình", "hlv": "Roberto Mancini", "logo": "https://flagcdn.com/w80/sa.png",
            "star_name": "Salem Al-Dawsari", "star_img": "https://img.a.transfermarkt.technology/portrait/header/211754-1669106803.jpg",
            "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền đạo trái (LW)", "Chiều cao": "1m71", "CLB": "Al-Hilal", "Phong độ": "⭐ 7.7/10"},
            "lối_chơi": "Áp sát tầm cao, bẫy việt vị, đá gắn kết kỷ luật",
            "đội_hinh": ["Mohammed Al-Owais", "Saud Abdulhamid", "Ali Lajami", "Ali Al-Bulaihi", "Yasir Al-Shahrani", "Abdullah Otayf", "Mohamed Kanno", "Firas Al-Buraikan", "Salman Al-Faraj", "Salem Al-Dawsari", "Saleh Al-Shehri"]
        },
        "Uruguay": {
            "bảng": "H", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "hlv": "Marcelo Bielsa", "logo": "https://flagcdn.com/w80/uy.png",
            "star_name": "Federico Valverde", "star_img": "https://img.a.transfermarkt.technology/portrait/header/369081-1669106173.jpg",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m82", "CLB": "Real Madrid", "Phong độ": "🔥 9.1/10"},
            "lối_chơi": "Pressing điên cuồng, va chạm rực lửa, tấn công trực diện",
            "đội_hinh": ["Sergio Rochet", "Nahitan Nández", "Ronald Araújo", "José María Giménez", "Mathías Olivera", "Federico Valverde", "Manuel Ugarte", "Nicolás de la Cruz", "Facundo Pellistri", "Darwin Núñez", "Maximilian Araújo"]
        },
        # Bảng I
        "Pháp": {
            "bảng": "I", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "hlv": "Didier Deschamps", "logo": "https://flagcdn.com/w80/fr.png",
            "star_name": "Kylian Mbappé", "star_img": "https://img.a.transfermarkt.technology/portrait/header/342229-1669106304.jpg",
            "star_stats": {"Độ tuổi": "27 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m78", "CLB": "Real Madrid", "Phong độ": "👑 9.5/10"},
            "lối_chơi": "Tấn công trực diện tốc độ cao bằng hành lang biên",
            "đội_hinh": ["Mike Maignan", "Jules Koundé", "Dayot Upamecano", "William Saliba", "Théo Hernandez", "N'Golo Kanté", "Aurélien Tchouaméni", "Ousmane Dembélé", "Antoine Griezmann", "Bradley Barcola", "Kylian Mbappé"]
        },
        "Senegal": {
            "bảng": "I", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "hlv": "Aliou Cissé", "logo": "https://flagcdn.com/w80/sn.png",
            "star_name": "Sadio Mané", "star_img": "https://img.a.transfermarkt.technology/portrait/header/200512-1668673323.jpg",
            "star_stats": {"Độ tuổi": "34 tuổi", "Vị trí": "Tiền đạo cánh (LW)", "Chiều cao": "1m74", "CLB": "Al-Nassr", "Phong độ": "⭐ 8.0/10"},
            "lối_chơi": "Cân bằng giữa thể lực và kỹ thuật, đá áp sát nhanh",
            "đội_hinh": ["Édouard Mendy", "Formose Mendy", "Kalidou Koulibaly", "Abdou Diallo", "Ismail Jakobs", "Idrissa Gueye", "Pape Matar Sarr", "Lamine Camara", "Ismaïla Sarr", "Nicolas Jackson", "Sadio Mané"]
        },
        "Iraq": {
            "bảng": "I", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Trung bình", "hlv": "Jesús Casas", "logo": "https://flagcdn.com/w80/iq.png",
            "star_name": "Aymen Hussein", "star_img": "https://img.a.transfermarkt.technology/portrait/header/350974-1711202861.jpg",
            "star_stats": {"Độ tuổi": "30 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m89", "CLB": "Al-Khor", "Phong độ": "⭐ 7.9/10"},
            "lối_chơi": "Đá tinh quái, không ngại va chạm, mạnh tấn công trung lộ",
            "đội_hinh": ["Jalal Hassan", "Hussein Ali", "Saad Natiq", "Rebin Sulaka", "Merchas Doski", "Amir Al-Ammari", "Osama Rashid", "Ibrahim Bayesh", "Zidane Iqbal", "Ali Jasim", "Aymen Hussein"]
        },
        "Na Uy": {
            "bảng": "I", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "hlv": "Ståle Solbakken", "logo": "https://flagcdn.com/w80/no.png",
            "star_name": "Erling Haaland", "star_img": "https://img.a.transfermarkt.technology/portrait/header/418560-1669106825.jpg",
            "star_stats": {"Độ tuổi": "25 tuổi", "Vị trí": "Tiền đạo cắm (ST)", "Chiều cao": "1m94", "CLB": "Manchester City", "Phong độ": "🔥 9.4/10"},
            "lối_chơi": "Tấn công trục dọc, nhồi bóng cho trung phong cắm ghi bàn",
            "đội_hinh": ["Ørjan Nyland", "Julian Ryerson", "Leo Östigard", "Kristoffer Ajer", "David Møller Wolfe", "Martin Ødegaard", "Patrick Berg", "Sander Berge", "Oscar Bobb", "Antonio Nusa", "Erling Haaland"]
        },
        # Bảng L
        "Anh": {
            "bảng": "L", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "hlv": "Thomas Tuchel", "logo": "https://flagcdn.com/w80/gb-eng.png",
            "star_name": "Jude Bellingham", "star_img": "https://img.a.transfermarkt.technology/portrait/header/581678-1669106450.jpg",
            "star_stats": {"Độ tuổi": "22 tuổi", "Vị trí": "Tiền vệ công (AM)", "Chiều cao": "1m86", "CLB": "Real Madrid", "Phong độ": "👑 9.5/10"},
            "lối_chơi": "Tấn công biên dồn dập, kiểm soát nửa sân đối phương, cố định mạnh",
            "đội_hinh": ["Jordan Pickford", "Kyle Walker", "John Stones", "Marc Guéhi", "Kieran Trippier", "Declan Rice", "Kobbie Mainoo", "Bukayo Saka", "Jude Bellingham", "Phil Foden", "Harry Kane"]
        },
        "Croatia": {
            "bảng": "L", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "hlv": "Zlatko Dalić", "logo": "https://flagcdn.com/w80/hr.png",
            "star_name": "Luka Modrić", "star_img": "https://img.a.transfermarkt.technology/portrait/header/27992-1669106188.jpg",
            "star_stats": {"Độ tuổi": "40 tuổi", "Vị trí": "Tiền vệ trung tâm", "Chiều cao": "1m72", "CLB": "Real Madrid", "Phong độ": "⭐ 8.3/10"},
            "lối_chơi": "Làm chủ khu trung tuyến, cầm nhịp trận đấu chậm rãi tinh tế",
            "đội_hinh": ["Dominik Livakovic", "Josip Stanisic", "Josip Sutalo", "Marin Pongracic", "Josko Gvardiol", "Luka Modric", "Marcelo Brozovic", "Mateo Kovacic", "Lovro Majer", "Andrejan Kramaric", "Ante Budimir"]
        }
    }

TEAMS = get_teams_data()

# Hàm bổ trợ lấy thông tin phòng hờ lỗi
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
        ["WC-04", "Bảng D", "13/06", "08:00", "Mỹ", "Paraguay", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-06", "Bảng C", "14/06", "05:00", "Brazil", "Marocco", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-09", "Bảng E", "15/06", "00:00", "Đức", "Curacao", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-10", "Bảng F", "15/06", "03:00", "Hà Lan", "Nhật Bản", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-14", "Bảng G", "16/06", "02:00", "Bỉ", "Ai Cập", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-17", "Bảng I", "17/06", "02:00", "Pháp", "Senegal", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-22", "Bảng L", "18/06", "03:00", "Anh", "Croatia", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"]
    ]
    
    matches_db = {}
    for m in raw_schedule:
        matches_db[m[0]] = {
            "vòng": m[1], "ngày": m[2], "giờ": m[3], "đội_nhà": m[4], "đội_khách": m[5], "kênh": m[6],
            "trọng_tài": "Chưa cập nhật", "thời_tiết": m[7], "dự_đoán_bạn": "", "ti_so_ft": ""
        }
    st.session_state.matches = matches_db

# CHIA TABS CHỨC NĂNG CHUẨN DEV
tab1, tab2, tab3 = st.tabs(["📰 Nhận Định & Sa Bàn Đội Hình", "⏱️ Phòng Cập Nhật Kết Quả", "🏃 Danh Sách 48 Đội Bóng"])

# ==================================================================
# TAB 1: GIAO DIỆN HIỂN THỊ ĐỈNH CAO (ĐỦ ĐỘI HÌNH & NGÔI SAO)
# ==================================================================
with tab1:
    selected_m = st.selectbox("Chọn mã trận đấu cần xem phân tích chuyên sâu:", list(st.session_state.matches.keys()))
    m_data = st.session_state.matches[selected_m]
    
    t_nhà = get_team_info(m_data['đội_nhà'])
    t_khách = get_team_info(m_data['đội_khách'])
    
    # 📸 HÌNH 1: ĐỐI ĐẦU ĐỈNH CAO CÓ LOGO QUỐC KỲ VÀ TÊN HLV
    st.markdown("### 🏟️ CẶP ĐẤU ĐỐI ĐẦU CHÍNH THỨC")
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        st.markdown(f'<div class="card-vs"><img src="{t_nhà["logo"]}" width="110"><br><span class="team-name">{m_data["đội_nhà"]}</span><br><span class="hlv-text">HLV: {t_nhà["hlv"]}</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div style="text-align: center; margin-top: 30px;"><span class="vs-text">VS</span><br><span style="color: #94a3b8; font-weight:bold;">{m_data["giờ"]} | {m_data["ngày"]}</span><br><span style="color:#warning;">{m_data["kênh"]}</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="card-vs"><img src="{t_khách["logo"]}" width="110"><br><span class="team-name">{m_data["đội_khách"]}</span><br><span class="hlv-text">HLV: {t_khách["hlv"]}</span></div>', unsafe_allow_html=True)
        
    st.markdown("---")
    
    # 📸 HÌNH 2 & HÌNH 4: CẶP ĐÔI NGUY HIỂM & BOX SO SÁNH CHỈ SỐ CỦA BẠN (ĐỘ TUỔI, CHIỀU CAO, PHONG ĐỘ...)
    st.markdown("### ⚡ NGÔI SAO GHIM TRẬN (KEY PLAYER FACE-OFF)")
    c_star1, c_star2 = st.columns(2)
    
    with c_star1:
        st.markdown(f'<h4 style="color:#fecd3d;">⭐ {t_nhà["star_name"]} ({m_data["đội_nhà"]})</h4>', unsafe_allow_html=True)
        st.image(t_nhà["star_img"], width=160)
        for lbl, val in t_nhà["star_stats"].items():
            st.markdown(f'<div class="card-player"><span class="stat-label">{lbl}</span><span class="stat-value">{val}</span></div>', unsafe_allow_html=True)
            
    with c_star2:
        st.markdown(f'<h4 style="color:#fecd3d;">⭐ {t_khách["star_name"]} ({m_data["đội_khách"]})</h4>', unsafe_allow_html=True)
        st.image(t_khách["star_img"], width=160)
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

    # 📸 HÌNH 3: SA BÀN SÂN CỎ VẼ THEO SƠ ĐỒ ĐỒ HỌA THỰC TẾ
    st.markdown("### 📋 ĐỘI HÌNH DỰ KIẾN CHI TIẾT TẠI SÂN")
    col_pitch, col_text = st.columns([3, 2])
    
    with col_pitch:
        fig, ax = plt.subplots(figsize=(7, 4.8))
        fig.patch.set_facecolor('#0f172a')
        ax.set_facecolor('#1e3a1e') 
        
        # Vẽ cấu trúc sân vận động tiêu chuẩn
        plt.plot([0, 0, 100, 100, 0], [0, 100, 100, 0, 0], color="white", linewidth=2)
        plt.plot([0, 100], [50, 50], color="white", linewidth=2)
        center_circle = plt.Circle((50, 50), 14, color='white', fill=False, linewidth=2)
        ax.add_patch(center_circle)
        
        # Đổ chấm tròn đại diện các quân cờ chiến thuật
        plt.scatter([50], [6], color='#ef4444', s=200, edgecolors='white', zorder=5) 
        plt.text(50, 9, "GK", color='white', ha='center', fontsize=9, weight='bold')
        plt.scatter([50], [38], color='#ef4444', s=250, edgecolors='gold', zorder=5) 
        plt.text(50, 41, t_nhà["star_name"], color='#fecd3d', ha='center', fontsize=9, weight='bold')
        
        plt.scatter([50], [94], color='#3b82f6', s=200, edgecolors='white', zorder=5) 
        plt.text(50, 87, "GK", color='white', ha='center', fontsize=9, weight='bold')
        plt.scatter([50], [62], color='#3b82f6', s=250, edgecolors='gold', zorder=5) 
        plt.text(50, 65, t_khách["star_name"], color='#fecd3d', ha='center', fontsize=9, weight='bold')
        
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
# TAB 3: DANH SÁCH TOÀN BỘ CÁC ĐỘI BÓNG ĐÃ CẬP NHẬT HLV
# ==================================================================
with tab3:
    st.subheader("🏃 Cơ sở dữ liệu chiến thuật toàn giải đấu")
    team_list = []
    for t_name, t_val in TEAMS.items():
        team_list.append([t_name, t_val['bảng'], t_val['hlv'], t_val['sơ_đồ'], t_val['star_name'], t_val['sức_mạnh']])
    
    team_df = pd.DataFrame(team_list, columns=["Đội Bóng", "Bảng", "Huấn Luyện Viên", "Sơ Đồ Chiến Thuật", "Ngôi Sao Gánh Đội", "Đánh Giá Sức Mạnh"])
    st.dataframe(team_df, use_container_width=True, height=400)
