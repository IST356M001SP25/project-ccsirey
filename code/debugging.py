from apicalls import get_directions

station_from = "16th St Mission"
station_to = "Ashby"

result = get_directions(station_from, station_to, mode="driving")
print("Result:", result)