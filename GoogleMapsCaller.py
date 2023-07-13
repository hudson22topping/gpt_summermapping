import googlemaps

# Enter your Google Maps API key here
API_KEY = 'YOUR_API_KEY'

# Initialize the Google Maps client
gmaps = googlemaps.Client(key=API_KEY)

def get_directions(departure_address, destination_address, mode):
    # Request directions from the Google Maps API
    directions_result = gmaps.directions(departure_address, destination_address, mode=mode)

    # Extract the relevant information from the directions response
    if len(directions_result) > 0:
        # Extract the duration and distance information for the first route
        leg = directions_result[0]['legs'][0]
        duration = leg['duration']['text']
        distance = leg['distance']['text']
        steps = leg['steps']

        # Print the directions
        print(f"Directions from {departure_address} to {destination_address} (Mode: {mode})")
        print(f"Duration: {duration}")
        print(f"Distance: {distance}")
        print("Steps:")
        for i, step in enumerate(steps):
            print(f"Step {i+1}: {step['html_instructions']}")
            print(f"Duration: {step['duration']['text']}")
            print("-----------------------")
    else:
        print("No directions found.")

# Example usage
departure_address = "123 Main St, City, State"
destination_address = "456 Elm St, City, State"
mode = "driving"  # Specify the desired mode of transportation

get_directions(departure_address, destination_address, mode)
