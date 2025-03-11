# StegPlus

## Overview
StegPlus is a command-line utility designed to embed and extract data within images using steganography techniques. It leverages the `stegosuite` library for steganography operations and provides a user-friendly interface for various steganography tasks. The tool supports embedding and extracting data with an optional encryption key for added security.

## Features
- Embed data into images.
- Extract data from images.
- Convert files to base64 or hex format.
- Download images using keywords.
- Optional encryption key for embedding and extracting data.

## Installation

### Prerequisites
- Python 3.x
- `stegosuite` library
- `cryptography` library

### Installation Steps
#### Clone the Repository
```bash
git clone https://github.com/yourusername/stegplus.git
cd stegplus
```
#### Install Dependencies
```bash
pip install stegosuite cryptography
```
#### Make the Bash Script Executable
```bash
chmod +x stegplus
```

## Usage

### Command-Line Interface
The tool provides a set of commands for various steganography operations. Here are some examples:

#### Embed Data into an Image
```bash
./stegplus -e secret.txt -k nature
```
This command embeds the contents of `secret.txt` into an image downloaded using the keyword "nature".

#### Extract Data from an Image
```bash
./stegplus -x output_image.png
```
This command extracts data from `output_image.png` and saves it to `extracted_data.txt`.

#### Convert a File to Base64
```bash
./stegplus -c secret.txt base64
```
This command converts `secret.txt` to a base64-encoded file.

#### Download an Image Using a Keyword
```bash
./stegplus -d nature
```
This command downloads an image using the keyword "nature".

#### Show Help Message
```bash
./stegplus -h
```
This command displays the help message with usage instructions.

#### Launch GUI
```bash
./stegplus -g
```
This command launches a simple text-based GUI for interactive use.

## Encryption Key
You can use an optional encryption key for embedding and extracting data to add an extra layer of security. The key can be generated using the `generate_key` function in the Python script.

### Generate a Key
```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
```

### Embed Data with a Key
```bash
./stegplus -e secret.txt -k nature -i temp_image.jpg --key your_generated_key
```

### Extract Data with a Key
```bash
./stegplus -x output_image.png --key your_generated_key
```

## Contributing
Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any questions or support, please open an issue in the repository or contact the maintainers.
