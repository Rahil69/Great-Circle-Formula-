import math
from scipy.optimize import minimize
def great_circle_distance(latitudeA, longitudeA, latitudeB, longitudeB):
    phi1 = math.radians(latitudeA)
    lambda1 = math.radians(longitudeA)

    phi2 = math.radians(latitudeB)
    lambda2 = math.radians(longitudeB)

    delta_lambda = abs(lambda2 - lambda1)

    y = math.sqrt(
        (math.cos(phi2) * math.sin(delta_lambda)) ** 2
        +
        (
            math.cos(phi1) * math.sin(phi2)
            - math.sin(phi1) * math.cos(phi2) * math.cos(delta_lambda)
        ) ** 2
    )

    x = (
        math.sin(phi1) * math.sin(phi2)
        +
        math.cos(phi1) * math.cos(phi2) * math.cos(delta_lambda)
    )

    central_angle = math.atan2(y, x)

    R = 6371.009
    return R * central_angle




def mse(x, locations, distances):
    mse = 0.0
    for location, distance in zip(locations, distances):
        distance_calculated = great_circle_distance(x[0], x[1], location[0], location[1])
        mse += math.pow(distance_calculated - distance, 2.0)
    return mse / len(distances)

## TRILATERATION OPTIMIZATION

# where locations is a list of towers/beacons locations = [
#     [20, 23],
#     [21, 24],
#     [19, 22]
# ]


# and x is the guessed location, x = [20.5, 73.2]
# guessed latitude = 20.5
# guessed longitude = 73.2


#distances is the real known distance of point(s) from the tower
#distances = [5.2, 3.8, 6.1]
# unknown point is 5.2 km from tower 1
# unknown point is 3.8 km from tower 2
# unknown point is 6.1 km from tower 3

# mse is the value of the error which is started at 0.0
# initial_location: (lat, long)
# locations: [ (lat1, long1), ... ]
# distances: [ distance1,     ... ] 




# Fake tower/beacon data
locations = [
    [20.000, 23.000],  # tower 1
    [20.100, 23.200],  # tower 2
    [19.900, 23.100],  # tower 3
    [20.050, 22.900],  # tower 4
]

distances = [
    15.0,  # distance from unknown point to tower 1 in km
    20.0,  # distance from unknown point to tower 2 in km
    8.0,   # distance from unknown point to tower 3 in km
    12.0,  # distance from unknown point to tower 4 in km
]
min_distance = float("inf")
closest_location = None

for location,distance in zip(locations,distances):
    if distance < min_distance:
        min_distance = distance 
        closest_location = location

initial_location = closest_location

result = minimize(
    mse,
    initial_location,
    args=(locations,distances),
    method="L-BFGS-B",
    options={
        "ftol":1e-5,
        "maxiter":100000
    }
)
estimated_location = result.x
print("Estimated latitude:", estimated_location[0])
print("Estimated longitude:", estimated_location[1])
print("Final MSE:", result.fun)
print("Optimization success:", result.success)