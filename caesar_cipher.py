def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char

    return result

# User input
message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))
mode = input("Type 'encrypt' or 'decrypt': ").lower()

# Output
output = caesar_cipher(message, shift, mode)
print(f"\nResult: {output}")
