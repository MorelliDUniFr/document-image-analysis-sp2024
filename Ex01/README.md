# Exercise 1: Image Downscaling

## Informations 
Author: Davide Morelli \
Github: https://github.com/MorelliDUniFr/document-image-analysis-sp2024/tree/main/Ex01

## Downscaling Algorithm Explanation

1. **Opening the Image**: 
   We start by opening the original image using the Python Imaging Library (PIL) module.

2. **Calculating Downscaled Dimensions**: 
   We calculate the dimensions of the downscaled image by dividing the original dimensions by the specified downscaling factor.

3. **Creating a Blank Downscaled Image**: 
   We create a new blank image with the calculated dimensions for the downscaled version.

4. **Iterating Over Each Pixel in the Downscaled Image**: 
   We iterate over each pixel position in the downscaled image.

5. **Calculating the Region in the Original Image to Average**: 
   For each pixel in the downscaled image, we calculate the corresponding region in the original image from which we will average the colors.

6. **Averaging Colors in the Region**: 
   We iterate over each pixel in the region of the original image, retrieve its color, and calculate the average color for that region.

7. **Setting the Average Color for the Corresponding Pixel in the Downscaled Image**: 
   We set the calculated average color as the color of the corresponding pixel in the downscaled image.

8. **Saving the Downscaled Image**: 
   Finally, we save the downscaled image with the averaged colors as a new image file.

### Idea Behind the Algorithm

The idea behind this algorithm is to downscale the image by averaging the colors of small regions in the original image. 
By taking the average color of each region, we effectively reduce the resolution of the image while preserving the overall appearance. 
This simple averaging approach allows us to downscale the image without losing too much detail, making it suitable for a variety of applications.
