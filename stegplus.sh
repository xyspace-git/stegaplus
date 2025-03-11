#!/bin/bash

# Function to display help message
show_help() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  -h, --help                Show this help message"
    echo "  -g, --gui                 Launch GUI (not implemented)"
    echo "  -x, --extract <image>     Extract data from an image"
    echo "  -e, --embed <file>       Embed data into an image"
    echo "  -i <image>               Specify an image file (optional)"
    echo "  -c, --convert <file> <type> Convert file to specified type (base64, hex)"
    echo "  -k <keyword>             Keyword for downloading an image (optional)"
    echo "  -d, --download <keyword>  Download an image using a keyword"
    echo "  -v, --version            Show the version of the tool"
    echo "  --key <key>              Encryption key for embedding and extracting data"
}

# Function to launch a simple text-based GUI
launch_gui() {
    echo "Welcome to the Steganography Tool GUI"
    echo "Please select an option:"
    echo "1. Embed data into an image"
    echo "2. Extract data from an image"
    echo "3. Convert file"
    echo "4. Download image"
    echo "5. Exit"
    read -p "Enter your choice: " choice

    case $choice in
        1)
            read -p "Enter the file to embed: " file
            read -p "Enter the image file (or press Enter to download): " image
            read -p "Enter a keyword for downloading an image (or press Enter to skip): " keyword
            read -p "Enter an encryption key (or press Enter to skip): " key
            python3 stegplus_process.py -e "$file" -i "$image" -k "$keyword" --key "$key"
            ;;
        2)
            read -p "Enter the image file: " image
            read -p "Enter an encryption key (or press Enter to skip): " key
            python3 stegplus_process.py -x "$image" --key "$key"
            ;;
        3)
            read -p "Enter the file to convert: " file
            read -p "Enter the conversion type (base64, hex): " type
            python3 stegplus_process.py -c "$file" "$type"
            ;;
        4)
            read -p "Enter a keyword for downloading an image: " keyword
            python3 stegplus_process.py -d "$keyword"
            ;;
        5)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please try again."
            launch_gui
            ;;
    esac
}

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -g|--gui)
            launch_gui
            exit 0
            ;;
        -x|--extract)
            shift
            if [ -z "$1" ]; then
                echo "Error: No image specified for extraction."
                exit 1
            fi
            image=$1
            shift
            key=""
            while [[ $# -gt 0 ]]; do
                case $1 in
                    --key)
                        shift
                        key=$1
                        ;;
                    *)
                        echo "Unknown option: $1"
                        exit 1
                        ;;
                esac
                shift
            done
            python3 stegplus_process.py -x "$image" --key "$key"
            exit 0
            ;;
        -e|--embed)
            shift
            if [ -z "$1" ]; then
                echo "Error: No file specified for embedding."
                exit 1
            fi
            file=$1
            shift
            image=""
            keyword=""
            key=""
            while [[ $# -gt 0 ]]; do
                case $1 in
                    -i)
                        shift
                        image=$1
                        ;;
                    -k)
                        shift
                        keyword=$1
                        ;;
                    --key)
                        shift
                        key=$1
                        ;;
                    *)
                        echo "Unknown option: $1"
                        exit 1
                        ;;
                esac
                shift
            done
            python3 stegplus_process.py -e "$file" -i "$image" -k "$keyword" --key "$key"
            exit 0
            ;;
        -c|--convert)
            shift
            if [ -z "$1" ]; then
                echo "Error: No file specified for conversion."
                exit 1
            fi
            file=$1
            shift
            if [ -z "$1" ]; then
                echo "Error: No type specified for conversion."
                exit 1
            fi
            type=$1
            python3 stegplus_process.py -c "$file" "$type"
            exit 0
            ;;
        -d|--download)
            shift
            if [ -z "$1" ]; then
                echo "Error: No keyword specified for downloading an image."
                exit 1
            fi
            keyword=$1
            python3 stegplus_process.py -d "$keyword"
            exit 0
            ;;
        -v|--version)
            python3 stegplus_process.py -v
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
    shift
done

# If no arguments are provided, show help
if [ $# -eq 0 ]; then
    show_help
    exit 0
fi
