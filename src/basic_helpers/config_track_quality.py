from __future__ import annotations
from typing import Final

from basic_helpers.types_osm import Quality

ASPHALT_HGWYS: Final[set[str]] = set(['primary', 'secondary', 'tertiary', 'unclassified', 'road', 'residential', 
                'living_street', 'track1', 'primary_link', 'secondary_link', 'tertiary_link', 'service'])
LIKELY_PAVED_HGWYS: Final[set[str]] = set(['driveway', 'cycleway', 'parking_aisle', 'rest_area', 'services'])
GRAVEL_TRACKS: Final[list[str]] = ['track2', 'track3', 'track']
DIRT_TRACKS: Final[list[str]] = ['track4', 'track5', 'path', 'bridleway']

CYCLE_PATH_QUALS: Final[list[Quality]] = [10,11,20,30,31,32,33]
CYCLE_PATH_HGWYS: Final[list[str]] = ['path', 'track', 'track1', 'track2', 'cycleway', 
                    'track3', 'footway', 'pedestrian', 'crossing']
CYCLE_PATH_BICYCLE_VALS: Final[list[str]] = ['designated', 'yes', 'permissive', 'allowed', 'official']

HIGHSPEED_HGWYS: Final[set[str]] = set(['primary', 'secondary', 'tertiary', 'unclassified', 'road', 
                        'primary_link', 'secondary_link', 'tertiary_link'] + \
                        ['cyclelane_' + n for n in ['primary', 'secondary', 'tertiary', 'primary_link', 
                        'unclassified', 'road', 'secondary_link', 'tertiary_link']])
MEDIUMSPEED_HGWYS: Final[set[str]] = set(['residential', 'living_street', 'track', 'track1', 'service'])

MAJOR_ROADS: Final[set[str]] = set(['primary', 'secondary', 'tertiary', 'primary_link', 'secondary_link', 'tertiary_link'] + 
                ['cyclelane_' + n for n in ['primary', 'secondary', 'tertiary', 'primary_link', 
                                            'secondary_link', 'tertiary_link']])

CW_DIR_QUAL_LS1: Final[list[Quality]] = [10,30,31,32,33,34,36,37,38,39]
CW_DIR_QUAL_LS2: Final[list[Quality]] = [10,30,31,32,33,34,35,37,38,39]
CW_DIR_VALS: Final[list[str | None]] = ['no', None, 'separate', 'use_sidepath', 'track']

CHECK_AREA_ID_LS: Final[set[str]] = set(['BN_47956680', 'BN_47956864', 'BN_55431852', 'BN_2093856590', 'BN_2093856588', 'BN_18778137'] + ['BN_347392672', 'BN_340517892', 'BN_340606758'])
LOC_NODE_DISTS = {'ferry_terminal': 150, 'halt': 75, 'islet': 100, 'locality': 50, 
                    'plot': 10, 'square': 25, 'station': 150}
LOC_TYPE_MAIN_LVL_VALS: Final[set[str]] = set(['city', 'town', 'village', 'island', 'municipality', 'archipelago'])

SIGNIF_TOURISM_NODES: Final[dict[str, int]] = {
    'alpine_hut': 10, 'aquarium': 10, 'aqueduct': 50, 'archaeological_site': 50, 'art': 10, 
    'arts_centre': 10, 'artwork': 10, 'attraction': 10, 'auditorium': 10, 'bakehouse': 10, 
    'baking_oven': 10, 'barefootpath': 10, 'barn': 10, 'bathing_place': 50, 'beach': 10, 
    'beach_resort': 50, 'bench': 10, 'biergarten': 50, 'binoculars': 10, 'bridge': 50, 
    'bicycle_rental': 100, 'bicycle_charging': 100, 'cafe': 10, 'camp_site': 100, 'castle': 100, 
    'castle_wall': 10, 'cathedral': 50, 'chapel': 10, 'church': 50, 'city_gate': 10, 
    'citywalls': 10, 'college': 10, 'colonnade': 10, 'drinking_water': 25, 
    'drinking_fountain': 25, 'fitness_station': 10, 'feeding_place': 10, 
    'fountain': 25, 'garden': 10, 'guest_house': 100, 'guidepost': 10, 'heritage': 10, 
    'heritage_building': 10, 'hospital': 10, 'hostel': 100, 'hotel': 100, 'ice_rink': 10, 
    'information': 10, 'kneipp_water_cure': 10, 'lawn': 10, 'manor': 50, 'maze': 10, 
    'meadow': 10, 'memorial': 10, 'milestone': 10, 'mine': 10, 'miniature_golf': 10, 
    'monastery': 50, 'monument': 25, 'mortuary': 10, 'motel': 100, 'museum': 10, 
    'nature_reserve': 50, 'palais': 25, 'park': 10, 'picnic_site': 10, 'picnic_table': 10, 
    'pitch': 10, 'place_of_worship': 10, 'planetarium': 10, 'playground': 10, 'pub': 10, 
    'public_building': 10, 'recreation_ground': 50, 'restaurant': 10, 'roman_road': 50, 
    'ruins': 10, 'scrub': 10, 'shrine': 10, 'shelter': 10, 'sports_centre': 10, 
    'sports_hall': 10, 'stadium': 50, 'swimming_area': 30, 'swimming_pool': 10, 
    'technical_monument': 10, 'theatre': 10, 'theme_park': 50, 'toilets': 10, 'tomb': 10, 
    'tower': 10, 'townhall': 10, 'university': 10, 'viewpoint': 50, 'village_green': 10, 
    'wall': 10, 'water_park': 50, 'water_pump': 10, 'watering_place': 10, 'wayside_chapel': 10, 
    'wayside_cross': 10, 'wayside_shrine': 10, 'wine_cellar': 50, 'winery': 50, 'zoo': 50, 
    'ferry_terminal': 150, 'station': 150, 'halt': 25, 'farm': 50, 'plot': 10, 'square': 25, 
    'locality': 50, 'isolated_dwelling': 25, 'islet': 50, 'hamlet': 50, 'city_block': 50, 
    'municipality': 150, 'village': 200, 'town': 150, 'neighbourhood': 200, 'suburb': 250, 
    'quarter': 250, 'island': 350, 'city': 350, 'map': 10, 'panorama': 25, 'map topo': 25,                    
    'map toposcope': 25, 'natural_monument': 25, 'bicycle_repair_station': 10, 
    'water_wheel': 10, 'granary': 25, 'arboretum': 25, 'soccer_golf': 10, 
    'windmill': 25, 'watermill': 25, 'viewpoint;information': 50, 'bicycle_parking': 5, 
    'ice_cream': 5, 'bakery': 10}

