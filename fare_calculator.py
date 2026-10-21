# Travel Fare Calculator
FARE_RATE = 14

#hello1
name = input("Enter Passenger's Name: ").strip()
while not name:
     print("Invalid Name.")
     name = input("Enter Passenger's Name: ").strip()

#hi2
while True:
     try:
       distance = float(input("Enter Distance (KM.) :  "))
       if distance > 0:
        break
        print("Distance must be > than 0")
     except ValueError:
        print("Enter valid num for distance")
        
#hellowniceneigbor3
while True:
    try:
       Passengers = float(input("Passenger Number :  "))
       if Passengers > 0:
        break
        print("Passenger must be > than 0")
    except ValueError:
        print("Enter valid num for Passenger")
        
tfare = distance * FARE_RATE * Passengers

print("\nPassenger:", name)
print("Total fare of this passenger is: PHP", round(tfare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
