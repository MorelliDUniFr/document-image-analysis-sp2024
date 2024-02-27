# Exercise 2: Histogram of RGB image

## Informations 
Author: Davide Morelli \
Github: https://github.com/MorelliDUniFr/document-image-analysis-sp2024/tree/main/Ex02

## Conversion of RGB image to grayscale
We open the original image, and create a new blank image with mode "L" (grayscale) using Image.new().
We iterate over each pixel in the original image, and for each pixel, we calculate the grayscale value using the luminosity method: 
`grayscale_value = 0.21*R + 0.72*G + 0.07*B`
where R, G, and B are the red, green, and blue values of the pixel, respectively.
We set the grayscale value for the corresponding pixel in the new image using putpixel(), and we finally return the new image.

## Histogram of Grayscale Image
1. **Initialize Histogram**:
   We initialize an empty histogram list with 256 bins (one for each possible grayscale value ranging from 0 to 255).

2. **Iterate Over Each Pixel in the Grayscale Image**:
   We iterate over each pixel in the grayscale image. `width` and `height` are the dimensions of the image.

3. **Get Grayscale Value of Pixel**:
   For each pixel, we retrieve its grayscale value using the `getpixel()` method. This method returns a single integer 
   value representing the grayscale intensity of the pixel (ranging from 0 to 255).

4. **Increment Corresponding Bin in Histogram**:
   We increment the count in the histogram bin corresponding to the grayscale value of the pixel. For example, if the 
   grayscale value of the pixel is 50, we increment the count in `histogram[50]` by 1.

5. **Repeat for All Pixels**:
   We repeat steps 3 and 4 for every pixel in the grayscale image, updating the histogram counts accordingly.

6. **Histogram Representation**:
   At the end of this process, `histogram` will contain the frequency (number of occurrences) of each grayscale value in 
   the image. The index of the list represents the grayscale value, and the value at each index represents the frequency 
   of that grayscale value in the image.

### Idea Behind the Algorithm:
The grayscale histogram algorithm calculates the frequency of occurrence of each grayscale intensity level in the image.
By iterating over each pixel and recording the intensity levels, we can obtain a statistical representation of the 
distribution of grayscale values in the image. This information is useful for various image processing tasks such as 
contrast enhancement, thresholding, and image normalization.

## Color Histogram of RGB Image
In order to compute the color histogram of an RGB image, we need to compute separate histograms for the red, green, and blue channels.
Then we can combine these histograms to obtain histograms for other colors such as magenta, cyan, yellow, and white.
This is done by taking the minimum value of corresponding bins in the red, green, and blue histograms for each intensity value.