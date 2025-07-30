# First, make sure you have the Pillow library installed:
# pip install Pillow

from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark():
    """
    Adds a text watermark to an image provided by the user.
    """
    # 1. Get input from the user
    image_path = input("Enter the path to your image: ")
    watermark_text = input("Enter the watermark text: ")

    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' was not found.")
        return

    try:
        # 2. Open the image
        # We convert to 'RGBA' to ensure we can add a watermark with transparency
        original_image = Image.open(image_path).convert("RGBA")
        width, height = original_image.size

        # Create a transparent layer for the text watermark
        watermark_layer = Image.new('RGBA', original_image.size, (255, 255, 255, 0))

        # 3. Prepare to draw
        draw = ImageDraw.Draw(watermark_layer)

        # 4. Set up the font
        # You may need to provide a path to a .ttf font file.
        # Download one from Google Fonts (e.g., 'Roboto') and place it in the same folder.
        # We'll try to load a font, and fall back to a default if it's not found.
        font_size = int(width / 20) # Dynamic font size based on image width
        try:
            # Make sure you have a font file like 'Arial.ttf' or 'Roboto-Bold.ttf' in your directory
            font = ImageFont.truetype("Arial.ttf", font_size)
        except IOError:
            print("Font file not found. Using default font.")
            font = ImageFont.load_default()

        # 5. Position the text
        # Calculate the bounding box of the text
        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Position at the bottom-right corner with a margin
        margin = 20
        x = width - text_width - margin
        y = height - text_height - margin

        # 6. Add the watermark text
        # The last value in the fill tuple is for transparency (0=fully transparent, 255=fully opaque)
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

        # Composite the watermark layer onto the original image
        watermarked_image = Image.alpha_composite(original_image, watermark_layer)

        # 7. Save the new image
        # Get the original filename and extension to create a new name
        base, extension = os.path.splitext(image_path)
        output_path = f"{base}_watermarked{extension}"
        
        # Convert back to RGB to save as JPG if needed, as JPG doesn't support alpha
        watermarked_image.convert("RGB").save(output_path)

        print(f"✅ Success! Watermarked image saved as: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Run the main function when the script is executed
if __name__ == "__main__":
    add_watermark()