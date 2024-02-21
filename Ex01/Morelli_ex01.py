from PIL import Image

def downscale_image(image_path, factor):
    # Open the original image
    original_image = Image.open(image_path)
    original_width, original_height = original_image.size

    print(f"Original image size: {original_width}x{original_height}")
    print(f"Downscaling factor: {factor}")

    # Calculate the dimensions of the downscaled image
    new_width = original_width // factor
    new_height = original_height // factor

    # Create a new blank image for the downscaled version
    downscaled_image = Image.new("RGB", (new_width, new_height))

    # Iterate over each pixel in the downscaled image
    for y in range(new_height):
        for x in range(new_width):
            # Calculate the region in the original image to average
            region_x_start = x * factor
            region_x_end = (x + 1) * factor
            region_y_start = y * factor
            region_y_end = (y + 1) * factor

            # Average the colors in the region
            region_pixels = []
            for region_y in range(region_y_start, region_y_end):
                for region_x in range(region_x_start, region_x_end):
                    region_pixels.append(original_image.getpixel((region_x, region_y)))
            average_color = tuple(
                int(sum(color[channel] for color in region_pixels) / len(region_pixels)) for channel in range(3))

            # Set the average color for the corresponding pixel in the downscaled image
            downscaled_image.putpixel((x, y), average_color)

    # Save the downscaled image
    downscaled_image.save("Output/downscaled_image.png")

    print(f"Downscaled image size: {new_width}x{new_height}")


if __name__ == "__main__":
    print("Exercise 01")

    image_path = "Images/aef-CSN-III-3-1_088-600x900.jpg"

    downscale_image(image_path, 3)
