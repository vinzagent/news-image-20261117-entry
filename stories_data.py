# Story data for the v3 edition of news-image-20261117.
# Every story happened, or was first reported, on Tuesday 17 November 2026
# (cross-checked against Reuters/AP/AFP/BBC/Al Jazeera reporting of the day).
# Contested claims are attributed in the wording.

REGIONS = {
    "NA": ("NORTH AMERICA", (29, 111, 184)),
    "SA": ("SOUTH AMERICA", (46, 158, 91)),
    "EU": ("EUROPE", (123, 79, 166)),
    "AF": ("AFRICA", (224, 138, 0)),
    "AS": ("ASIA", (192, 57, 43)),
    "OC": ("OCEANIA", (14, 149, 148)),
    "GL": ("GLOBAL", (90, 90, 90)),
}

DATE_LINE = "Tuesday 17 November 2026"
TOTAL_STORIES = 29

# Leads: (region, topic, headline, summary, lat, lon, tile, caption)
LEADS = [
    ("EU", "UKRAINE WAR", "Ukraine Says a Crimean Bridge Road Span Fell Into the Sea",
     "A second strike in two days on the Kerch Bridge; President Zelenskyy hailed "
     "an \u201cunprecedented\u201d hit on the crossing to annexed Crimea.",
     45.3, 36.5, "bridge", "KERCH STRAIT · STRUCK FOR A SECOND DAY"),
    ("AS", "IRAN WAR", "Iran Sends Drones at a US Radar in Bahrain; US Hits Back",
     "Bahrain says all the drones were downed; US jets then struck Iran's Qeshm "
     "island in the Strait of Hormuz.",
     26.2, 50.6, "gulf", "BAHRAIN · QESHM ISLAND"),
    ("AS", "DIPLOMACY", "Trump Holds His First Quad Summit, in Manila",
     "Minerals deals unveiled with Quad partners; Putin lands in Shenzhen for "
     "Thursday's three-way meeting.",
     14.6, 121.0, "quad", "MANILA · QUAD SUMMIT"),
]

# Secondaries: (region, topic, headline, summary, lat, lon, banner)
# banner = (background, foreground, big text, motif)
SECONDARIES = [
    ("AF", "HEALTH", "Ebola Cases in DR Congo Top 11,000, WHO Says",
     "Cases more than doubled in three months; about 5,400 have died.",
     0.5, 29.5, ((122, 28, 24), (255, 250, 240), "11,000+ CASES", "dots")),
    ("NA", "BUSINESS", "Nvidia's Quarterly Sales Double to $115.8bn",
     "First results since Jensen Huang quit; the Dow fell 849 points (-1.6%).",
     37.4, -121.9, ((16, 34, 24), (240, 200, 90), "$115.8BN SALES", "bars")),
    ("NA", "HEALTH", "US, Mexico and Bolivia Lose Measles-Free Status",
     "PAHO cites a year of spread; the US has 5,700+ cases in 2026.",
     38.5, -98.0, ((250, 243, 230), (150, 30, 25), "5,700+ CASES", "rash")),
    ("AS", "GAZA", "Gaza Winter Aid Held Up at Crossings",
     "UN agencies say 1.4m face acute hunger as cold sets in.",
     31.4, 34.3, ((38, 64, 96), (255, 250, 240), "1.4M FACE HUNGER", "wave")),
    ("AS", "DEFENCE", "Japan Scrambles Jets at Russian Incursion",
     "Two planes entered near Fukuoka; Tokyo protests, first since 2024.",
     33.6, 130.4, ((24, 52, 92), (255, 250, 240), "JETS SCRAMBLED", "plane")),
    ("EU", "LABOUR", "France Struck Again Over the Cost of Living",
     "146,000 marched by police count; the CGT claimed 500,000.",
     48.9, 2.3, ((90, 30, 44), (255, 250, 240), "146,000 MARCH", "crowd")),
    ("AS", "AIR CRASH", "Russian An-12 Crash in Siberia Kills All 19",
     "The air force plane came down near Kemerovo; a fault is suspected.",
     55.3, 86.1, ((40, 40, 44), (255, 250, 240), "ALL 19 KILLED", "plane")),
    ("GL", "CLIMATE", "COP31 Divided Over a Fossil-Fuel Phase-Out",
     "Nations weigh the first draft; the Antalya talks end Friday.",
     36.9, 30.7, ((16, 78, 70), (255, 250, 240), "PHASE-OUT FIGHT", "globe")),
]

NUMBERS_LINE = [
    ("1,441", " drones downed  ·  "),
    ("$115.8bn", " Nvidia sales  ·  "),
    ("11,000+", " Ebola cases  ·  "),
    ("5,700+", " US measles cases"),
]

TICKER = ("DOW -849 (-1.6%)  |  NVIDIA $115.8BN RECORD  |  EBOLA 11,000+ CASES  |  "
          "1,441 DRONES DOWNED  |  SERBIA: STUDENT BLOC WINS")

DECK = ("A bridge span in the sea, drones over Bahrain, a first Quad summit in "
        "Manila and a chipmaker's sales doubling")

# Right-hand box beside the map: (label, value)
BOX_TITLE = "THE DAY IN FIGURES"
BOX_ROWS = [
    ("DRONES DOWNED", "1,441"),
    ("NVIDIA SALES", "$115.8bn"),
    ("EBOLA CASES", "11,000+"),
    ("US MEASLES CASES", "5,700+"),
    ("FACE HUNGER IN GAZA", "1.4m"),
    ("PRAGUE TRAIN INJURED", "46"),
    ("AN-12 DEAD", "19"),
    ("DISPLACED RETURNED, SYRIA", "4m"),
    ("MARCHED IN FRANCE (POLICE)", "146,000"),
    ("DOW JONES", "-849 pts"),
]

# Also-list: (region, lead-in, clause, lat, lon)
ALSO = [
    ("EU", "Russia", "1,441 drones downed overnight", 55.7, 37.6),
    ("EU", "Kyiv", "missiles hit both Dnipro bridges", 50.4, 30.5),
    ("EU", "Prague", "two trains collide, 46 injured", 50.1, 14.4),
    ("EU", "Poland", "Tusk survives confidence vote", 52.2, 21.0),
    ("AS", "Turkey", "police seize Sözcü TV", 41.0, 28.9),
    ("AS", "West Bank", "settlers kill a woman, 72", 31.9, 35.2),
    ("SA", "Pope Leo", "struck near eye in Peru visit", -12.0, -77.0),
    ("AS", "Dhaka", "tear gas at garment workers", 23.8, 90.4),
    ("EU", "Serbia", "student bloc takes parliament", 44.8, 20.5),
    ("AS", "Mongolia", "president says he will resign", 47.9, 106.9),
    ("AF", "Mozambique", "opposition leader on trial", -25.9, 32.6),
    ("AS", "India", "Cyclone Akvan nears Odisha coast", 20.3, 85.8),
    ("OC", "Darwin", "M6.6 quake off Indonesia, no tsunami", -12.5, 130.9),
    ("NA", "Apple", "outage hits Pay, iCloud, App Store", 37.3, -122.0),
    ("AF", "Eritrea", "WHO says trachoma eliminated", 15.3, 38.9),
    ("AS", "Yemen", "Houthis advance toward Aden", 12.8, 45.0),
    ("EU", "Football", "Norway win 3–2 in Denmark", 55.7, 12.6),
    ("AS", "Syria", "4m displaced have returned — UN", 33.5, 36.3),
]

FOOTER = ("Every story happened or was first reported on Tuesday 17 November 2026. "
          "Disputed claims are attributed. Sources: Reuters · AP · AFP · BBC · "
          "Al Jazeera · UN · WHO · PAHO. Original drawings.")
