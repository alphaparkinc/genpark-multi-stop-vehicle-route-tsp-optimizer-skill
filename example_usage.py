from client import MultiStopVehicleRouteTspOptimizerClient

def main():
    client = MultiStopVehicleRouteTspOptimizerClient()
    res = client.optimize_delivery_sequence()
    print('Multi-Stop Route Optimizer: ' + res['routing_id'])
    print('Optimal Sequence: ' + str(res['optimal_waypoint_sequence']) + ' | Distance: ' + str(res['total_route_distance_km']) + 'km')
    print('Manifest URL: ' + res['turn_by_turn_manifest_url'])

if __name__ == '__main__':
    main()
