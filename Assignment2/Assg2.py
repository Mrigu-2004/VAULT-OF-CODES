#Secret Code Generator
# Function to encode a message
def encode_message(message, shift):
    encoded_message = ""  # Initialize an empty string to store the encoded message
    for char in message:  # Iterate over each character in the input message
        # Check if the character is an uppercase letter
        if char.isupper():
            # Convert to ASCII, apply the shift, and wrap around with modulo 26 for uppercase letters
            encoded_message += chr(((ord(char) - 65 + shift) % 26) + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Convert to ASCII, apply the shift, and wrap around with modulo 26 for lowercase letters
            encoded_message += chr(((ord(char) - 97 + shift) % 26) + 97)
        else:
            # If the character is not a letter, add it unchanged to the encoded message
            encoded_message += char
    return encoded_message  # Return the final encoded message

# Function to decode a message
def decode_message(encoded_message, shift):
    decoded_message = ""  # Initialize an empty string to store the decoded message
    for char in encoded_message:  # Iterate over each character in the encoded message
        # Check if the character is an uppercase letter
        if char.isupper():
            # Convert to ASCII, reverse the shift, and wrap around with modulo 26 for uppercase letters
            decoded_message += chr(((ord(char) - 65 - shift) % 26) + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Convert to ASCII, reverse the shift, and wrap around with modulo 26 for lowercase letters
            decoded_message += chr(((ord(char) - 97 - shift) % 26) + 97)
        else:
            # If the character is not a letter, add it unchanged to the decoded message
            decoded_message += char
    return decoded_message  # Return the final decoded message

# Function to handle user input and menu choices
def secret_code_generator():
    while True:  # Start an infinite loop for the main menu
        print("\nSecret Code Generator Menu")  # Display menu title
        print("1: Encode a message")  # Option to encode a message
        print("2: Decode a message")  # Option to decode a message
        print("3: Exit")  # Option to exit the program

        choice = input("Choose an option (1/2/3): ")  # Prompt the user for their choice
        
        if choice == '1':  # If user chooses to encode a message
            message = input("Enter the message to encode: ")  # Prompt for the message to encode
            while True:  # Loop to repeatedly ask for shift value until valid input is provided
                try:
                    shift = int(input("Enter the shift number: "))  # Prompt for the shift number
                    encoded_message = encode_message(message, shift)  # Call encode function
                    print(f"Encoded Message: {encoded_message}")  # Display the encoded message
                    break  # Exit the loop once a valid integer shift is entered
                except ValueError:  # Catch non-integer input for shift
                    print("Invalid shift number. Please enter a valid integer.")  # Error message
        
        elif choice == '2':  # If user chooses to decode a message
            encoded_message = input("Enter the message to decode: ")  # Prompt for the message to decode
            while True:  # Loop to repeatedly ask for shift value until valid input is provided
                try:
                    shift = int(input("Enter the shift number: "))  # Prompt for the shift number
                    decoded_message = decode_message(encoded_message, shift)  # Call decode function
                    print(f"Decoded Message: {decoded_message}")  # Display the decoded message
                    break  # Exit the loop once a valid integer shift is entered
                except ValueError:  # Catch non-integer input for shift
                    print("Invalid shift number. Please enter a valid integer.")  # Error message
        
        elif choice == '3':  # If user chooses to exit
            print("Exiting the program. Goodbye!")  # Display exit message
            break  # Break the loop to end the program
        else:  # If an invalid menu choice is made
            print("Invalid choice. Please select 1, 2, or 3.")  # Error message for invalid menu choices

# Call the main menu function to run the program
if __name__ == "__main__":
    secret_code_generator()  # Start the program by calling the main function
