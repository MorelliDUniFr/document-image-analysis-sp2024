import numpy as np
from PIL import Image

def binarization_non_adaptative_thresholding(img):
    # Convert the image to grayscale
    grayscale_image = img.convert("L")

    # Create a new blank image for the binarized version
    binarized_image = Image.new("1", grayscale_image.size)

    # Set the threshold value
    threshold = 128

    # Iterate over each pixel in the grayscale image
    for y in range(grayscale_image.height):
        for x in range(grayscale_image.width):
            # Get the grayscale value of the pixel
            grayscale_value = grayscale_image.getpixel((x, y))

            # Set the corresponding pixel in the binarized image
            if grayscale_value < threshold:
                binarized_image.putpixel((x, y), 0)
            else:
                binarized_image.putpixel((x, y), 1)

    # Save the binarized image
    binarized_image.save("Output/Non-Adaptative_Image.jpg")


def binarization_global_thresholding(img):
    # Convert the image to grayscale
    grayscale_image = img.convert("L")

    # Convert the grayscale image to a NumPy array
    grayscale_array = np.array(grayscale_image)

    # Compute histogram of the input grayscale image
    histogram, _ = np.histogram(grayscale_array, bins=256, range=(0, 256))
    num_pixels = grayscale_array.size

    # Initialize variables for optimal threshold and maximum between-class variance
    optimal_threshold = 0
    max_between_class_variance = 0

    # Iterate through all possible threshold values
    for threshold in range(1, 256):  # Thresholds must be within the range [1, 255]
        # Compute probabilities of foreground and background classes
        prob_background = np.sum(histogram[:threshold]) / num_pixels
        prob_foreground = np.sum(histogram[threshold:]) / num_pixels

        # Compute mean intensities of foreground and background classes
        mean_background = np.sum(np.arange(threshold) * histogram[:threshold]) / (np.sum(histogram[:threshold]) + 1e-10)
        mean_foreground = np.sum(np.arange(threshold, 256) * histogram[threshold:]) / (
                np.sum(histogram[threshold:]) + 1e-10)

        # Compute between-class variance
        between_class_variance = prob_background * prob_foreground * (mean_background - mean_foreground) ** 2

        # Check if between-class variance is greater than the maximum so far
        if between_class_variance > max_between_class_variance:
            max_between_class_variance = between_class_variance
            optimal_threshold = threshold

    # Binarize the image using the optimal threshold
    binarized_image = np.where(grayscale_array >= optimal_threshold, 255, 0).astype(np.uint8)

    # Convert the binarized image array to a PIL Image object
    binarized_image_pil = Image.fromarray(binarized_image)

    # Save the binarized image
    binarized_image_pil.save("Output/Global_Thresholding_Image.jpg")


def binarization_local_adpatative_thresholding(img):
    grayscale_image = img.convert("L")
    width, height = grayscale_image.size
    binarized_image = np.zeros((height, width), dtype=np.uint8)

    # Iterate through each pixel in the grayscale image
    for y in range(height):
        for x in range(width):
            # Define local neighborhood
            neighborhood = get_local_neighborhood(grayscale_image, x, y, window_size=35)

            local_threshold = np.mean(neighborhood)

            # Binarize the pixel based on the local threshold
            if grayscale_image.getpixel((x, y)) >= local_threshold:
                binarized_image[y, x] = 255
            else:
                binarized_image[y, x] = 0

    # Convert the binarized image array to a PIL Image object
    binarized_image = Image.fromarray(binarized_image)

    # Save the binarized image
    binarized_image.save("Output/Local_Adaptative_Thresholding_Image.jpg")


def get_local_neighborhood(image, x, y, window_size):
    half_size = window_size // 2
    neighborhood = []

    for j in range(y - half_size, y + half_size + 1):
        for i in range(x - half_size, x + half_size + 1):
            # Ensure the coordinates are within image bounds
            if 0 <= i < image.width and 0 <= j < image.height:
                neighborhood.append(image.getpixel((i, j)))

    return neighborhood


if __name__ == "__main__":
    print("Exercise 03")

    # Load the image
    image_path = "Images/aef-CSN-III-3-1_088-600x900.jpg"

    original_image = Image.open(image_path)
    original_image.save('Output/Original_Image.jpg')

    # Binzarization using non-adaptative thresholding
    binarization_non_adaptative_thresholding(original_image)

    # Binzarization using global thresholding
    binarization_global_thresholding(original_image)

    # Binarization using local adaptative thresholding
    binarization_local_adpatative_thresholding(original_image)

    print("End of the exercise 03")

