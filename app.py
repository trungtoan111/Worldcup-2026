import streamlit as st
import pandas as pd

# Thiết lập cấu hình trang web
st.set_page_config(page_title="World Cup 2026 - Realtime AI Dashboard", layout="wide")

# ------------------------------------------------------------------
# 1. DATABASE CHUẨN CHỈNH: ĐỦ ĐỘI BÓNG, HLV VÀ 11 CẦU THỦ DỰ KIẾN
# ------------------------------------------------------------------
@st.cache_data
def get_teams_data():
    return {
        # Bảng A
        "Mexico": {
            "bảng": "A", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "ngôi_sao": "Santiago Giménez", "hlv": "Javier Aguirre",
            "lối_chơi": "Kiểm soát bóng ngắn, áp đặt thế trận, tấn công biên tốc độ",
            "đội_hinh": ["Guillermo Ochoa", "Jorge Sánchez", "César Montes", "Johan Vásquez", "Jesús Gallardo", "Edson Álvarez", "Luis Chávez", "Orbelín Pineda", "Roberto Alvarado", "Julián Quiñones", "Santiago Giménez"]
        },
        "Nam Phi": {
            "bảng": "A", "sơ_đồ": "4-4-2", "sức_mạnh": "Trung bình", "ngôi_sao": "Percy Tau", "hlv": "Hugo Broos",
            "lối_chơi": "Phòng ngự số đông, lùi sâu đội hình, phản công bóng dài",
            "đội_hinh": ["Ronwen Williams", "Khuliso Mudau", "Ime Okon", "Mbekezeli Mbokazi", "Aubrey Modiba", "Thalente Mbatha", "Yaya Sithole", "Teboho Mokoena", "Oswin Appollis", "Lyle Foster", "Percy Tau"]
        },
        "Hàn Quốc": {
            "bảng": "A", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "ngôi_sao": "Son Heung-min", "hlv": "Hong Myung-bo",
            "lối_chơi": "Đá giãn biên, chồng cánh tốc độ cao, áp sát pressing liên tục",
            "đội_hinh": ["Jo Hyeon-woo", "Kim Min-jae", "Kim Young-gwon", "Kim Jin-su", "Seol Young-woo", "Hwang In-beom", "Park Yong-woo", "Lee Kang-in", "Lee Jae-sung", "Hwang Hee-chan", "Son Heung-min"]
        },
        "CH Séc": {
            "bảng": "A", "sơ_đồ": "3-4-2-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Tomas Soucek", "hlv": "Ivan Hasek",
            "lối_chơi": "Kỷ luật thép, va chạm rực lửa, mạnh không chiến và cố định",
            "đội_hinh": ["Jindrich Stanek", "Tomas Holes", "Robin Hranac", "Ladislav Krejci", "Vladimir Coufal", "Tomas Soucek", "Lukas Provod", "David Doudera", "Vaclav Cerny", "Patrik Schick", "Jan Kuchta"]
        },
        "Argentina": {
            "bảng": "A", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Lionel Messi", "hlv": "Lionel Scaloni",
            "lối_chơi": "Kiểm soát bóng ngắn, luân chuyển bóng nhanh, đột biến trung lộ",
            "đội_hinh": ["Emi Martínez", "Nahuel Molina", "Cristian Romero", "Nicolás Otamendi", "Nicolás Tagliafico", "Rodrigo De Paul", "Enzo Fernández", "Alexis Mac Allister", "Lionel Messi", "Julián Álvarez", "Ángel Di María"]
        },
        "Algeria": {
            "bảng": "A", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "ngôi_sao": "Riyad Mahrez", "hlv": "Vladimir Petkovic",
            "lối_chơi": "Kỹ thuật cá nhân tốt, chuộng đá biên và ban bật ngắn",
            "đội_hinh": ["Anthony Mandrea", "Youcef Atal", "Aissa Mandi", "Ramy Bensebaini", "Rayyan Aït-Nouri", "Nabil Bentaleb", "Ismaël Bennacer", "Riyad Mahrez", "Houssem Aouar", "Saïd Benrahma", "Baghdad Bounedjah"]
        },
        # Bảng B
        "Canada": {
            "bảng": "B", "sơ_đồ": "4-4-2", "sức_mạnh": "Trung bình", "ngôi_sao": "Alphonso Davies", "hlv": "Jesse Marsch",
            "lối_chơi": "Tấn công biên dựa vào tốc độ, chuyển trạng thái nhanh",
            "đội_hinh": ["Maxime Crépeau", "Alistair Johnston", "Moïse Bombito", "Derek Cornelius", "Alphonso Davies", "Tajon Buchanan", "Stephen Eustáquio", "Ismaël Koné", "Liam Millar", "Jonathan David", "Cyle Larin"]
        },
        "Bosnia": {
            "bảng": "B", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Edin Dzeko", "hlv": "Sergej Barbarez",
            "lối_chơi": "Chậm rãi, chắc chắn khu trung tuyến, tận dụng bóng bổng",
            "đội_hinh": ["Kenan Piric", "Anel Ahmedhodzic", "Dennis Hadzikadunic", "Sead Kolasinac", "Jusuf Gazibegovic", "Rade Krunic", "Benjamin Tahirovic", "Haris Hajradinovic", "Miroslav Stevanovic", "Ermedin Demirovic", "Edin Dzeko"]
        },
        "Qatar": {
            "bảng": "B", "sơ_đồ": "5-3-2", "sức_mạnh": "Trung bình", "ngôi_sao": "Akram Afif", "hlv": "Tintín Márquez",
            "lối_chơi": "Phòng ngự phản công, phối hợp nhỏ nhóm trung lộ",
            "đội_hinh": ["Meshaal Barsham", "Pedro Miguel", "Al-Mahdi Ali", "Lucas Mendes", "Tarek Salman", "Homam Ahmed", "Hassan Al-Haydos", "Ahmed Fathy", "Jassem Gaber", "Almoez Ali", "Akram Afif"]
        },
        "Thụy Sĩ": {
            "bảng": "B", "sơ_đồ": "3-4-2-1", "sức_mạnh": "Khá", "ngôi_sao": "Granit Xhaka", "hlv": "Murat Yakin",
            "lối_chơi": "Kỷ luật cao, tổ chức đội hình khoa học, bọc lót tốt",
            "đội_hinh": ["Yann Sommer", "Manuel Akanji", "Nico Elvedi", "Ricardo Rodríguez", "Silvan Widmer", "Remo Freuler", "Granit Xhaka", "Dan Ndoye", "Xherdan Shaqiri", "Ruben Vargas", "Breel Embolo"]
        },
        # Bảng C
        "Brazil": {
            "bảng": "C", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Vinicius Jr", "hlv": "Dorival Júnior",
            "lối_chơi": "Tấn công rực lửa, áp đặt thế trận kỹ thuật cá nhân đỉnh cao",
            "đội_hinh": ["Alisson Becker", "Danilo", "Marquinhos", "Gabriel Magalhães", "Wendell", "Bruno Guimarães", "Douglas Luiz", "Lucas Paquetá", "Rodrygo", "Raphinha", "Vinicius Jr"]
        },
        "Marocco": {
            "bảng": "C", "sơ_đồ": "4-1-4-1", "sức_mạnh": "Khá", "ngôi_sao": "Hakimi", "hlv": "Walid Regragui",
            "lối_chơi": "Phòng ngự khối trung bình (Mid-block), kỷ luật thép phản công",
            "đội_hinh": ["Yassine Bounou", "Achraf Hakimi", "Nayef Aguerd", "Romain Saïss", "Yahia Attiyat Allah", "Sofyan Amrabat", "Azzedine Ounahi", "Selim Amallah", "Hakim Ziyech", "Amine Adli", "Youssef En-Nesyri"]
        },
        "Haiti": {
            "bảng": "C", "sơ_đồ": "4-5-1", "sức_mạnh": "Yếu", "ngôi_sao": "Frantzdy Pierrot", "hlv": "Sébastien Migné",
            "lối_chơi": "Phòng ngự lùi sâu, tận dụng thể lực áp sát tầm xa",
            "đội_hinh": ["Johny Placide", "Carlens Arcus", "Ricardo Adé", "Jean-Kevin Duverne", "Alex Christian", "Bryan Alceus", "Leverton Pierre", "Duckens Nazon", "Derrick Etienne", "Fafà Picault", "Frantzdy Pierrot"]
        },
        "Scotland": {
            "bảng": "C", "sơ_đồ": "3-4-2-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Andy Robertson", "hlv": "Steve Clarke",
            "lối_chơi": "Lối đá Anh truyền thống, tạt cánh đánh đầu, tranh chấp mạnh",
            "đội_hinh": ["Angus Gunn", "Jack Hendry", "Grant Hanley", "Scott McKenna", "Anthony Ralston", "Billy Gilmour", "Callum McGregor", "Andy Robertson", "Scott McTominay", "John McGinn", "Che Adams"]
        },
        # Bảng D
        "Mỹ": {
            "bảng": "D", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "ngôi_sao": "Pulisic", "hlv": "Mauricio Pochettino",
            "lối_chơi": "Pressing tầm cao, chuyển trạng thái nhanh dựa vào tốc độ biên",
            "đội_hinh": ["Matt Turner", "Sergiño Dest", "Chris Richards", "Tim Ream", "Antonee Robinson", "Weston McKennie", "Tyler Adams", "Yunush Musah", "Timothy Weah", "Folarin Balogun", "Christian Pulisic"]
        },
        "Paraguay": {
            "bảng": "D", "sơ_đồ": "4-4-2", "sức_mạnh": "Trung bình", "ngôi_sao": "Almirón", "hlv": "Gustavo Alfaro",
            "lối_chơi": "Thủ chặt phá lối chơi đối phương, không ngại va chạm áp sát",
            "đội_hinh": ["Carlos Coronel", "Robert Rojas", "Gustavo Gómez", "Junior Alonso", "Blas Riveros", "Miguel Almirón", "Mathías Villasanti", "Andrés Cubas", "Ramón Sosa", "Antonio Sanabria", "Álex Arce"]
        },
        "Úc": {
            "bảng": "D", "sơ_đồ": "4-4-2", "sức_mạnh": "Trung bình", "ngôi_sao": "Harry Souttar", "hlv": "Tony Popovic",
            "lối_chơi": "Thiên về thể chất, bóng bổng và các tình huống cố định",
            "đội_hinh": ["Mathew Ryan", "Gethin Jones", "Harry Souttar", "Kye Rowles", "Aziz Behich", "Martin Boyle", "Keanu Baccus", "Jackson Irvine", "Craig Goodwin", "Kusini Yengi", "Mitchell Duke"]
        },
        "Thổ Nhĩ Kỳ": {
            "bảng": "D", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "ngôi_sao": "Arda Güler", "hlv": "Vincenzo Montella",
            "lối_chơi": "Kỷ luật, đá cống hiến, tấn công trung lộ rất mạnh",
            "đội_hinh": ["Mert Günok", "Zeki Çelik", "Samet Akaydin", "Abdülkerim Bardakcı", "Ferdi Kadıoğlu", "Hakan Çalhanoğlu", "Salih Özcan", "Cengiz Ünder", "Arda Güler", "Kerem Aktürkoğlu", "Barış Alper Yılmaz"]
        },
        # Bảng E
        "Đức": {
            "bảng": "E", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "ngôi_sao": "Jamal Musiala", "hlv": "Julian Nagelsmann",
            "lối_chơi": "Kiểm soát thế trận, pressing tầm cao, ban bật cự ly ngắn",
            "đội_hinh": ["Manuel Neuer", "Joshua Kimmich", "Jonathan Tah", "Antonio Rüdiger", "Maximilian Mittelstädt", "Robert Andrich", "Toni Kroos", "Jamal Musiala", "Ilkay Gündogan", "Florian Wirtz", "Kai Havertz"]
        },
        "Curacao": {
            "bảng": "E", "sơ_đồ": "4-4-2", "sức_mạnh": "Yếu", "ngôi_sao": "Juninho Bacuna", "hlv": "Dick Advocaat",
            "lối_chơi": "Phòng ngự số đông, tận dụng tốc độ tiền đạo bứt tốc",
            "đội_hinh": ["Eloy Room", "Jurien Gaari", "Roshon van Eijma", "Cuco Martina", "Sherel Floranus", "Brandley Kuwas", "Vurnon Anita", "Leandro Bacuna", "Kenji Gorré", "Rangelo Janga", "Juninho Bacuna"]
        },
        "Bờ Biển Ngà": {
            "bảng": "E", "sơ_đồ": "4-3-3", "sức_mạnh": "Trung bình", "ngôi_sao": "Franck Kessié", "hlv": "Emerse Faé",
            "lối_chơi": "Cậy nhờ thể lực, giàu tốc độ, đá trực diện áp sát",
            "đội_hinh": ["Yahia Fofana", "Wilfried Singo", "Ousmane Diomande", "Evan Ndicka", "Ghislain Konan", "Franck Kessié", "Jean Michaël Seri", "Seko Fofana", "Max Gradel", "Simon Adingra", "Sebastien Haller"]
        },
        "Ecuador": {
            "bảng": "E", "sơ_đồ": "3-4-3", "sức_mạnh": "Khá", "ngôi_sao": "Moisés Caicedo", "hlv": "Sebastián Beccacece",
            "lối_chơi": "Đá rực lửa, pressing mạnh ở biên, giàu thể lực",
            "đội_hinh": ["Alexander Domínguez", "Félix Torres", "Willian Pacho", "Piero Hincapié", "Angelo Preciado", "Moisés Caicedo", "Alan Franco", "Pervis Estupiñán", "Kendry Páez", "Jeremy Sarmiento", "Enner Valencia"]
        },
        # Bảng F
        "Hà Lan": {
            "bảng": "F", "sơ_đồ": "3-4-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Virgil van Dijk", "hlv": "Ronald Koeman",
            "lối_chơi": "Tấn công tổng lực, đẩy cao hai biên, kiểm soát bóng chủ động",
            "đội_hinh": ["Bart Verbruggen", "Lutsharel Geertruida", "Virgil van Dijk", "Nathan Aké", "Denzel Dumfries", "Jerdy Schouten", "Tijjani Reijnders", "Daley Blind", "Xavi Simons", "Cody Gakpo", "Memphis Depay"]
        },
        "Nhật Bản": {
            "bảng": "F", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Khá", "ngôi_sao": "Kaoru Mitoma", "hlv": "Hajime Moriyasu",
            "lối_chơi": "Phối hợp nhóm nhỏ tốc độ cao, kỷ luật vị trí cực tốt",
            "đội_hinh": ["Zion Suzuki", "Yukinari Sugawara", "Ko Itakura", "Shogo Taniguchi", "Hiroki Ito", "Wataru Endo", "Hidemasa Morita", "Takefusa Kubo", "Takumi Minamino", "Kaoru Mitoma", "Ayase Ueda"]
        },
        "Thụy Điển": {
            "bảng": "F", "sơ_đồ": "4-4-2", "sức_mạnh": "Khá", "ngôi_sao": "Alexander Isak", "hlv": "Jon Dahl Tomasson",
            "lối_chơi": "Tổ chức chặt chẽ, chơi bóng dài bổng hiệu quả",
            "đội_hinh": ["Robin Olsen", "Emil Holm", "Isak Hien", "Victor Lindelöf", "Ludwig Augustinsson", "Dejan Kulusevski", "Jens Cajuste", "Anton Salétros", "Emil Forsberg", "Viktor Gyökeres", "Alexander Isak"]
        },
        "Tunisia": {
            "bảng": "F", "sơ_đồ": "4-5-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Ellyes Skhiri", "hlv": "Faouzi Benzarti",
            "lối_chơi": "Phòng ngự kỷ luật, phá lối chơi đối phương",
            "đội_hinh": ["Bechir Ben Saïd", "Wajdi Kechrida", "Dylan Bronn", "Montassar Talbi", "Ali Abdi", "Ellyes Skhiri", "Aïssa Laïdouni", "Anis Ben Slimane", "Hamza Rafia", "Sayfallah Ltaief", "Youssef Msakni"]
        },
        # Bảng G
        "Bỉ": {
            "bảng": "G", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Kevin De Bruyne", "hlv": "Domenico Tedesco",
            "lối_chơi": "Tấn công trung lộ, ban bật nhanh dựa vào các tiền vệ sáng tạo",
            "đội_hinh": ["Koen Casteels", "Timothy Castagne", "Wout Faes", "Jan Vertonghen", "Arthur Theate", "Orel Mangala", "Amadou Onana", "Kevin De Bruyne", "Jérémy Doku", "Leandro Trossard", "Romelu Lukaku"]
        },
        "Ai Cập": {
            "bảng": "G", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "ngôi_sao": "Mohamed Salah", "hlv": "Hossam Hassan",
            "lối_chơi": "Phòng ngự chặt, dồn bóng cho ngôi sao đột phá tốc độ",
            "đội_hinh": ["Mohamed El Shenawy", "Mohamed Hany", "Mohamed Abdelmonem", "Yasser Ibrahim", "Ali Maâloul", "Marwan Attia", "Mohamed Elneny", "Hamdi Fathi", "Mohamed Salah", "Trézéguet", "Mostafa Mohamed"]
        },
        "Iran": {
            "bảng": "G", "sơ_đồ": "4-4-2", "sức_mạnh": "Khá", "ngôi_sao": "Mehdi Taremi", "hlv": "Amir Ghalenoei",
            "lối_chơi": "Khối phòng ngự lùi sâu vững chãi, phản công sắc bén",
            "đội_hinh": ["Alireza Beiranvand", "Ramin Rezaeian", "Hossein Kanaanizadegan", "Shojae Khalilzadeh", "Milad Mohammadi", "Saman Ghoddos", "Saeid Ezatolahi", "Alireza Jahanbakhsh", "Mehdi Torabi", "Sardar Azmoun", "Mehdi Taremi"]
        },
        "New Zealand": {
            "bảng": "G", "sơ_đồ": "4-4-2", "sức_mạnh": "Yếu", "ngôi_sao": "Chris Wood", "hlv": "Darren Bazeley",
            "lối_chơi": "Bóng bổng, dựa vào thể hình tranh chấp bóng hai",
            "đội_hinh": ["Oliver Sail", "Tim Payne", "Michael Boxall", "Nando Pijnaker", "Liberato Cacace", "Joe Bell", "Matthew Garbett", "Sarpreet Singh", "Ben Old", "Kosta Barbarouses", "Chris Wood"]
        },
        # Bảng H
        "Tây Ban Nha": {
            "bảng": "H", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Lamine Yamal", "hlv": "Luis de la Fuente",
            "lối_chơi": "Tiki-taka hiện đại, luân chuyển bóng cực nhanh, kiểm soát tuyệt đối",
            "đội_hinh": ["Unai Simón", "Dani Carvajal", "Robin Le Normand", "Aymeric Laporte", "Marc Cucurella", "Rodri", "Pedri", "Fabian Ruiz", "Lamine Yamal", "Nico Williams", "Alvaro Morata"]
        },
        "Cabo Verde": {
            "bảng": "H", "sơ_đồ": "4-3-3", "sức_mạnh": "Trung bình", "ngôi_sao": "Ryan Mendes", "hlv": "Bubista",
            "lối_chơi": "Chơi phòng ngự phản công dựa vào tốc độ các cầu thủ chạy cánh",
            "đội_hinh": ["Vozinha", "Steven Moreira", "Logan Costa", "Roberto Lopes", "João Paulo", "Kevin Pina", "Jamiro Monteiro", "Deroy Duarte", "Ryan Mendes", "Garry Rodrigues", "Jovane Cabral"]
        },
        "Saudi Arabia": {
            "bảng": "H", "sơ_đồ": "4-5-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Salem Al-Dawsari", "hlv": "Roberto Mancini",
            "lối_chơi": "Áp sát tầm cao, bẫy việt vị, đá gắn kết kỷ luật",
            "đội_hinh": ["Mohammed Al-Owais", "Saud Abdulhamid", "Ali Lajami", "Ali Al-Bulaihi", "Yasir Al-Shahrani", "Abdullah Otayf", "Mohamed Kanno", "Firas Al-Buraikan", "Salman Al-Faraj", "Salem Al-Dawsari", "Saleh Al-Shehri"]
        },
        "Uruguay": {
            "bảng": "H", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Federico Valverde", "hlv": "Marcelo Bielsa",
            "lối_chơi": "Pressing điên cuồng, va chạm rực lửa, tấn công trực diện",
            "đội_hinh": ["Sergio Rochet", "Nahitan Nández", "Ronald Araújo", "José María Giménez", "Mathías Olivera", "Federico Valverde", "Manuel Ugarte", "Nicolás de la Cruz", "Facundo Pellistri", "Darwin Núñez", "Maximilian Araújo"]
        },
        # Bảng I
        "Pháp": {
            "bảng": "I", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "ngôi_sao": "Kylian Mbappé", "hlv": "Didier Deschamps",
            "lối_chơi": "Tấn công trực diện tốc độ cao bằng hành lang biên",
            "đội_hinh": ["Mike Maignan", "Jules Koundé", "Dayot Upamecano", "William Saliba", "Théo Hernandez", "N'Golo Kanté", "Aurélien Tchouaméni", "Ousmane Dembélé", "Antoine Griezmann", "Bradley Barcola", "Kylian Mbappé"]
        },
        "Senegal": {
            "bảng": "I", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "ngôi_sao": "Sadio Mané", "hlv": "Aliou Cissé",
            "lối_chơi": "Cân bằng giữa thể lực và kỹ thuật, đá áp sát nhanh",
            "đội_hinh": ["Édouard Mendy", "Formose Mendy", "Kalidou Koulibaly", "Abdou Diallo", "Ismail Jakobs", "Idrissa Gueye", "Pape Matar Sarr", "Lamine Camara", "Ismaïla Sarr", "Nicolas Jackson", "Sadio Mané"]
        },
        "Iraq": {
            "bảng": "I", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Aymen Hussein", "hlv": "Jesús Casas",
            "lối_chơi": "Đá tinh quái, không ngại va chạm, mạnh tấn công trung lộ",
            "đội_hinh": ["Jalal Hassan", "Hussein Ali", "Saad Natiq", "Rebin Sulaka", "Merchas Doski", "Amir Al-Ammari", "Osama Rashid", "Ibrahim Bayesh", "Zidane Iqbal", "Ali Jasim", "Aymen Hussein"]
        },
        "Na Uy": {
            "bảng": "I", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "ngôi_sao": "Erling Haaland", "hlv": "Ståle Solbakken",
            "lối_chơi": "Tấn công trục dọc, nhồi bóng cho trung phong cắm ghi bàn",
            "đội_hinh": ["Ørjan Nyland", "Julian Ryerson", "Leo Östigard", "Kristoffer Ajer", "David Møller Wolfe", "Martin Ødegaard", "Patrick Berg", "Sander Berge", "Oscar Bobb", "Antonio Nusa", "Erling Haaland"]
        },
        # Bảng J
        "Áo": {
            "bảng": "J", "sơ_đồ": "4-2-2-2", "sức_mạnh": "Khá", "ngôi_sao": "David Alaba", "hlv": "Ralf Rangnick",
            "lối_chơi": "Gegenpressing điên cuồng, bóp nghẹt không gian đối thủ",
            "đội_hinh": ["Patrick Pentz", "Stefan Posch", "Kevin Danso", "David Alaba", "Phillipp Mwene", "Nicolas Seiwald", "Konrad Laimer", "Marcel Sabitzer", "Christoph Baumgartner", "Michael Gregoritsch", "Marko Arnautovic"]
        },
        "Jordan": {
            "bảng": "J", "sơ_đồ": "3-4-3", "sức_mạnh": "Trung bình", "ngôi_sao": "Mousa Al-Tamari", "hlv": "Jamal Sellami",
            "lối_chơi": "Phòng ngự kỷ luật, phản công chớp nhoáng ở biên",
            "đội_hinh": ["Yazeed Abulaila", "Abdallah Nasib", "Yazan Al-Arab", "Salem Al-Ajalin", "Ehsan Haddad", "Nizar Al-Rashdan", "Noor Al-Rawabdeh", "Mahmoud Al-Mardi", "Mousa Al-Tamari", "Ali Olwan", "Yazan Al-Naimat"]
        },
        # Bảng K
        "Bồ Đào Nha": {
            "bảng": "K", "sơ_đồ": "4-3-3", "sức_mạnh": "Mạnh", "ngôi_sao": "Bruno Fernandes", "hlv": "Roberto Martínez",
            "lối_chơi": "Tấn công áp đặt đa dạng, hoán đổi vị trí biên liên tục",
            "đội_hinh": ["Diogo Costa", "João Cancelo", "Rúben Dias", "Pepe", "Nuno Mendes", "João Palhinha", "Vitinha", "Bruno Fernandes", "Bernardo Silva", "Rafael Leão", "Cristiano Ronaldo"]
        },
        "Uzbekistan": {
            "bảng": "K", "sơ_đồ": "3-4-2-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Eldor Shomurodov", "hlv": "Srecko Katanec",
            "lối_chơi": "Tính kỷ luật chiến thuật cực cao, thủ chặt phản công sắc",
            "đội_hinh": ["Utkir Yusupov", "Abdukodir Khusanov", "Umar Eshmurodov", "Rustam Ashurmatov", "Khojiakbar Alijonov", "Otabek Shukurov", "Odiljon Hamrobekov", "Sherzod Nasrullaev", "Abbosbek Fayzullaev", "Jaloliddin Masharipov", "Eldor Shomurodov"]
        },
        "Colombia": {
            "bảng": "K", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "ngôi_sao": "Luis Díaz", "hlv": "Néstor Lorenzo",
            "lối_chơi": "Đá kỹ thuật và rực lửa Nam Mỹ, đột biến hành lang cánh",
            "đội_hinh": ["Camilo Vargas", "Daniel Muñoz", "Davinson Sánchez", "Carlos Cuesta", "Johan Mojica", "Richard Ríos", "Jefferson Lerma", "Jhon Arias", "James Rodríguez", "Luis Díaz", "Jhon Córdoba"]
        },
        "CHDC Congo": {
            "bảng": "K", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Chancel Mbemba", "hlv": "Sébastien Desabre",
            "lối_chơi": "Đá giàu tốc độ và va chạm thể lực từ khu trung tuyến",
            "đội_hinh": ["Lionel Mpasi", "Gédéon Kalulu", "Chancel Mbemba", "Henoc Inonga", "Arthur Masuaku", "Samuel Moutoussamy", "Charles Pickel", "Theo Bongonda", "Gaël Kakuta", "Yoane Wissa", "Cédric Bakambu"]
        },
        # Bảng L
        "Anh": {
            "bảng": "L", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Mạnh", "ngôi_sao": "Jude Bellingham", "hlv": "Thomas Tuchel",
            "lối_chơi": "Tấn công biên dồn dập, kiểm soát nửa sân đối phương, cố định mạnh",
            "đội_hinh": ["Jordan Pickford", "Kyle Walker", "John Stones", "Marc Guéhi", "Kieran Trippier", "Declan Rice", "Kobbie Mainoo", "Bukayo Saka", "Jude Bellingham", "Phil Foden", "Harry Kane"]
        },
        "Croatia": {
            "bảng": "L", "sơ_đồ": "4-3-3", "sức_mạnh": "Khá", "ngôi_sao": "Luka Modric", "hlv": "Zlatko Dalic",
            "lối_chơi": "Làm chủ khu trung tuyến, cầm nhịp trận đấu chậm rãi tinh tế",
            "đội_hinh": ["Dominik Livakovic", "Josip Stanisic", "Josip Sutalo", "Marin Pongracic", "Josko Gvardiol", "Luka Modric", "Marcelo Brozovic", "Mateo Kovacic", "Lovro Majer", "Andrejan Kramaric", "Ante Budimir"]
        },
        "Ghana": {
            "bảng": "L", "sơ_đồ": "4-2-3-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Mohammed Kudus", "hlv": "Otto Addo",
            "lối_chơi": "Tấn công trực diện, bứt tốc quãng ngắn mạnh mẽ",
            "đội_hinh": ["Lawrence Ati-Zigi", "Alidu Seidu", "Alexander Djiku", "Mohammed Salisu", "Gideon Mensah", "Salo Abdul Samed", "Thomas Partey", "Jordan Ayew", "Mohammed Kudus", "Ernest Nuamah", "Inaki Williams"]
        },
        "Panama": {
            "bảng": "L", "sơ_đồ": "5-4-1", "sức_mạnh": "Trung bình", "ngôi_sao": "Michael Murillo", "hlv": "Thomas Christiansen",
            "lối_chơi": "Phòng ngự số đông co cụm, phá bóng rát",
            "đội_hinh": ["Orlando Mosquera", "Michael Murillo", "José Córdoba", "Edgardo Fariña", "Roderick Miller", "Eric Davis", "Aníbal Godoy", "Adalberto Carrasquilla", "José Luis Rodríguez", "Yoel Bárcenas", "José Fajardo"]
        }
    }

TEAMS = get_teams_data()
def get_team_info(name):
    return TEAMS.get(name, {
        "bảng": "Vòng bảng", "sơ_đồ": "4-2-3-1", "lối_chơi": "Lối chơi tập thể", "ngôi_sao": "Đội trưởng", "sức_mạnh": "Trung bình", "hlv": "Chưa cập nhật",
        "đội_hinh": ["Thủ môn", "Hậu vệ 1", "Hậu vệ 2", "Hậu vệ 3", "Hậu vệ 4", "Tiền vệ 1", "Tiền vệ 2", "Tiền vệ 3", "Tiền đạo 1", "Tiền đạo 2", "Tiền đạo 3"]
    })

# ------------------------------------------------------------------
# 2. KHỞI TẠO LỊCH THI ĐẤU CHUẨN VÀ THỜI TIẾT REAL-TIME
# ------------------------------------------------------------------
if 'matches' not in st.session_state:
    raw_schedule = [
        # Lượt 1
        ["WC-01", "Bảng A", "12/06", "02:00", "Mexico", "Nam Phi", "VTV3, VTV10, VTV6", "Mát mẻ, 24°C (Sân Azteca)"],
        ["WC-02", "Bảng A", "12/06", "09:00", "Hàn Quốc", "CH Séc", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-03", "Bảng B", "13/06", "02:00", "Canada", "Bosnia", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-04", "Bảng D", "13/06", "08:00", "Mỹ", "Paraguay", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-05", "Bảng B", "14/06", "02:00", "Qatar", "Thụy Sĩ", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-06", "Bảng C", "14/06", "05:00", "Brazil", "Marocco", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-07", "Bảng C", "14/06", "08:00", "Haiti", "Scotland", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-08", "Bảng D", "14/06", "11:00", "Úc", "Thổ Nhĩ Kỳ", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-09", "Bảng E", "15/06", "00:00", "Đức", "Curacao", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-10", "Bảng F", "15/06", "03:00", "Hà Lan", "Nhật Bản", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-11", "Bảng E", "15/06", "06:00", "Bờ Biển Ngà", "Ecuador", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-12", "Bảng F", "15/06", "09:00", "Thụy Điển", "Tunisia", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-13", "Bảng H", "15/06", "23:00", "Tây Ban Nha", "Cabo Verde", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-14", "Bảng G", "16/06", "02:00", "Bỉ", "Ai Cập", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-15", "Bảng H", "16/06", "05:00", "Saudi Arabia", "Uruguay", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-16", "Bảng G", "16/06", "08:00", "Iran", "New Zealand", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-17", "Bảng I", "17/06", "02:00", "Pháp", "Senegal", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-18", "Bảng I", "17/06", "05:00", "Iraq", "Na Uy", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-19", "Bảng A", "17/06", "08:00", "Argentina", "Algeria", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-20", "Bảng J", "17/06", "11:00", "Áo", "Jordan", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-21", "Bảng K", "18/06", "00:00", "Bồ Đào Nha", "CHDC Congo", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-22", "Bảng L", "18/06", "03:00", "Anh", "Croatia", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-23", "Bảng L", "18/06", "06:00", "Ghana", "Panama", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-24", "Bảng K", "18/06", "09:00", "Uzbekistan", "Colombia", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        
        # Lượt 2
        ["WC-25", "Bảng A (L2)", "18/06", "23:00", "CH Séc", "Nam Phi", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-26", "Bảng B (L2)", "19/06", "02:00", "Thụy Sĩ", "Bosnia", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-27", "Bảng B (L2)", "19/06", "05:00", "Canada", "Qatar", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-28", "Bảng A (L2)", "19/06", "08:00", "Mexico", "Hàn Quốc", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-29", "Bảng D (L2)", "20/06", "02:00", "Mỹ", "Úc", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-30", "Bảng C (L2)", "20/06", "05:00", "Scotland", "Marocco", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-31", "Bảng C (L2)", "20/06", "07:30", "Brazil", "Haiti", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-32", "Bảng D (L2)", "20/06", "10:00", "Thổ Nhĩ Kỳ", "Paraguay", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-33", "Bảng F (L2)", "21/06", "00:00", "Hà Lan", "Thụy Điển", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-34", "Bảng E (L2)", "21/06", "03:00", "Đức", "Bờ Biển Ngà", "VTV3, VTV10, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-35", "Bảng E (L2)", "21/06", "07:00", "Ecuador", "Curacao", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        ["WC-36", "Bảng F (L2)", "21/06", "11:00", "Tunisia", "Nhật Bản", "VTV3, VTV6", "Chưa cập nhật (Chờ BTC)"],
        
        # Lượt 3
        ["WC-53", "Bảng A (L3)", "25/06", "08:00", "Nam Phi", "Hàn Quốc", "VTV2", "Chưa cập nhật (Chờ BTC)"],
        ["WC-54", "Bảng A (L3)", "25/06", "08:00", "CH Séc", "Mexico", "VTV3", "Chưa cập nhật (Chờ BTC)"],
        ["WC-72", "Bảng J (L3)", "28/06", "09:00", "Jordan", "Argentina", "VTV3", "Chưa cập nhật (Chờ BTC)"]
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

# ------------------------------------------------------------------
# 3. THUẬT TOÁN QUÉT LỊCH SỬ PHONG ĐỘ THỜI GIAN THỰC
# ------------------------------------------------------------------
def get_team_history_insight(team_name):
    played_matches = []
    for code, m in st.session_state.matches.items():
        if m["ti_so_ft"] != "" and (m["đội_nhà"] == team_name or m["đội_khách"] == team_name):
            played_matches.append((code, m))
            
    if not played_matches:
        if team_name == "Mexico":
            return "Đang có chuỗi 3 trận giao hữu thắng liên tiếp ngay sát thềm giải đấu, tâm lý cực tốt."
        elif team_name == "Nam Phi":
            return "Vừa trải qua loạt 4 trận giao hữu không biết mùi chiến thắng, phong độ có phần chuệch choạc."
        return "Sẵn sàng ra quân trận mở màn với đầy đủ quân bài tốt nhất."

    last_code, last_m = played_matches[-1]
    is_home = last_m["đội_nhà"] == team_name
    try:
        score_parts = last_m["ti_so_ft"].split("-")
        goals_for = int(score_parts[0]) if is_home else int(score_parts[1])
        goals_against = int(score_parts[1]) if is_home else int(score_parts[0])
    except:
        return "Hoàn thành lượt đấu trước kịch tính."

    opp = last_m["đội_khách"] if is_home else last_m["đội_nhà"]
    if goals_for > goals_against:
        return f"🔥 Hừng hực khí thế sau chiến thắng vang dội {last_m['ti_so_ft']} trước {opp} ở trận trước."
    elif goals_for < goals_against:
        return f"⚠️ Áp lực tâm lý nặng nề sau thất bại cay đắng {last_m['ti_so_ft']} trước đối thủ {opp}."
    else:
        return f"⚖️ Đá thận trọng, thực dụng sau trận hòa níu chân {last_m['ti_so_ft']} với {opp}."

# ------------------------------------------------------------------
# 4. THUẬT TOÁN AI DỰ ĐOÁN TỈ SỐ & GIẢI THÍCH CHIẾN THUẬT CHUẨN XÁC
# ------------------------------------------------------------------
def ai_calculate_prediction(home, away):
    h_info = get_team_info(home)
    a_info = get_team_info(away)
    
    power_points = {"Mạnh": 4, "Khá": 3, "Trung bình": 2, "Yếu": 1}
    h_score = power_points.get(h_info['sức_mạnh'], 2)
    a_score = power_points.get(a_info['sức_mạnh'], 2)
    
    diff = h_score - a_score
    if diff >= 3:
        return "3 - 0", f"Chênh lệch đẳng cấp quá lớn. Lối đánh áp đặt của chiến lược gia {h_info['hlv']} sẽ đè bẹp hệ thống phòng ngự lỏng lẻo bên phía {away}."
    elif diff == 2:
        return "2 - 0", f"Đội chủ nhà kiểm soát thế trận áp đảo. Sự lọc lõi của HLV {h_info['hlv']} sẽ giúp họ giải mã thành công sơ đồ thủ sâu của đối thủ."
    elif diff == 1:
        return "2 - 1", f"{home} nhỉnh hơn về nhân sự tuyến giữa. HLV {h_info['hlv']} có nhiều bài đánh biên sắc bén hơn, dù {away} có thể gỡ gạc bằng cố định."
    elif diff == 0:
        if h_info['sức_mạnh'] == 'Mạnh':
            return "1 - 1", f"Trận đại chiến đấu trí đỉnh cao giữa hai HLV {h_info['hlv']} và {a_info['hlv']}. Cả hai đều quá già giơ nên thế trận rất dễ chia điểm."
        return "0 - 0", f"Màn so tài thực dụng. Cả hai huấn luyện viên đều ưu tiên sự an toàn bảo vệ mành lưới nên kịch bản khan hiếm bàn thắng dễ xảy ra."
    elif diff == -1:
        return "1 - 2", f"Dù phải đá sân khách nhưng đấu pháp trực diện của HLV {a_info['hlv']} đồng đều hơn. Ngôi sao gánh đội sẽ giúp đội khách bỏ túi 3 điểm."
    else:
        return "0 - 2", f"Sức mạnh áp đảo từ đội khách. Hệ thống pressing tầm cao do HLV {a_info['hlv']} bài binh bố trận sẽ bóp nghẹt mọi ý đồ tấn công của chủ nhà."

# ------------------------------------------------------------------
# 5. THUẬT TOÁN AI AUTO XUẤT BÀI BÁO NHẬN ĐỊNH BÓNG ĐÁ
# ------------------------------------------------------------------
def ai_generate_editorial(match_id, home, away):
    h_info = get_team_info(home)
    a_info = get_team_info(away)
    h_insight = get_team_history_insight(home)
    a_insight = get_team_history_insight(away)
    
    pred_score, pred_reason = ai_calculate_prediction(home, away)
    
    title = f"📰 Nhận định, soi kèo {home} vs {away} - {st.session_state.matches[match_id]['giờ']} ngày {st.session_state.matches[match_id]['ngày']}"
    
    content = f"### {title}\n\n"
    content += f"**Tình hình phong độ thực tế từ Dashboard:**\n"
    content += f"* **{home}**: {h_insight}\n"
    content += f"* **{away}**: {a_insight}\n\n"
    
    content += f"**Phân tích chiến thuật từ Băng ghế Huấn luyện:**\n"
    content += f"Đội tuyển **{home}** dưới sự dẫn dắt của HLV lão làng **{h_info['hlv']}** chuẩn bị xuất phát với sơ đồ **{h_info['sơ_đồ']}**. "
    content += f"Đấu pháp chủ đạo của ông là *{h_info['lối_chơi']}*, dồn mọi đường bóng sáng nước cho hạt nhân **{h_info['ngôi_sao']}** gánh vác hàng công.\n\n"
    content += f"Phía bên kia chiến tuyến, vị thuyền trưởng **{a_info['hlv']}** bên phía **{away}** đáp trả bằng sơ đồ thực dụng **{a_info['sơ_đồ']}**. "
    content += f"Chiến thuật cốt lõi mà ông áp dụng cho các học trò là *{a_info['lối_chơi']}*, đặt niềm tin tuyệt đối vào mũi nhọn **{a_info['ngôi_sao']}** nhằm trừng phạt sai lầm đối thủ.\n\n"
    
    content += f"--- \n"
    content += f"📋 **ĐỘI HÌNH XUẤT PHÁT DỰ KIẾN CỦA 2 ĐỘI:**\n\n"
    
    col_h = f"**🔥 {home} (HLV: {h_info['hlv']} - Sơ đồ: {h_info['sơ_đồ']}):**\n"
    col_a = f"**🛡️ {away} (HLV: {a_info['hlv']} - Sơ đồ: {a_info['sơ_đồ']}):**\n"
    
    for idx, player in enumerate(h_info['đội_hinh']):
        col_h += f"{idx+1}. {player}\n"
    for idx, player in enumerate(a_info['đội_hinh']):
        col_a += f"{idx+1}. {player}\n"
        
    return content, col_h, col_a, pred_score, pred_reason

# ==================================================================
# GIAO DIỆN MÀN HÌNH WEB APP (STREAMLIT UI)
# ==================================================================
st.title("🏆 TRANG DASHBOARD TIN TỨC & QUẢN LÝ WORLD CUP 2026")
st.markdown("---")

tab1, tab2, tab3 = st.tabs(["📰 Trang Tin Nhận Định Chuyên Sâu", "⏱️ Cập Nhật Kết Quả Real-Time", "🏃 Lực Lượng Chuẩn 48 Đội Bóng"])

# ------------------------------------------------------------------
# TAB 1: GIAO DIỆN XEM BÀI BÁO & ĐỘI HÌNH DỰ KIẾN CHI TIẾT
# ------------------------------------------------------------------
with tab1:
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        selected_m = st.selectbox("Chọn trận đấu muốn xem bài viết nhận định & phân tích đội hình:", list(st.session_state.matches.keys()))
        m_data = st.session_state.matches[selected_m]
        
        # Chạy thuật toán xuất văn bản và đội hình hlv
        editorial_text, list_home_players, list_away_players, ai_score, ai_reason = ai_generate_editorial(selected_m, m_data['đội_nhà'], m_data['đội_khách'])
        
        st.markdown(editorial_text)
        
        # Chia 2 cột hiển thị tên HLV và 11 cầu thủ đá chính cực đẹp
        c_home, c_away = st.columns(2)
        with c_home:
            st.info(list_home_players)
        with c_away:
            st.success(list_away_players)
        
    with col_right:
        st.markdown("### 🤖 Trợ Lý AI Dự Đoán Kết Quả")
        st.success(f"🎯 **AI Dự đoán Tỉ số:** {ai_score}")
        st.info(f"🧠 **Giải thích đấu pháp:** {ai_reason}")
        
        st.markdown("---")
        st.markdown("### 📊 Trạng Thái Trận Đấu & Kênh Phát")
        st.warning(f"📺 **Kênh phát sóng:** {m_data['kênh']}")
        st.text(f"🏟️ **Khu vực / Thời tiết:** {m_data['thời_tiết']}")
        st.text(f"👤 **Trọng tài bắt chính:** {m_data['trọng_tài']}")
        
        if m_data['ti_so_ft'] != "":
            st.error(f"🏁 Tỉ số thực tế FT: {m_data['ti_so_ft']} (HT: {m_data['ti_so_ht']})")
        else:
            st.caption("⏳ Trận đấu chưa diễn ra")
            
        m_data['dự_đoán_bạn'] = st.text_input(f"Góc dự đoán tỉ số của bạn:", m_data['dự_đoán_bạn'])

        st.markdown("---")
        st.markdown("### 🕒 Danh sách trận đấu vòng bảng")
        list_grid = []
        for c, m in st.session_state.matches.items():
            status = m['ti_so_ft'] if m['ti_so_ft'] != "" else "Chưa đá"
            list_grid.append([c, m['ngày'], m['đội_nhà'], status, m['đội_khách']])
        grid_df = pd.DataFrame(list_grid, columns=["Mã", "Ngày", "Đội Nhà", "Kết Quả", "Đội Khách"])
        st.dataframe(grid_df, use_container_width=True, height=180)

# ------------------------------------------------------------------
# TAB 2: NƠI NHẬP TIẾN ĐỘ REAL-TIME & CẬP NHẬT THỜI TIẾT THỰC TẾ
# ------------------------------------------------------------------
with tab2:
    st.subheader("⏱️ Phòng Cập Nhật Diễn Biến Trận Đấu Real-Time")
    update_m = st.selectbox("Chọn Mã Trận cần nhập thông số trực tiếp:", list(st.session_state.matches.keys()))
    curr_m = st.session_state.matches[update_m]
    
    st.markdown(f"### 📍 Đang ghi nhận dữ liệu: **{curr_m['đội_nhà']} vs {curr_m['đội_khách']}**")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 🕒 Thông số Giữa Hiệp (HT)")
        curr_m['ti_so_ht'] = st.text_input("Tỉ số giữa hiệp (Vd: 1-0)", curr_m['ti_so_ht'])
        curr_m['sút_ht'] = st.text_input("Số cú sút Hiệp 1 (Chủ/Khách)", curr_m['sút_ht'])
        curr_m['thời_tiết'] = st.text_input("Thời tiết thực tế tại sân (Vd: Mưa rào, 19°C)", curr_m['thời_tiết'])
    with c2:
        st.markdown("#### 🏁 Thông số Hết Trận (FT)")
        curr_m['ti_so_ft'] = st.text_input("Tỉ số chung cuộc (Vd: 2-0)", curr_m['ti_so_ft'])
        curr_m['sút_ft'] = st.text_input("Tổng cú sút cả trận", curr_m['sút_ft'])
        curr_m['chuyền_ft'] = st.text_input("Tổng số đường chuyền", curr_m['chuyền_ft'])
    with c3:
        st.markdown("#### ⚠️ Chỉ số Phạ & Thẻ Phạt")
        curr_m['góc_ft'] = st.text_input("Số quả phạt góc", curr_m['góc_ft'])
        curr_m['thẻ_vàng'] = st.text_input("Số Thẻ Vàng", curr_m['thẻ_vàng'])
        curr_m['thẻ_đỏ'] = st.text_input("Số Thẻ Đỏ", curr_m['thẻ_đỏ'])
        curr_m['trọng_tài'] = st.text_input("Trọng tài bắt chính", curr_m['trọng_tài'])
        
    if st.button("💾 XÁC NHẬN LƯU KẾT QUẢ & ĐỒNG BỘ AI"):
        st.toast(f"Hệ thống đã lưu kết quả trận {update_m} thành công!", icon="⚡")

# ------------------------------------------------------------------
# TAB 3: DANH SÁCH CHI TIẾT LỐI CHƠI, HLV & LỰC LƯỢNG 48 ĐỘI
# ------------------------------------------------------------------
with tab3:
    st.subheader("🏃 Danh sách HLV, Chiến Thuật & Sức mạnh 48 đội (Đầy đủ 100%)")
    team_list = []
    for t_name, t_val in TEAMS.items():
        squad_txt = ", ".join(t_val['đội_hinh'][:3]) + "... và các cầu thủ khác"
        team_list.append([t_name, t_val['bảng'], t_val['hlv'], t_val['sơ_đồ'], t_val['lối_chơi'], t_val['ngôi_sao'], t_val['sức_mạnh']])
    
    team_df = pd.DataFrame(team_list, columns=["Tên Đội Bóng", "Bảng", "Huấn Luyện Viên", "Sơ Đồ Chiến Thuật", "Lối Chơi Chủ Đạo", "Ngôi Sao Gánh Đội", "Đánh Giá Cửa"])
    st.dataframe(team_df, use_container_width=True, height=450)