# --- comprehension is done for everythhing that is iterable



#---- list comprehension = running a for loop on a list with conditions by using a single line of code
# new_list = [expression for item in iterable if condition]


squares = [x**2 for x in range(10)]  # creates a list of squares from 0 to 9
print(squares)

squares = [x**2 for x in range(10) if x % 2 == 0]  # creates a list of squares of even numbers from 0 to 9
print(squares)

unique_initials = {item[0].lower() for item in ["Alice", "Bob", "alex", "Beta"]}  # creates a set of unique initials in lowercase
print(unique_initials)

 


# ---- nested list comprehension = doing list comprehension within another list comprehension
# new_list = [expression for item in iterable if condition for item2 in iterable2 if condition2]

nested_squares = [[x**2 for x in range(i, i+5) if x % 2 == 0] for i in range(1, 10, 3)] 
print("Nested Squares:", nested_squares)
# basically the inner list comprehension runs for each value of i in the outer list comprehension
# for first i=1, inner loop runs for x in range(1,6) and so on





# ---- dictionary comprehension = create a new dictionary from an iterable using a single line of code
# new_dict = {key:value for (key,value) in iterable if condition}

number_descriptions = {
    num: ("Even and divisible by 3 " if num % 2 == 0 and num % 3 == 0
          else "Even " if num % 2 == 0
          else "Odd and divisible by 3 " if num % 3 == 0
          else "Odd ")
    for num in range(1, 11)
}
print("Number Descriptions:", number_descriptions)
# creates a dictionary with numbers from 1 to 11 as keys and their descriptions as values



