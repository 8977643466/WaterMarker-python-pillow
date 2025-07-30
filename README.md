# Command-Line Image Watermarker 🖼️

A simple yet powerful Python script that adds a text watermark to any image directly from your command line. This tool uses the Pillow library to overlay customizable text onto an image, positioning it in the bottom-right corner with a semi-transparent effect.

![Example of a watermarked image](https://i.imgur.com/your-image-link.png) 
*An example of an image watermarked with this tool.*

***

## Table of Contents
- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [How to Use](#how-to-use)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

***

## About The Project
This project provides a straightforward command-line interface (CLI) to apply a text watermark to images. It's designed to be easy to use for developers and content creators who need a quick way to protect or label their images without using heavy graphical software. The script dynamically adjusts the font size based on the image's width and places the text neatly at the bottom-right.

***

## Key Features
- **Custom Text:** Add any watermark text you want.
- **Dynamic Font Size:** The font size automatically scales with the image width for better visibility.
- **Semi-Transparent Watermark:** The text is applied with 50% transparency to be non-intrusive.
- **Error Handling:** The script checks if the specified image file exists before processing.
- **Automatic Naming:** The watermarked image is saved automatically with a `_watermarked` suffix, preserving your original file.

***

## Project Structure
Here is the recommended layout for your files:
WaterMarker-python-pillow/
├── README.md
├── watermarker.py
├── Arial.ttf
└── images/
├── input_image.jpg
└── input_image_watermarked.jpg
- **`watermarker.py`**: The main Python script.
- **`Arial.ttf`**: The font file used for the watermark.
- **`images/`**: A directory to store your input and output images.

***

## Prerequisites
Make sure you have the following installed on your system:
- **Python 3.x**
- **pip** (Python package installer)

***

## Installation & Setup
Follow these steps to get the project set up.

1.  **Clone the Repository**
    Open your terminal and clone this repository:
    ```bash
    git clone [https://github.com/8977643466/WaterMarker-python-pillow.git](https://github.com/8977643466/WaterMarker-python-pillow.git)
    cd WaterMarker-python-pillow
    ```

2.  **Install Dependencies**
    This project relies on the **Pillow** library. Install it using pip:
    ```bash
    pip install Pillow
    ```

3.  **Add a Font File (Recommended)**
    For the best results, place a TrueType Font file (`.ttf`) in the project's root directory. The script is configured to look for `Arial.ttf`. You can download fonts from [Google Fonts](https://fonts.google.com/).

***

## How to Use
Running the script is done entirely through the command line.

1.  **Navigate to the project directory** in your terminal.

2.  **Run the script** using the `python` command:
    ```bash
    python watermarker.py
    ```

3.  **Follow the prompts:**
    - The script will first ask you to **enter the path to your image**.
    - Next, it will ask you to **enter the watermark text**.

4.  **Done!** The script will process the image and save a new file in the same directory.

#### **Example Interaction:**
```bash
$ python watermarker.py
Enter the path to your image: images/ship.jpg
Enter the watermark text: This is a ship
✅ Success! Watermarked image saved as: images/ship_watermarked.jpg
