encryption_key = {
    'A': '9', 'B': '8', 'C': '7', 'D': '6', 'E': '5', 'F': '4', 'G': '3', 'H': '2', 'I': '1', 'J': '0',
    'K': 'A', 'L': 'B', 'M': 'C', 'N': 'D', 'O': 'E', 'P': 'F', 'Q': 'G', 'R': 'H', 'S': 'I', 'T': 'J',
    'U': 'K', 'V': 'L', 'W': 'M', 'X': 'N', 'Y': 'O', 'Z': 'P',
    'a': 'q', 'b': 'r', 'c': 's', 'd': 't', 'e': 'u', 'f': 'v', 'g': 'w', 'h': 'x', 'i': 'y', 'j': 'z',
    'k': '!', 'l': '@', 'm': '#', 'n': '$', 'o': '%', 'p': '^', 'q': '&', 'r': '*', 's': '(', 't': ')',
    'u': '-', 'v': '+', 'w': '=', 'x': '{', 'y': '}', 'z': '?'
}

def encrypt_text(text, key):
    encrypted_text = "".join(key.get(char, char) for char in text)
    return encrypted_text

def main():
    file_path = 'info_security.txt'  # Replace 'info_security.txt' with the actual input file path
    output_file_path = 'encrypted.txt'  # Replace 'encrypted.txt' with the desired output file path

    try:
        with open(file_path, 'r') as infile:
            text = infile.read()

        encrypted_text = encrypt_text(text, encryption_key)

        with open(output_file_path, 'w') as outfile:
            outfile.write(encrypted_text)

        print("Encryption complete. Encrypted text written to 'encrypted.txt'.")

    except FileNotFoundError:
        print("File doesn't exist.")


if __name__ == "__main__":
    main()
