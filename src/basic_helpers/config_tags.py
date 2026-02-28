from typing import Union, Set, List, Dict, Tuple

CYCLING_HGWY_EXCL: Set[str] = set([
    'trunk', 'trunk_link', 'raceway', 'motorway', 'motorway_link', 'proposed', 'platform', 
    'emergency_bay', 'corridor', 'bus_stop', 'escape', 'via_ferrata', 'trail', 'razed', 'ladder'])

CYCLING_HGWY: Set[str] = set([
    'residential', 'service', 'track', 'footway', 'unclassified', 'path', 'primary', 'secondary', 
    'tertiary', 'cycleway', 'living_street', 'crossing', 'pedestrian', 'road', 'rest_area', 'construction',
    'steps', 'elevator', 'primary_link', 'secondary_link', 'bridleway', 'services', 'tertiary_link', 
    'ferry', 'shuttle_train', 'shuttle_bus'])

KEEP_HGWY: Set[str] = set([
    'residential', 'unclassified', 'path', 'primary', 'secondary', 'tertiary', 'cycleway', 'living_street', 
    'crossing', 'road', 'service', 'primary_link', 'secondary_link', 'tertiary_link', 'shuttle_train', 'shuttle_bus'])

HIKE_HGWYS: Set[str] = set([
    'trail', 'path', 'cycleway', 'footway', 'pedestrian', 'steps', 'bridleway'])

ONEWAY_DISMOUNT_HGWYS: Set[str] = set([
    'track', 'path', 'cycleway', 'footway', 'pedestrian', 'crossing', 'residential', 'living_street'])

BIKE_PATHS_MED_PRIO: Set[str] = set([
    'track', 'path', 'crossing', 'footway', 'pedestrian'])

BIKE_PATHS_LOW_PRIO: Set[str] = set([
    'bridleway', 'pedestrian', 'steps', 'footway', 'elevator'])

HIKE_SURFACE_GOOD: Set[str] = set([
    'asphalt', 'metal', 'paved/concrete', 'plastic/rubber', 'timber', 'wood'])

HIKE_SURFACE_OK: Set[str] = set([
    'forest_soil', 'grass', 'gravel/sand', 'ground/dirt', 'ground/dirt/grass', 
    'ground/grass', 'ground/gravel', 'salt'])

HIKE_SURFACE_POOR: Set[str] = set([
    'ground/rocks', 'ground/roots', 'rocks', 'rubble', 'scrub', 'snow/ice', 
    'stone/cobblestone'])

PISTE_TYPE_HIKING: Set[str] = set([
    'nordic', 'downhill', 'hike', 'skitour', 'nordic;hike', 'snowshoe', 
    'hike;nordic', 'hike;snowshoe', 'nordic;hike;snowshoe', 'nordic;skitour', 
    'alpine', 'snowshoe;fatbike', 'backcountry', 'hike;skitour', 'hiking'])

PISTE_TYPE_BICYCLE: Set[str] = set([
    'nordic', 'sled', 'connection', 'fatbike', 'sleigh', 'nordic;fatbike', 
    'fatbike;hike', 'nordic;fatbike;hike', 'hike;fatbike', 'nordic;hike;fatbike'])

PARKING_NO_ACCESS: Set[str] = set(['private', 'no', 'customers', 'delivery', 'limited'])

SUMMER_LS: Set[str] = set(['summer', 'yes', 'yes|summer'])

SERVICES_INVALID: Set[str] = set([
    'drive-through', 'drive_through', 'parking', 'emergency_access', 'industrial', 'camp_site', 
    'traffic_park', 'pipestem', 'quarry', 'training', 'test_track',  'bus', 'busway', 'repair', 'dealer',
    'gps', 'service_station', 'service_road', 'fuel', 'weigh_station', 'bus_rapid_transit', 'private', 
    'allotments', 'cemetery', 'bypass', 'military', 'car_wash', 'delivery', 'garages', 
    'waterway', 'slipway', 'railway'])

HGWY_TAGS: Set[str] = set([
    "highway", "area", "man_made", "informal", "access", "locked", "blocked", "gate_locked", "tracktype", 
    "surface", "smoothness", "junction", "maxspeed", "lanes", "oneway", "temporary:oneway", "service", 
    'motor_vehicle', 'vehicle', 'motorcar', 'toll', 'ford', 'incline', 'living_street', "scenic", 
    'traffic', "services", "footway", "crossing", "crossing_ref", "crossing:island", "route", "bridge", 
    "tunnel", "layer", "aerialway"])

PERMISSIBLE_STATES: Set[str] = set([
    'yes', 'Yes', 'designated', 'permissive', 'official', 'passable', 'fwd', 'bwd'])

NOT_PERMISSIBLE_STATES: Set[str] = set([
    'no', 'private', 'discouraged', 'use_sidepath', 'impassable', 'destination', 
    'military', 'forestry', 'delivery', 'customers', 'students', 'construction', 
    'employees', 'emergency', 'limited', 'private;customers', 'customers;private'])

DISUSED_HIGHWAYS: Set[str] = set([
    'abandoned:highway', 'disused:highway', 'demolished:highway', 'closed:highway',
    'was:highway', 'razed:highway', 'removed:highway', 'destroyed:highway', 
    'construction:highway', 'not:highway', 'historic:highway', 'no:highway', 
    'old:highway', 'ruins:highway', 'former:highway', 'suspended:highway', 
    'hidden:highway', 'incorrect:highway', 'disabled:highway', 'unused:highway', 
    'dismantled:highway', 'damage:highway', 'damaged:highway', 'obliterated:highway', 
    'discouraged:highway', 'hide:highway', 'informal:highway', 'invisible:highway', 
    'illegal:highway', 'collapsed:highway', 'overgrown:highway', 'diverted:highway',
    'disused:route', 'abandoned:route', 'abandoned:bridge',
    'destroyed:bridge', 'was:bridge', 'disused:bridge', 'razed:bridge',])

FUTURE_HIGHWAYS: Set[str] = set(['proposed:highway', 'planned:highway'])


NATURAL_REGION: Set[str] = set(['mountain_range', 'mountain_area', 'tourism', 'valley'])

RAILWAY_LS: List[str] = ['rail', 'subway', 'narrow_gauge', 'funicular']


CYCLE_TAGS: Set[str] = set([
    "bicycle", "bicycle:forward", "bicycle:backward", "bicycle:lanes:forward", "mtb:scale", 
    "bicycle:lanes:backward", "routing:bicycle", "shoulder:bicycle", "oneway:bicycle", "moped",
    "cycleway", "cycleway:bicycle", "cycleway:lane", "cycleway:oneway", "cycleway:smoothness", 
    "cycleway:surface", "cycleway:both", "cycleway:both:bicycle", "cycleway:both:lane", 
    "cycleway:both:surface", "cycleway:both:smoothness", "cycleway:right", "cycleway:right:bicycle", 
    "cycleway:right:lane", "cycleway:right:oneway", "cycleway:right:smoothness", "cycleway:right:surface", 
    "cycleway:left", "cycleway:left:bicycle", "cycleway:left:lane", "cycleway:left:oneway", 
    "cycleway:left:smoothness", "cycleway:left:surface", "class:bicycle", "class:bicycle:commute", 
    "class:bicycle:mtb", "class:bicycle:non_experienced", "class:bicycle:roadcycling", "class:bicycle:touring", 
    "bicycle_road", "cyclestreet", "hazard:bicycle", "toll:bicycle", "mtb:type", "mtb:scale:uphill",
    "mtb:scale:imba", 'adfc_hl_net', 'is_sidepath', 'is_sidepath:of', 'is_sidepath_of', 
    'is_sidepath:of:name', 'is_sidepath:of:ref', 'is_sidepath:ref', "broken",
    "access:bicycle", "shoulder:access:bicycle", "class:bicycle:mtb:technical", "surface:cycleway", 
    "cycleway:right:surface:cycleway", "cycleway:left:surface:cycleway", "cycleway:surface:cycleway", 
    "sidewalk:bicycle", "sidewalk:right:bicycle", "sidewalk:left:bicycle", "sidewalk:both:bicycle"])
     
# HINWEIS: Elemente in dieser Liste müssen auch zu HGWY_TAGS oder CYCLE_TAGS hinzugefügt werden # 
TAG_MAP_DEP_ORDER: List[str] = [
    "railway", 'path', 'tracktype', 'mtb:scale', 'mtb:scale:uphill', 'mtb:scale:imba', 
    'mtb:scale:type', "ford", "is_sidepath", 'is_sidepath_of', 'is_sidepath:of', 'is_sidepath:ref', 
    'is_sidepath:of:ref', 'is_sidepath:of:name', "indoor", "covered", 'services', 'service', 'smoothness',
    'route', 'adfc_hl_net', 'temporary:oneway', "trail_visibility", "incline", "width", "sac_scale", 
    'motorcar:conditional', 'vehicle:conditional', 'motor_vehicle:conditional', 'toll:bicycle', 
    'toll', 'cycleway:right:surface:cycleway', 'cycleway:left:surface:cycleway', 'crossing:island', 
    'crossing_ref', 'footway', 'man_made', 'oneway:conditional', 'embankment',
    'oneway', 'surface', 'bicycle', 'scenic', 'traffic', 'construction',
    'cycleway:left:smoothness', 'cycleway:lefst:lane', 'cycleway:oneway', 'cycleway:right:lane', 
    'cycleway:right:oneway', 'cycleway:both:surface', 'cycleway:both:lane', 'cycleway:lane', 
    'cycleway:left', 'cycleway:both', 'cycleway:right', 'cycleway', 'hazard:bicycle', 
    "sidewalk:bicycle", "sidewalk:right:bicycle", "sidewalk:left:bicycle", "sidewalk:both:bicycle", 
    "access:foot", "foot", 'footway:both', 'footway:left', 'footway:right', 
    "hike_surface", "hike_smoothness", "hike_overgrown", 
    "hike_condition", "sidewalk", "sidewalk:right", "sidewalk:left", "sidewalk:both"]

SAC_SCALE_VALS: List[str] = [
    'strolling', 'hiking', 'mountain_hiking', 'demanding_mountain_hiking', 'alpine_hiking', 
    'demanding_alpine_hiking', 'difficult_alpine_hiking']

CLS_BICYCLE_MAP: Dict[Union[str, int], int] = {
    '-3': -3, '-2': -2, '-1': -1, '0': 0, '1': 1, '2': 2, '3': 3, 
    -3: -3, -2: -2, -1: -1, 0: 0, 1: 1, 2: 2, 3: 3}

CLS_BICYCLE_TAGS: List[str] = ["class:bicycle", "class:bicycle:touring", "class:bicycle:commute"]
# class:bicycle:trailer im Moment außen vor, da nur 20 Ways eine negative Bewertung haben
CLS_ROADBIKE_TAGS: List[str] = ["class:roadbike", "class:bicycle:roadcycling"]
CLS_MTB_TAGS: List[str] = ["class:bicycle:mtb", "class:bicycle:mtb:technical"]

MTB_TYPES: Set[str] = set([
    'crosscountry', 'allmountain', 'enduro', 'downhill', 'freeride', 'dirtjump', 'pumptrack', 'pumptrail', 
    'xc', 'slopestyle', 'bikepark', 'uphill', 'dh', '0', '1', '2', 'pump_track', 'northshore'])
MTB_TYPES_DOWNHILL: List[str] = ['downhill', 'freeride', 'slopestyle', 'dh', 'bikepark', 'northshore']
MTB_TYPES_UPHILL: List[str] = ['uphill', 'xc', 'crosscountry', 'allmountain', 'enduro', '0', '1', '2']

#NO_ACCESS = ['no', 'private', 'restricted', 'discouraged', 'customer', 'delivery', 'limited', 'bus', 
#             'construction', 'guest', 'employee', 'licence', 'military', 'locked', 'resident', 'emergency']

# BRIDGE + TUNNEL
IS_BRIDGE_LIST = set([
    'yes', 'covered', 'viaduct', 'cantilever', 'movable', 'boardwalk', 'low_water_crossing', 
    'abandoned', 'building_passage', 'trestle', 'simple_brunnel', 'pier', 'stone_bridge'])

IS_TUNNEL_LIST = set(['yes', 'building_passage', 'covered', 'underpass', 'passage'])

IS_WATER_TUNNEL_LIST = set(['yes', 'culvert', 'pipe', 'flooded', 'drain', 'channel'])

# CROSSING TYPES 
# CROSSING_TYPES = {'marked': 'marked', 'unmarked': 'unmarked', 'uncontrolled': 'uncontrolled', 'traffic_signals': 'traffic_signals', 
#                   'zebra': 'zebra', 'pedestrian_signals': 'traffic_signals', 'pelican': 'traffic_signals', 'toucan': 'traffic_signals', 
#                   'traffic_lights': 'traffic_signals', 'yes': '', 'traffic_island': '', 'island': '', 'cycleway': '', 'no': 'no', 
#                   'crossing': '', 'controlled': 'traffic_signals', 'puffin': 'traffic_signals', 'pegasus': 'traffic_signals', 
#                   'tiger': 'traffic_signals'}

## TOURISM et al
TOURISM_TYPES: Set[str] = set([
    'viewpoint', 'artwork', 'monument', 'memorial', 'zoo', 'aquarium', 'wine_cellar', 'winery', 
    'attraction', 'hotel', 'guest_house', 'hostel', 'motel', 'camp_site', 'alpine_hut']) 

TOURISM_SWIMMING: Set[str] = set(["swimming_area", "water_park", "beach_resort"])
                    # wilderness_hut <=> ist Gegensatz zu den anderen Optionen unbewirtschaftet

HISTORIC_TYPES: Set[str] = set([
    'castle', 'building', 'monument', 'memorial', 'archaelogical_site', 'ruins', 
    'wayside_cross', 'wayside_shrine', 'wayside_chapel', 'city_walls', 'city_gate', 
    'roman_road', 'aqueduct', 'monastery', 'chapel', 'church'])

AMENITY_TYPES: Set[str] = set([
    'biergarten', 'drinking_water', 'fountain', 'cafe', 'bicycle_rental', 'charging_station',
    'ice_cream', 'bakery', 'shelter'])    # place_of_worship, restaurant <=> nicht relevant

BICYCLE_RENTAL_EXCL: Set[Union[str, None]] = {None, 'docking_station', 'shop', 'dropoff_point', 'yes'}

BUILDING_TYPES: Set[str] = set([
    'church', 'castle', 'chapel', 'stadium', 'tower', 'cathedral', 'monastery', 
    'marketplace', 'museum', 'villa', 'bakehouse'])

REL_LOCALITY_TYPES: Set[str] = set([
    'village', 'locality', 'hamlet', 'islet', 'isolated_dwelling', 'farm', 'plot', 'neighbourhood', 
    'suburb', 'quarter', 'town', 'island', 'city_block', 'square', 'city', 'municipality'])

## Guideposts
DIRECTION_LIST: List[Tuple[str, str]] = [
    ('N', '_north'), ('NE', '_northeast'), ('E', '_east'), ('SE', '_southeast'), ('S', '_south'), 
    ('SW', '_southwest'), ('W', '_west'), ('NW', '_northwest')]

DIR_EXCL_LIST: Set[str] = set([
    'NORTH', 'EAST', 'WEST', 'SOUTH', 'NORTHEAST', 'SOUTHEAST', 'NORTHWEST', 'SOUTHWEST', 
    'W', 'N', 'E', 'S', 'NW', 'SW', 'NE', 'SE', 'NNW', 'NNE', 'SSW', 'SSE', 'WNW', 'ENE', 'WSW', 'ESE',
    'FORWARD', 'BACKWARD', 'CLOCKWISE', 'ANTICLOCKWISE'])

REL_MEMBER_ROLES: Set[str] = set([
    'guidepost', 'giudepost', 'guidepost ', 'gudiepost', 'guidepost', 'route_marker', 
    'info', 'information', 'information:board', 'information_board', 'map'])

NETWORK_KEYS: Set[str] = set(['rcn', 'lcn', 'ncn', 'bicycle', 'rcn;rwn', 'rwn;rcn', 'lcn;lwn', 'lwn;lcn'])

HIKING_NETWORK_KEYS: Set[str] = set([
    'rwn', 'lwn', 'nwn', 'rcn;rwn', 'rwn;rcn', 'lcn;lwn', 'lwn;lcn', 'rwn;lwn', 'nwn;lwn'])

GP_LIST: Set[str] = {'guidepost', 'route_marker', 'map'}

## Shops and vending machines (=> doch eher über OVERPASS wg Komplexität und Dauer <=> Nodes, Ways, Relations)
#SHOP_TYPES = set(["bakery", "convenience", "supermarket", "grocery", "dairy", "cheese", "kiosk", "food", "bicycle", "confectionery", 
#                  "pastry", "chocolate", "farm", "butcher", "deli", "water", "beverages",  
#                  "chemist", "pasta", "honey", "rice", "tortilla", "snacks"]) 
# bakery;pastry, pastry;bakery, convenience;alcohol, coffee;tea, tea;coffee, butcher;convenience, bakery;convenience, alcohol;convenience, supermarket;convenience, convenience;beverages, convenience;supermarket, convenience;bakery, bakery;butcher, gas;convenience, mall;supermarket, butcher;deli, bakery;deli, convenience;greengrocer;butcher;clothes])
# "convenience;gas", "farm" (Hofladen), water (Trinkwasser), chemist (Drogerie)
# "perfumery", "health_food", "nutition_supplements", "cannabis", "seafood", "wine", "outdoor", "coffee", "tea",
#VENDING_TYPES = set(["drinks", "food", "coffee", "sweets", "water", "bread", "pizza", "milk", "ice_cream", "eggs", "snacks", "meat", 
#                     "cheese", "hot_drinks", "snack", "beverages"])
# drinks;sweets, drinks;food, drinks;food;sweets, food;drinks, sweets;drinks, water;food, coffee;drinks, food;eggs, drinks;coffee, drinks;water, food;sweets, drinks;sweets;food, snacks;drinks, coffee;drinks;sweets

# Highways and waterways
# WATERWAY_TYPES = ['river', 'stream', 'canal', 'ditch', 'rapids']
WATERWAY_TYPES: Dict[str, int] = {'river': 1, 'canal': 2, 'rapids': 3, 'stream': 4, 'ditch': 5}

HIGHWAY_TYPES: Set[str] = {
    'trunk', 'trunk_link', 'raceway', 'motorway', 'motorway_link', 'primary', 
    'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link', 'road'}

FOOTWAY_TYPES: Set[str] = {
    'sidewalk', 'path', 'yes', 'link', 'designated', 'track', 'footway', 'pedestrian', 
    'shortcut', 'service', 'trail', 'footpath', 'boardwalk', 'crossing'}

CROSSING_TYPES: Set[str] = {'crossing', 'traffic_island', 'island'}
HIKING_HGWYS: Set[str] = {'trail', 'via_ferrata', 'bus_stop', 'ladder'}

highway2id: Dict[str, int] = {hgwy: id for hgwy, id in zip(HIGHWAY_TYPES, range(len(HIGHWAY_TYPES)))}

WATERWAY_MEM_ROLES: Set[str] = set([
    'main_stream', 'side_stream', 'anabranch', 'tributary', 'waterbody', 'distributary'])

# WATER_TYPE_PRIO und WATERWAY_TYPES werden genutzt, um übergeordneten Typen bei der Benennung der Wasserflächen zu priorisieren
# z.B. See vor Fluss, Fluss vor Bach etc.
WATER_TYPE_PRIO: Dict[Union[str, None], int] = {
    'lake': 0, 'lagoon': 0, 'shallow': 0, 'wastewater': 0, 'bay':0, 'reservoir': 1, 'harbour': 1, 
    'basin': 1, 'pond': 1, 'fishpond': 1, 'oxbow': 1, 'moat': 1, 'beach': 50, 'lock': 50, None: 99}
for k, v in WATERWAY_TYPES.items():
    WATER_TYPE_PRIO[k] = v

HIGHWAY_NODES: Set[str] = set([
    "elevator", "traffic_signals", "crossing", "turning_circle", "stop", "give_way", "footway",
    "turning_loop", "mini_roundabout", "traffic_signals;crossing", "crossing;traffic_signals"])

FOOT_BARRIER_LS: Set[str] = set([
    "kissing_gate", "footgate", "stile", "v_stile", "turnstile", "squeeze", "squeeze_stile", 
    "cycle_barrier", "bicycle_barrier", "horse_stile", "horse_jump", "step_over", "horse_barrier", 
    "cattle_grid", "motorcyle_barrier", "bollard", "car_barrier", "car_trap"])

# Residential areas <=> localities: list of relevant locality types:
LOCALITY_TAG_VALS: Set[str] = set([
    'borough', 'city', 'city_block', 'hamlet', 'island', 'isolated_dwelling', 'locality', 
    'municipality', 'neighbourhood', 'quarter', 'suburb', 'town', 'village', 'farm'])
LRG_LOCALITY_TAG_VALS: Set[str] = {'city', 'island', 'municipality', 'town', 'village'}
# farm = isolated_dwelling (Einzelgehöfte oder alleinstehende Häuser)
LOCALITY_TAG_VALS_NOT_USED: Set[str] = {'archipelago', 'islet', 'plot', 'square', 'allotment'}
# archipelago - uninterressant, weil aus mehreren (idR) benannten Inseln bestehend (z.B. Kanaren vs Teneriffa)
# islet = zu klein
# plot, allotments = idR unbewohnt
# square = Name idR Teil des Straßennamens

# Overriding misleading / missing tourism = VIEWPOINT tags (had tourism=information instead)
VIEWPTS_NODES: Set[int] = set([
    6388605431, 385295165, 3792706718, 8464898307, 11023622894, 730630702, 3785884608, 7906230694, 
    1349844023, 1350936369, 3268274619, 3883131138, 6925480834, 7289441637, 8443656122, 9192874824, 
    11383644401, 11502684355, 11508674469, 11508672384, 11499568853, 10037901873, 10017518135, 
    8350215039, 8145688904, 8091231045, 6726479564, 5354799046, 4976768227, 4560576974, 4283714692, 
    3476729736, 1818136201, 1342126300, 872148810, 489788647, 662942483, 721099736, 732290963, 
    1092934984, 1258796648, 1306018271, 1362612065, 1542089884, 1721115964, 1752645570, 1789887450, 
    1862074466, 1862074453, 1862074474, 1862074483, 1862074487, 2481358951, 3002077435, 3919178172, 
    4941744030, 4442623244, 5056987665, 6299076047, 6418385020, 6812313237, 7110242726, 7242230161, 
    7273765068, 7396081481, 7446803516, 7615031045, 7717571125, 7750222720, 7777538873, 8598365609, 
    8598365616, 8598365616, 8948358340, 10556514803, 11146782200, 410223627, 447957653, 567251720, 
    732647696, 847850317, 847850781, 848784348, 879124133, 942455709, 998736588, 1259921328, 
    1278604809, 2339665641, 2339665646, 2339665648, 2444971448, 2721893149, 2891224468, 3113626731, 
    3542176389, 3627395275, 3786232933, 4058183395, 4294811497, 4438932693, 4438977291, 4582413920, 
    4593067082, 5843323149, 7197210907, 7197210908, 7341529408, 7513733345, 7556528514, 7556528538, 
    7641101631, 7676560985, 8045110649, 8116435772, 8690346767, 8747497969, 8771506184, 8771506185, 
    8800106953, 9403406103, 9460292923, 9573150095, 10274172660, 10274172661, 10654182913, 10935098943, 
    11212040530, 11282989280, 11535173266, 11537828800, 11738788855, 11779233816, 11792031164])
