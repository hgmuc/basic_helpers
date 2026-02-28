import os
from .file_helper import do_gzip_pkl   # keine Umstellung wg cycle import
from typing import List, Dict, Set

# External packages
#PKG_DIRS = ['geom-helpers', 'basic-helpers', 'shape2code-helper', 'rd-observability', 'code-dem-helper',
#            'env-api-helper', 'dtz-code-helper', 'llm-helpers', 'terrainclassifier', 'add-features', 'photon-helper']


# Data directory
data_base_path: str = 'C:\\01_AnacondaProjects\\osmium'

BIKESITE_CSV_PATH: str = "C:\\Users\\helmu\\Desktop\\Tracks\\bikesite-data1\\csv"


BINNEN_REGIONS: List[str] = ['AT', 'CH', 'LI', 'LU', 'CZ', 'SK', 'HU', 'RS', 'MAC', 'AN', 'MDA', 'KO', 
                  'DE-BY', 'DE-BW', 'DE-RLP', 'DE-SAAR', 'DE-HE', 'DE-NRW', 'DE-BB', 'DE-TH', 'DE-SAN', 'DE-SA', 
                  'PL-SLA', 'PL-MAL', 'PL-DOL', 'PL-KUJ', 'PL-LOD', 'PL-LUBE', 'PL-LUBU', 'PL-MAZ', 'PL-OPO', 'PL-PODK',
                  'PL-PODL', 'PL-SWI', 'PL-WIE', 'SM',
                  'NL-LI', 'NL-DR', 'NL-NB', 'NL-GE', 'NL-UT', 'NL-OV',
                  'FR-LORR', 'FR-ILFR', 'FR-FRCO', 'FR-CHAR', 'FR-BOUR', 'FR-CNTR', 'FR-ALSA', 'FR-RALP', 'FR-MIPY', 'FR-AUVE', 'FR-LIMO',
                  'ES-MA', 'ES-EX', 'ES-AR', 'ES-CM', 'ES-CL', 'ES-NA', 'ES-RI']


FNAME_ADMIN_CTRY_MAP: Dict[str, str] = {'AN': 'AD',
                                        'AT': 'AT',
                                        'BE': 'BE',
                                        'CH': 'CH',
                                        'CZ': 'CZ',
                                        'DE-BB': 'DE',
                                        'DE-BR': 'DE',
                                        'DE-BW': 'DE',
                                        'DE-BAY': 'DE',
                                        'DE-BY': 'DE',
                                        'DE-HE': 'DE',
                                        'DE-HH': 'DE',
                                        'DE-MV': 'DE',
                                        'DE-NDS': 'DE',
                                        'DE-NRW': 'DE',
                                        'DE-RLP': 'DE',
                                        'DE-SA': 'DE',
                                        'DE-SAAR': 'DE',
                                        'DE-SAN': 'DE',
                                        'DE-SH': 'DE',
                                        'DE-TH': 'DE',
                                        'DK': 'DK',
                                        'ES-AN': 'ES',
                                        'ES-AR': 'ES',
                                        'ES-AS': 'ES',
                                        'ES-BA': 'ES',
                                        'ES-CA': 'ES',
                                        'ES-CE': 'ES',
                                        'ES-CL': 'ES',
                                        'ES-CM': 'ES',
                                        'ES-CT': 'ES',
                                        'ES-EX': 'ES',
                                        'ES-GA': 'ES',
                                        'ES-MA': 'ES',
                                        'ES-ME': 'ES',
                                        'ES-MU': 'ES',
                                        'ES-NA': 'ES',
                                        'ES-PV': 'ES',
                                        'ES-RI': 'ES',
                                        'ES-VA': 'ES',
                                        'ES-CN': 'ES',
                                        'FI': 'FI',
                                        'FR-ALSA': 'FR',
                                        'FR-AQUI': 'FR',
                                        'FR-AUVE': 'FR',
                                        'FR-BANO': 'FR',
                                        'FR-BOUR': 'FR',
                                        'FR-BRET': 'FR',
                                        'FR-CHAR': 'FR',
                                        'FR-CNTR': 'FR',
                                        'FR-CORS': 'FR',
                                        'FR-FRCO': 'FR',
                                        'FR-HANO': 'FR',
                                        'FR-ILFR': 'FR',
                                        'FR-LARO': 'FR',
                                        'FR-LIMO': 'FR',
                                        'FR-LORR': 'FR',
                                        'FR-MIPY': 'FR',
                                        'FR-NPDC': 'FR',
                                        'FR-PDLL': 'FR',
                                        'FR-PICA': 'FR',
                                        'FR-POCH': 'FR',
                                        'FR-PROV': 'FR',
                                        'FR-RALP': 'FR',
                                        'GB-ENG': 'GB',
                                        'GB-MAN': 'GB',
                                        'GB-SCO': 'GB',
                                        'GB-WAL': 'GB',
                                        'HR': 'HR',
                                        'HU': 'HU',
                                        'IE': 'IE',
                                        'IT-CTRO': 'IT',
                                        'IT-ISOL': 'IT',
                                        'IT-NEST': 'IT',
                                        'IT-NOVE': 'IT',
                                        'IT-SUD': 'IT',
                                        'LI': 'LI',
                                        'LU': 'LU',
                                        'MON': 'MC',
                                        'NL-DR': 'NL',
                                        'NL-FL': 'NL',
                                        'NL-FR': 'NL',
                                        'NL-GE': 'NL',
                                        'NL-GR': 'NL',
                                        'NL-LI': 'NL',
                                        'NL-NB': 'NL',
                                        'NL-NH': 'NL',
                                        'NL-OV': 'NL',
                                        'NL-UT': 'NL',
                                        'NL-ZE': 'NL',
                                        'NL-ZH': 'NL',
                                        'NO': 'NO',
                                        'PL-DOL': 'PL',
                                        'PL-KUJ': 'PL',
                                        'PL-LOD': 'PL',
                                        'PL-LUBE': 'PL',
                                        'PL-LUBU': 'PL',
                                        'PL-MAL': 'PL',
                                        'PL-MAZ': 'PL',
                                        'PL-OPO': 'PL',
                                        'PL-PODK': 'PL',
                                        'PL-PODL': 'PL',
                                        'PL-POM': 'PL',
                                        'PL-SLA': 'PL',
                                        'PL-SWI': 'PL',
                                        'PL-WAR': 'PL',
                                        'PL-WIE': 'PL',
                                        'PL-ZAC': 'PL',
                                        'RS': 'RS',
                                        'SI': 'SI',
                                        'SK': 'SK', 
                                        'AL': 'AL',
                                        'BG': 'BG',
                                        'BIH': 'BA',
                                        'CPV': 'CV',
                                        'CYP': 'CY',
                                        'EST': 'EE',
                                        'FAR': 'FO',
                                        'FRO': 'FO',
                                        'GR': 'GR',
                                        'GUE': 'GG',
                                        'ISL': 'IS',
                                        'KO': 'XK',
                                        'LIT': 'LT',
                                        'LAT': 'LV',
                                        'MAC': 'MK',
                                        'MAL': 'MT',
                                        'MNT': 'ME',
                                        'PT': 'PT',
                                        'RU-KAL': 'RU',
                                        'BLR': 'BY',
                                        'ARM': 'AM',
                                        'GEO': 'GE',
                                        'MDA': 'MD', 
                                        'RO': 'RO',
                                        'SW': 'SE',
                                        'UA': 'UA',
                                        'TR': 'TR',
                                        'SM': 'SM',
                                        }


# Cycling-related settings
profile: str = ""   # one of "" | "mtb" | "roadbike"

# NOT USED
#PEDESTRIAN_AREAS = [178269048, # Fröttmaning U-Bahn


INCLUDED_FTWYS: Set[int] = set([31512448, 108295773, 31512449, 129916610, 796668697, 398011267, 75672254, # Bahnhof Dachau
                      90139983, 307043133, 1168594557, # U-Bahn Fröttmaning
                      1154606660, 1154606659, # Tutzing Schönmoosweg vom Bhf in Ri Süden zur Hauptstr
                      631036413, # Attel / Elend an der B15
                      247990039, 116509133, 307287751, 23478597, 358565122, 
                      51728547, # Ludwigshöhe Ebersberg
                      661546822, 24779651, # Dietlhofer See
                      23056209, 90975379, 144015702, # Denninger Anger + Cosimapark
                      148015122, 23056176, 23056209, 90975379, # Denninger Anger zur Nettelbeckstraße
                      959700062, 23464481, 959698102, 28648108, 28648109, 28648110, 28648111,  
                      # Versuch mit einigen Linien auf dem Starnberger See 
                      243022345, 45132647, 45132650, 45133009, 45133011, 379777135, 45133984, 379777133, 46254902, 
                      46254900, 45135420, 45135421, # Kesselbergstraße (Bundesstraße)
                      # 158179260, Feldweg Schorn - Oberdill Autobahnmeisterei falls nicht verfügbar
                      41736217, 41736216, # Prien Osternacher Str
                      30851904, # Hoher Peißenberg (parking_aisle = Zufahrt zum Gasthof und Aussichtspkt)
                      57768792, 583422026, # Achele - Weg von Straße zu Anleger
                      27644952, # Pilsensee Strandbad in Hechendorf - Weg über den Parkplatz (parking_aisle)
                      25961420, 963229765, 25961419, 513160516, 577832276, # Pilsensee Campingplatz Seefeld
                      68959669, 31405172, # Hechtsee Strandbad - Weg über den Parkplatz (parking_aisle)
                      162957877, 151266076, # Kiefersfelden Umfahrung Bergfriedhof
                      5230171, 4935356, 24247434, 24247468, 5230173, 1000310096, 338348001, 4891137, 
                      338347990, 4890491, 25454126, 34119028, 551467465, # Inn Uferweg - Wasserburg Kraftwerk
                      # 34118909, 219700249, 372800122, 372800124, 219700225, 219700240, # Inn Uferweg - Heberthal bis Kraftwerk
                      32389335, 26658939, # DAH-Etzenhausen zur Windkraftanlage
                      32651555, # Brücke zw Erdweg und Eisenhofen
                      4701102, 477060021, # Regattasee (womöglich wirklich nur Fußweg)
                      39129548, 691058674, 691058675, # Egglsee (EBE)
                      32886515, 8447547, # Feldbahnstraße, Eggartensiedlung
                      63075888, # Dornach Otto-Hahn-Str
                      161810307, 161810303, # Ebersberger Forst / Egglburger See (sac_scale)
                      300974451, 174974195, 174974191, 277880583, 279162266, 86069233, 30054960, # Tregler Alm (sac_scale)
                      4690999, 47035603, 242487626, 4691002, 331073429, 4691003, 
                      245797653, 245797652, 47035637, 23550163, 25416448, 25416449, 23550162, 1164097797, 
                      723848316, 254798453, 1080273017, 723963585, # Freising Bhf Unterführung
                      23884607, 195449715, 195449717, # FS Bahnunterführung Münchner Str
                      52474624, 52474622, 4440620, 759009403, 729084024, 729084008, 729084016, 729084037, 729084038, 
                      # FS Bahnunterführung Ottostr-/Schießstättstraße (Treppen)
                      24246231, 131188930, 27059277, 27059276, # FS bei Bahnunterführung Otto-/Parkstraße
                      1137543604, 1137543600, 729138915, 729138918, # FS Südl Korbinianbrücke - Radwege enden sonst im Nichts
                      172966750, # Krzg Kornwegerstraße - Würmtalstraße (München)
                      252215586, 252215587, # Fußgängerampel Radolfzeller Str
                      1137210598, # FS Erdinger Straße                      
                      1163011425, # Heimstetten Industriegebiet
                      28309604, 54154250, # Parking aisles - mit Zugang zu weiteren Nebenstrecken (Ohu, Gelting)
                      417076930, 40388471, 157558558, 159922577, 26307089, 26307088, 26307086, 507799578, 32018857, 
                      281662878, 281662876, 417076782, 417076796,  # Kraftwerk Jettenbach am Inn (Baustelle)
                      153431406, 708455419, 708455418, 1014411305, # Heimstetten Hauptstraße (Bauarbeit mit access = no)
                      27198900, 40750926, # Unterführung A99 hinter Aschheim am Abfanggraben (Baustelle bis Herbst 2024)
                      513652431, # Straßenneubau in Freiham-Nord (Baustelle)
                      70023291, # Schloßberg bei Rosenheim
                      25858675, # Fasaneriesee Unterführung
                      521757161, # Neuaubing Anbindung an Radweg nach Freiham statt Riesenumweg
                      212313654, 106299456, # Bad Tölz Isarkraftwerk (1x SAC_SCALE)
                      31963699, # Bad Tölz Marktstraße - Klammergasse (HGWY = pedestrian)
                      645756122, # Grubmühle (Mangfallknie, SAC_SCALE)
                      35355678, # EBE Forst - Weg zur Sauschütt - grade5
                      611659090, 772453928, 772453926, # Salzburg Fußgängerüberweg bei Mozartsteg
                      4817693, # für Überquerung der Montgelasstr bei der Törringstraße in MUC 
                      846856289, 846856288, 37972230, 846856287, 26395234, 193208822, 26395233, # Loisachsteg in Maxkron
                      300095131, 378559609, 378559608, 310662576, 64386628, 30055565, # Wörthsee Ostseite - Seeleite
                      33825071, 217483353, 174964555, 174964556, 174964557, 174964558, 217485852, 174832193, 257002277, 
                      257002270, 257002279, 257002287, 31172173, 174964563, 638038107, 638038088, 638038087, 638038089, 
                      638038106, 638038090, 174964564, 638038096, 638038095, 31174233, 638038122, 638038121, 31172730, 
                      12370698, 638038124, 638038127, 638038125, 638038126, 638038128, 25700426, 41125438, 25737449,
                      # Kreuth Lange Au + Schwaigeralm (SAC_SCALE)
                      4717850, 4718330, 97980887, 97980889, 25843911, 356960368, # Valepp - Kaiserklamm (SAC_SCALE)
                      56314771, 10527141, 56314770, 10527142, 735121007, 735121006, 10527139, 1141757531, # Süd- und Westufer Feringasee
                      226442184, 375889133, 375889130, 375889128, # Unterfühung München Ost (Treppe)
                      35947205, 47152955, 47152956, 35947206, 28825819, 28825822, 30342977, 
                      900510238, 900510239, 900510240, # Taufkirchen (Vils) - Wege zum Schloss
                      36733304, 24361145, 24210084, # Dorfen - von Isener Str zum Weiher und Skulpturenweg
                      70155995, 430861629, # Unterprienmühle - erster Feldweg in Richtung Aschau
                      239292661, 26646073, # Altenerding Wehr (nur Fußgänger)
                      298367090, # Riem
                      30732414, 30731435, 30731402, # Aschheim Erholungspark Südwest
                      27187415, 27569261, 696956827, 925957789, # Tutzing Nordbad
                      34142334, 34142329, 34142385, 34142253, 34142402, 550314812, 1103655467, 34142257, 361447814,  
                      # Haag - Lengdor über alte Bahnstrecke statt neuem Radweg an der Hauptstraße
                      26506696, 26506693, 162532813, 162532812, 119246773, 116530649, # Unterhadermark in Ri Tittmoning
                      160591704, 160591699, 295529437, 166540831, # Piusheim => overrule "emergency_access"
                      4926865, 1169009195, 4926898, 34955733, 35416357, 438041944, # Perlacher Forst Baustelle Rohrleitung
                      198488497, # Füssen Weg vom Lech hinauf zur Fußgängerzone unterhalb vom Schloss (bicycle=discouraged)
                      213510691, # Brücke über den Gröbenbach bei Puchheim-Ort (durch access=no, bicycle=no, foot=yes gesperrt)
                      162532813, # Unterhadermark in Ri Tittmoning (MTB_SCALE bei der Holzbrücke)
                      887016451, # EBE Polizei (Notlösung)
                      453078000, # Verbindung zum Distlhofweg (Mittersendling)
                      # 335330391, 335330393, 335330392, # Tittmoning Wasservorstadt
                      11981390, 344843916, # Heimstettner See von Feldkirchen durch Unterführung her
                      208354483, # Kranzberger See Parkplatz
                      498068326, 768494681, 768494682, # Unteralting Parapluie
                      335391526, # Strandbad Starnberg
                      205680075, # Aidenbachstraße überqueren
                      #132196795, 97202344, 27753615, # Feichtetstraße Pöcking - Possenhofen (SAC_SCALE)
                      35763835, 1089445976, # Murnau Bahnunterführung
                      112455481, 115082345, 112455487, 112455446, # Murnau Seidlpark
                      4211091, 712503320, # Überquerung Johanneskirchner Str
                      933854061, 27290938, # Günzburg Fußgängerzone (für Radfahrer erlaubt?)
                      5096849, 18640726, 18640724, 18640721, 84686434,  # Starnberg Seepromenade (Fußweg)
                      26744114, 39947093, 39947094, 26735913, 26735912, # Irschenhauser Weg von Mörlbach durch den Wald
                      34210951, 112194434, # Bernried Reitweg (SAC_SCALE) bzw Fußweg zum Dampfersteg
                      25411605, 25411943, 203079627, 203079633, 54147357, 308181000, 160514406, # Ferchensee - Elmau (SAC_SCALE)
                      28180109, # Mittenwald - Scharnitz: Fußpfad über die Gleise vor der Grenze
                      242229300, # Feldafing Trainingsplatz
                      #739093594, 739093593, 41661315, 41661316, 41661313, # Guglhör (sehr schwieriger Untergrund)
                      441954992, 4396414296, 366288206, 290956812, 2944361368, # Unterschleißheim Ampelquerung
                      712213555, 1039138477, 1039138478, 625436561, 712213560, 1039138482, 712213566, 6203551,  # Unterschleißheim Unterführung
                      362849686, # Unterschleißheim Parkplatz am S-Bahnhof
                      4430172, # Isarbrücke Oberhummel
                      610621676, 610621664, 610621673, # Karlsfeld MAN Truck Forum
                      60294143, 52939623, 52939625, # Eisolzried - Bergkirchen: Feldweg an der Maisach
                      191072622, # Garmisch Bahnhofstraße
                      35951202, # Walgerfranzweg
                      217999753, # Umleitung wg Neubau Radweg zw St. Afra im Feld und B2 bei Augsburg
                      676628764, # Bad Tölz Isarufer
                      1163370170, 1163370171, 36910187, # Oberau - Eschenlohe: Brücke (SAC_SCALE)
                      542133003, 542133004, 542133005, # Ruhpolding Bahnhofstraße
                      15699803, # Haag in Obb - Anbindung an Am Schachenwald
                      116036152, # Kendlmühlfilze
                      396053668, 550263733, # Aschheim Ismaninger Straße (Fußweg oder auch Radweg)
                      4058068, 111525153, 486399764, 4058074, 220678111, # Am Bahnhof in Haar
                      256356300, 256363974, 31112191, 234962700, 27488835, 37086877, 33825074, 866321555, 
                      866321554, 37121773, 973272605,  # Wildbad Kreuth
                      310382893, # Olypark: vom Rudolf-Harbig-Weg zum Werner-Dörpfeld-Weg (zT nur für Fußgänger wg 15% Gefälle)
                      25653470, 25653466, 124924141, 25653471, 25653468, 25653469, 638270737, # Wifling in Ri Weiher
                      86775600, 207108126, 83757265, 45736787, 45736790, 81341418, 81341415, 81341416, # Weßlinger See Südufer
                      155188406, # Kufstein Fischergries am Inn
                      33766101, # Verbindung zw Seestraße und Radweg an Bernrieder Str bei Tabaluga Heim
                      257397303, # Kleßheimer Allee, Szg, Verbindungsstück zw Radweg und Straße
                      110548394, 167518058, # Oberteisendorf an der Sur
                      105000489, 621707864, 105000463, 169351138, 621707862, 105000495, 105000513, # Poing Bergfeldstraße
                      1091799021, 722440394, 651520795, 1000439363, 1091799022, 651520794, 651520797, 526429114, 20191230,
                      723362431, 52303667, 32038801, 30295272, 513296429, 471924651, 209836380, 471924647,
                      36977509, 934766011, 36813857, 20135075, 36813859, 36813860, # Weihenstephan TU + Hofgarten
                      378167095, 26117329, 378167092, 378167093, 722686316, 768949742, 722686317, 954650137, # Weihenstephan TUM Jubiläumsbrücke
                      1000092076, # Zur Wurzn
                      119243387, # Riedenberg in die Glemmbachklamm (sehr schlecht MTB:SCALE 2-)
                      816436536, 877654116, 816436537, 816436532, 816436534, 816436542, # Ingolstadt Adenauer-Brücke
                      10066255, 10065802, 282017113, # Helene-Mayer-Ring
                      54776505, # am Lerchenauer See
                      288899471, 1062817471, 1062817472, 281893879, 30324146, 242664817, 281893878, 189197977, 
                      # Nadistr, Helene-Mayer-Ring, Lerchenauer Str
                      10065498, 19724457, 1051288861, # Connollystr
                      124911408, 301080691, # Bad Wiessee vom Strandbad zur Spielbank rauf
                      39670852, 38476992, 23631346, # Königssee Seeklause
                      28019444, # Kirchsee - vom Kiosk bis zum See
                      810691903, # Fußweg von der Straße zur Walchstädter Höhe 
                      17903108, 1051287214, 19724277, 19724274, # vom Werner-Seidenberg-Damm und Kusocinskidamm zur Connolly-Str
                      4706906, 199886297, 31306095, 1288460259, 1288460250, 1288460252, 23603773, # Freising Domberg
                      481039561, 1168600718, 1168600717, 26694563, # Königsbrunn
                      # 1350377316, # Mammendorf
                      ])

try:
    #do_pickle(INCLUDED_FTWYS, os.path.join(data_base_path, "lvl1", "INCLUDED_FTWYS.pkl"))
    do_gzip_pkl(INCLUDED_FTWYS, os.path.join(data_base_path, "lvl1", "INCLUDED_FTWYS.gzip")) # kein meta wg cycle import
except Exception as e:
    print("Could not create INCLUDED_FTWYS.gzip", e)

