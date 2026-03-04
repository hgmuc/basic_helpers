from typing import Dict, Final, Literal, Union, List, cast

FnamesValid = Literal['AL', 'AN', 'AT', 'BE', 'BG', 'BIH', 'CH', 'CPV', 'CYP', 'CZ', 
                      'DE-BB', 'DE-BR', 'DE-BW', 'DE-BY', 'DE-HE', 'DE-HH', 'DE-MV', 'DE-NDS', 
                      'DE-NRW', 'DE-RLP', 'DE-SA', 'DE-SAAR', 'DE-SAN', 'DE-SH', 'DE-TH', 
                      'DK', 'ES-AN', 'ES-AR', 'ES-AS', 'ES-BA', 'ES-CA', 'ES-CE', 'ES-CL', 
                      'ES-CM', 'ES-CN', 'ES-CT', 'ES-EX', 'ES-GA', 'ES-MA', 'ES-ME', 'ES-MU', 
                      'ES-NA', 'ES-PV', 'ES-RI', 'ES-VA', 'EST', 'FI', 
                      'FR-ALSA', 'FR-AQUI', 'FR-AUVE', 'FR-BANO', 'FR-BOUR', 'FR-BRET', 'FR-CHAR', 
                      'FR-CNTR', 'FR-CORS', 'FR-FRCO', 'FR-HANO', 'FR-ILFR', 'FR-LARO', 'FR-LIMO', 
                      'FR-LORR', 'FR-MIPY', 'FR-NPDC', 'FR-PDLL', 'FR-PICA', 'FR-POCH', 'FR-PROV', 
                      'FR-RALP', 'FRO', 'GB-ENG', 'GB-MAN', 'GB-SCO', 'GB-WAL', 'GR', 'GUE', 'HR', 
                      'HU', 'IE', 'ISL', 'IT-CTRO', 'IT-ISOL', 'IT-NEST', 'IT-NOVE', 'IT-SUD', 
                      'KO', 'LAT', 'LI', 'LIT', 'LU', 'MAC', 'MAL', 'MNT', 'MON', 
                      'NL-DR', 'NL-FL', 'NL-FR', 'NL-GE', 'NL-GR', 'NL-LI', 'NL-NB', 'NL-NH', 
                      'NL-OV', 'NL-UT', 'NL-ZE', 'NL-ZH', 'NO', 
                      'PL-DOL', 'PL-KUJ', 'PL-LOD', 'PL-LUBE', 'PL-LUBU', 'PL-MAL', 'PL-MAZ', 'PL-OPO', 
                      'PL-PODK', 'PL-PODL', 'PL-POM', 'PL-SLA', 'PL-SWI', 'PL-WAR', 'PL-WIE', 'PL-ZAC', 
                      'PT', 'RO', 'RS', 'SI', 'SK', 'SM', 'SW', 'TR', 'RU-KAL', 'MDA']

FnamesInvalid = Literal['ARM', 'BLR', 'CY-LVL5', 'Catalunya', 'DE', 'DE-NDS_SA_TH_LVL4', 'ES2', 'FR-NW_LVL4', 
                        'FR-O_LVL4', 'FR-SW_LVL4', 'FR2', 'GB', 'GB-ENG2', 'GB-ENG_WAL', 'GB-SCO2', 'GEO', 
                        'GUE-JER', 'Girona', 'IE-LVL5', 'IT', 'IT-ER_LA_PU_LVL4', 'LIT2', 'LT-SIA', 'LVL6_1', 
                        'LVL6_2', 'LVL6_3', 'LVL6_4', 'MON2', 'NL2', 'NO2', 'OBB', 'PL', 'PT-MAD', 
                        'PT2', 'RU', 'RU-KAL2', 'SM1', 'SM2', 'TR2', 'UA', 'LVL6_4', 'GUE-JER', 
                        'BAY', 'FR', 'NL', 'ES']

FnameKeys = Union[FnamesValid, FnamesInvalid]

UpdatePkgs = Dict[int, dict[str, str]] 

# OSM files config
fnames: Final[Dict[FnameKeys, str]] = {}
fnames['AN'] = "andorra-latest.osm.pbf"
fnames['AT'] = "austria-latest.osm.pbf"
fnames['BE'] = "belgium-latest.osm.pbf"
fnames['CH'] = "switzerland-latest.osm.pbf"
fnames['CZ'] = "czech-republic-latest.osm.pbf"
fnames['DE-BB'] = "brandenburg-latest.osm.pbf"
fnames['DE-BR'] = "bremen-latest.osm.pbf"
fnames['DE-BW'] = "baden-wuerttemberg-latest.osm.pbf"
fnames['DE-BY'] = "bayern-latest.osm.pbf"
fnames['DE-HE'] = "hessen-latest.osm.pbf"
fnames['DE-HH'] = "hamburg-latest.osm.pbf"
fnames['DE-MV'] = "mecklenburg-vorpommern-latest.osm.pbf"
fnames['DE-NDS'] = "niedersachsen-latest.osm.pbf"
fnames['DE-NRW'] = "nordrhein-westfalen-latest.osm.pbf"
fnames['DE-RLP'] = "rheinland-pfalz-latest.osm.pbf"
fnames['DE-SAAR'] = "saarland-latest.osm.pbf"
fnames['DE-SAN'] = "sachsen-anhalt-latest.osm.pbf"
fnames['DE-SA'] = "sachsen-latest.osm.pbf"
fnames['DE-SH'] = "schleswig-holstein-latest.osm.pbf"
fnames['DE-TH'] = "thueringen-latest.osm.pbf"
fnames['DK'] = "denmark-latest.osm.pbf"

fnames['ES-AN'] = "andalucia-latest.osm.pbf"
fnames['ES-AR'] = "aragon-latest.osm.pbf"
fnames['ES-AS'] = "asturias-latest.osm.pbf"
fnames['ES-BA'] = "islas-baleares-latest.osm.pbf"
fnames['ES-CA'] = "cantabria-latest.osm.pbf"
fnames['ES-CE'] = "ceuta-latest.osm.pbf"
fnames['ES-CL'] = "castilla-y-leon-latest.osm.pbf"
fnames['ES-CM'] = "castilla-la-mancha-latest.osm.pbf"
fnames['ES-CT'] = "cataluna-latest.osm.pbf"
fnames['ES-EX'] = "extremadura-latest.osm.pbf"
fnames['ES-GA'] = "galicia-latest.osm.pbf"
fnames['ES-RI'] = "la-rioja-latest.osm.pbf"
fnames['ES-MA'] = "madrid-latest.osm.pbf"
fnames['ES-ME'] = "melilla-latest.osm.pbf"
fnames['ES-MU'] = "murcia-latest.osm.pbf"
fnames['ES-NA'] = "navarra-latest.osm.pbf"
fnames['ES-PV'] = "pais-vasco-latest.osm.pbf"
fnames['ES-VA'] = "valencia-latest.osm.pbf"
fnames['ES-CN'] = 'canary-islands-latest.osm.pbf'

#fnames['ES'] = "spain-latest.osm.pbf"

fnames['FR-ALSA'] = "alsace-latest.osm.pbf"
fnames['FR-AQUI'] = "aquitaine-latest.osm.pbf"
fnames['FR-AUVE'] = "auvergne-latest.osm.pbf"
fnames['FR-BANO'] = "basse-normandie-latest.osm.pbf"
fnames['FR-BOUR'] = "bourgogne-latest.osm.pbf"
fnames['FR-BRET'] = "bretagne-latest.osm.pbf"
fnames['FR-CNTR'] = "centre-latest.osm.pbf"
fnames['FR-CHAR'] = "champagne-ardenne-latest.osm.pbf"
fnames['FR-CORS'] = "corse-latest.osm.pbf"
fnames['FR-FRCO'] = "franche-comte-latest.osm.pbf"
fnames['FR-HANO'] = "haute-normandie-latest.osm.pbf"
fnames['FR-ILFR'] = "ile-de-france-latest.osm.pbf"
fnames['FR-LARO'] = "languedoc-roussillon-latest.osm.pbf"
fnames['FR-LIMO'] = "limousin-latest.osm.pbf"
fnames['FR-LORR'] = "lorraine-latest.osm.pbf"
fnames['FR-MIPY'] = "midi-pyrenees-latest.osm.pbf"
fnames['FR-NPDC'] = "nord-pas-de-calais-latest.osm.pbf"
fnames['FR-PDLL'] = "pays-de-la-loire-latest.osm.pbf"
fnames['FR-PICA'] = "picardie-latest.osm.pbf"
fnames['FR-POCH'] = "poitou-charentes-latest.osm.pbf"
fnames['FR-PROV'] = "provence-alpes-cote-d-azur-latest.osm.pbf"
fnames['FR-RALP'] = "rhone-alpes-latest.osm.pbf"
fnames['HR'] = "croatia-latest.osm.pbf"
fnames['HU'] = "hungary-latest.osm.pbf"
fnames['IT-CTRO'] = "centro-latest.osm.pbf"
fnames['IT-ISOL'] = "isole-latest.osm.pbf"
fnames['IT-NEST'] = "nord-est-latest.osm.pbf"
fnames['IT-NOVE'] = "nord-ovest-latest.osm.pbf"
fnames['IT-SUD'] = "sud-latest.osm.pbf"
#fnames['IT'] = "italy-latest.osm.pbf"
fnames['LI'] = "liechtenstein-latest.osm.pbf"
fnames['LU'] = "luxembourg-latest.osm.pbf"

fnames['NL-DR'] = "drenthe-latest.osm.pbf"
fnames['NL-FL'] = "flevoland-latest.osm.pbf"
fnames['NL-FR'] = "friesland-latest.osm.pbf"
fnames['NL-GE'] = "gelderland-latest.osm.pbf"
fnames['NL-GR'] = "groningen-latest.osm.pbf"
fnames['NL-LI'] = "limburg-latest.osm.pbf"
fnames['NL-NB'] = "noord-brabant-latest.osm.pbf"
fnames['NL-NH'] = "noord-holland-latest.osm.pbf"
fnames['NL-OV'] = "overijssel-latest.osm.pbf"
fnames['NL-UT'] = "utrecht-latest.osm.pbf"
fnames['NL-ZE'] = "zeeland-latest.osm.pbf"
fnames['NL-ZH'] = "zuid-holland-latest.osm.pbf"
#fnames['NL'] = "netherlands-latest.osm.pbf"

#fnames['PL'] = "poland-latest.osm.pbf"
fnames['PL-DOL'] = "dolnoslaskie-latest.osm.pbf"
fnames['PL-KUJ'] = "kujawsko-pomorskie-latest.osm.pbf"
fnames['PL-LOD'] = "lodzkie-latest.osm.pbf"
fnames['PL-LUBE'] = "lubelskie-latest.osm.pbf"
fnames['PL-LUBU'] = "lubuskie-latest.osm.pbf"
fnames['PL-MAL'] = "malopolskie-latest.osm.pbf"
fnames['PL-MAZ'] = "mazowieckie-latest.osm.pbf"
fnames['PL-OPO'] = "opolskie-latest.osm.pbf"
fnames['PL-PODK'] = "podkarpackie-latest.osm.pbf"
fnames['PL-PODL'] = "podlaskie-latest.osm.pbf"
fnames['PL-POM'] = "pomorskie-latest.osm.pbf"
fnames['PL-SLA'] = "slaskie-latest.osm.pbf"
fnames['PL-SWI'] = "swietokrzyskie-latest.osm.pbf"
fnames['PL-WAR'] = "warminsko-mazurskie-latest.osm.pbf"
fnames['PL-WIE'] = "wielkopolskie-latest.osm.pbf"
fnames['PL-ZAC'] = "zachodniopomorskie-latest.osm.pbf"
#fnames['PL'] = "poland-latest.osm.pbf"
fnames['PT'] = "portugal-latest.osm.pbf"
fnames['RS'] = "serbia-latest.osm.pbf"
fnames['SI'] = "slovenia-latest.osm.pbf"
fnames['SK'] = "slovakia-latest.osm.pbf"
fnames['SM'] = "san-marino-overpass.osm.bz2"
fnames['MON'] = "monaco-latest.osm.pbf"

fnames['NO'] = 'ext/norway-latest.osm.pbf'
fnames['FI'] = 'ext/finland-latest.osm.pbf'
fnames['GB-ENG'] = 'ext/england-latest.osm.pbf'
fnames['GB-SCO'] = 'ext/scotland-latest.osm.pbf'
fnames['GB-WAL'] = 'ext/wales-latest.osm.pbf'
fnames['GB-MAN'] = 'ext/isle-of-man-latest.osm.pbf'
fnames['GUE'] = 'ext/guernsey-jersey-latest.osm.pbf'
fnames['BIH'] = 'ext/bosnia-herzegovina-latest.osm.pbf'
fnames['IE'] = 'ext/ireland-and-northern-ireland-latest.osm.pbf'
fnames['LAT'] = 'ext/latvia-latest.osm.pbf'
fnames['RO'] = 'ext/romania-latest.osm.pbf'
fnames['LIT'] = 'ext/lithuania-latest.osm.pbf'
fnames['EST'] = 'ext/estonia-latest.osm.pbf'
fnames['SW'] = 'ext/sweden-latest.osm.pbf'
fnames['MAL'] = 'ext/malta-latest.osm.pbf'
fnames['MAC'] = 'ext/macedonia-latest.osm.pbf'
fnames['MNT'] = 'ext/montenegro-latest.osm.pbf'

fnames['ISL'] = 'ext/iceland-latest.osm.pbf'
fnames['CYP'] = 'ext/cyprus-latest.osm.pbf'
fnames['FRO'] = 'ext/faroe-islands-latest.osm.pbf'
fnames['CPV'] = 'cape-verde-latest.osm.pbf'

fnames['GR'] = 'ext/greece-latest.osm.pbf'
fnames['KO'] = 'ext/kosovo-latest.osm.pbf'
fnames['AL'] = 'ext/albania-latest.osm.pbf'
fnames['BG'] = 'ext/bulgaria-latest.osm.pbf'
fnames['TR'] = 'ext/turkey-latest.osm.pbf'

fnames['MON2'] = "admin/monaco.osm"
fnames['FR2'] = "admin/france.osm"
fnames['ES2'] = "admin/spain.osm"
fnames['NL2'] = "admin/nederland.osm"
fnames['Catalunya'] = "admin/catalunya.osm"
fnames['Girona'] = "admin/girona.osm"

fnames['NO2'] = 'admin/norway.osm'
fnames['PT2'] = 'admin/portugal.osm'
fnames['GB'] = 'admin/uk.osm'
fnames['DE'] = 'admin/germany.osm'
fnames['PL'] = 'admin/poland.osm'
fnames['IT'] = 'admin/italy.osm'
fnames['SM1'] = 'admin/san_marino.osm'  # möglicherweise deprecated, da eigener Export aus Overpass jetzt verfügbar ist. -> fnames['SM]
fnames['SM2'] = 'admin/san_marino2.osm'  # möglicherweise deprecated, da eigener Export aus Overpass jetzt verfügbar ist. -> fnames['SM]
fnames['GB-ENG2'] = 'admin/england.osm'
fnames['GB-ENG_WAL'] = 'admin/gb_eng_wales.osm'
fnames['GUE-JER'] = 'admin/jersey_towns.osm'
fnames['LIT2'] = 'admin/lithuania.osm'
fnames['GB-SCO2'] = 'admin/scotland.osm'
fnames['RU'] = 'admin/russia.osm'
fnames['RU-KAL2'] = 'admin/russia_kaliningrad.osm'
fnames['TR2'] = 'admin/turkey.osm'
fnames['PT-MAD'] = 'admin/pt_madeira.osm'
fnames['IE-LVL5'] = 'admin/ie_lvl5.osm'
fnames['LT-SIA'] = 'admin/lt_bzk_schaulen.osm'
fnames['CY-LVL5'] = 'admin/cy_lvl5.osm'
fnames['LVL6_1'] = 'admin/lvl6_1.osm'
fnames['LVL6_2'] = 'admin/lvl6_2_Sachsen.osm'
fnames['LVL6_3'] = 'admin/lvl6_3_ES.osm'
fnames['LVL6_4'] = 'admin/lvl6_4_FR.osm'

fnames['OBB'] = "oberbayern-latest.osm.pbf"
fnames['RU-KAL'] = 'ext/kaliningrad-latest.osm.pbf'
fnames['MDA'] = 'ext/moldova-latest.osm.pbf'

# Die vier folgenden Dateien wurden noch nie heruntergeladen
fnames['BLR'] = 'ext/belarus-latest.osm.pbf'
fnames['UA'] = 'ext/ukraine-latest.osm.pbf'
fnames['GEO'] = 'ext/georgia-latest.osm.pbf'
fnames['ARM'] = 'ext/armenia-latest.osm.pbf'


fnames['DE-NDS_SA_TH_LVL4'] = 'admin/de_nds_sa_th_lvl4.osm'
fnames['IT-ER_LA_PU_LVL4'] = 'admin/it_er_la_pu_lvl4.osm'
fnames['FR-NW_LVL4'] = 'admin/fr_NW_lvl4.osm'
fnames['FR-O_LVL4'] = 'admin/fr_O_lvl4.osm'
fnames['FR-SW_LVL4'] = 'admin/fr_SW_lvl4.osm'

ext_fnames2: list[FnamesValid] = ['TR', 'GR', 'BG', 'AL', 'KO']
ext_fnames3: list[FnameKeys] = ['RU-KAL', 'CPV', 'UA', 'MDA', 'ARM', 'BLR', 'GEO']
ext_fnames: list[FnamesValid] = [
    'NO', 'RO', 'GB-ENG', 'MNT', 'LIT', 'SW', 'IE', 'MAC', 'EST', 'BIH', 'GB-WAL', 
    'MAL', 'FI', 'GUE', 'GB-SCO', 'LAT', 'GB-MAN', 'CYP', 'ISL', 'FRO']

ext_fnames_admin: list[FnamesInvalid] = [
    'NO2', 'PT2', 'GB', 'GB-ENG2', 'GB-SCO2', 'LIT2', 'PT-MAD', 'IE-LVL5', 'LT-SIA', 
    'CY-LVL5', 'RU-KAL2', 'DE', 'PL', 'IT', 'SM1', 'SM2', #'DE-NDS_SA_TH_LVL4', 
    'IT-ER_LA_PU_LVL4', 'FR-NW_LVL4', 'GB-ENG_WAL', 'GUE-JER', 'LVL6_4']

# FR, IT, NL etc sind excluded, weil stattdessen die regionalen Files verwendet werden.
excl_fnames: List[FnameKeys] = [
    'OBB', 'BAY', 'CPV', 'RU-KAL', 'FR', 'IT', 'PL', 'NL', 
    'DE', 'IT', 'SM1', 'DE-NDS_SA_TH_LVL4', 'FR-O_LVL4', 'FR-SW_LVL4', 
    'FR-NW_LVL4', 'GB-ENG_WAL', 
    'GUE-JER', 'LVL6_1', 'LVL6_2', 'LVL6_3', 'LVL6_4', 'IT-ER_LA_PU_LVL4', 
    'ES', 'MON2', 'NL2', 'FR2', 'ES2', 'Catalunya', 'Girona', 'RU', 'TR2']

fname: str = fnames['LI']
#fname_list = ['HR', 'RS'] + [n for n in sorted(fnames) if n not in ['BAY', 'OBB', 'HR', 'RS', 'MON2', 'NL2', 'FR2', 'ES2', 
#                                                                    'Catalunya', 'Girona']]
fname_list: List[FnamesValid] = [cast(FnamesValid, n) for n in sorted(fnames) 
                                 if n not in ext_fnames + ext_fnames2 + 
                                 ext_fnames3 + excl_fnames + ext_fnames_admin]
# fname_admin_list -> used in ReadAdminStructure to process the additional OSM files (e.g. admin/monaco.osm) as well
# These have been downloaded from the Overpass API.
fname_admin_list: List[FnameKeys] = [cast(FnameKeys, fname) for fname in 
                                     ['HR', 'RS'] + [n for n in sorted(fnames)
                                     if n not in ['BAY', 'OBB', 'HR', 'RS']]]

fnames_cyr: List[FnameKeys] = [
    'HR', 'RS', 'MAC', 'MNT', 'BG', 'RU-KAL', 'BLR', 
    'UA', 'RU-KAL2', 'RU', 'MDA', 'MDA']  # MN = Mongolei, 'BL', 'BY', 'TJ', 'MN', 

fnames_el: List[FnamesValid] = ['GR', 'CYP']
fnames_other_writing: List[FnameKeys] = ['GEO', 'ARM'] # 'GE', 'AM' - 2-letter-codes für Georgien und Armenien
fnames_translit: List[FnameKeys] = fnames_cyr + fnames_el + fnames_other_writing  # Georgien und Armenien

# Mapping der FNAMES (Files) auf Länder-Kürzel in ADMIN_ID_HIERARCHY
# In dieser Liste fehlt GI (Gibraltar), vmtl weil es kein FNAME hat, sondern bei Spanien dabei ist.
# -> Ebenso fehlt hier SM (San Marino), Teil von den italienischen Files.
# In dieser Liste wird die Isle of Man (GB-MAN) GB zugeschlagen; scheint offiziell aber ein Land zu sein (IM).

AFR_CTRYS: list[str] = ['canary-islands', 'cape-verde']

upd_packages: UpdatePkgs = {
    0: {'norway': 'norway', 'finland': 'finland',
        # UK - Update funktioniert zurzeit nicht, da sich die Server URL geändert hat,
        # und diese ist auch Bestandteil des PBF Files. Das PBF File zeigt noch auf GB statt auf UK.
        # Am besten vollständigen PBFs nochmal komplett von UK herunterladen.
        
        # NEUE URL Update Pfade
        'united_kingdom-england': 'england', 'united_kingdom-scotland': 'scotland', 
        'united_kingdom-wales': 'wales',                     
        
        # DEPRECATED - alte URL Update Pfade
        #'great_britain-england': 'england', 'great_britain-scotland': 'scotland', 
        #'great_britain-wales': 'wales', 
        'bosnia_herzegovina': 'bosnia-herzegovina', 
        'isle_of_man': 'isle-of-man', 'guernsey_jersey': 'guernsey-jersey', 
        'ireland_and_northern_ireland': 'ireland-and-northern-ireland', 
        'latvia': 'latvia', 'romania': 'romania', 'lithuania': 'lithuania',
        'estonia': 'estonia', 'sweden': 'sweden', 'malta': 'malta', 
        'iceland': 'iceland', 'cyprus': 'cyprus', 'faroe_islands': 'faroe-islands', 
        'macedonia': 'macedonia', 'montenegro': 'montenegro', 'bulgaria': 'bulgaria',
        'greece': 'greece', 'turkey': 'turkey', 'albania': 'albania', 'kosovo': 'kosovo', 
        'kaliningrad': 'kaliningrad', 'moldova': 'moldova',
    }, 
    5: {'spain-la_rioja': 'la-rioja', 'portugal': 'portugal', 
        'spain-asturias': 'asturias', 'spain-cantabria': 'cantabria', 'hungary': 'hungary', 
        'denmark': 'denmark', 'italy-centro': 'centro', 'switzerland': 'switzerland',
        'italy-isole': 'isole', 'italy-nord_est': 'nord-est', 'italy-nord_ovest': 'nord-ovest', 
        'italy-sud': 'sud', 'spain-andalucia': 'andalucia', 'spain-aragon': 'aragon', 
        'spain-castilla_la_mancha': 'castilla-la-mancha', 'spain-castilla_y_leon': 'castilla-y-leon', 
        'spain-cataluna': 'cataluna', 'spain-ceuta': 'ceuta', 'spain-extremadura': 'extremadura', 
        'spain-galicia': 'galicia', 'spain-islas_baleares': 'islas-baleares', 
        'spain-madrid': 'madrid', 'spain-melilla': 'melilla', 'canary_islands': 'canary-islands', 
        'spain-murcia': 'murcia', 'spain-navarra': 'navarra', 'spain-pais_vasco': 'pais-vasco', 
        'spain-valencia': 'valencia', 'cape_verde': 'cape-verde', 
        }, 
    2: {'germany-saarland': 'saarland', 'germany-bremen': 'bremen', 'germany-hamburg': 'hamburg', 
        'germany-brandenburg': 'brandenburg', 'germany-hessen': 'hessen', 'germany-sachsen': 'sachsen', 
        'germany-niedersachsen': 'niedersachsen', 'germany-sachsen_anhalt': 'sachsen-anhalt',
        'germany-schleswig_holstein': 'schleswig-holstein', 'germany-rheinland_pfalz': 'rheinland-pfalz', 
        'germany-nordrhein_westfalen': 'nordrhein-westfalen', 'germany-bayern-oberbayern': 'oberbayern', 
        'germany-mecklenburg_vorpommern': 'mecklenburg-vorpommern', 'germany-thueringen': 'thueringen',
        'andorra': 'andorra', 'liechtenstein': 'liechtenstein', },
    3: {'luxembourg': 'luxembourg', 'monaco': 'monaco', 'netherlands-drenthe': 'drenthe', 
        'slovenia': 'slovenia', 'czech_republic': 'czech-republic', 'austria': 'austria',  
        'belgium': 'belgium', 'netherlands-flevoland': 'flevoland', 
        'netherlands-friesland': 'friesland', 'netherlands-gelderland': 'gelderland', 
        'netherlands-groningen': 'groningen', 'netherlands-limburg': 'limburg', 
        'netherlands-noord_brabant': 'noord-brabant', 'netherlands-noord_holland': 'noord-holland', 
        'netherlands-overijssel': 'overijssel', 'netherlands-utrecht': 'utrecht', 
        'netherlands-zeeland': 'zeeland', 'netherlands-zuid_holland': 'zuid-holland'}, 
    4: {'france-alsace': 'alsace', 'france-aquitaine': 'aquitaine', 'france-auvergne': 'auvergne', 
        'france-basse_normandie': 'basse-normandie', 'france-bourgogne': 'bourgogne', 
        'france-bretagne': 'bretagne', 'france-centre': 'centre', 'france-corse': 'corse', 
        'france-champagne_ardenne': 'champagne-ardenne', 'france-franche_comte': 'franche-comte', 
        'france-haute_normandie': 'haute-normandie', 'france-ile_de_france': 'ile-de-france', 
        'france-languedoc_roussillon': 'languedoc-roussillon', 'france-limousin': 'limousin', 
        'france-lorraine': 'lorraine', 'france-midi_pyrenees': 'midi-pyrenees', 
        'france-nord_pas_de_calais': 'nord-pas-de-calais', 'france-pays_de_la_loire': 'pays-de-la-loire', 
        'france-picardie': 'picardie', 'france-poitou_charentes': 'poitou-charentes', 
        'france-provence_alpes_cote_d_azur': 'provence-alpes-cote-d-azur', 
        'france-rhone_alpes': 'rhone-alpes'},
    1: {'croatia': 'croatia', 'slovakia': 'slovakia', 'serbia': 'serbia', 
        'poland-dolnoslaskie': 'dolnoslaskie', 'poland-kujawsko_pomorskie': 'kujawsko-pomorskie', 
        'poland-lodzkie': 'lodzkie', 'poland-lubelskie': 'lubelskie', 'poland-lubuskie': 'lubuskie', 
        'poland-malopolskie': 'malopolskie', 'poland-mazowieckie': 'mazowieckie', 
        'poland-opolskie': 'opolskie', 'poland-podkarpackie': 'podkarpackie', 
        'poland-podlaskie': 'podlaskie', 'poland-pomorskie': 'pomorskie', 'poland-slaskie': 'slaskie', 
        'poland-swietokrzyskie': 'swietokrzyskie', 'poland-warminsko_mazurskie': 'warminsko-mazurskie',
        'poland-wielkopolskie': 'wielkopolskie', 'poland-zachodniopomorskie': 'zachodniopomorskie',
        'germany-bayern': 'bayern', 'germany-baden_wuerttemberg': 'baden-wuerttemberg'}, 
    #8: {'hungary': 'hungary', 'denmark': 'denmark'}
    }

# Liste der Regionen rund um DE für genauere Auswertung der Tags / Conditional Tags gemacht wird
REL_KEYS: list[str] = [
    'AT', 'CH', 'LI', 'CZ', 'LU', 'BE', 'SI', 'DK', 'IT-NEST', 
    'IT-NOVE', 'FR-ALSA', 'FR-CHAR', 'FR-FRCO', 'FR-LORR']

REL_KEYS += [k for k in fname_list if k.startswith("DE-")]
REL_KEYS += [k for k in fname_list if k.startswith("NL-")]
