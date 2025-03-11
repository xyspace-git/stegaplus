import requests
import argparse
import os
import base64
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data)

def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data)

def download_image(keyword):
    search_url = f"https://duckduckgo.com/?q={keyword}&t=h_&iar=images&iax=images&ia=images"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        image_url = extract_first_image_url(response.text)
        if image_url:
            img_response = requests.get(image_url, headers=headers)
            if img_response.status_code == 200:
                with open("temp_image.jpg", "wb") as file:
                    file.write(img_response.content)
                return "temp_image.jpg"
    
    raise Exception("Failed to download image")

def extract_first_image_url(html):
    import re
    match = re.search(r'"(https?:\\/\\/[^"\\]+)"', html)
    if match:
        return match.group(1).replace('\\/', '/')
    return None

def embed_data(embed_file, keyword, key=None):
    image = download_image(keyword)
    print(f"Downloaded image saved as: {image}")
    
    with open(embed_file, "rb") as f:
        data = f.read()
    
    if key:
        encrypted_data = encrypt_data(data, key)
    else:
        encrypted_data = data
    
    with open("temp_data.bin", "wb") as f:
        f.write(encrypted_data)
    
    print("Data prepared for embedding.")

def extract_data(image, key=None):
    with open("extracted_data.bin", "rb") as f:
        encrypted_data = f.read()
    
    if key:
        data = decrypt_data(encrypted_data, key)
    else:
        data = encrypted_data
    
    with open("extracted_data.txt", "wb") as f:
        f.write(data)
    
    print("Data extracted successfully.")

def convert_file(file, file_type):
    if file_type == "base64":
        with open(file, "rb") as f:
            data = f.read()
        encoded_data = base64.b64encode(data)
        with open(f"{file}.base64", "wb") as f:
            f.write(encoded_data)
        print("File converted to base64")
    elif file_type == "hex":
        with open(file, "rb") as f:
            data = f.read()
        hex_data = data.hex()
        with open(f"{file}.hex", "w") as f:
            f.write(hex_data)
        print("File converted to hex")
    else:
        raise ValueError("Unsupported conversion type")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--embed", type=str, help="Data file to embed")
    parser.add_argument("--keyword", type=str, help="Keyword for image search")
    parser.add_argument("--key", type=str, help="Encryption key")
    parser.add_argument("--extract", type=str, help="Extract data from an image")
    parser.add_argument("--convert", nargs=2, metavar=("file", "type"), help="Convert file to specified type (base64, hex)")
    parser.add_argument("--version", action="store_true", help="Show the version of the tool")
    args = parser.parse_args()
    
    if args.version:
        print("Steganography Tool Version 1.0")
    elif args.embed:
        embed_data(args.embed, args.keyword, args.key)
    elif args.extract:
        extract_data(args.extract, args.key)
    elif args.convert:
        convert_file(args.convert[0], args.convert[1])
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
