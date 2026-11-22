# x = 100
# print("The value of x is", x, "and ID of x is", id(x))

# x = 200
# print("The value of x is", x, "and ID of x is", id(x))

# str1 = 'Hello, World!'
# print(str1)
# len(str1)
# str1[1]
# str1[0] = 'o'
# str1[1:4]

# raw_s = r'Hi\nHello'
# print(raw_s) 
# text='Dragons\'s and tiger\'s den'
# print(text)

# s1 = "string1"
# s2 = "string2"
# print(s1 + s2)
# print(s1 == s1)
# print(s1 == s2)
# s2 = s1
# print(s1)
# print(s2)
# print( s1 * 2)
# print(s1 != s1)
# print(s1 != s2)

# text = ("Zxl![]")
# print(max(text), min(text))

# text = ' hello '
# print(text)
# print(' hello '.strip())
# print(' hello '.lstrip())
# print(' hello '.rstrip())

# import random
# low = 1  
# high = 100  
# random_number = random.randint(low, high)  
# print("Random Number:", str(random_number))

# num_rolls = 10  
# outcomes = ""  
# for _ in range(num_rolls):  
#     roll = random.randint(1, 6)  
#     outcomes += str(roll) + ", "  # Append each roll as a string  
# print("Dice Rolls:", outcomes.strip(", "))  # Remove last comma and space

# target = 4  
# target_count = outcomes.count(str(target))  
# total_rolls = num_rolls  

# probability = target_count / total_rolls  
# print("Probability of rolling a 4:", probability)

# print("Outcomes:", outcomes.strip(", "))  
# print("Estimated Probability of rolling a 4:", probability)

# # my_script.py
# def greet():
#     print("Hello! Welcome to the Python world.")

# if __name__ == "__main__":
#     greet()  # This will only run if the script is executed directly.
    
# # another_script.py
# import my_script

# original_string = input("Enter the original string: ")
# substring_to_replace = input("Enter the substring to replace: ")
# replacement_substring = input("Enter the replacement substring: ")

# # Replace substring in original string  
# result = original_string.replace(substring_to_replace, replacement_substring)
# print(result)

# main_string = input("Enter the main string: ")
# substring = input("Enter the substring: ")

# # Find the starting index of the substring (case-insensitive)
# index = main_string.lower().find(substring.lower())

# if index != -1:
#     print(f"Starting index: {index}")
# else:
#     print("Substring not found.")

# input_string = input("Enter a string: ")

# # Reverse the order of words  
# words = input_string.split()  # Split the string into words  
# reversed_words = ' '.join(reversed(words))  # Reverse the list of words and join back  
# print(reversed_words)

# input_string = input("Enter a string: ")

# # Count frequency of each character  
# frequency = {}
# for char in input_string:
#     frequency[char] = frequency.get(char, 0) + 1  # Count each character

# # Sort the dictionary by character  
# sorted_frequency = dict(sorted(frequency.items()))
# print(sorted_frequency)

# # Take input from the user for the string  
# input_string = input("Enter a string: ")

# # Take input from the user for the number  
# index = int(input("Enter a number (index): "))

# # Slice the string from the beginning to the given index  
# sliced_string = input_string[:index]

# # Print the result  
# print(sliced_string)

# # Take input from the user  
# input_string = input("Enter a string: ")

# # Normalize the string: convert to lowercase  
# normalized_string = input_string.lower()  # Convert to lowercase

# # Initialize an empty string for the normalized result  
# final_normalized_string = ""

# # Loop through each character in the normalized string  
# for c in normalized_string:
#     if c.isalnum():  # Check if the character is alphanumeric  
#         final_normalized_string += c  # Add the character to the result if it is alphanumeric

# # Check if the normalized string is the same backward  
# if final_normalized_string == final_normalized_string[::-1]:
#     print("This string is a palindrome.")
# else:
#     print("This string is not a palindrome.")

# text = "Donald bought a pen!"
# print(text[16:end])

s = "I'm a string"
print(type(s))