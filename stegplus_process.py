import argparse
import os
import requests
import subprocess
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
    url = f"https://source.unsplash.com/1600x900/?{keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        with open("temp_image.jpg", "wb") as file:
            file.write(response.content)
        return "temp_image.jpg"
    else:
        raise Exception("Failed to download image")

def embed_data(file, image, keyword=None, key=None):
    if not image:
        if not keyword:
            raise ValueError("No image specified and no keyword provided for downloading an image.")
        image = download_image(keyword)

    with open(file, "rb") as f:
        data = f.read()

    if key:
        encrypted_data = encrypt_data(data, key)
    else:
        encrypted_data = data

    with open("temp_data.bin", "wb") as f:
        f.write(encrypted_data)

    subprocess.run(["stegosuite", "-e", "-i", image, "-o", "output_image.png", "-p", "temp_data.bin"])
    print(f"Data embedded into {image}")

def extract_data(image, key=None):
    subprocess.run(["stegosuite", "-d", "-i", image, "-o", "extracted_data.bin"])

    with open("extracted_data.bin", "rb") as f:
        encrypted_data = f.read()

    if key:
        data = decrypt_data(encrypted_data, key)
    else:
        data = encrypted_data

    with open("extracted_data.txt", "wb") as f:
        f.write(data)

    print(f"Data extracted from {image}")

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
    parser = argparse.ArgumentParser(description="Steganography Tool")
    parser.add_argument("-e", "--embed", type=str, help="Embed data into an image")
    parser.add_argument("-i", "--image", type=str, help="Specify an image file (optional)")
    parser.add_argument("-k", "--keyword", type=str, help="Keyword for downloading an image (optional)")
    parser.add_argument("-x", "--extract", type=str, help="Extract data from an image")
    parser.add_argument("-c", "--convert", nargs=2, metavar=("file", "type"), help="Convert file to specified type (base64, hex)")
    parser.add_argument("-d", "--download", type=str, help="Download an image using a keyword")
    parser.add_argument("-v", "--version", action="store_true", help="Show the version of the tool")
    parser.add_argument("--key", type=str, help="Encryption key for embedding and extracting data")

    args = parser.parse_args()

    if args.version:
        print("Steganography Tool Version 1.0")
    elif args.embed:
        embed_data(args.embed, args.image, args.keyword, args.key)
    elif args.extract:
        extract_data(args.extract, args.key)
    elif args.convert:
        convert_file(args.convert[0], args.convert[1])
    elif args.download:
        download_image(args.download)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
