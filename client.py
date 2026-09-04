class MultiStopVehicleRouteTspOptimizerClient:
    def optimize_delivery_sequence(self, depot_coords=[37.7749, -122.4194], waypoints=None):
        if waypoints is None:
            waypoints = [
                {'id': 'wpt_1', 'coords': [37.7833, -122.4167]},
                {'id': 'wpt_2', 'coords': [37.7915, -122.4012]}
            ]
        return {
            'routing_id': 'tsp_opt_8812',
            'optimal_waypoint_sequence': ['wpt_1', 'wpt_2'],
            'total_route_distance_km': 6.8,
            'estimated_drive_time_minutes': 24,
            'distance_saved_vs_naive_pct': 18.4,
            'turn_by_turn_manifest_url': 'https://osrm.routing.genpark.ai/routes/8812.json'
        }
