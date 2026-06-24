import math

def great_circle_distance(latitudeA, longitudeA,latitudeB, longitudeB):
    phi1 = math.radians(latitudeA)
    lambda1 = math.radians(longitudeA)

    phi2 = math.radians(latitudeB)
    lambda2 = math.radians(longitudeB)

    #delta Y
    delta_lambda = math.fabs(lambda2 - lambda1)
    central_angle = \
    math.atan2 \
    (
        math.sqrt(
            math.pow(
                math.cos(phi2) * math.sin(delta_lambda)
                , 2.0
            )
            +
            math.pow(
                math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) *
math.cos(delta_lambda)
                , 2.0
            )
        )
        (
            math.sin(phi1) * math.sin(phi2) +
            math.cos(phi1) * math.cos(phi2) *
math.cos(delta_lambda)
        )
    )
    R = 6371.009
    return R * central_angle
