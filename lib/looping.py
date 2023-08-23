def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")

# Call the function to start the countdown
happy_new_year()

# new code
def square_integers(integer_list):
    squared_list = []  # Initialize an empty list to store squared elements
    for num in integer_list:
        squared_list.append(num ** 2)  # Append the squared value to the squared_list
    return squared_list

# Example usage
input_list = [1, 2, 3, 4, 5]
result = square_integers(input_list)
print(result)  # Should print [1, 4, 9, 16, 25]

# new code
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Call the function to print the FizzBuzz sequence
fizzbuzz()
