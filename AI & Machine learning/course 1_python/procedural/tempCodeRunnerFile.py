# exception = events detected during execution that interrupt the flow of the program

# try:
#     numerator = int(input("Enter a numerator: "))
#     denominator = int(input("Enter a denominator: "))   # this can cause an exception. like dividing by zero . which can crash the program
#     result = numerator / denominator                    # so we will catch the exception and will not give its output. instead we give the except block as output
#     print(result)
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# except ValueError:
#     print("Please enter a valid number.")
# except Exception:                                        # the "Exception" will catch any other exception that we have no idea about                      
#     print("something went wrong.")



# try:
#     numerator = int(input("Enter a numerator: "))
#     denominator = int(input("Enter a denominator: "))  
#     result = numerator / denominator                    
#     print(result)
# except ZeroDivisionError as e:
#     print(e)                                # this will give the error message
#     print("You cannot divide by zero.")
# except ValueError as e:
#     print(e)
#     print("Please enter a valid number.")
# except Exception as e:
#     print(e)
#     print("something went wrong.")


