# Concatenation python
name = "Random string" # Assigning a random string
name = input("Please input your first name: ") # Asking the user for their name
welcome_message_1 = "Hi there, " # First part of the welcome message
welcome_message_2 = ". Welcome to python!" # Second part of the welcome message

name_refactor = name.strip().title() # Refactors the name to firstly remove the white spaces with strip() and then capitalises each word with title()

print(welcome_message_1 + name + welcome_message_2) # Bringing all the above together, using concatenation. Notice the spaces we had to allocate in the welcome messages above
print(welcome_message_1 + name_refactor + welcome_message_2)

# Interpolation python
full_name = "Random string" # Assigning a random string
full_name = input("Please input your full name: ") # Asking the user for their full name
welcome_message_3 = "Hi there" # First part of the welcome message
welcome_message_4 = "Welcome to python!" # Second part of the welcome message

full_name_refactor = full_name.strip().title() # Refactors the name to firstly remove the white spaces with strip() and then capitalises each word with title()

print(welcome_message_3, full_name, welcome_message_4) # Bringing all the above together with interpolation. Since this method automatically adds spaces, we don't have to account for that above
print(welcome_message_3, full_name_refactor, welcome_message_4)