"""
This file says how old you are when you input your year of birth
Code developed my Masino
"""
name = input("Hi dear!\nWhat is your name please? ")
print(f"Hello {name}! You are welcome here.")
def say_age():
    
    try:
        birth_year = input("Now tell us the year you were born: ")
        age = 2024 - int(birth_year)
        message = f"Wow, you are {age} years old."
        print(message)
        # return message
    except ValueError:
        print("Please enter a valid year.")
        say_age()
    except Exception as e:
        print(f"An error occurred: {e}")
        say_age()
if __name__ == "__main__":
    say_age()
    print("Thank you for using this program.")