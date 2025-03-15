# StegaPlus

## Rename Update:
StegPlus >> StegaPlus
## Introduction
StegaPlus is a command-line tool that allows users to embed and extract data from images using steganography. It also provides features for downloading images, encrypting embedded data, and converting files to different formats (Base64, Hex).

## Features
- Embed data into an image
- Extract data from an image
- Convert files to Base64 or Hex
- Download images from the internet
- Encrypt and decrypt data with a key
- GUI-based interaction (basic text-based)

## Installation
Ensure you have the required dependencies installed:

```bash
pip install cryptography requests
```

Make the Bash script executable:

```bash
chmod +x stegplus
```

## Usage

### Show Help
```bash
./stegplus -h
```

### Launch GUI Mode
```bash
./stegplus -g
```

### Embed Data into an Image
```bash
./stegplus -e <file> -i <image> --key <encryption_key>
```
- `<file>`: File to embed
- `<image>`: Image file to use
- `--key`: (Optional) Encryption key

### Extract Data from an Image
```bash
./stegplus -x <image> --key <encryption_key>
```
- `<image>`: Image file to extract data from
- `--key`: (Optional) Encryption key

### Convert File to Base64 or Hex
```bash
./stegplus -c <file> <type>
```
- `<file>`: File to convert
- `<type>`: `base64` or `hex`

### Download an Image
```bash
./stegplus -d <keyword>
```
- `<keyword>`: Keyword for searching an image

### Check Version
```bash
./stegplus -v
```

## Python Backend (stegplus_process.py)
The script processes embedding, extraction, and encryption using the `cryptography` module.

### Key Functions
- `download_image(keyword)`: Downloads an image from Unsplash.
- `embed_data(file, image, keyword, key)`: Embeds a file into an image with optional encryption.
- `extract_data(image, key)`: Extracts hidden data from an image.
- `convert_file(file, file_type)`: Converts a file to Base64 or Hex.

## Notes
- The tool relies on external steganography software (`stegosuite`), so ensure it's installed.
- Encryption is done using the `cryptography` library.

## Contributing
Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any questions or support, please open an issue in the repository or contact the maintainers.
