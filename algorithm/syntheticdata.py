# Hardcoded data for stations
stations = [
    {'id': 'Station1', 'latitude': 28.128398440291996, 'longitude': 77.22059050010184},
    {'id': 'Station2', 'latitude': 24.050814303825412, 'longitude': 81.98785177197064},
    {'id': 'Station3', 'latitude': 20.407997782810067, 'longitude': 81.34884571199639},
    {'id': 'Station4', 'latitude': 20.087228756031042, 'longitude': 72.26612508951033},
    {'id': 'Station5', 'latitude': 20.206107003529556, 'longitude': 73.57870733541212},
    {'id': 'Station6', 'latitude': 25.53815824120218, 'longitude': 75.39190114492322},
    {'id': 'Station7', 'latitude': 21.73069608430462, 'longitude': 75.61975895224232},
    {'id': 'Station8', 'latitude': 26.73442708758101, 'longitude': 77.79650798753536},
    {'id': 'Station9', 'latitude': 23.044818973991525, 'longitude': 78.90034881415006},
    {'id': 'Station10', 'latitude': 19.84181107103201, 'longitude': 75.56146473708496},
]

# Hardcoded data for sidings
siding = [
    {'id': 'Siding1', 'latitude': 28.2483002490234, 'longitude': 79.24180583585434},
    {'id': 'Siding2', 'latitude': 24.028692674766468, 'longitude': 80.4338244544533},
    {'id': 'Siding3', 'latitude': 25.400240518940382, 'longitude': 80.58966558260848},
    {'id': 'Siding4', 'latitude': 20.282407774737546, 'longitude': 73.47803453854853},
]


# Hardcoded data for trains
trains = [
    # Trains in station 1
    {'id': 'Train1', 'status': 'in maintenance', 'capacity': 430, 'kilometers_remaining': 13547, 'station_id': 'Station1', 'num_wagons': 40},
    {'id': 'Train2', 'status': 'free', 'capacity': 947, 'kilometers_remaining': 12168, 'station_id': 'Station1', 'num_wagons': 49},
    {'id': 'Train3', 'status': 'occupied', 'capacity': 655, 'kilometers_remaining': 12583, 'station_id': 'Station1', 'num_wagons': 44},
    {'id': 'Train4', 'status': 'occupied', 'capacity': 418, 'kilometers_remaining': 14774, 'station_id': 'Station1', 'num_wagons': 46},
    {'id': 'Train5', 'status': 'free', 'capacity': 525, 'kilometers_remaining': 14035, 'station_id': 'Station1', 'num_wagons': 48},
    {'id': 'Train6', 'status': 'free', 'capacity': 508, 'kilometers_remaining': 10938, 'station_id': 'Station1', 'num_wagons': 52},
    {'id': 'Train7', 'status': 'in maintenance', 'capacity': 658, 'kilometers_remaining': 7443, 'station_id': 'Station1', 'num_wagons': 49},
    {'id': 'Train8', 'status': 'free', 'capacity': 572, 'kilometers_remaining': 14218, 'station_id': 'Station1', 'num_wagons': 54},
    # Trains in station 2
    {'id': 'Train9', 'status': 'free', 'capacity': 986, 'kilometers_remaining': 7498, 'station_id': 'Station2', 'num_wagons': 58},
    {'id': 'Train10', 'status': 'occupied', 'capacity': 642, 'kilometers_remaining': 6234, 'station_id': 'Station2', 'num_wagons': 47},
    {'id': 'Train11', 'status': 'in maintenance', 'capacity': 481, 'kilometers_remaining': 8032, 'station_id': 'Station2', 'num_wagons': 54},
    {'id': 'Train12', 'status': 'free', 'capacity': 777, 'kilometers_remaining': 5987, 'station_id': 'Station2', 'num_wagons': 45},
    {'id': 'Train13', 'status': 'free', 'capacity': 559, 'kilometers_remaining': 13412, 'station_id': 'Station2', 'num_wagons': 40},
    {'id': 'Train14', 'status': 'occupied', 'capacity': 676, 'kilometers_remaining': 11246, 'station_id': 'Station2', 'num_wagons': 53},
    {'id': 'Train15', 'status': 'free', 'capacity': 744, 'kilometers_remaining': 7203, 'station_id': 'Station2', 'num_wagons': 56},
    {'id': 'Train16', 'status': 'in maintenance', 'capacity': 488, 'kilometers_remaining': 9265, 'station_id': 'Station2', 'num_wagons': 44},
    # Trains in station 3
    {'id': 'Train17', 'status': 'occupied', 'capacity': 502, 'kilometers_remaining': 11934, 'station_id': 'Station3', 'num_wagons': 58},
    {'id': 'Train18', 'status': 'free', 'capacity': 689, 'kilometers_remaining': 13500, 'station_id': 'Station3', 'num_wagons': 41},
    {'id': 'Train19', 'status': 'free', 'capacity': 467, 'kilometers_remaining': 7430, 'station_id': 'Station3', 'num_wagons': 52},
    {'id': 'Train20', 'status': 'occupied', 'capacity': 858, 'kilometers_remaining': 9884, 'station_id': 'Station3', 'num_wagons': 47},
    {'id': 'Train21', 'status': 'in maintenance', 'capacity': 709, 'kilometers_remaining': 6568, 'station_id': 'Station3', 'num_wagons': 56},
    {'id': 'Train22', 'status': 'occupied', 'capacity': 753, 'kilometers_remaining': 8034, 'station_id': 'Station3', 'num_wagons': 48},
    {'id': 'Train23', 'status': 'free', 'capacity': 593, 'kilometers_remaining': 8777, 'station_id': 'Station3', 'num_wagons': 46},
    {'id': 'Train24', 'status': 'in maintenance', 'capacity': 536, 'kilometers_remaining': 12987, 'station_id': 'Station3', 'num_wagons': 50},
    # Trains in station 4
    {'id': 'Train25', 'status': 'free', 'capacity': 400, 'kilometers_remaining': 12000, 'station_id': 'Station4', 'num_wagons': 45},
    {'id': 'Train26', 'status': 'occupied', 'capacity': 750, 'kilometers_remaining': 8000, 'station_id': 'Station4', 'num_wagons': 58},
    {'id': 'Train27', 'status': 'in maintenance', 'capacity': 480, 'kilometers_remaining': 9500, 'station_id': 'Station4', 'num_wagons': 47},
    {'id': 'Train28', 'status': 'free', 'capacity': 500, 'kilometers_remaining': 11000, 'station_id': 'Station4', 'num_wagons': 53},
    {'id': 'Train29', 'status': 'free', 'capacity': 600, 'kilometers_remaining': 7000, 'station_id': 'Station4', 'num_wagons': 42},
    {'id': 'Train30', 'status': 'in maintenance', 'capacity': 440, 'kilometers_remaining': 13000, 'station_id': 'Station4', 'num_wagons': 55},
    {'id': 'Train31', 'status': 'occupied', 'capacity': 470, 'kilometers_remaining': 5000, 'station_id': 'Station4', 'num_wagons': 40},
    {'id': 'Train32', 'status': 'free', 'capacity': 690, 'kilometers_remaining': 15000, 'station_id': 'Station4', 'num_wagons': 56},
    # Trains for station 5
    {'id': 'Train33', 'status': 'occupied', 'capacity': 430, 'kilometers_remaining': 14000, 'station_id': 'Station5', 'num_wagons': 51},
    {'id': 'Train34', 'status': 'free', 'capacity': 820, 'kilometers_remaining': 6000, 'station_id': 'Station5', 'num_wagons': 54},
    {'id': 'Train35', 'status': 'free', 'capacity': 510, 'kilometers_remaining': 9000, 'station_id': 'Station5', 'num_wagons': 44},
    {'id': 'Train36', 'status': 'in maintenance', 'capacity': 670, 'kilometers_remaining': 10500, 'station_id': 'Station5', 'num_wagons': 58},
    {'id': 'Train37', 'status': 'occupied', 'capacity': 730, 'kilometers_remaining': 8500, 'station_id': 'Station5', 'num_wagons': 52},
    {'id': 'Train38', 'status': 'free', 'capacity': 560, 'kilometers_remaining': 7000, 'station_id': 'Station5', 'num_wagons': 46},
    {'id': 'Train39', 'status': 'occupied', 'capacity': 490, 'kilometers_remaining': 13000, 'station_id': 'Station5', 'num_wagons': 43},
    {'id': 'Train40', 'status': 'free', 'capacity': 650, 'kilometers_remaining': 8000, 'station_id': 'Station5', 'num_wagons': 57},
    # Trains for station 6
    {'id': 'Train41', 'status': 'free', 'capacity': 500, 'kilometers_remaining': 10000, 'station_id': 'Station6', 'num_wagons': 48},
    {'id': 'Train42', 'status': 'occupied', 'capacity': 600, 'kilometers_remaining': 9000, 'station_id': 'Station6', 'num_wagons': 52},
    {'id': 'Train43', 'status': 'in maintenance', 'capacity': 550, 'kilometers_remaining': 12000, 'station_id': 'Station6', 'num_wagons': 45},
    {'id': 'Train44', 'status': 'free', 'capacity': 700, 'kilometers_remaining': 8000, 'station_id': 'Station6', 'num_wagons': 56},
    {'id': 'Train45', 'status': 'occupied', 'capacity': 480, 'kilometers_remaining': 11000, 'station_id': 'Station6', 'num_wagons': 40},
    {'id': 'Train46', 'status': 'free', 'capacity': 530, 'kilometers_remaining': 7000, 'station_id': 'Station6', 'num_wagons': 58},
    {'id': 'Train47', 'status': 'in maintenance', 'capacity': 620, 'kilometers_remaining': 6000, 'station_id': 'Station6', 'num_wagons': 50},
    {'id': 'Train48', 'status': 'occupied', 'capacity': 680, 'kilometers_remaining': 13000, 'station_id': 'Station6', 'num_wagons': 54},
    # Trains for station 7
    {'id': 'Train49', 'status': 'free', 'capacity': 450, 'kilometers_remaining': 14000, 'station_id': 'Station7', 'num_wagons': 47},
    {'id': 'Train50', 'status': 'occupied', 'capacity': 710, 'kilometers_remaining': 5000, 'station_id': 'Station7', 'num_wagons': 42},
    {'id': 'Train51', 'status': 'in maintenance', 'capacity': 560, 'kilometers_remaining': 9000, 'station_id': 'Station7', 'num_wagons': 53},
    {'id': 'Train52', 'status': 'free', 'capacity': 640, 'kilometers_remaining': 7500, 'station_id': 'Station7', 'num_wagons': 55},
    {'id': 'Train53', 'status': 'occupied', 'capacity': 590, 'kilometers_remaining': 8500, 'station_id': 'Station7', 'num_wagons': 49},
    {'id': 'Train54', 'status': 'free', 'capacity': 520, 'kilometers_remaining': 9500, 'station_id': 'Station7', 'num_wagons': 51},
    {'id': 'Train55', 'status': 'in maintenance', 'capacity': 650, 'kilometers_remaining': 10500, 'station_id': 'Station7', 'num_wagons': 58},
    {'id': 'Train56', 'status': 'occupied', 'capacity': 470, 'kilometers_remaining': 11500, 'station_id': 'Station7', 'num_wagons': 46},
    # Trains for station 8
    {'id': 'Train57', 'status': 'free', 'capacity': 550, 'kilometers_remaining': 10500, 'station_id': 'Station8', 'num_wagons': 44},
    {'id': 'Train58', 'status': 'occupied', 'capacity': 650, 'kilometers_remaining': 9500, 'station_id': 'Station8', 'num_wagons': 57},
    {'id': 'Train59', 'status': 'in maintenance', 'capacity': 500, 'kilometers_remaining': 12000, 'station_id': 'Station8', 'num_wagons': 46},
    {'id': 'Train60', 'status': 'free', 'capacity': 600, 'kilometers_remaining': 8000, 'station_id': 'Station8', 'num_wagons': 53},
    {'id': 'Train61', 'status': 'occupied', 'capacity': 480, 'kilometers_remaining': 7000, 'station_id': 'Station8', 'num_wagons': 40},
    {'id': 'Train62', 'status': 'free', 'capacity': 700, 'kilometers_remaining': 11000, 'station_id': 'Station8', 'num_wagons': 58},
    {'id': 'Train63', 'status': 'in maintenance', 'capacity': 670, 'kilometers_remaining': 13000, 'station_id': 'Station8', 'num_wagons': 50},
    {'id': 'Train64', 'status': 'occupied', 'capacity': 520, 'kilometers_remaining': 9000, 'station_id': 'Station8', 'num_wagons': 55},
    # Trains for station 9
    {'id': 'Train65', 'status': 'free', 'capacity': 540, 'kilometers_remaining': 10000, 'station_id': 'Station9', 'num_wagons': 48},
    {'id': 'Train66', 'status': 'occupied', 'capacity': 750, 'kilometers_remaining': 8500, 'station_id': 'Station9', 'num_wagons': 52},
    {'id': 'Train67', 'status': 'in maintenance', 'capacity': 610, 'kilometers_remaining': 12000, 'station_id': 'Station9', 'num_wagons': 45},
    {'id': 'Train68', 'status': 'free', 'capacity': 680, 'kilometers_remaining': 9500, 'station_id': 'Station9', 'num_wagons': 56},
    {'id': 'Train69', 'status': 'occupied', 'capacity': 490, 'kilometers_remaining': 11000, 'station_id': 'Station9', 'num_wagons': 40},
    {'id': 'Train70', 'status': 'free', 'capacity': 530, 'kilometers_remaining': 7500, 'station_id': 'Station9', 'num_wagons': 58},
    {'id': 'Train71', 'status': 'in maintenance', 'capacity': 620, 'kilometers_remaining': 6000, 'station_id': 'Station9', 'num_wagons': 50},
    {'id': 'Train72', 'status': 'occupied', 'capacity': 560, 'kilometers_remaining': 13000, 'station_id': 'Station9', 'num_wagons': 54},
    # Trains for station 10
    {'id': 'Train73', 'status': 'free', 'capacity': 470, 'kilometers_remaining': 14000, 'station_id': 'Station10', 'num_wagons': 47},
    {'id': 'Train74', 'status': 'occupied', 'capacity': 710, 'kilometers_remaining': 5000, 'station_id': 'Station10', 'num_wagons': 42},
    {'id': 'Train75', 'status': 'in maintenance', 'capacity': 560, 'kilometers_remaining': 9000, 'station_id': 'Station10', 'num_wagons': 53},
    {'id': 'Train76', 'status': 'free', 'capacity': 640, 'kilometers_remaining': 7500, 'station_id': 'Station10', 'num_wagons': 55},
    {'id': 'Train77', 'status': 'occupied', 'capacity': 590, 'kilometers_remaining': 8500, 'station_id': 'Station10', 'num_wagons': 49},
    {'id': 'Train78', 'status': 'free', 'capacity': 520, 'kilometers_remaining': 9500, 'station_id': 'Station10', 'num_wagons': 51},
    {'id': 'Train79', 'status': 'in maintenance', 'capacity': 650, 'kilometers_remaining': 10500, 'station_id': 'Station10', 'num_wagons': 58},
    {'id': 'Train80', 'status': 'occupied', 'capacity': 470, 'kilometers_remaining': 11500, 'station_id': 'Station10', 'num_wagons': 46},
]
