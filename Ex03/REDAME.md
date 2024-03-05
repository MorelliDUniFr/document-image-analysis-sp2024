# Exercise 3: Binarization

## Informations 
Author: Davide Morelli \
Github: https://github.com/MorelliDUniFr/document-image-analysis-sp2024/tree/main/Ex03

## Description of algorithms
### Binarization with non-adaptative thresholding
The algorithm begins by converting the input image to grayscale, simplifying it to single intensity values per pixel.
It then creates a new blank image to store the binarized version. Employing a predetermined threshold value of 128, 
it iterates through each pixel in the grayscale image. For each pixel, if its intensity value falls below the threshold, 
it assigns a value of 0 (black) in the binarized image; otherwise, it assigns a value of 1 (white). This process results 
in a binary representation of the input image, where pixels are either black or white based on their intensity relative to the threshold. 
Finally, the binarized image is saved. Adjusting the threshold can influence the level of detail and contrast in the resulting binary image.

### Binarization with global thresholding
* We compute the histogram of the input grayscale image using np.histogram.
* We iterate through all possible threshold values from 1 to 255 (as thresholds must be within this range).
* For each threshold, we compute the probabilities of the foreground and background classes, as well as the mean intensities of both classes.
* Using these values, we calculate the between-class variance, which measures the separability between foreground and background classes.
* We update the optimal threshold if the between-class variance is greater than the maximum between-class variance encountered so far.
* Finally, we binarize the image using the optimal threshold and display both the original and binarized images for visualization.

### Binzarization with local adaptative thresholding
 Initially, the input grayscale image is converted, and necessary variables are initialized.
 The algorithm then iterates through each pixel of the image, defining a local neighborhood centered around it.
 Within this neighborhood, a local threshold is computed based on either the mean or median intensity values, 
 as per the chosen method. Subsequently, each pixel's intensity is compared to its local threshold, and it is binarized accordingly, 
 resulting in a binary image where pixels are classified as foreground or background. 
 Finally, the binarized image is returned as a NumPy array, offering adaptability and efficiency in various image processing applications.