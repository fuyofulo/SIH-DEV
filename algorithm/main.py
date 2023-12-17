from syntheticdata import siding, stations, trains
from step1algorithm import find_suitable_train
from datetime import datetime


def get_user_input():
    try:
        siding_name = input("Enter the name of the siding: ")
        coal_to_be_collected = float(input("Enter the amount of coal to be collected (in tons): "))
        destination_latitude = float(input("Enter the destination latitude: "))
        destination_longitude = float(input("Enter the destination longitude: "))
        arrival_date_time_str = input("Enter the date and time for the train to reach the siding (YYYY-MM-DD HH:MM): ")
        

        # Convert the input string to a datetime object
        arrival_date_time = datetime.strptime(arrival_date_time_str, "%Y-%m-%d %H:%M")

        # Find the siding with the matching name and update values
        matching_sidings = [s for s in siding if s['id'] == siding_name]
        
        if matching_sidings:
            matching_siding = matching_sidings[0]
            matching_siding['coal_to_be_collected'] = coal_to_be_collected
            matching_siding['destination_latitude'] = destination_latitude
            matching_siding['destination_longitude'] = destination_longitude
            matching_siding['arrival_date_time'] = arrival_date_time
            return matching_siding 
        else:
            print(f"Siding with the name '{siding_name}' not found.")
            return None
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return None

if __name__ == "__main__":
    siding_data = get_user_input()
    if siding_data:
        suitable_train_id = find_suitable_train(siding_data, stations, trains)
        if suitable_train_id:
            print(f"Train {suitable_train_id} is suitable for the request from {siding_data['id']}.")
        else:
            print(f"No suitable train found for the request from {siding_data['id']}.")
