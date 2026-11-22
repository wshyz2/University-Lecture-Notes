# x = "Dexter" * (2 + 3)
# y = "Dexter" * (2 + 3) == "Laboratory" + "is cool"

# a = ("Dexter" + " and Dee Dee" * 2)
# b = ("Dexter" + " and Dee Dee" * 2) * (3 - 1) 
# c = "Dexter and Dee DeeDee Dee" * 2 
# d = "Dexter and Dee DeeDee Dee" * 2 + " is smart!" * (1 + 1) 
# e = "Dexter and Dee DeeDee Dee" * 2 + " is smart!" * (1 + 1) > "Dexter is cool!"
# f = ("Dexter" + " and Dee Dee" * 2) * (3 - 1) == "Dexter and Dee DeeDee Dee" * 2 + " is smart!" * (1 + 1) > "Dexter is cool!"

# p = (5 < 10 and "Dexter" != "Dee Dee")
# q = (3 * 2 == 6 and not (4 > 5))
# r = ("Hello" * 2 == "HelloHello" or "World" != "world")
# s = (5 < 10 and "Dexter" != "Dee Dee") or (3 * 2 == 6 and not (4 > 5))
# t = (5 < 10 and "Dexter" != "Dee Dee") or (3 * 2 == 6 and not (4 > 5)) and ("Hello" * 2 == "HelloHello" or "World" != "world")


# print("x =", x)
# print("y =", y)
# print("\n")

# print("a =", a)
# print("b =", b)
# print("c =", c)
# print("d =", d)
# print("e =", e)
# print("f =", f)
# print("\n")

# print("p =", p)
# print("q =", q)
# print("r =", r)
# print("s =", s)
# print("t =", t)
# print("\n")

# # Program using for loop, break, and continue  
# print("Doctor Strange's Spell Casting:")

# for spell_number in range(1, 11):  # Casting spells from 1 to 10  
#     if spell_number % 2 == 0:  # Skip even spell numbers  
#         continue  
#     if spell_number == 8:  # Stop casting at spell number 8  
#         break  
#     print(f"Casting spell number: {spell_number}")

# # Program using while loop, break, continue, and pass  
# print("Doctor Strange's Spell Practice Timer:")
# timer = 0

# while timer < 10:  # Practice until 10 minutes  
#     timer += 1  
#     if timer == 5:  # Skip practicing at 5 minutes  
#         continue  
#     if timer > 8:  # Stop practicing if timer exceeds 8 minutes  
#         break  
#     if timer == 7:  # Do nothing at 7 minutes  
#         pass  
#     print(f"Practicing spell for {timer} minute(s)")

# # Program using if-else with break, continue, and pass  
# print("Doctor Strange's Spell Element Review:")

# for element in ["air", "fire", "water", "earth", "lightning"]:  # Different spell elements  
#     if element == "fire":  # Skip the fire element  
#         continue  
#     if element == "earth":  # Stop the review if encountering earth  
#         break  
#     if element == "water":  # Do nothing for the water element  
#         pass  
#     print(f"Reviewing spell element: {element}")

# # Original message  
# message = "Kafka Hibino, Kaiju No. 8, is ready to fight!"

# # Constructing the final message with string methods, indexing, and slicing  
# final_message = (message.lower().replace("kaiju", "monster").strip() + 
#     " let's go! " .rstrip("\n") + message[14:20])

# if final_message.endswith(" "):  # Example check if the message ends with an exclamation mark  
#     is_alnum = message[16:19].isalnum()  # Check if the sliced part is alphanumeric  
#     final_message += " - Alphanumeric Check: " + str(is_alnum)  # Append the result of the alphanumeric check  
# else:
#     final_message += " - Message does not end with a space."

# # Print the final result  
# print("Final Message:", final_message)

# # Original function to display product details  
# def display_product_details(brand, product_name, price, ingredients):
#     print(f"Brand: {brand}")
#     print(f"Product: {product_name}")
#     print(f"Price: ${price:.2f}")
#     print("Ingredients:")
#     for ingredient in ingredients:
#         print(f"- {ingredient}")

# # Example usage  
# brand_name = "Dior"
# product = "Radiant Foundation"
# product_price = 29.99  
# product_ingredients = ["Water", "Titanium Dioxide", "Glycerin", "Dimethicone"]

# display_product_details(brand_name, product, product_price, product_ingredients)

# # One parameter and one arguments
# def display_product_details(product_info):
#     brand = product_info.get("brand")
#     product_name = product_info.get("product_name")
#     price = product_info.get("price")
#     ingredients = product_info.get("ingredients", [])
    
#     print(f"Brand: {brand}")
#     print(f"Product: {product_name}")
#     print(f"Price: ${price:.2f}")
#     print("Ingredients:")
#     for ingredient in ingredients:
#         print(f"- {ingredient}")

# product_info = {
#     "brand": "Glamour Cosmetics",
#     "product_name": "Radiant Foundation",
#     "price": 29.99,
#     "ingredients": ["Water", "Titanium Dioxide", "Glycerin", "Dimethicone"]
# }

# display_product_details(product_info)

# # One parameter and a list of arguments
# def display_product_details(product_details):
#     brand, product_name, price, ingredients = product_details  
#     print(f"Brand: {brand}")
#     print(f"Product: {product_name}")
#     print(f"Price: ${price:.2f}")
#     print("Ingredients:")
#     for ingredient in ingredients:
#         print(f"- {ingredient}")

# product_details = ["Glamour Cosmetics", "Radiant Foundation", 29.99, ["Water", "Titanium Dioxide", "Glycerin", "Dimethicone"]]
# display_product_details(product_details)

# # Using default parameter values
# def display_product_details(brand, product_name, price=0.0, ingredients=["Water", "Titanium Dioxide", "Glycerin", "Dimethicone"]):
#     print(f"Brand: {brand}")
#     print(f"Product: {product_name}")
#     print(f"Price: ${price:.2f}")
#     print("Ingredients:")
#     for ingredient in ingredients:
#         print(f"- {ingredient}")
# display_product_details("Glamour Cosmetics", "Radiant Foundation")

# # Using variable-length arguments (args)
# def display_product_details(brand, product_name, *ingredients):
#     print(f"Brand: {brand}")
#     print(f"Product: {product_name}")
#     print("Ingredients:")
#     for ingredient in ingredients:
#         print(f"- {ingredient}")

# display_product_details("Glamour Cosmetics", "Radiant Foundation", "Water", "Titanium Dioxide", "Glycerin", "Dimethicone")

# # Combining default values and keyword arguments
# def display_product_details(brand, product_name, price=0.0, ingredients=None):
#     if ingredients is None:
#         ingredients = []
#     print(f"Brand: {brand}")
#     print(f"Product: {product_name}")
#     print(f"Price: ${price:.2f}")
#     print("Ingredients:")
#     for ingredient in ingredients:
#         print(f"- {ingredient}")

# display_product_details(
#     brand="Glamour Cosmetics",
#     product_name="Radiant Foundation",
#     ingredients=["Water", "Titanium Dioxide", "Glycerin", "Dimethicone"])

# # Define the ocean name  
# ocean_name = "Pacific"

# # Function to print the pattern  
# def print_ocean_pattern(ocean_name):
#     # Iterate through the length of the ocean name  
#     for i in range(len(ocean_name) + 1):
#         # Print the substring from the start to the current index  
#         print(ocean_name[:i])

# # Call the function to print the pattern  
# print_ocean_pattern(ocean_name)

# # List of oceans in the world  
# oceans = ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Arctic Ocean"]

# # Function to print names of oceans in pyramid shape  
# def print_ocean_pyramid(oceans):
#     for ocean in oceans:
#         for i in range(len(ocean) + 1):  # Loop through each character in ocean name  
#             print(ocean[:i])  # Print the substring from the start to the current index  
#         print()  # Print a newline for better separation between ocean names

# # Call the function to print the pyramid shape  
# print_ocean_pyramid(oceans)

# # List of different cakes  
# cakes = ["Chocolate Cake", "Vanilla Cake", "Red Velvet Cake", "Carrot Cake", "Cheesecake"]

# # Function to print cake names with a message  
# def print_cake_messages(cakes):
#     for cake in cakes:
#         print(f"{cake} is delicious!")

# # Call the function to display the messages  
# print_cake_messages(cakes)


# cake_messages_tuple = tuple(f"{cake} is delicious!" for cake in cakes) 
# cake_messages_set = {f"{cake} is delicious!" for cake in cakes}
# cake_messages_dict = {cake: f"{cake} is delicious!" for cake in cakes}
# cake_messages_list = [f"{cake} is delicious!" for cake in cakes]

# print(cake_messages_tuple)
# print(cake_messages_set)
# print(cake_messages_dict)
# print(cake_messages_list)

# # List of questions and answers about data types in Python  
# questions_answers = [
#     ("What is a list?", "Mutable"),
#     ("What is a tuple?", "Immutable"),
#     ("What is a set?", "Unordered"),
#     ("What is a dictionary?", "Ordered"),
#     ("Can a list have duplicates?", "Yes"),
#     ("Can a tuple have duplicates?", "Yes"),
#     ("Does a set allow duplicates?", "No"),
#     ("Can you change a tuple after creation?", "No"),
#     ("What is type casting?", "Changing type"),
#     ("Are lists ordered?", "Yes"),
#     ("Are dictionaries ordered?", "Yes (Python 3.7+)"),
# ]

# # Open a file to write the output in tabular format using write and append modes  
# with open("data_types_questions.txt", "w") as file:
#     # Write the header  
#     file.write("Question\tAnswer\n")
#     file.write("-" * 40 + "\n")  # Separator line
    
#     # Write the first question and answer in write mode  
#     file.write(f"{questions_answers[0][0]}\t{questions_answers[0][1]}\n")

# # Open the same file in append mode to add more questions  
# with open("data_types_questions.txt", "a") as file:
#     # Append the remaining questions and answers  
#     for question, answer in questions_answers[1:]:
#         file.write(f"{question}\t{answer}\n")

# print("Questions and answers have been written to 'data_types_questions.txt'.")

# import numpy as np

# # Array representing planets and their diameters (in kilometers)
# # Each row contains [Planet Name (as a string), Diameter]
# planets = np.array([
#     ["Mercury", 4879],
#     ["Venus", 12104],
#     ["Earth", 12756],
#     ["Mars", 6779]
# ])

# # Extract the diameter column and convert it to an integer type for calculations  
# diameters = np.array(planets[:, 1], dtype=int)
# print("diameters = ",diameters)

# # Modify the diameter array: double the diameters and add the sum of diameters along axis 0  
# modified_diameters = diameters * (120 - 2 * 10) + np.sum(diameters, axis=0)
# print("modified_daiameters = ", modified_diameters)

# # Combine the modified diameters with the planet names  
# modified_planets = np.column_stack((planets[:, 0], modified_diameters))

# # Print the modified array  
# print("modified_planets = ", modified_planets)

# a = np.sum(diameters, axis=0)
# print(a)


# import pandas as pd

# # Creating a dictionary with flower names, their growth stages, and their native regions  
# data = {
#     'Flower': ['Rose', 'Daffodil', 'Tulip'],
#     'Growth Stage (Years)': [2, 3, 4],
#     'Native Region': ['Europe', 'Asia', 'North America']
# }

# # Creating a DataFrame from the flower data  
# df = pd.DataFrame(data)

# # Adding 1 year to each flower's growth stage to represent maturation  
# df['Growth Stage (Years)'] = df['Growth Stage (Years)'] + 1

# # Printing the updated flower DataFrame  
# print("Flower Data:")
# print(df)

# # Creating a Pandas Series representing the number of flower species in different gardens  
# flower_series = pd.Series([15, 20, 12, 18], index=['Rose Garden', 'Daffodil Patch', 'Tulip Field', 'Sunflower Grove'])
# print("\nFlower Species in Various Gardens:")
# print(flower_series)

# # Creating a DataFrame to represent information about flower types in different botanical collections  
# flower_data_frame = pd.DataFrame({
#     'Flower Name': ['Rose', 'Daffodil', 'Tulip'],
#     'Petal Count': [5, 6, 6],
#     'Botanical Collection': ['Herbarium A', 'Herbarium B', 'Herbarium C']
# })

# # Printing the flower data DataFrame  
# print("\nFlowers in Different Botanical Collections:")
# print(flower_data_frame)

# # initializing string 
# test_str = "PolyU"
# # initializing number
# test_int = 4
# # printing original string 
# print("The original string is : " + test_str)
# # printing number
# print("The original number : " + str(test_int))
# # using type conversion
# # Inserting number in string 
# res1 = test_str + str(test_int) + test_str
# # printing result 
# print("The string after adding number is : " + str(res1))
# res2 = (test_str + "%d" + test_str) % test_int
# # printing result 
# print("The string after adding number is : " + str(res2))

# numbers = [1, 2, 3]

# result = isinstance(numbers, list)
# print(numbers,'instance of list?', result)

# result = isinstance(numbers, dict)
# print(numbers,'instance of dict?', result)

# result = isinstance(numbers, (dict, list))
# print(numbers,'instance of dict or list?', result)

# number = 5

# result = isinstance(number, list)
# print(number,'instance of list?', result)

# result = isinstance(number, int)
# print(number,'instance of int?', result)

# def check_number(var):
#     if isinstance(var, (int, float)):
#         print('variable', var, 'is instance of numeric type')
#     else:
#         print('variable', var, 'is not instance of numeric type')

# num1 = 80
# check_number(num1)
# # Output variable 80 is instance of numeric type

# num2 = 55.70
# check_number(num2)
# # Output variable 55.7 is instance of numeric type

# num3 = '20'
# check_number(num3)
# # Output variable '20' is not instance of numeric type


# L = [1, 5, 4, 2, 3]
 
# # Sorting the list in-place using sort()
# L.sort()
 
# # Print the sorted list
# print("Sorted list:")
# print(L)
 
# # Print the original list after sorting
# print("\nOriginal list after sorting:")
# print(L)


# # List
# x_list = ['q', 'w', 'r', 'e', 't', 'y']
# print("Original List:", x_list)
# sorted_list = sorted(x_list)
# print("Sorted List:", sorted_list)
 
# # Tuple
# x_tuple = ('q', 'w', 'e', 'r', 't', 'y')
# print("\nOriginal Tuple:", x_tuple)
# sorted_tuple = sorted(x_tuple)
# print("Sorted Tuple:", sorted_tuple)

# # Sorting a list  
# numbers = [5, 2, 9, 1, 5, 6]
# print("Original list:", numbers)

# # Using sort() (in-place sorting)
# numbers.sort()
# print("Sorted list (in-place):", numbers)

# # Using sorted() (returns a new sorted list)
# sorted_numbers = sorted([5, 2, 9, 1, 5, 6])
# print("Sorted list (new list):", sorted_numbers)

# # Sorting a tuple (Tuples are immutable, so we use sorted())
# my_tuple = (3, 1, 4, 1, 5, 9)
# sorted_tuple = sorted(my_tuple)
# print("Sorted tuple:", sorted_tuple)

# # Sorting a set  
# my_set = {3, 1, 4, 1, 5, 9, 2}
# print("Original set:", my_set)

# # Using sorted() to sort a set (returns a new sorted list)
# sorted_set = sorted(my_set)
# print("Sorted set:", sorted_set)

# # Sorting a dictionary by keys  
# my_dict = {'banana': 3, 'apple': 4, 'orange': 2}
# print("Original dictionary:", my_dict)

# # Using sorted() to sort the dictionary by keys  
# sorted_dict_by_keys = sorted(my_dict)
# print("Dictionary sorted by keys:", sorted_dict_by_keys)

# # Function to get the value from the dictionary item  
# def get_value(item):
#     return item[1]

# # Sorting the dictionary by values  
# sorted_dict_by_values = sorted(my_dict.items(), key=get_value)
# print("Dictionary sorted by values:", sorted_dict_by_values)

# # Sort a list of dictionaries by a specific key  
# list_of_dicts = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 20}, {'name': 'Dave', 'age': 30}]
# print("Original list of dictionaries:", list_of_dicts)

# # Function to get the 'age' value from the dictionary  
# def get_age(item):
#     return item['age']

# # Sorting the list of dictionaries by the 'age' key  
# sorted_list_of_dicts = sorted(list_of_dicts, key=get_age)
# print("List of dictionaries sorted by age:", sorted_list_of_dicts)

# def count_stations_recursive(stations):
#     # Base case: if there's no station left  
#     if not stations:
#         return 0  
    
#     # Count this station and continue with the rest  
#     return 1 + count_stations_recursive(stations[1:])

# def get_english_name(item):
#     # Ensure the item is a tuple and return the English name  
#     if isinstance(item, tuple):
#         return item[0]  # Return the English name  
#     return ""

# def get_chinese_name(item):
#     # Ensure the item is a tuple and return the Chinese name  
#     if isinstance(item, tuple):
#         return item[1]  # Return the Chinese name  
#     return ""

# # Example usage  
# mtr_stations = [
#     ('Admiralty', '金鐘'),
#     ('Central', '中環'),
#     ('Tsim Sha Tsui', '尖沙咀'),
#     ('Jordan', '佐敦'),
#     ('Yau Ma Tei', '油麻地'),
#     ('Mong Kok', '旺角'),
#     ('Causeway Bay', '銅鑼灣'),
#     ('Tai Wai', '大圍')
# ]

# # Call the function to count total stations  
# total_stations = count_stations_recursive(mtr_stations)
# print("Total stations:", total_stations)

# # Sort the stations in place by English names using sort() method  
# mtr_stations.sort(key=get_english_name)  # Sort by English name  
# print("Stations sorted by English names:", mtr_stations)

# # Create a new sorted list by Chinese names using sorted() function  
# sorted_stations_chinese = sorted(mtr_stations, key=get_chinese_name)  # Sort by Chinese name  
# print("Stations sorted by Chinese names:", sorted_stations_chinese)

# # Combine English and Chinese names into a single sorted list  
# combined_stations = []

# # Add English names first  
# for item in mtr_stations:
#     combined_stations.append(get_english_name(item))  # Append English name

# # Add Chinese names next  
# for item in mtr_stations:
#     combined_stations.append(get_chinese_name(item))  # Append Chinese name

# print("Combined list with English names first:", combined_stations)

# def is_numeric(item):
#     # Check if the item is an int or float  
#     return isinstance(item, (int, float))

# # Define the list of MTR stations and durations  
# mtr_stations = [
#     'Admiralty', '金鐘', 3.5, 'Central', '中環', 4,
#     'Tsim Sha Tsui', '尖沙咀', 5, 'Jordan', '佐敦', 2.5,
#     'Yau Ma Tei', '油麻地', 3, 'Mong Kok', '旺角', 2,
#     'Causeway Bay', '銅鑼灣', 4.5, 'Tai Wai', '大圍', 6  
# ]

# # Separate names and numbers into two lists  
# names = [item for item in mtr_stations if not is_numeric(item)]
# numbers = [item for item in mtr_stations if is_numeric(item)]

# # Sort both lists  
# sorted_names = sorted(names)
# sorted_numbers = sorted(numbers)

# # Combine the sorted results  
# sorted_combined = sorted_names + sorted_numbers

# # Print the sorted combined list  
# print("Combined list in ascending order:")
# for item in sorted_combined:
#     print(item)