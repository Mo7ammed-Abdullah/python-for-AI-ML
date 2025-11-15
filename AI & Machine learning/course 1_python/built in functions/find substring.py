# in operator is used to check for substring presence in a string


main_string = "Hello World"
substring = "World"

if substring in main_string:
    print(f"'{substring}' found in '{main_string}'")
else:
        print(f"'{substring}' not found in '{main_string}'")