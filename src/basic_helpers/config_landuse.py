# LANDUSE
LANDUSE_WATER_TYPES: set[str] = set(['reservoir', 'basin', 'salt_pond', 'aquaculture'])

INDUSTRIAL_TYPES: set[str] = set([
    'industrial', 'commercial', 'retail', 'quarry', 'construction', 'logistics',
    'military', 'railway', 'landfill', 'greenhouse_horticulture', 
    'harbour', 'greenhouse', 'tourism', 'peat_cutting', 
    'dump', 'utility', 'garages', 'depot', 'brownfield', 'wastewater_plant'])
# brownfield = Brachfläche/verlassenes Gelände; greenfield=Baugrundstück

PLANTATION_TYPES: set[str] = set([
    'vineyard', 'orchard', 'flowerbed', 'plantation', 'plant_nursery', 'allotments'])

FARMLAND_TYPES: set[str] = set([
    'farmland', 'farmyard', 'farm', 'livestock', 'paddock', 'animal_keeping', 'field', 'paddy'])

MEADOWS_TYPES: set[str] = set([
    'meadow', 'village_green', 'grass', 'greenery', 'garden', 'park', 'nature', 'natural',
    'greenfield', 'grassland', 'pasture', 'natural_reserve', 'nature_reserve', 'natural␣reserve'])

FOREST_TYPES: set[str] = set(["forest", "forestry", "wood", "timber", "logging"])
GEOLOGY_TYPES: set[str] = set([
    'bare_rock', 'bedrock', 'cliff', 'rock', 'gorge', 'earth_bank', 
    'cape', 'reef', 'peninsula', 
    'sand', 'desert', 'dune', 'blockfield', 'landslide', 'scree', 
    'volcano', 'crater', 'hot_spring', 
    'valley', 'ridge', 'arete', 'hill', 'plateau', 'sinkhole', 'gully',
    'mountain_range', 'glacier'])

PUBLIC_BUILDINGS: set[str] = set([
    "education", "institutional", "school", "civic_admin", 
    "governmental", "government", "public", "civic", 
    "religious", 'cemetery', 'churchyard'])

PUBL_INFRASTRUCTURE: set[str] = set([
    'fairground',  'parking', 'highway', 'traffic_island', "static_caravan"])

PARK_TYPES: set[str] = set(["park", "garden", "golf_course", "nature_reserve", "recreation_ground"])
NATIONAL_PARK_TYPES: list[str] = ["national_park", "nature_reserve"]

# lagoon, tidal=yes / natural = water: Lagunen von Venedig, Marano oder Grado 
# Bays: Bucht von Sistiana < Golf von Triest < Golf von Venedig => Natural = bay, tidal = yes?
# Bays: Flensburger Förde: nur Bay, nix Tidal
# Bays am Bodensee: Überlinger See, Markelfinger Winkel (kleine Bucht in der Nähe der Insel Reichenau)
# Wattenmeer -> nur place = sea, keine Bay, keine Lagune
LANDUSE_TOURISM_TYPES: list[str] = ['recreation_ground']

NATURAL_MAPPING: dict[str, str] = {
    'scrub': 'forest', 'grassland': 'meadows', 'beach': 'water', 
    'tree_group': 'forest', 'tree_row': 'forest', 'trees': 'forest', 'tree-row': 'forest'}
NATURAL_MAPPING['heath'] = 'forest'
NATURAL_MAPPING['tundra'] = 'forest'

