## Equation to find the angle between two points on the earth

`pyhon equations.py`
<img width="1188" height="164" alt="image" src="https://github.com/user-attachments/assets/d529b8e3-7d7e-4f1f-a63d-4d363dcd8700" />

## central angle \* Radius of earth = distance between point P & Q

# TRILATERATION

`pip install scipy`
`python3 trilat.py`

1. calculate distance between lat and long points. (phi,lambda)
2. Measure how WRONG a guessed location is (cause cell tower data can be noisy in practical application)
3. use minimize() to find the guessed location with the smallest error, this is the optimizer it tries to find the lat and long set where the error is the smallest

### Great circle distance()

`def great_circle_distance(latitudeA, longitudeA, latitudeB, longitudeB):`

- takes 2 GPS positions -> point A = latitudeA, longitude B point B = latitudeA, longitudeB
- returns the distance between them in kilometers.

### python trigonometric functions need radians so convert.

`phi1 = math.radians(latitudeA)`
`lambda1 = math.radians(longitudeA)`

`phi2 = math.radians(latitudeB)`
`lambda2 = math.radians(longitudeB`
where phi (weird eclipse looking symbol) is latitude and lambda is longitude

### difference in longitude

`delta_lambda = abs(lambda2 - lambda1)`

- same as finding the cartesian distance on a flat graph `delta y =  (y2 - y1)`

### Central angle

- the central angle is the FROM earths center between the two points A and B

### angle to distance

- distance = Radius of the earth x central_angle

## MSE

`def mse(x, locations,distances)`

- This function checks how good a guessed location is.
- x is the guessed unknown location:
  `x = [latitude, longitude]`

- TOWER LOCATIONS
- locations = [
  [20.000, 23.000],
  [20.100, 23.200],
  [19.900, 23.100],
  [20.050, 22.900]
  ]
