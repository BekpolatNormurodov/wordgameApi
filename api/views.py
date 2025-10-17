from rest_framework.response import Response
from rest_framework.views import APIView
import random

class HangmanAPIView(APIView):
    def get(self, request):
        names = "Abbos", "Abdulaziz", "Abdulloh", "Abror", "Adham", "Akbar", "Akmal", "Alisher", "Amir", "Amirbek", "Amirxon", "Anvar", "Asad", "Asliddin", "Asror", "Azamat", "Azimjon", "Aziz", "Azizbek", "Baxtiyor", "Bekmurod", "Bekzod", "Bilol", "Bobur", "Botir", "Davron", "Dilshod", "Elyor", "Ergash", "Erkin", "Farruh", "Farrux", "Farhod", "Fayzulla", "Firdavs", "Habib", "Habibulloh", "Hakim", "Hamid", "Hamza", "Hasan", "Hasanboy", "Hikmat", "Hikmatulloh", "Hojiakbar", "Humoyun", "Husan", "Husanboy", "Husniddin", "Ilhom", "Iskandar", "Islom", "Ismoil", "Ibrohim", "Jamol", "Jamshid", "Jaloliddin", "Jasur", "Javlon", "Javohir", "Karim", "Kamoliddin", "Komil", "Laziz", "Lochin", "Lutfulla", "Madamin", "Mahmud", "Malik", "Mansur", "Mashrab", "Mirjalol", "Mirkomil", "Mironshoh", "Murod", "Muhriddin", "Muhammad", "Muzaffar", "Najmiddin", "Nodir", "Nurbek", "Nuriddin", "Odil", "Olim", "Oybek", "Qahhor", "Qahramon", "Qobil", "Qodir", "Qosim", "Qurbon", "Quvonch", "Rahim", "Rashid", "Ravshan", "Rustam", "Rustamjon", "Samandar", "Sanjar", "Sardor", "Sarvar", "Said", "Shahboz", "Shahriyor", "Shahzod", "Shams", "Shamsiddin", "Shavkat", "Sherali", "Sherzod", "Shodiyor", "Shodmon", "Shokir", "Shohjahon", "Shohruh", "Siroj", "Sirojiddin", "Sobir", "Sobit", "Sodiq", "Sohib", "Suhrob", "Sulton", "Temur", "Tohir", "Tolib", "Ubaydulla", "Ubaydulloh", "Ulug'bek", "Umid", "Umar", "Usmon", "Valijon", "Vohid", "Xayrulloh", "Xojiakbar", "Xolmat", "Xudoyor", "Xurshid", "Yahyo", "Yodgor", "Yoqub", "Yunus", "Yusuf", "Zafar", "Zavqiddin", "Zayniddin", "Zohid", "Zokir", "Adolat", "Aziza", "Barno", "Dilafruz", "Dildora", "Dilnoza", "Feruza", "Fotima", "Gulbahor", "Gulchehra", "Gulhayo", "Gulnora", "Gulnoza", "Gulsanam", "Gulshan", "Gulruh", "Humora", "Husniya", "Iroda", "Kamola", "Kumush", "Lobar", "Malohat", "Manzura", "Mashhura", "Maftuna", "Mehribon", "Muhayyo", "Mubina", "Mukarram", "Muqaddas", "Munira", "Munisa", "Mushtariy", "Nilufar", "Nigora", "Nodira", "Nozima", "Ozoda", "Oysara", "Oygul", "Parizoda", "Rano", "Rayhona", "Ruxshona", "Saida", "Saodat", "Sanobar", "Shahlo", "Shahzoda", "Shamsiya", "Shoira", "Shukrona", "Surayyo", "Umida", "Xadicha", "Xalima", "Xilola", "Xosiyat", "Xurriyat", "Zarnigor", "Zebo", "Zilola", "Ziyoda", "Zuhra", "Madina", "Mahliyo", "Malika", "Mehriniso", "Muslima", "Nasiba", "Nafisa", "Nafosat", "Nargiza", "Nigina", "Robiya", "Sabina", "Sanam", "Shahrizoda", "Sitora", "Sadoqat", "Sohiba", "Tahmina", "Tomaris", "Zaynab", "Zulfiya", "Zarina", "Zarifa", "Asal", "Barchinoy", "Dilorom", "Dilshoda", "Firuza", "Gulandon", "Gulsara", "Halima", "Hanifa", "Husnora", "Jamila", "Karima", "Komila", "Lola", "Marhabo", "Munavvar", "Oysuluv", "Rano", "Sabohat", "Shirin", "Shohista", "Xonzoda", "Xurshida", "Zebiniso", "Dilnora", "Guljahon", "Guljamol", "Husniyo", "Iymona", "Latofat", "Nigoh", "Ruxsora", "Sabrina", "Shaxnoza", "Shodiyona", "Shohsanam", "Umriniso", "Xumora", "Zubayda", "Zulayho"
        colors = "Oq", "Qora", "Qizil", "Ko'k", "Yashil", "Sariq", "Malla", "Pushti", "Moviy", "Zangori", "Binafsha", "Kulrang", "Jigarrang"
        calendar = "Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr", "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba", "Bahor", "Yoz", "Kuz", "Qish"
        animals = "It", "Mushuk", "Ot", "Sigir", "Qo'y", "Eshak", "Tovuq", "Xo'roz", "O'rdak", "G'oz", "Qo'zi", "Buqa", "Baliq", "Quyon", "Sher", "Arslon", "Yo'lbars", "Tulki", "Bo'ri", "Ayiq", "Chumchuq", "Qaldirg'och", "Qarg'a", "Qurbaqa", "Maymun", "Fil", "Jirafa", "Kapalak", "Asalari", "Chayon", "Ilon", "Sichqon", "Jayron", "Bug'u", "Burgut", "Qirg'iy", "Turna", "Tovus", "Toychoq", "Bo'taloq", "Echkichi", "Akula", "Delfin", "Timsah", "Pingvin", "Qoplon", "Tustovuq", "Baqa", "Tulpor", "Chittak", "Laylak", "Boyo'g'li", "Ohu", "Qunduz", "Bo'rsiq", "Kaptar", "Lochin", "Ko'rsichqon", "Toshbaqa", "Kalamush", "Tuya", "Qo'y", "Jayra", "Panda", "Koala", "Shilliqurt", "Qirg'ovul", "Kaklik", "O'rdak", "Chumoli", "Bo'g'mailon", "Mushuk", "Xo'tik", "Turna"
        fruit = "Olma", "Anor", "Uzum", "Nok", "Shaftoli", "Gilos", "Olcha", "Shaftoli", "Banan", "Apelsin", "Mandarin", "Limon", "Kivi", "Ananas", "Mango", "Papayya", "Avokado", "Kokos", "Injir", "Xurmo", "Tut", "Behi", "Qulupnay", "Malina", "Chernika", "Smorodina", "O'rik"
        vegetables = "Kartoshka", "Piyoz", "Sarimsoq", "Sabzi", "Bodring", "Pomidor", "Baqlajon", "Qalampir", "Karam", "Gulkaram", "Qovoq", "Kadi", "Turp", "Rediska", "Sholg'om", "Ismaloq", "Kashnich", "Ukrop", "Shivit", "Petrushka", "Zanjabil"
        ovqatlar = "Palov", "Kabob", "Sho'rva", "Mastava", "Dimlama", "Chuchvara", "Manti", "Norin", "Lag'mon", "Honim", "Barak", "Somsa", "Qazi", "Shashlik", "Jigar", "Beshbarmoq", "Halim", "Sumalak", "Burger", "Xotdog", "Shaurma", "Donar", "Lavash", "Pizza", "Sendvich", "Chizburger"
        obhavo = "Quyosh", "Bulut", "Yomg'ir", "Qor", "Shamol", "Jala", "Bo'ron", "Tornado", "Chaqmoq", "Momaqaldiroq", "Dovul"
        transport = "Mashina", "Avtobus", "Poyezd", "Samolyot", "Kema", "Traktor", "Velosiped", "Mototsikl", "Metro", "Skuter", "Tramvay", "Avtomobil"
        osimliklar = "Gul", "Lola", "Chinor", "Tol", "Terak", "Qayin", "Tut", "Kaktus"
        ichimlik = "Choy", "Qahva", "Sut", "Sharbat", "Suv", "Kefir", "Kompot", "CocaCola", "Pepsi", "Fanta", "Limonad", "Mors"
        fan = "Matematika", "Fizika", "Kimyo", "Biologiya", "Geografiya", "Astronomiya", "Informatika", "Tarix", "Adabiyot", "Tilshunoslik", "Psixologiya", "Iqtisodiyot", "Falsafa", "Huquq", "Tibbiyot", "Ekologiya", "Musiqa", "San'at", "Texnologiya", "Muhandislik", "Robototexnika", "Nanotexnologiya", "Genetika", "Geologiya", "Agronomiya"
        vaqt = "Sekund", "Minut", "Soat", "Kun", "Hafta", "Oy", "Yil", "Asr", "Tong", "Kech", "Tun"
        qurollar = "Qilich", "Nayza", "Kamon", "Xanjar", "Pichoq", "Qamchi", "Bolta", "Qalqon", "Miltiq", "Pistolet", "Avtomat", "Snayper", "Patron", "Granata", "Mina", "Raketa", "Yadro", "Zambarak", "Pulimyot", "Elektroshoker"
        musiqa_asboblari = "Doira", "Karnay", "Surnay", "G'ijjak", "Tanbur", "Dutor", "Rubob", "Tor", "Gitara", "Pianino", "Skripka", "Saksofon", "Baraban"
        oila_va_qarindoshlar = "Ota", "Ona", "Bola", "O'g'il", "Qiz", "Aka", "Uka", "Opa", "Singil", "Amaki", "Tog'a", "Xola", "Amma", "Buvi", "Bobo", "Kelin", "Kuyov", "Er", "Xotin", "Jiyan", "Nevara", "Chaqaloq", "Qaynona", "Qaynota", "Qaynuka", "Qaynsingil", "Qaynopa", "Nevara", "O'gayona", "O'gayota", "O'gayuka", "O'gayaka", "O'gayopa", "Buvijon", "Bobojon", "Opajon", "Akajon", "Ukajon", "Onajon", "Qizaloq", "Enaga", "Amakivachcha", "Qudag'ay", "Quda", "Qaynona", "Qaynota"
        human_body = "Bosh", "Soch", "Peshona", "Ko'z", "Qosh", "Kiprik", "Burun", "Lab", "Og'iz", "Tish", "Til", "Yonoq", "Jag'", "Quloq", "Bo'yin", "Tomoq", "Yelka", "Qo'l", "Bilak", "Kaft", "Barmoq", "Tirnoq", "Yurak", "O'pka", "Jigar", "Oshqozon", "Buyrak", "Ichak", "Bel", "Qorin", "Son", "Tizza", "Oyoq", "Tovon", "Skelet", "Suyak", "Muskul", "Tomir", "Asab", "Teri", "Qon", "Miya", "Umurtqa", "Qovurg'a"
        sports = "Futbol", "Boks", "Kurash", "Tennis", "Shaxmat", "Shashka", "Basketbol", "Voleybol", "Dzyudo", "Taekvondo", "Karate", "Sambo", "Suzish", "Gimnastika", "Velosport", "Handbol", "Xokkey", "Amerika futzal", "Beysbol", "Golf", "Bilyard", "O'qotish", "Yugurish", "Avtopoyga"
        maktab_anjomlar = "Daftar", "Qalam", "Ruchka", "Chizg'ich", "O'chirg'ich", "Qalamdon", "sumka", "Jild", "Doska", "Marker", "Bo'yoq", "Kley", "Qaychi", "Sirkul", "Proyektor", "Bo'r", "Jurnal", "Kitob", "Alifbo", "Kundalik"
        jobs = "O'qituvchi", "Shifokor", "Haydovchi", "Dehqon", "Oshpaz", "Quruvchi", "Tikuvchi", "Sartarosh", "Politsiya", "Harbiy", "Hamshira", "Sotuvchi", "Elektrik", "Santexnik", "Hisobchi", "Farmatsevt", "Muhandis", "Advokat", "Dasturchi", "Aktyor", "Qo'shiqchi", "Rassom", "Dizayner", "Fotograf", "Jurnalist", "Kutubxonachi", "Imom", "Ofitsiant", "Kassir", "Bankir", "Tadbirkor", "Mashinasoz", "Mexanik", "Fermer", "Veterinar", "Temirchi", "Duradgor", "Haykaltarosh", "Geodezist", "Tarjimon", "Professor", "Psixolog", "Arxitektor", "Astronom", "Robototexnik", "Hayvonotshunos", "Hacker", "Arxeolog", "O'rmonchi", "Iqtisodchi", "SMM", "Operator", "Rejissyor", "Musiqachi", "Dirijyor", "Sportchi", "Futbolchi", "Bokschi", "Kurashchi", "Trener", "Hakim", "Massajchi", "Hamomchi", "Instruktor", "Usta", "Elektrotexnik", "Energetik", "Konchi", "Neftchi", "Kimyogar", "Biolog", "Fizik", "Ximik", "Direktor", "Dekan", "Advokat", "Sudya", "Prokuror", "Notarius", "Banker", "Pochtalyon", "Uchuvchi", "Styuardessa", "Dengizchi"
        nature = "Quyosh", "Oy", "Yulduz", "Bulut", "Yomg'ir", "Qor", "Shamol", "Tog'", "Daraxt", "Gul", "O't", "Suv", "Ko'l", "Daryo", "Okean", "Cho'l", "Dasht", "O'rmon", "Tuproq", "Tosh", "Qoya", "Chashma", "Soy", "Vodiy", "Jar", "Ko'k", "Osmon", "Kamalak", "Nur", "Barg", "Shox", "Ildiz", "Giyoh", "Lola", "Chinor", "Terak", "Tol", "O'rik", "Chaman", "Bog'", "Gulzor", "O'tloq", "Dashtzor", "Cho'qqi", "Sahro", "Qumtepa", "Shag'al", "Ko'mir", "Neft", "Oltin", "Kumush", "Mis", "Qoyatosh", "Orol", "Sharshara", "G'or", "Buloq", "Bo'ron", "Jala", "Chaqmoq", "Momaqaldiroq", "Tornado", "Sel", "Zilzila", "Vulqon", "Lava", "Muzlik", "Aysberg", "Sahro", "Qum", "Dengiz"
        birds = "Qaldirg'och", "Bulbul", "Kaptar", "To'ti", "Qarg'a", "Turna", "Qirg'iy", "Burgut", "Boyqush", "Chumchuq", "Tovus", "Bedana", "O'rdak", "G'oz", "Tovuq", "Xo'roz", "Laylak", "Kaklik", "Qizilishton", "Qizilqanot"
        phones = "Apple", "Samsung", "Huawei", "Xiaomi", "Oppo", "Vivo", "Realme", "OnePlus", "Honor", "Motorola", "Nokia", "Sony", "Pixel", "ZTE", "Tecno", "Infinix", "Micromax", "Panasonic", "Philips", "Siemens"
        uzb_regions = "Toshkent", "Samarqand", "Buxoro", "Xiva", "Urganch", "Nukus", "Andijon", "Namangan", "Farg'ona", "Qo'qon", "Marg'ilon", "Qarshi", "Shahrisabz", "Guliston", "Termiz", "Chirchiq", "Olmaliq", "Angren", "Bekobod", "Zarafshon", "Denov", "Asaka", "Pop", "Chust", "Rishton", "Koson", "Kitob", "Zomin", "Parkent", "Zangiota", "Chortoq", "Yangiqo'rg'on", "Paxtakor", "Boysun", "Nurafshon", "G'ijduvon", "Chiroqchi", "Sherobod", "Uchqo'rg'on", "Bo'stonliq", "Olot", "To'rako'rg'on", "Bektemir", "Yashnobod", "MirzoUlug'bek", "Shayxontohur", "Yakkasaroy", "Uchtepa", "Yunusobod", "Sergeli", "Chilonzor", "Mirobod", "Hazorasp", "Xonqa", "Yangiariq", "Xonobod", "Paxtaobod", "Oltinko'l", "Baliqchi", "Jalaquduq", "Izboskan", "Xo'jaobod", "Uychi", "Norin", "To'raqo'rg'on", "Kosonsoy", "Davlatobod", "Do'stlik", "Mirzacho'l", "Forish", "Yangiobod", "Gagarin", "O'rtaChirchiq", "Yangiyo'l", "Qibray", "Ohangaron", "QuyiChirchiq", "Qamashi", "Dehqonobod", "Nishon", "Registon", "ShohiZinda", "Ichanqal'a", "Chorsu", "Aydarko'l", "Beldersoy", "Chimgan"
        countries = "Amerika", "Rossiya", "Xitoy", "Turkiya", "Koreya", "Hindiston", "Yaponiya", "Italiya", "Fransiya", "Angliya", "Germaniya", "Ispaniya", "Kanada", "Braziliya", "Saudiya", "Misr", "Afrika", "Argentina", "Isroil", "Qatar", "Ukraina", "Turkmaniston", "O'zbekiston", "Qozog'iston", "Qirg'iziston", "Tojikiston", "Avstraliya", "Indoneziya", "Meksika", "Shveysariya", "Shotlandiya", "Tailand", "Singapur", "Niderlandiya", "Shvetsiya", "Norvegiya", "Finlyandiya", "Avstriya", "Belgiya", "Polsha", "Gretsiya", "Chexiya", "Vengriya", "Portugaliya", "Irlandiya", "Zelandiya", "Marokash", "Filippin", "Vetnam", "Malayziya", "Pokiston", "Eron", "Iroq", "Kuvayt", "Oman", "Iordaniya", "Livan", "Suriya", "Afgoniston", "Bangladesh", "ShriLanka", "Nepal", "Myanma", "Kambodja", "Laos", "Efiopiya", "Keniya", "Tanzaniya", "Uganda", "Nigeriya", "Gana", "Senegal", "Kamerun", "Kongo", "Angola", "Zambiya", "Zimbabve", "Madagaskar", "Mozambik", "Botsvana", "Namibiya", "Islandiya", "Litva", "Latviya", "Estoniya", "Gruziya", "Armaniston", "Ozarbayjon", "Moldova", "Belarus", "Serbiya", "Bosniya", "Xorvatiya", "Sloveniya", "Slovakiya", "Boliviya", "Paragvay", "Urugvay", "Chili", "Peru"
        kiyim_kichaklar = "Ko'ylak", "Shim", "Kostyum", "Poyabzal", "Etik", "Krossovka", "Tufli", "Futbolka", "Mayka", "Jinsi", "Kurtka", "Pidjak", "Sharf", "Paypoq", "Shapka", "Qo'lqop", "Kepka", "Chopon", "Kofta", "Sviter", "Halat", "Yubka", "Ro'mol","Kamzul"
        oshxona_buyumlar = "Tarelka", "Lagan", "Piyola", "Kosa", "Choynak", "Stakan", "Likopcha", "Patnis", "Bakal", "Termos", "Qoshiq", "Vilka", "Pichoq", "Cho'mich", "Qirg'ich", "Elak", "Taxtacha", "Qozon", "Kastryulka", "Tova", "Qazan", "Samovar", "Banka", "Tog'ora", "Qopqoq", "Gazplita", "Duxovka", "muzlatgich", "Multivarka", "Mikser", "Blender", "Sochiq", "Fartuk", "O'choq", "Savat"
        cars = "Chevrolet", "Daewoo", "Nexia", "Spark", "Matiz", "Damas", "Tiko", "Lacetti", "Gentra", "Kobalt", "Malibu", "Tracker", "Kaptiva", "Onix", "Epika", "Orlando", "Toyota", "Kamry", "Prado", "Lexus", "Honda", "Kia", "Optima", "Sportage", "Sorento", "Hyundai", "Sonata", "Elantra", "SantaFe", "MercedesBenz", "BMW", "Audi", "Volkswagen", "Polo", "Golf", "Ford", "Focus", "Mustang", "Nissan", "Patrol", "XTrail", "Outlander", "Lancer", "Suzuki", "RangeRover", "LandRover", "Jaguar", "Tesla", "Cybertruck", "Ferrari", "Lamborghini", "Bugatti", "RollsRoyce", "Bentley", "Maserati", "BWD", "Chazor"
        his_tuygular =  "Sevgi", "Muhabbat", "Mehr", "Oqibat", "Sadoqat", "Do'stlik", "Ishonch", "Umid", "Shodlik", "Quvonch", "Baxt", "Hursandchilik", "Hayrat", "Faxr", "G'urur", "Qiziqish", "Sog'inch", "Orzu", "Havas", "Samimiyat", "Qo'rquv", "Vahima", "Xavotirlanish", "Tashvish", "Iztirob", "Alam", "G'am", "Hasrat", "Yolg'izlik", "Jahldorlik", "G'azab", "Nafrat", "Hasad", "Achinish", "Afsuslanish", "Uyat", "Xijolat", "Ishonchsizlik", "Motam", "Qayg'u", "Hayajon", "O'kinch", "Xafalik", "G'araz", "Umidsizlik", "Shubha", "Iztirob", "Vijdon"
        produxtalar = "Go'sht", "Baliq", "Yog'", "Saryog'", "Un", "Non", "Makaron", "Guruch", "Mosh", "Noxat", "Loviya", "Tuxum", "Sut", "Qatiq", "Qaymoq", "Tvorog", "Pishloq", "Kolbasa", "Sosiska", "Qand", "Shakar", "Asal", "Choy", "Qahva", "Tuz", "Murch", "Zira", "Kashnich", "Ukrop", "Sirke", "Ketchup", "Mayonez"
        movies = "Titanik", "Avatar", "Terminator", "Rambo", "Rokki", "Gladiator", "Spartak", "Jasur yurak", "Matritsa", "Yulduzlararo", "GarriPotter", "Uzuklarhukmdori", "Xobbit", "O'rgimchakodam", "Supermen", "Betmen", "Temirodam", "Qasoskorlar", "QoraPantera", "Forsaj", "Transformatorlar", "Yuradavri", "KingKong", "Godzilla", "Qirolsher", "Uydayolg'iz", "Tarzan", "Alovuddin", "Muzlikdavri", "Shrek", "Madagaskar", "KungFuPanda", "Muzyurak", "TomvaJerri", "Pokémon", "Kalmaro'yini", "Qamoqdanqochish", "Taxtlaro'yini", "Mahalladaduvduvgap", "Abdullajon", "Shumbola"
        diniy = "Alloh", "Quron", "Hadis", "Islom", "Iymon", "Musulmon", "Ummat", "Duo", "Namoz", "Ro'za", "Haj", "Zakot", "Sadaqa", "Halol", "Harom", "Qibla", "Masjid", "Azon", "Ibodat", "Sajda", "Ruku", "Qiyom", "Takbir", "Tasbeh", "Tahorat", "G'usl", "Tayammum", "Imom", "Muazzin", "Jamoat", "Vitr", "Sunnat", "Farz", "Nafl", "Tarovih", "Janoza", "Sura", "Oyat", "Juz", "Tajvid", "Qiroat", "Tafsir", "Tazkiya", "Zikr", "Tasavvuf", "Tarbiya", "Shirk", "Kufr", "Munofiq", "Taqvo", "Sabr", "Shukr", "Adolat", "Tavba", "Payg'ambar", "Sahoba", "Ramazon", "Hayit", "Hijrat", "Inshaalloh", "Alhamdulillah", "Subhanalloh", "Lailahaillalloh", "Astagfirulloh", "Jannat", "Do'zax", "Mahshar", "Sirat", "Qazo", "Qadar" # 70 
        zvaniya = "Askar", "Kichikserjant", "Serjant", "Kattaserjant", "KichikLeytenant", "Leytenant", "KattaLeytenant", "Kapitan", "Mayyor", "Podpolkovnik", "Polkovnik", "Generalmayor", "GeneralLeytenant", "GeneralPolkovnik", "General"
        inson_haraktirlari = "Mehribon", "Sadoqatli", "Halol", "Adolatli", "Sabrli", "Shukrli", "Ishchan", "Mehnatkash", "Jasur", "Oqko'ngil", "Samimiy", "Tashabbuskor", "Sahiy", "Fidoiy", "Mard", "Muloyim", "Iymonli", "Oqibatli", "G'ururli", "Qadrdon", "O'zgaruvchan", "Topqir", "Tezkor", "Yordamchi", "Masuliyatli", "Qanoatli", "Xushmuomala", "Kamtar", "O'jar", "Maqtanchoq", "Mag'rur", "Ikkiyuzlamachi", "Adolatsiz", "Yolg'onchi", "Xasis", "Ochko'z", "Qo'rqoq", "Dangasa", "Jahldor", "Hasadchi", "Beparvo", "Qo'pol", "Nozik", "Oqil", "Tarbiyali", "Odobli", "Ishonchli", "O'ylovchan", "Sergap", "Hayolparast", "Hazilkash", "Xushchaqchaq"
        games = "Shaxmat", "Shashka", "Domino", "Narda", "Karta", "Futbol", "Basketbol", "Voleybol", "Tennis", "Badminton", "Bilyard", "Bowling", "PUBG", "Durak", "FIFA", "PES", "ClashofClans", "ClashRoyale", "CandyCrush", "AngryBirds"
        cities = "Parij", "London", "Dubai", "Tokio", "Roma", "Istanbul", "Madrid", "Berlin", "Maskva", "Pekin", "Shanxay", "Toshkent", "Samarqand", "Bali", "Antaliya", "Seul", "Bangkok", "Barselona", "LasVegas", "HongKong", "LosAngeles", "Sidney", "Florensiya", "Granada", "Sevilya", "Valensiya", "Bilbao", "Lyon", "Shiraz", "Qohira", "Budapesht", "Colombo", "KualaLumpur", "SanFransisko", "RiodeJaneyro", "Kasablanka", "Marakesh", "SanktPeterburg", "Mexiko" # 40
        banks = "Xalq", "Agro", "Mikrokredit", "Aloqa", "Ipoteka", "Turon", "Asaka", "Tenge", "Kapital", "Universal", "Hamkor", "Anor", "Davr", "Uzum", "Savdogar", "OrientFinans", "IpakYo'li", "Garant", "Infin", "Markaziy"
        futbol_jamoalar = "RealMadrid", "Barselona", "Atletiko", "Sevilla", "Valensia", "Villarreal", "Liverpool", "Chelsea", "Arsenal", "Tottenham", "Newcastle", "AstonVilla", "Everton", "WestHam", "Bavariya", "Borussia", "Juventus", "Inter", "Milan", "Napoli", "Roma", "Lazio", "PSG", "Ajax", "Porto", "Benfica", "Galatasaray",  "Lokomotiv", "AlHilal", "AlNassr", "Paxtakor", "Navbahor", "Bunyodkor", "Nasaf"
        football_players = "Pele", "Maradona", "Zidane", "Ronaldo", "Ronaldinho", "Karlos", "Pirlo", "Beckham", "Raul", "Henry", "DelPiero", "Kaka", "Eto'o", "Drogba", "Shevchenko", "Torres", "Rooney", "Lampard", "Gerrard", "Xavi", "Iniesta", "Casillas", "Puyol", "Neuer", "DaniAlves", "Marcelo", "Pique", "Ramos", "Vidic", "Terry", "Ferdinand", "Nesta", "Cannavaro", "Buffon", "Cristiano", "Messi", "Neymar", "Suarez", "Bale", "Lewandowski", "Benzema", "Ibragimovich", "Mbappe", "Haaland", "DeBruyne", "Modric", "Kroos", "Muller", "Schweinsteiger", "Robben", "Ribery", "O'zil", "Hazard", "Griezmann", "Kane", "Mane", "Salah", "Aubameyang", "Cavani", "Aguero", "DiMaria", "Dybala", "Coutinho", "DavidVilla", "Hierro", "Sanchez", "Navas", "Courtois"
        sifatlar = "katta", "kichik", "uzun", "qisqa", "baland", "past", "issiq", "sovuq", "qalin", "yupqa", "keng", "tor", "tez", "sekin", "yangi", "eski", "chiroyli", "xunuk", "yumshoq", "qattiq"
        oq = "qor", "sut", "bo'r", "un", "paxta", "tuz", "shakar", "kefir", "qog'oz", "yog'"  
        qora = "ko'mir", "qahva", "choy", "tun", "ruchka"  
        qizil = "olcha", "gilos", "anor", "atirgul", "qon", "qizilolma"  
        yashil = "barg", "maysa", "ko'kat", "ismaloq", "bodring", "kivi", "archa"  
        sariq = "limon", "banan", "jo'xori", "kungaboqar", "asal", "sabzi", "oltin"  
        kok = "osmon", "dengiz", "ruchka", "choy"
        osmon = "quyosh", "oy", "bulut", "yulduz", "samolyot", "raketa", "osmon", "qush", "kamalak", "parashyut"
        shirinlik = "shokolad", "konfet", "tort", "pechenye", "pahlava", "murabbo", "shakar", "medavoy", "vafli"
        joy = "maktab", "kasalxona", "bozor", "uy", "kutubxona", "park", "masjid", "oshxona", "stadion", "teatr"
        mebel = "stol", "stul", "divan", "kreslo", "karovat", "javon", "eshik", "deraza", "gilam", "oyna"
        quyosh_tizimi = "yer", "oy", "quyosh", "mars", "venera", "yupiter", "saturn", "uran", "neptun", "merkuriY", "platon", "asteroid", "kometa", "orbitA", "atmosfera", "meteorit", "yulduz", "galaktika", "koinot", "kosmos"
        matematika = "Son", "Raqam", "Nol", "Bir", "Ikki", "Uch", "To'rt", "Besh", "Olti", "Yetti", "Sakkiz", "To'qqiz", "O'n", "Yuz", "Ming", "Million", "Milliard", "Juft", "Toq", "Qo'shish", "Ayirish", "Ko'paytirish", "Bo'lish", "Qoldiq", "Foiz", "Daraja", "Kvadrat", "Kub", "IldizOsti", "Yig'indi", "Ayirma", "Kasr", "Musbat", "Manfiy", "NaturalSon", "Butunson", "Ratsionalson", "Irratsionalson", "Radius", "Diametr", "Aylana", "Doira", "Perimetr", "Yuza", "Hajm", "Uchburchak", "To'rtburchak", "To'g'riburchak", "O'tkirburchak", "O'tmasburchak", "Paralel", "Perpendikulyar", "Chiziq", "Koordinata", "Grafik", "Formula", "Misol", "Masala", "Javob", "Tenglama", "Tengsizlik", "Funksiya", "Qiymat", "Logarifm", "Trigonometrik", "Sinus", "Kosinus", "Tangens", "Kotangens", "Pifagor", "Determinant", "Vektor", "Hisoblash", "Proportsiya", "Diagramma", "Faktorial", "Mediana", "Limit", "Integral", "Hosila" # 80         
        fizika = "Modda", "Jism", "Zarra", "Atom", "Molekula", "Proton", "Neytron", "Elektron", "Massa", "Hajm", "Zichlik", "Tezlik", "Tezlanish", "Vaqt", "Energiya", "Ish", "Quvvat", "Harakat", "Inersiya", "Kuch", "Tortish kuchi", "Gravitatsiya", "Ishqalanish", "Impuls", "Moment", "Bosim", "Og'irlik", "Arximedkuchi", "Prujina", "Taranglikkuchi", "Blok", "Harorat", "Termometr", "Issiqlik", "Qaynash", "Erish", "Bug'lanish", "Kondensatsiya", "Sublimatsiya", "Kaloriya", "Kelvin", "Tselsiy", "Farengeyt", "Tok", "Kuchlanish", "Qarshilik", "Ampermetr", "Voltmetr", "Galvanometr", "Generator", "Transformator", "Elektromagnit", "Magnitmaydon", "Tokkuchi", "Kondensator", "Induktsiya", "Elektrod", "Elektr", "Dielektrik", "Yoruglik", "Nurlanish", "Refleksiya", "Sinish", "Linza", "Oyna", "Mikroskop", "Teleskop", "Spektr", "Lazer", "Tovush", "Chastota", "Amplituda", "To'lqin", "Uzunlik", "Rezonans", "Vibratsiya", "Akustika", "Infratovush", "Ultratovush", "Termodinamika", "Konveksiya", "Radiatsiya", "Sig'imi", "O'tkazuvchanlik", "Entropiya", "Supero'tkazgich", "Dispersiya", "Interferensiya", "Difraksiya", "Kvant", "Foton", "Yadro", "Alfa", "Beta", "Gamma", "Relativlik", "Qoratuynuk", "Kvars" # 100
        kimyo = "Modda", "Element", "Atom", "Molekula", "Proton", "Neytron", "Elektron", "Izotop", "Ion", "Kation", "Anion", "Gaz", "Suyuqlik", "Plazma", "Uglerod", "Vodorod", "Kislorod", "Azot", "Metan", "Etan", "Propan", "Butan", "Natriy", "Kaliy", "Kaltsiy", "Magniy", "Alyuminiy", "Temir", "Mis", "Rux", "Qalay", "Qo'rg'oshin", "Oltin", "Kumush", "Platina", "Xlor", "Ftor", "Brom", "Yod", "Sul'fur", "Fosfor", "Silikon", "Benzol", "Spirt", "Glyukoza", "Suxaroza", "Oqsil", "Uglevod", "Polimer", "Plastik", "Kauchuk", "Teflon", "Aralashma", "Birikma", "Reaksiya", "Reagent", "Mahsulot", "Katalizator", "Yonish", "Neytrallash", "Oksidlanish", "Qaytarilish", "Eritma", "Erituvchi", "Kislota", "Konsentratsiya", "Diffuziya", "Distillatsiya", "Filtratsiya", "Kristallanish", "Bug'lanish", "Kondensatsiya", "Endotermik", "Ekzotermik", "Probirka", "Kolba", "Byureta", "Pipetka", "Termometr", "Laboratoriya" # 80
        metall = "Oltin", "Kumush", "Mis", "Temir", "Rux", "Qalay", "Qo'rg'oshin", "Alyuminiy", "Platina", "Titan", "Nikel", "Xrom"
        metros = "Olmazor", "Chilonzor", "MirzoUlug'bek", "Novza", "Milliybog'", "Xalqlardo'stligi", "O'zbekiston", "Kosmonavtlar", "Paxtakor", "Mustaqillikmaydoni", "AmirTemur", "HamidOlimjon", "Pushkin", "BuyukIpakyo'li", "Beruniy", "Tinchlik", "Chorsu", "G'afurG'ulom", "AlisherNavoiy", "Oybek", "Toshkent", "Mashinasozlar", "Do'stlik", "Mingo'rik", "YunusRajabiy", "AbdullaQodiriy", "Minor", "Bodomzor", "Shahriston", "Yunusobod", "Turkiston", "Texnopark", "Yashnobod", "Tuzel", "Olmos", "Rohat", "Yangibozor", "Qo'yliq", "Matonat", "Tolariq", "Qiyot", "Xonobod", "Turon", "Chinor", "Qipchoq" 
        company = "Uzcard", "Humo", "Beeline", "Ucell", "Mobiuz", "Uzmobile", "Uztelecom", "Apple", "Samsung", "Huawei", "Nokia", "Sony", "LG", "HP", "Dell", "Asus", "Acer", "Artel", "Akfa", "Google", "Amazon", "Facebook", "Intel", "Nike", "Adidas", "Puma", "Zara", "Gucci", "Prada", "Rolex", "Canon", "Nikon", "Panasonic", "Bosch", "Nestle", "CocaCola", "Pepsi", "McDonalds", "Disney", "Pixar", "Marvel", "Fox", "Starbucks", "Lenovo", "Microsoft", "Epam", "Netflix", "Tesla", "SpaceX", "Toshiba", "Hitachi", "Yandex", "Alibaba" 
        program = "Oson", "Click", "Payme", "Paynet", "IMO", "OLX", "Clock", "Word", "Excel", "Zoom", "Gmail", "Google", "Browser", "Telegram", "Messenger", "WhatsApp", "Instagram", "Facebook", "YouTube", "Calendar", "Gallery", "Calculator", "Viber", "Skype", "Shazam", "Netflix", "Chrome", "MXPlayer", "Canva", "Twitter", "WeChat", "MyTaxi", "YandexGo", "GooglePlay", "PlayMarket", "AppStore", "GoogleMaps", "VoiceRecorder", "PowerPoint", "AnyDesk", "CapCut", "ChatGPT", "Telegraph", "Snapchat", "BigoLive", "AliExpress", "Amazon", "ZoodMall", "UzumMarket" # 50
        programming = "R", "Go", "PHP", "CSS", "Git", "SQL", "JSON", "XML", "Dart", "Rust", "Ruby", "Java", "Sass", "Less", "HTML", "Nodejs", "Linux", "Swift", "Vue", "jQuery", "Oracle", "MySQL", "Python", "React", "GSAP", "Flask", "Redis", "Vue", "Nextjs", "Nuxtjs", "MongoDB", "Chartjs", "Threejs", "Docker", "GitHub", "GitLab", "aHost", "Heroku", "Netlify", "Vercel", "Railway", "Firebase", "SQLite", "Tailwind", "Angular", "Django", "Spring", "Laravel", "Symfony", "NestJS", "FastAPI", "Expressjs", "Bootstrap", "Postman", "WebStorm", "PhpStorm", "CLion", "Xcode", "VSCode", "Brackets", "Webpack", "Matlab", "Kotlin", "Kalkulyator", "VisualStudio", "PyCharm", "Nextjs", "ObjectiveC", "IntelliJ IDEA", "AndroidStudio", "SublimeText", "CodeBlocks", "DigitalOcean", "JupyterNotebook", "PostgreSQL", "GoogleCloud", "WebSocket" # 80
        tecnology = "Soat", "Radio", "GPS", "WiFi", "iOS", "VPN", "iPad", "iPhone", "Dron", "Robot", "Kamera", "Planshet", "Android", "SIMkarta", "Naushnik", "Quloqchin", "Fleshka", "Windows", "Laptop", "Monitor", "Printer", "Skaner", "Server", "Router", "Kompyuter", "Smartfon", "Kalkulyator", "Televizor", "Muzlatgich", "Kirmashina", "Changyutgich", "Mikropech", "Gazplita", "Ventilyator", "Termometr", "Bankomat", "Navigator", "Notebook", "Klaviatura", "Protsessor", "Bluetooth", "Internet", "Zaryadlagich", "PowerBank", "Smartwatch", "Konditsioner", "PlayStation", "Desktop", "Modem" # 50      





        lvl_1 = {
            "category": "Ism",
            "word": random.choice(names),
        }

        lvl_2 = {
            "category": "Rang",
            "word": random.choice(colors),
        }

        lvl_3 = {
            "category": "Kalendar",
            "word": random.choice(calendar),
        }

        lvl_4 = {
            "category": "Hayvon",
            "word": random.choice(animals),
        }

        lvl_5 = {
            "category": "Meva",
            "word": random.choice(fruit),
        }

        lvl_6 = {
            "category": "Sabzavot",
            "word": random.choice(vegetables),
        }

        lvl_7 = {
            "category": "Ovqat",
            "word": random.choice(ovqatlar),
        }

        lvl_8 = {
            "category": "Ob-Havo",
            "word": random.choice(obhavo),
        }

        lvl_9 = {
            "category": "Transport turlari",
            "word": random.choice(transport),
        }

        lvl_10 = {
            "category": "Ovqat",
            "word": random.choice(osimliklar),
        }

        lvl_11 = {
            "category": "Ichimlik",
            "word": random.choice(ichimlik),
        }

        lvl_12 = {
            "category": "Fan",
            "word": random.choice(fan),
        }

        lvl_13 = {
            "category": "Vaqt",
            "word": random.choice(vaqt),
        }

        lvl_14 = {
            "category": "Qurol",
            "word": random.choice(qurollar),
        }

        lvl_15 = {
            "category": "Musiqa Asbobi",
            "word": random.choice(musiqa_asboblari),
        }

        lvl_16 =  {
            "category": "Oila azosi yoki Qarindosh",
            "word": random.choice(oila_va_qarindoshlar),
        }

        lvl_17 = {
            "category": "Inson tana azolari",
            "word": random.choice(human_body),
        }

        lvl_18 = {
            "category": "Sport turi",
            "word": random.choice(sports),
        }
        
        lvl_19 = {
            "category": "Maktab anjomi",
            "word": random.choice(maktab_anjomlar),
        }

        lvl_20 = {
            "category": "Kasb",
            "word": random.choice(jobs),
        }

        lvl_21 = {
            "category": "Tabiat",
            "word": random.choice(names),
        }

        lvl_22 = {
            "category": "Qush",
            "word": random.choice(birds),
        }

        lvl_23 = {
            "category": "Telefon",
            "word": random.choice(phones),
        }

        lvl_24 = {
            "category": "Uzb Shahar-tumanlar",
            "word": random.choice(uzb_regions),
        }

        lvl_25 = {
            "category": "Davlatlar",
            "word": random.choice(countries),
        }

        lvl_26 = {
            "category": "Kiyim-Kichak",
            "word": random.choice(kiyim_kichaklar),
        }

        lvl_27 = {
            "category": "Oshxona buyumlar",
            "word": random.choice(oshxona_buyumlar),
        }

        lvl_28 = {
            "category": "Moshina",
            "word": random.choice(cars),
        }

        lvl_29 = {
            "category": "His-tuyg'u",
            "word": random.choice(his_tuygular),
        }

        lvl_30 = {
            "category": "Produxta",
            "word": random.choice(produxtalar),
        }

        lvl_31 = {
            "category": "Kino nomi",
            "word": random.choice(movies),
        }

        lvl_32 = {
            "category": "Islomiy so'zlar",
            "word": random.choice(diniy),
        }

        lvl_33 = {
            "category": "Unvon",
            "word": random.choice(zvaniya),
        }

        lvl_34 = {
            "category": "Inson haraktiri",
            "word": random.choice(inson_haraktirlari),
        }

        lvl_35 = {
            "category": "O'yin",
            "word": random.choice(games),
        }

        lvl_36 = {
            "category": "Mashhur Shahar",
            "word": random.choice(cities),
        }

        lvl_37 = {
            "category": "Bank",
            "word": random.choice(banks),
        }

        lvl_38 = {
            "category": "Futbol klub",
            "word": random.choice(futbol_jamoalar),
        }

        lvl_39 = {
            "category": "Futbolchi",
            "word": random.choice(football_players),
        }

        lvl_40 = {
            "category": "Sifat",
            "word": random.choice(sifatlar),
        }

        lvl_41 = {
            "category": "Oq rang",
            "word": random.choice(oq),
        }

        lvl_42 = {
            "category": "Qora rang",
            "word": random.choice(qora),
        }

        lvl_43 = {
            "category": "Qizil rang",
            "word": random.choice(qizil),
        }

        lvl_44 = {
            "category": "Sariq rang",
            "word": random.choice(sariq),
        }

        lvl_45 = {
            "category": "Yashil rang",
            "word": random.choice(yashil),
        }

        lvl_46 = {
            "category": "Ko'k rang",
            "word": random.choice(kok),
        }

        lvl_47 = {
            "category": "Osmon",
            "word": random.choice(osmon),
        }

        lvl_48 = {
            "category": "Shirinlik",
            "word": random.choice(shirinlik),
        }

        lvl_49 = {
            "category": "Joy (bino)",
            "word": random.choice(joy),
        }

        lvl_50 = {
            "category": "Mebel",
            "word": random.choice(mebel),
        }

        lvl_51 = {
            "category": "Quyosh tizimi",
            "word": random.choice(quyosh_tizimi),
        }

        lvl_52 = {
            "category": "Matematika",
            "word": random.choice(matematika),
        }

        lvl_53 = {
            "category": "Fizika",
            "word": random.choice(fizika),
        }

        lvl_54 = {
            "category": "Kimyo",
            "word": random.choice(kimyo),
        }

        lvl_55 = {
            "category": "Metall",
            "word": random.choice(metall),
        }

        lvl_56 = {
            "category": "Metro bekati",
            "word": random.choice(metros),
        }

        lvl_57 = {
            "category": "Kampaniya",
            "word": random.choice(company),
        }

        lvl_58 = {
            "category": "Kerakli Dasturlar",
            "word": random.choice(program),
        }

        lvl_59 = {
            "category": "Dasturlash",
            "word": random.choice(programming),
        }

        lvl_60 = {
            "category": "Texnologiya",
            "word": random.choice(tecnology),
        }
 
        summ = [lvl_1, lvl_2, lvl_3, lvl_4, lvl_5, lvl_6, lvl_7, lvl_8, lvl_9, lvl_10, lvl_11, lvl_12, lvl_13, lvl_14, lvl_15, lvl_16, lvl_17, lvl_18, lvl_19, lvl_20, lvl_21, lvl_22, lvl_23, lvl_24, lvl_25, lvl_26, lvl_27, lvl_28, lvl_29, lvl_30, lvl_31, lvl_32, lvl_33, lvl_34, lvl_35, lvl_36, lvl_37, lvl_38, lvl_39, lvl_40, lvl_41, lvl_42, lvl_43, lvl_44, lvl_45, lvl_46, lvl_47, lvl_48, lvl_49, lvl_50, lvl_51, lvl_52, lvl_53, lvl_54, lvl_55, lvl_56, lvl_57, lvl_58, lvl_59, lvl_60]

        # ID qo‘shish
        data = [{"id": i + 1, **item} for i, item in enumerate(summ)]

        return Response(data)
    

class CrosswordAPIView(APIView):
    def get(self, request):
        data = [
            {
                "level": 1,
                "letters": ["B","O","L","A"],
                "words": ["BOL","LAB","OLO"]
            },
            {
                "level": 2,
                "letters": ["K","U","T","I","B"],
                "words": ["KITOB","BUT","TIB"]
            },
            {
                "level": 3,
                "letters": ["S","O","N","I","Y"],
                "words": ["SON","SINO","YON"]
            },
            {
                "level": 4,
                "letters": ["D","A","R","S","T"],
                "words": ["DARS","STAR","DRAS"]
            },
            {
                "level": 5,
                "letters": ["Q","I","L","O","M"],
                "words": ["QIL","QILOM","MOL"]
            },
            {
                "level": 6,
                "letters": ["O","T","I","S","H"],
                "words": ["OTISH","HITS","TOSH"]
            },
            {
                "level": 7,
                "letters": ["Y","U","G","U","R","T"],
                "words": ["YUGURT","GURU","TUGU"]
            },
            {
                "level": 8,
                "letters": ["F","A","R","M","O","N"],
                "words": ["FARMO","RAMON","MON"]
            },
            {
                "level": 9,
                "letters": ["X","I","S","O","B"],
                "words": ["XISOB","BOSH","SHOX"]
            },
            {
                "level": 10,
                "letters": ["S","A","H","O","B","I"],
                "words": ["SAHOBI","HIBA","OBI"]
            }
        ]
 
        return Response(data)


class CrosswordAPIView(APIView):
    def get(self, request):
        data = [
            {
                "level": 1,
                "words": ["CAT", "DOG", "BIRD", "FISH"]
            },
            {
                "level": 2,
                "words": ["APPLE", "PEAR", "PLUM", "MANGO", "GRAPE"]
            },
            {
                "level": 3,
                "words": ["RED", "BLUE", "GREEN", "YELLOW", "PINK"]
            },
            {
                "level": 4,
                "words": ["CAR", "BUS", "TRAIN", "PLANE", "BIKE"]
            },
            {
                "level": 5,
                "words": ["JAVA", "DART", "FLUTTER", "KOTLIN", "PYTHON"]
            },
            {
                "level": 6,
                "words": ["EARTH", "MARS", "VENUS", "JUPITER", "PLUTO"]
            },
            {
                "level": 7,
                "words": ["BOOK", "PEN", "PAPER", "BAG", "CHAIR"]
            },
            {
                "level": 8,
                "words": ["MUSIC", "DANCE", "PAINT", "MOVIE", "DRAMA"]
            },
            {
                "level": 9,
                "words": ["TASHKENT", "LONDON", "PARIS", "TOKYO", "BERLIN"]
            },
            {
                "level": 10,
                "words": ["UZBEKISTAN", "KAZAKHSTAN", "KYRGYZSTAN", "TAJIKISTAN", "TURKMENISTAN"]
            }
        ]

 
        return Response(data)
