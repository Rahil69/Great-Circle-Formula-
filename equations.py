import math

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

print(great_circle_distance(20, 23, 52, 34))