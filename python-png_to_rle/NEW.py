from PIL import Image

def convert_image_to_c(image_path, output_file, target_size=(100, 100)):
    # Open the image and resize it to 100x100
    img = Image.open(image_path)
    img = img.resize(target_size, Image.ANTIALIAS)  # Resize image to target size (100x100)
    img = img.convert("RGB")  # Convert to RGB format

    width, height = img.size
    pixels = list(img.getdata())

    # Open output file to write the C array
    with open(output_file, "w") as f:
        f.write(f"const unsigned int image[{width * height}] = {{\n")
        for i, pixel in enumerate(pixels):
            r, g, b = pixel
            # Convert each pixel to RGB565 format
            color = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
            if i % width == 0:
                f.write("\n")
            f.write(f"0x{color:04X}, ")
        f.write("\n};\n")

# Use the function
convert_image_to_c("icon.png", "icon.h", target_size=(100, 100))
