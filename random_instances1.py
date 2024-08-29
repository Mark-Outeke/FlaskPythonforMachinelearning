import random
import json
from datetime import datetime, timedelta

# Sample list of Ugandan names
uganda_names = [
    "Akello",
"Okello",
"Mbabazi",
"Apio",
"Asiimwe",
"Auma",
"Nabirye",
"Biira",
"Opio",
"Tumusiime",
"Birungi",
"Muhindo",
"Babirye",
"Byaruhanga",
"Natukunda",
"Odongo",
"Kabugho",
"Kiiza",
"Adong",
"Nabwire",
"Atim",
"Mugisha",
"Bwambale",
"Kato",
"Ojok",
"Nangobi",
"Naigaga",
"Adongo",
"Byamukama",
"Nalubega",
"Masika",
"Katushabe",
"Namatovu",
"Acen",
"Ajok",
"Namutebi",
"Otim",
"Matovu",
"Ogwang",
"Mbambu",
"Musinguzi",
"Lubega",
"Nakato",
"Nansubuga",
"Nsubuga",
"Bako",
"Kyomugisha",
"Ninsiima",
"Mutesi",
"Akullu",
"Katusabe",
"Katusiime",
"Akumu",
"Mukasa",
"Tumwebaze",
"Waiswa",
"Ahimbisibwe",
"Ocen",
"Arinaitwe",
"Agaba",
"Okot",
"Kansiime",
"Tusiime",
"Namubiru",
"Kobusingye",
"Baguma",
"Tumuhimbise",
"Candiru",
"Masereka",
"Awor",
"Namaganda",
"Nakate",
"Mugisa",
"Nabukenya",
"Isabirye",
"Nakyanzi",
"Akol",
"Ogwal",
"Baluku",
"Bukenya",
"Kyomuhendo",
"Omara",
"Tumwesigye",
"Muhumuza",
"Atuhaire",
"Mubiru",
"Nantongo",
"Okumu",
"Asio",
"Nyangoma",
"Nekesa",
"Nakanwagi",
"Sunday",
"Wandera",
"Chebet",
"Nambuya",
"Namulondo",
"Anyango",
"Tugume",
"Aciro",
"Nambozo",
"Namukose",
"Acan",
"Namakula",
"Nankya",
"Aguti",
"Nanyonga",
"Namara",
"Tumushabe",
"Kyomukama",
"Nabakooza",
"Odong",
"Namusisi",
"Namuli",
"Nuwagaba",
"Kule",
"Sanyu",
"Akullo",
"Wasswa",
"Mirembe",
"Kakooza",
"Busingye",
"Kizza",
"Nansamba",
"Kagoya",
"Aceng",
"Musisi",
"Namuddu",
"Ainembabazi",
"Kisembo",
"Kiwanuka",
"Nakalema",
"Mwesigwa",
"Nantale",
"Nambi",
"Namukasa",
"Nyakato",
"Namata",
"Nagawa",
"Tusingwire",
"Kiconco",
"Chandiru",
"Amuge",
"Asaba",
"Nanyonjo",
"Tumwine",
"Katongole",
"Kizito",
"Apolot",
"Ndagire",
"Nayiga",
"Kobusinge",
"Mutebi",
"Twesigye",
"Nakabugo",
"Mugerwa",
"Kyomuhangi",
"Ayikoru",
"Opolot",
"Angom",
"Musoke",
"Nafuna",
"Muwonge",
"Twinomugisha",
"Bogere",
"Muhwezi",
"Nayebare",
"Mwesigye",
"Mutonyi",
"Twikirize",
"Nafula",
"Mukisa",
"Nabukeera",
"Logose",
"Kasozi",
"Chemutai",
"Awino",
"Ssali",
"Businge",
"Atimango",
"Alum",
"Twinomujuni",
"Nandutu",
"Tumuhairwe",
"Karungi",
"Ayoo",
"Namayanja",
"Komakech",
"Kyarimpa",
"Nanteza",
"Nabatanzi",
"Kusemererwa",
"Tushabe",
"Gumisiriza",
"Nazziwa",
"Mugume",
"Sande",
"Mwesige",
"Kisakye",
"Nalukwago",
"Onyango",
"Isingoma",
"Nassali",
"Ayo",
"Mayanja",
"Kembabazi",
"Namwanje",
"Kyarisiima",
"Alupo",
"Bwire",
"Ouma",
"Kintu",
"Nuwamanya",
"Nampijja",
"Nandudu",
"Monday",
"Yiga",
"Nalumansi",
"Mujuni",
"Namusoke",
"Ongom",
"Namutosi",
"Ngobi",
"Namanya",
"Acayo",
"Nantume",
"Kyarikunda",
"Naturinda",
"Nakintu",
"Apiyo",
"Ejang",
"Night",
"Nalwoga",
"Acio",
"Byarugaba",
"Awori",
"Akao",
"Kamugisha",
"Kemigisa",
"Kabagambe",
"Ngabirano",
"Nakazibwe",
"Tushemerirwe",
"Wafula",
"Ssentongo",
"Akidi",
"Achieng",
"Akot",
"Okiror",
"Lukwago",
"Kemirembe",
"Namagembe",
"Namirembe",
"Nakitende",
"Kirabo",
"Nakamya",
"Nagudi",
"Namono",
"Among",
"Katende",
"Ithungu",
"Komugisha",
"Akankwasa",
"Musiimenta",
"Kemigisha",
"Baluka",
"Opiyo",
"Orishaba",
"Akech",
"Tumukunde",
"Mugabi",
"Alinaitwe",
"Abalo",
"Mudondo",
"Mucunguzi",
"Amongin",
"Tino",
"Chelangat",
"Lakot",
"Niwagaba",
"Akurut",
"Ayebazibwe",
"Kyaligonza",
"Achola",
"Kakuru",
"Tumuramye",
"Nalwadda",
"Mulindwa",
"Kasule",
"Thembo",
"Kyeyune",
"Nanyanzi",
"Akongo",
"Nasasira",
"Akugizibwe",
"Adeke",
"Kaahwa",
"Nakafeero",
"Nalwanga",
"Amongi",
"Tuhaise",
"Driciru",
"Nalugo",
"Ssemakula",
"Okwir",
"Athieno",
"Nakiwala",
"Nalubowa",
"Nanfuka",
"Olupot",
"Namwase",
"Wabwire",
"Nakirya",
"Mwanje",
"Mugoya",
"Kyakimwa",
"Amoding",
"Kamya",
"Namugenyi",
"Kasande",
"Ochieng",
"Mukiibi",
"Mugabe",
"Namataka",
"Kebirungi",
"Kakayi",
"Namanda",
"Adiru",
"Nakitto",
"Kavuma",
"Musimenta",
"Ocan",
"Nakibuuka",
"Twebaze",
"Byamugisha",
"Mugenyi",
"Were",
"Mugala",
"Atugonza",
"Amony",
"Turyahebwa",
"Kafuko",
"Odeke",
"Masaba",
"Turyasingura",
"Twinamatsiko",
"Lwanga",
"Nakimuli",
"Kalema",
"Okurut"
]

# Function to generate a random date between two dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

# Generate tracked entity instances
tracked_entity_instances = []
start_date = datetime.strptime("2019-01-01", "%Y-%m-%d")
end_date = datetime.strptime("2024-12-31", "%Y-%m-%d")

for i in range(500):
    name = random.choice(uganda_names)
    surname = random.choice(uganda_names)
    enrollment_date = random_date(start_date, end_date).strftime("%Y-%m-%dT00:00:00.000")

    instance = {
        "trackedEntityType": "MCPQUTHX1Ze",
        "orgUnit": "Q6qNTXu3yRx",
        "attributes": [
            {
                "attribute": "Ewi7FUfcHAD",
                "value": f"{random.randint(100000000, 999999999)}{random.choice('abcdefghijklmnopqrstuvwxyz')}"
            },
            {
                "attribute": "GnL13HAVFOm",
                "value": random.choice(["Male", "Female"])
            },
            {
                "attribute": "ZkNZOxS24k7",
                "value": f"{random.randint(1000, 9999)}/{random.randint(10, 99)}"
            },
            {
                "attribute": "jWjSY7cktaQ",
                "value": random.choice(["Acanit",
"Achen",
"Akello",
"Ba",
"Baadal",
"Baadal",
"Baageshawaree",
"Baageshree",
"Baageshwari",
"Baahir",
"Baahir",
"Baahir",
"Baaji",
"Baako",
"Baal",
"Baala",
"Baala",
"Baalaa",
"Baalaaji",
"Baalaamani",
"Baalaamjali",
"Baalaark",
"Baalaraju",
"Baalath",
"Baalath-beer",
"Baalayya",
"Baal-berith",
"Baal-gad",
"Baal-hamon",
"Baal-hermon",
"Baali",
"Baalim",
"Baalis",
"Baalkrishan",
"Baalkrishan",
"Baal-meon",
"Baal-peor",
"Baal-perazim",
"Baal-shalisha",
"Baal-tamar",
"Baalzebub",
"Baal-zebub",
"Baal-zephon",
"Baanah",
"Baanan",
"Baanbhatt",
"Baani",
"Baanke",
"Baanuraekha",
"Baaodhav",
"Baapiraaju",
"Baaqi",
"Baari",
"Baariq",
"Baaseiah",
"Baasha",
"Baasha",
"Baasim",
"Baasim",
"Baasim",
"Baasima",
"Baasima",
"Baasima",
"Baasit",
"Baasu",
"Bab",
"Bacia",
"Bale",
"Bülent",
"C“ng",
"Ca",
"Ca",
"Cabal",
"Cabbon",
"Cabe",
"Cable",
"Cable",
"Cabul",
"Caca",
"Cacamwri",
"Cacanisius",
"Cace",
"Cacey",
"Cacey",
"Cachamwri",
"Cachi",
"Caci",
"Cacia",
"Cacia",
"Cacia",
"Cadabyr",
"Cadarn",
"Cadawg",
"Cadby",
"Cadby",
"Cadda",
"Caddaham",
"Caddaric",
"Caddarik",
"Caddawyc",
"Caddell",
"Caddoc",
"Caddock",
"Cade",
"Cade",
"Cade",
"Cadee",
"Cadee",
"Cadel",
"Cadell",
"Cadell",
"Cadellin",
"Caden",
"Cadena",
"Cadence",
"Cadence",
"Cadence",
"Cadence",
"Cadencia",
"Cadenza",
"Cadeo",
"Cadhla",
"Cadhla",
"Cadi",
"Cadi",
"Cadi",
"Cadie",
"Cadie",
"Cadis",
"Cadman",
"Cadman",
"Cadman",
"Cadman",
"D‚l",
"D‚sh",
"D‚wei",
"Da",
"Da",
"Daamin",
"Daaminee",
"Daamodar",
"Daana",
"Daanesh /Daanish",
"Daania",
"Daania",
"Daania",
"Daanish",
"Daanish",
"Daanveera",
"Daanya",
"Daarshik",
"Daaruk",
"Daarun",
"Daasu",
"Daba",
"Dabang",
"Dabareh",
"Dabbah",
"Dabbasheth",
"Dabeet",
"Dabeet",
"Daberath",
"Dabhit",
"Dabhiti",
"Dabi",
"Dabir",
"Dabir",
"Dabir",
"Dabria",
"Dace",
"Dace",
"Dace",
"Dacey",
"Dacey",
"Dacey",
"Dacey",
"Dacia",
"Dacia",
"Dacian",
"Dacian",
"Dacian",
"Dacio",
"Dacio",
"Dack",
"Dacso",
"Dacy",
"Dad",
"Dad",
"D'Angelo",
"D'anton",
"D'Arcy",
"D'Arcy",
"D'arcy",
"D'Arcy",
"D'arcy",
"D'Ary",
"Dembe",
"D'or",
"Ea",
"Eachan",
"Eachann",
"Eachann",
"Eachthighearn",
"Eacnung",
"Eada",
"Eadaion",
"Eadbeorht",
"Eadbert",
"Eadburt",
"Eadda",
"Eadelmarr",
"Eadgar",
"Eadgard",
"Eadger",
"Eadgyth",
"Eadgyth",
"Eadig",
"Eadignes",
"Eadlin",
"Eadlyn",
"Eadmund",
"Eadmund",
"Eadric",
"Eadsele",
"Eadward",
"Eadward",
"Eadwardsone",
"Eadweald",
"Eadweard",
"Eadwiella",
"Eadwine",
"Eadwine",
"Eadwyn",
"Eadwyn",
"Eagan",
"Eagon",
"Eairrdsidh",
"Eairrsidh",
"Eakant",
"Eakshaa",
"Ealadhach",
"Ealahweemah",
"Ealaot Wadass",
"Ealaothek Kaunis",
"Ealasaid",
"Ealdian",
"Ealdun",
"Ealdwode",
"Ealga",
"Ealhdun",
"Ealhhard",
"Eallair",
"Eallard",
"Eallison",
"Ealuvig",
"Eaman",
"Eames",
"Eamon",
"Eamon",
"Eamon",
"Eamon",
"Eamon",
"Fa",
"Fa Ying",
"Faadi",
"Faadil",
"Faaiq",
"Faaiz",
"Faakhir",
"Faakhir",
"Faakhir",
"Faalgun",
"Faalgunee",
"Faaris",
"Faaris",
"Faarooq",
"Faarooq",
"Faas",
"Faatih",
"Faatin",
"Faatin",
"Faatina",
"Faatir",
"Faaz",
"Faaz",
"Faazel",
"Fabayo",
"Faber",
"Fabi",
"Fabia",
"Fabia",
"Fabian",
"Fabian",
"Fabian",
"Fabian",
"Fabian",
"Fabian, Fabio",
"Fabiana",
"Fabiana",
"Fabianna",
"Fabianne",
"Fabiano",
"Fabien",
"Fabienne",
"Fabio",
"Fabio",
"Fabiola",
"Fabion",
"Fabra",
"Fabre",
"Fabrice",
"Fabrizio",
"Fabrizio",
"Fabrizius",
"Fabron",
"Fabroni",
"Fachnan",
"Faddei",
"Faddei",
"Fadeaushka",
"Fadeelah",
"Fadeelah",
"Fadeuka",
"Fadey",
"Fadey",
"F'enton",
"Jendyose",
"Kaikara",
"Kenyangi",
"Kizza",
"Mirembe",
"Mukasa",
"Naabhi",
"Naadir",
"Naadir",
"Naadir",
"Naag",
"Naag",
"Naag",
"Naagarjun",
"Naagarjun",
"Naagarjun",
"Naagbaalaa",
"Naagchand",
"Naagdhar",
"Naagendra",
"Naagesh",
"Naagpal",
"Naagpal",
"Naagpal",
"Naagpati",
"Naag-raaj",
"Naagraj",
"Naailah",
"Naairah",
"Naa'irah",
"Naajidah",
"Naajy",
"Naajy",
"Naakesh",
"Naakesh",
"Naal",
"Naalnish",
"Naalyehe ya sidahi",
"Naamagal",
"Naamah",
"Naamah",
"Naaman",
"Naaman",
"Naamdev",
"Naamdev",
"Naamit",
"Naanak",
"Naaraayan",
"Naaraayan",
"Naarad",
"Naarah",
"Naarai",
"Naari",
"Naasih",
"Naasih",
"Naathim",
"Naathim",
"Naava",
"Naavah",
"Naavah",
"Naavarasi",
"Naavarasi",
"Naavya",
"Naayantara",
"Naayantara",
"Naayantara",
"Na'eemah",
"Na'ilah",
"Na'imah",
"Namazzi",
"Nándor",
"Nantale",
"Nasiche",
"Ochen",
"Saa",
"Saabir",
"Saabir",
"Saabira",
"Saachee",
"Saachee",
"Saachi",
"Saachi",
"Saachi",
"Saad",
"Saad",
"Saad",
"Saada",
"Saadaat",
"Saadah",
"Saadah",
"Saadat",
"Saadat",
"Saadhanaa",
"Saadia",
"Saadia",
"Saadiq",
"Saadiya",
"Saadiya",
"Saaedah",
"Saafir",
"Saafir",
"Saagar",
"Saagar",
"Saagarica",
"Saahana",
"Saahid",
"Saahil",
"Saahir",
"Saahir",
"Saaiq",
"Saajana",
"Saajid",
"Saajid",
"Saakaar",
"Saaksh",
"Saakshi",
"Saal",
"Saaleha",
"Saalih",
"Saalih",
"Saaliha",
"Saaliha",
"Saaliha",
"Saaliha",
"Saalima",
"Saam",
"Saaman",
"Saamiya",
"Saamiya",
"Saamiya",
"Saanchi",
"Saanchitha",
"Saandeep",
"Saanidhya",
"Saanjh",
"Saanjh",
"Sølve",
"Sólyom",
"T m",
"Taahir",
"Taahir",
"Taahira",
"Taahira",
"Taalah",
"Taamir",
"Taamir",
"Taamraparnee",
"Taanach",
"Taanach-shilo",
"Taani",
"Taanish",
"Taanusiya",
"Taanvi",
"Taapasee",
"Taaraa",
"Taaraka",
"Taarank",
"Taaresh",
"Taarika",
"Taarikaa",
"Taarush",
"Taavetti",
"Taavi",
"Tab",
"Tab",
"Tab",
"Tab",
"Tabaan",
"Tabalah",
"Tabalah",
"Taban",
"Taban",
"Taban",
"Taban",
"Tabansi",
"Tabari",
"Tabassum",
"Tabassum",
"Tabassum",
"Tabasum",
"Tabasumm",
"Tabbar",
"Tabbart",
"Tabbath",
"Tabby",
"Taber",
"Taber",
"Taberah",
"Tabesh / Tabish",
"Tabia",
"Tabia",
"Tabinda",
"Tabinda",
"Tabish",
"Tabish",
"Tabitha",
"Tabitha",
"Tabitha",
"Tabitha",
"Tabitha",
"Tétény",
"T'iis",
"Ya akove",
"Ya Chai",
"Ya el",
"Yaa",
"Yaachana",
"Yaadave",
"Yaag",
"Yaagnya",
"Yaagyasenee",
"Yaaja",
"Yaakov",
"Yaalchelvan",
"Yaalini",
"Yaalisai",
"Yaalisai",
"Yaallini",
"Yaalmani",
"Yaalvendan",
"Yaalvendan",
"Yaamoli",
"Yaamoli",
"Yaar",
"Yaashvan",
"Yaatiesh",
"Yaatri",
"Yabel",
"Yachak",
"Yachana",
"Yachi",
"Yachiel",
"Yachika",
"Yachna",
"Yachne",
"Yadagiri",
"Yadav",
"Yadava",
"Yadavalli",
"Yadavaprakasa",
"Yadavendra",
"Yadavesvara",
"Yadavi",
"Yadavi",
"Yadavi",
"Yadawa",
"Yadgar",
"Yadgiri",
"Yadhana",
"Yadhav",
"Yadhavan",
"Yadhokshaja",
"Yadid",
"Yadid",
"Yadip",
"Yadira",
"Yadita",
"Yadleen",
"Yadleen",
"Yadnya",
"Yadnyesh",
"Yadnysena",
"Yadon",
"Yadu",
"Yadu",
"Yadu",
"Zaaei",
"Zaafir",
"Zaafir",
"Zaafira",
"Zaahid",
"Zaahir",
"Zaahir",
"Zaahirah",
"Zaahirah",
"Zaakir",
"Zaanannim",
"Zaara",
"Zaara",
"Zaara",
"Zaba",
"Zabby",
"Zabdi",
"Zabdiel",
"Zabel",
"Zabel",
"Zabi",
"Zabia",
"Zabiullah",
"Zabrina",
"Zabrina",
"Zabulon",
"Zac",
"Zacarias",
"Zacarias",
"Zacary",
"Zaccai",
"Zaccary",
"Zacchaeus",
"Zacchaeus",
"Zaccheo",
"Zaccheus",
"Zach",
"Zach",
"Zach",
"Zachaios",
"Zacharey",
"Zachari",
"Zacharia",
"Zacharia",
"Zachariah",
"Zacharie",
"Zachary",
"Zachary",
"Zachary",
"Zachely",
"Zacheriah",
"Zachery",
"Zachni",
"Zachory",
"Zachrey",
"Zachry",
"Zack",
"Zack",
"Zackariah",
"Zackariya",
"Zádor",
"Zágon",
"Zámor",
"Zétény"])
            },
            {
                "attribute": "sB1IHYu2xQT",
                "value": name
            },
            {
                "attribute": "ENRjVGxVL6l",
                "value": surname
            }
        ],
        "enrollments": [
            {
                "program": "wfd9K4dQVDR",
                "orgUnit": "Q6qNTXu3yRx",
                "enrollmentDate": enrollment_date,
                "incidentDate": enrollment_date
            }
        ]
    }
    tracked_entity_instances.append(instance)

# Create the final JSON structure
data = {
    "trackedEntityInstances": tracked_entity_instances
}

# Save to a JSON file
with open('tracked_entity_instances.json', 'w') as f:
    json.dump(data, f, indent=4)

print("JSON file generated successfully.")