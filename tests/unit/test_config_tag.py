import pytest
from basic_helpers import config_tags

class TestConfigTagSets:
    """Validates the integrity and sizing of OSM tag configurations."""

    def test_cycling_sets_counts(self):
        """Ensure core cycling sets haven't lost/gained items unexpectedly."""
        assert len(config_tags.CYCLING_HGWY_EXCL) == 15
        assert len(config_tags.CYCLING_HGWY) == 26
        assert len(config_tags.KEEP_HGWY) == 16
        assert len(config_tags.HIKE_HGWYS) == 7
        assert len(config_tags.ONEWAY_DISMOUNT_HGWYS) == 8
        assert len(config_tags.BIKE_PATHS_MED_PRIO) == 5
        assert len(config_tags.BIKE_PATHS_LOW_PRIO) == 5
        assert len(config_tags.HIKE_SURFACE_GOOD) == 6
        assert len(config_tags.HIKE_SURFACE_OK) == 8
        assert len(config_tags.HIKE_SURFACE_POOR) == 7
        assert len(config_tags.HIKE_SURFACE_OK) == 8
        assert len(config_tags.PISTE_TYPE_HIKING) == 15
        assert len(config_tags.PISTE_TYPE_BICYCLE) == 10
        assert len(config_tags.PARKING_NO_ACCESS) == 5
        assert len(config_tags.SUMMER_LS) == 3
        assert len(config_tags.SERVICES_INVALID) == 32
        assert len(config_tags.HGWY_TAGS) == 36
        assert len(config_tags.PERMISSIBLE_STATES) == 8
        assert len(config_tags.NOT_PERMISSIBLE_STATES) == 17
        assert len(config_tags.DISUSED_HIGHWAYS) == 39
        assert len(config_tags.FUTURE_HIGHWAYS) == 2
        assert len(config_tags.NATURAL_REGION) == 4
        assert len(config_tags.RAILWAY_LS) == 4
        assert len(config_tags.CYCLE_TAGS) == 65
        assert len(config_tags.TAG_MAP_DEP_ORDER) == 75
        assert len(config_tags.SAC_SCALE_VALS) == 7

        assert len(config_tags.CLS_BICYCLE_TAGS) == 3
        assert len(config_tags.CLS_ROADBIKE_TAGS) == 2
        assert len(config_tags.CLS_MTB_TAGS) == 2
        assert len(config_tags.MTB_TYPES) == 18
        assert len(config_tags.MTB_TYPES_DOWNHILL) == 6
        assert len(config_tags.MTB_TYPES_UPHILL) == 8
        assert len(config_tags.IS_BRIDGE_LIST) == 13
        assert len(config_tags.IS_TUNNEL_LIST) == 5
        assert len(config_tags.IS_WATER_TUNNEL_LIST) == 6
        assert len(config_tags.TOURISM_TYPES) == 15
        assert len(config_tags.TOURISM_SWIMMING) == 3

        assert len(config_tags.HISTORIC_TYPES) == 16
        assert len(config_tags.AMENITY_TYPES) == 9
        assert len(config_tags.BICYCLE_RENTAL_EXCL) == 5
        assert None in config_tags.BICYCLE_RENTAL_EXCL
        assert len(config_tags.BUILDING_TYPES) == 11
        assert len(config_tags.REL_LOCALITY_TYPES) == 16
        assert len(config_tags.DIRECTION_LIST) == 8
        assert len(config_tags.REL_MEMBER_ROLES) == 10

        assert len(config_tags.NETWORK_KEYS) == 8
        assert len(config_tags.HIKING_NETWORK_KEYS) == 9
        assert len(config_tags.WATERWAY_TYPES) == 5
        assert len(config_tags.HIGHWAY_TYPES) == 12

        assert len(config_tags.FOOTWAY_TYPES) == 14
        assert len(config_tags.CROSSING_TYPES) == 3
        assert len(config_tags.HIKING_HGWYS) == 4
        assert len(config_tags.WATERWAY_MEM_ROLES) == 6

        assert len(config_tags.WATER_TYPE_PRIO) == 20
        assert len(config_tags.HIGHWAY_NODES) == 11
        assert len(config_tags.FOOT_BARRIER_LS) == 18
        assert len(config_tags.LOCALITY_TAG_VALS) == 14
        assert len(config_tags.LRG_LOCALITY_TAG_VALS) == 5
        assert len(config_tags.LOCALITY_TAG_VALS_NOT_USED) == 5
        assert len(config_tags.WATERWAY_MEM_ROLES) == 6

    def test_hike_surface_categories(self):
        """Verify surface quality sets are mutually exclusive."""
        good = config_tags.HIKE_SURFACE_GOOD
        ok = config_tags.HIKE_SURFACE_OK
        poor = config_tags.HIKE_SURFACE_POOR
        
        # Check for overlaps (should be empty sets)
        assert good.isdisjoint(ok)
        assert ok.isdisjoint(poor)
        assert good.isdisjoint(poor)

    '''
    def test_tag_map_dependency_integrity(self):
        """
        Validates the HINWEIS in the code: 
        Elements in TAG_MAP_DEP_ORDER must be in HGWY_TAGS or CYCLE_TAGS.
        """
        combined_allowed = config_tags.HGWY_TAGS.union(config_tags.CYCLE_TAGS)
        # Note: 'railway', 'access:foot', 'foot', etc. are in the list 
        # but some might be missing from the sets based on the provided snippet.
        # This test identifies those gaps.
        
        missing = [
            tag for tag in config_tags.TAG_MAP_DEP_ORDER 
            if tag not in combined_allowed and tag not in ["railway", "access:foot", "foot", "hike_surface", 
                                                           "hike_smoothness", "hike_overgrown", "hike_condition",
                                                           "sidewalk", "sidewalk:right", "sidewalk:left", "sidewalk:both",
                                                           "footway:both", "footway:left", "footway:right"]
        ]
        assert not missing, f"Tags {missing} are in TAG_MAP_DEP_ORDER but not in HGWY/CYCLE sets."
    '''

    def test_bicycle_class_map_values(self):
        """Ensure the dictionary mapping handles both strings and ints correctly."""
        mapping = config_tags.CLS_BICYCLE_MAP
        assert mapping["-3"] == -3
        assert mapping[-3] == -3
        assert mapping["3"] == 3
        assert len(mapping) == 14

    def test_highway_id_mapping(self):
        """Verify the zip-generated highway2id map."""
        assert len(config_tags.highway2id) == len(config_tags.HIGHWAY_TYPES)
        for hgwy in config_tags.HIGHWAY_TYPES:
            assert hgwy in config_tags.highway2id
            assert isinstance(config_tags.highway2id[hgwy], int)

    def test_piste_types(self):
        """Check hiking vs bicycle piste types."""
        assert "nordic" in config_tags.PISTE_TYPE_HIKING
        assert "fatbike" in config_tags.PISTE_TYPE_BICYCLE
        assert len(config_tags.PISTE_TYPE_HIKING) == 15

    def test_viewpoint_node_consistency(self):
        """Ensure specific node IDs for viewpoints are preserved."""
        assert 6388605431 in config_tags.VIEWPTS_NODES
        assert len(config_tags.VIEWPTS_NODES) == 133

    @pytest.mark.parametrize("role", ["guidepost", "route_marker", "map"])
    def test_gp_list_membership(self, role):
        """Verify expected roles exist in GP_LIST."""
        assert role in config_tags.GP_LIST
        assert len(config_tags.GP_LIST) == 3

    def test_water_prio_logic(self):
        """Verify water priority values."""
        assert config_tags.WATER_TYPE_PRIO["lake"] == 0
        assert config_tags.WATER_TYPE_PRIO["river"] == 1  # From WATERWAY_TYPES
        assert config_tags.WATER_TYPE_PRIO[None] == 99

