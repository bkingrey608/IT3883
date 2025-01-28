# Program Name: Assignment_1.py
# Course: IT3883/Section W02
# Student Name: Brian Kingrey
# Assignment Number: Lab#1
# Due Date: 01/27/2025
# Purpose: The program creates an empty buffer and provides options for the user to append,
# clear, and display the buffer.
# Resources used:  For this assignment I reviewed the first three lecture videos.  I've also been
# studying a Python Youtube series created by Dave Gray.  I've taken Advanced Java already, so
# mostly this is nothing new, just different syntax.  The more challenging part is setting up
# Github properly.  I've used it before in a Web Development class but I placed everything there manually

input_buffer = [] # create an empty list

while True:  # continue displaying the menu until the user exits the program
    print('\nMenu:')
    print('1. Append Data to the input buffer.' )
    print('2. Clear the input buffer.')
    print('3. Display the input buffer.')
    print('4. Exit the program.')

    selection = input('\nPlease select 1-4  ') # assign user input to the variable 'selection'

    if selection == '1':
        append_data = input('Enter data to append to the buffer:  ') #assing user input to append_data
        input_buffer.append(append_data) # add user input to the list
    elif selection == '2':
        input_buffer.clear() # clear the list
    elif selection == '3':
        print('\nInput Buffer: ', ' '.join(input_buffer)) # join each entry together, separated by a space
    elif selection == '4':
        print('Exiting the program.')
        break # exit the program
    else:
        print('Invalid selection.  Please choose 1-4.')
