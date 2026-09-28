
# Secret Code Generator: Encode and Decode Messages using a Caesar Cipher

# Function to encode a message
def encode_message(message, shift):
    encoded_message = ""
    for char in message:
        # Check if it's an uppercase letter
        if char.isupper():
            # Shift character and handle wrap-around using modulo 26
            encoded_message += chr(((ord(char) - 65 + shift) % 26) + 65)
        # Check if it's a lowercase letter
        elif char.islower():
            # Shift character and handle wrap-around using modulo 26
            encoded_message += chr(((ord(char) - 97 + shift) % 26) + 97)
        else:
            # If it's not a letter, add it as is
            encoded_message += char
    return encoded_message

# Function to decode a message
def decode_message(encoded_message, shift):
    decoded_message = ""
    for char in encoded_message:
        # Check if it's an uppercase letter
        if char.isupper():
            # Reverse shift and handle wrap-around using modulo 26
            decoded_message += chr(((ord(char) - 65 - shift) % 26) + 65)
        # Check if it's a lowercase letter
        elif char.islower():
            # Reverse shift and handle wrap-around using modulo 26
            decoded_message += chr(((ord(char) - 97 - shift) % 26) + 97)
        else:
            # If it's not a letter, add it as is
            decoded_message += char
    return decoded_message

# Function to handle user input and menu choices
def secret_code_generator():
    while True:
        print("\nSecret Code Generator Menu")
        print("1: Encode a message")
        print("2: Decode a message")
        print("3: Exit")

        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            # Encoding
            message = input("Enter the message to encode: ")
            try:
                shift = int(input("Enter the shift number: "))
                encoded_message = encode_message(message, shift)
                print(f"Encoded Message: {encoded_message}")
            except ValueError:
                print("Invalid shift number. Please enter a valid integer.")
        
        elif choice == '2':
            # Decoding
            encoded_message = input("Enter the message to decode: ")
            try:
                shift = int(input("Enter the shift number: "))
                decoded_message = decode_message(encoded_message, shift)
                print(f"Decoded Message: {decoded_message}")
            except ValueError:
                print("Invalid shift number. Please enter a valid integer.")
        
        elif choice == '3':
            # Exit
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Call the main menu function to run the program
if __name__ == "__main__":
    secret_code_generator()

