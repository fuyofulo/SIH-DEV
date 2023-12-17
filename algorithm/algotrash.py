import datetime
from math import radians, sin, cos, sqrt, atan2
from operator import itemgetter
from syntheticdata import stations, siding, trains

average_speed_kmph = 80  # Average speed in km/h
acceptable_time_difference_seconds = 712000  # 8.2 Days in seconds

def haversine(lat1, lon1, lat2, lon2):
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    r = 6371  # Radius of Earth in kilometers
    return c * r

average_speed_kmph = 80  # Average speed in km/h


def find_suitable_train(siding, stations, trains):
    # Calculate the distance from the siding to each station
    distances = [(station['id'], haversine(siding['latitude'], siding['longitude'], station['latitude'], station['longitude'])) for station in stations]

    # Rank the stations based on distance
    ranked_stations = sorted(distances, key=itemgetter(1))

    # Go through the stations starting with the closest
    for station_id, _ in ranked_stations:
        # Filter out trains that are at this station, are available, and have enough capacity
        available_trains = [train for train in trains if train['station_id'] == station_id
                            and train['status'] == 'free'
                            and train['capacity'] >= siding['coal_to_be_collected']
                            and train['kilometers_remaining'] >= haversine(siding['latitude'], siding['longitude'], siding['destination_latitude'], siding['destination_longitude'])]
        

        # If there are any suitable trains, return the first one
        if available_trains:
            return available_trains[0]['id']

    # If no suitable train is found, return None
    return None






def find_suitable_train(siding, stations, trains):
    closest_train_eta = None
    suitable_train_id = None

    distances = [(station['id'], haversine(siding['latitude'], siding['longitude'], station['latitude'], station['longitude'])) for station in stations]
    ranked_stations = sorted(distances, key=itemgetter(1))

    for station_id, distance_to_siding in ranked_stations:
        for train in trains:
            if train['station_id'] == station_id and train['status'] == 'free':

                eta_hours = distance_to_siding / average_speed_kmph
                eta = datetime.datetime.now() + datetime.timedelta(hours=eta_hours)

                if closest_train_eta is None or eta < closest_train_eta:
                    closest_train_eta = eta

                if train['capacity'] >= siding['coal_to_be_collected'] and abs((eta - siding['arrival_date_time']).total_seconds()) <= acceptable_time_difference_seconds:
                    if train['kilometers_remaining'] >= haversine(siding['latitude'], siding['longitude'], siding['destination_latitude'], siding['destination_longitude']):
                        suitable_train_id = train['id']
                        break

        if suitable_train_id:
            break 

    return suitable_train_id, closest_train_eta
