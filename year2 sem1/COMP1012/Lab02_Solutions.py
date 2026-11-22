#Q1
print("Name\t\tItem_1\t\tItem_2\nMickey_Mouse\tMap\t\tcompass\nDonald_Duck\tgold_coins\tmagical_lamp\nGoofy\t\tmystical_key\tcrown")

#Q2(a)
M = 10
C = 2
E = M*C**2
print(E)

#Q2(b)
M = int(input("Enter Mass:"))
C = int(input("Enter Speed of light:"))
E = M*C**2
print(E)

#Q2(c)
M = int(input("Enter Mass:"))
C = 3*(10**8)
E = M*C**2
print(E)

#Q2(d)
M1 = float(input("Enter Mass:"))
M2 = M1/1000
C = 3*(10**8)
E = M2*C**2
print('E =',E)

#Q3(a)
# Step 1: Accept user input for temperature in degree Celsius.
celsius = float(input("Enter temperature in Celsius: "))
# Step 2: Apply the conversion formula.
fahrenheit = (celsius * 9/5) + 32
# Step 3: Display the converted temperature in Fahrenheit
print(celsius,"degrees Celsius is equal to", fahrenheit, "degrees Fahrenheit.")

#Q3(b)
# Step 1: Accept user input for temperature in Fahrenheit.
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
# Step 2: Apply the conversion formula.
celsius = 5/9 * (fahrenheit - 32)
# Step 3: Display the converted temperature in Celsius
print(fahrenheit, "degrees Fahrenheit is equal to", celsius, "degrees Celsius.")

#Q4
import math
# Heights of three Pokémon in meters
pikachu_height = 0.41
charizard_height = 1.70
bulbasaur_height = 0.71
# Applying different rounding methods
pikachu_ceil = math.ceil(pikachu_height)
charizard_ceil = math.ceil(charizard_height)
bulbasaur_ceil = math.ceil(bulbasaur_height)
pikachu_floor = math.floor(pikachu_height)
charizard_floor = math.floor(charizard_height)
bulbasaur_floor = math.floor(bulbasaur_height)
pikachu_round = round(pikachu_height)
charizard_round = round(charizard_height)
bulbasaur_round = round(bulbasaur_height)
pikachu_trunc = math.trunc(pikachu_height)
charizard_trunc = math.trunc(charizard_height)
bulbasaur_trunc = math.trunc(bulbasaur_height)

# Displaying the results
print("Original Heights:")
print("Pikachu:", pikachu_height, "meters")
print("Charizard:", charizard_height, "meters")
print("Bulbasaur:", bulbasaur_height, "meters")
print("\nCeil Values:")
print("Pikachu:", pikachu_ceil, "meters")
print("Charizard:", charizard_ceil, "meters")
print("Bulbasaur:", bulbasaur_ceil, "meters")
print("\nFloor Values:")
print("Pikachu:", pikachu_floor, "meters")
print("Charizard:", charizard_floor, "meters")
print("Bulbasaur:", bulbasaur_floor, "meters")
print("\nRound Values:")
print("Pikachu:", pikachu_round, "meters")
print("Charizard:", charizard_round, "meters")
print("Bulbasaur:", bulbasaur_round, "meters")
print("\nTruncate Values:")
print("Pikachu:", pikachu_trunc, "meters")
print("Charizard:", charizard_trunc, "meters")
print("Bulbasaur:", bulbasaur_trunc, "meters")

#Q5
print(fahrenheit, "degrees Fahrenheit is equal to", round(celsius, 2), "degrees Celsius.")

#Q6
import math
# Coordinates of Mars
x1 = 1.0
y1 = 2.0
z1 = 3.0
# Coordinates of Phobos
x2 = 4.0
y2 = 5.0
z2 = 6.0
# Calculate the distance using the distance formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

# Display the distance with different formatting options
print("Distance between Mars and Phobos:")
print("Formatted to 5 decimal places: {:5f}".format(distance))
print("Formatted to 1 decimal place: {:5.1f}".format(distance))
print("Formatted to 2 decimal places: {:5.2f}".format(distance))
print("Formatted to 3 decimal places: {:5.3f}".format(distance))
print("Formatted to 4 decimal places: {:5.4f}".format(distance))

#Q7
import math
# Given sides of the triangle
a = 15
b = 24
c = 20
# Method A: Compute Area First, Then Altitudes, Then Angles
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
h_a = (2 * area) / a
h_b = (2 * area) / b
h_c = (2 * area) / c
A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
print(f"Method A:")
print(f"Area of the triangle: {area:.2f}")
print(f"Altitude to side a: {h_a:.2f}")
print(f"Altitude to side b: {h_b:.2f}")
print(f"Altitude to side c: {h_c:.2f}")
print(f"Angle A: {A:.2f} degrees")
print(f"Angle B: {B:.2f} degrees")
print(f"Angle C: {C:.2f} degrees")
print()

# Method B: Compute Angles First, Then Area, Then Altitudes
A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
h_a = (2 * area) / a
h_b = (2 * area) / b
h_c = (2 * area) / c
print(f"Method B:")
print(f"Angle A: {A:.2f} degrees")
print(f"Angle B: {B:.2f} degrees")
print(f"Angle C: {C:.2f} degrees")
print(f"Area of the triangle: {area:.2f}")
print(f"Altitude to side a: {h_a:.2f}")
print(f"Altitude to side b: {h_b:.2f}")
print(f"Altitude to side c: {h_c:.2f}")

# Method C: Compute Angles First, Then Altitudes, Then Area
A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
h_a = (2 * area) / a
h_b = (2 * area) / b
h_c = (2 * area) / c
print(f"Method C:")
print(f"Angle A: {A:.2f} degrees")
print(f"Angle B: {B:.2f} degrees")
print(f"Angle C: {C:.2f} degrees")
print(f"Altitude to side a: {h_a:.2f}")
print(f"Altitude to side b: {h_b:.2f}")
print(f"Altitude to side c: {h_c:.2f}")
print(f"Area of the triangle: {area:.2f}")
print()

# Method D: Compute Altitudes First, Then Angles, Then Area
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
h_a = (2 * area) / a
h_b = (2 * area) / b
h_c = (2 * area) / c
A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
print(f"Method D:")
print(f"Altitude to side a: {h_a:.2f}")
print(f"Altitude to side b: {h_b:.2f}")
print(f"Altitude to side c: {h_c:.2f}")
print(f"Angle A: {A:.2f} degrees")
print(f"Angle B: {B:.2f} degrees")
print(f"Angle C: {C:.2f} degrees")
print(f"Area of the triangle: {area:.2f}")
print()
