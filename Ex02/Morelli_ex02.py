from PIL import Image
import matplotlib.pyplot as plt


def rgb_to_grayscale(image_path):
    # Open the original image
    original_image = Image.open(image_path)
    width, height = original_image.size

    # Create a new blank image for the grayscale version
    grayscale_image = Image.new("L", (width, height))

    # Iterate over each pixel in the original image
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the pixel
            r, g, b = original_image.getpixel((x, y))

            # Calculate the grayscale value using the luminosity method
            grayscale_value = int(0.21 * r + 0.72 * g + 0.07 * b)

            # Set the grayscale value for the corresponding pixel in the new image
            grayscale_image.putpixel((x, y), grayscale_value)

    print("RGB to Grayscale conversion completed")
    return grayscale_image

def grayscale_histogram(grayscale_image):
    # Create a histogram of the grayscale values
    histogram = [0] * 256
    width, height = grayscale_image.size

    # Iterate over each pixel in the grayscale image
    for y in range(height):
        for x in range(width):
            # Get the grayscale value of the pixel
            grayscale_value = grayscale_image.getpixel((x, y))

            # Increment the corresponding value in the histogram
            histogram[grayscale_value] += 1

    print("Grayscale Histogram created")
    return histogram

def plot_histogram(histogram, title, color):
    plt.figure()
    plt.bar(range(256), histogram, color=color)
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.savefig('Output/' + title + '.png')
    print(title + " plotted and saved")

def compute_combined_histogram(hist_r, hist_g, hist_b):
    hist_m = [0] * 256
    hist_c = [0] * 256
    hist_y = [0] * 256
    hist_w = [0] * 256

    for i in range(256):
        hist_y[i] = min(hist_r[i], hist_g[i])
        hist_m[i] = min(hist_r[i], hist_b[i])
        hist_c[i] = min(hist_g[i], hist_b[i])
        hist_w[i] = min(hist_r[i], hist_g[i], hist_b[i])

    print("Combined Histogram computed")
    return [hist_r, hist_g, hist_b, hist_m, hist_c, hist_y, hist_w]

def plot_combined_histogram(histogram):
    plt.figure()

    for i in range(len(histogram)):
        plt.bar(range(256), histogram[i], color=color_map[list(color_map.keys())[i]], alpha=1.0)

    plt.title('Combined Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.savefig('Output/Combined_Histogram.png')
    print("Combined Histogram plotted and saved")


if __name__ == "__main__":
    print("Exercise 02")

    color_map = {
        'r': 'red',
        'g': 'green',
        'b': 'blue',
        'm': 'magenta',
        'c': 'cyan',
        'y': 'yellow',
        'w': 'grey'
    }

    # Load the image
    image_path = "Images/utp-0101_016v-1000x1500.jpg"

    original_image = Image.open(image_path)
    original_image.save('Output/Original_Image.jpg')

    # Convert the image to grayscale
    greyscale_image = rgb_to_grayscale(image_path)
    greyscale_image.save('Output/Grayscale_Image.jpg')

    # Create a histogram of the grayscale values
    histogram = grayscale_histogram(greyscale_image)
    plot_histogram(histogram, 'Grayscale Histogram', 'gray')

    # Split the image into 3 channels
    r, g, b = original_image.split()

    # Create a histogram of the grayscale values for each channel
    histogram_r = grayscale_histogram(r)
    histogram_g = grayscale_histogram(g)
    histogram_b = grayscale_histogram(b)
    plot_histogram(histogram_r, 'Red Histogram', color_map['r'])
    plot_histogram(histogram_g, 'Green Histogram', color_map['g'])
    plot_histogram(histogram_b, 'Blue Histogram', color_map['b'])

    # Create a combined histogram
    combined_histogram = compute_combined_histogram(histogram_r, histogram_g, histogram_b)
    plot_combined_histogram(combined_histogram)

    print("Exercise 02 completed")
