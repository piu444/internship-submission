def xor_encrypt_decrypt(data, key):
    return bytes([b ^ key for b in data])

def encrypt_file(input_path, key):
    with open(input_path, 'rb') as f:
        data = f.read()
    
    encrypted_data = xor_encrypt_decrypt(data, key)
    
    output_path = input_path + ".enc"
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)
    
    print(f"File encrypted and saved as: {output_path}")

def decrypt_file(input_path, key):
    if not input_path.endswith(".enc"):
        print("Error: This file does not appear to be encrypted with this tool.")
        return
    
    with open(input_path, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = xor_encrypt_decrypt(encrypted_data, key)
    
    output_path = input_path.replace(".enc", ".dec")
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)

    print(f"File decrypted and saved as: {output_path}")

def main():
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Enter your choice (1/2): ")

    file_path = input("Enter the full file path: ")
    try:
        key = int(input("Enter an integer key (0-255): "))
        if key < 0 or key > 255:
            raise ValueError("Key must be between 0 and 255")
    except ValueError as e:
        print("Invalid key:", e)
        return

    if choice == '1':
        encrypt_file(file_path, key)
    elif choice == '2':
        decrypt_file(file_path, key)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
