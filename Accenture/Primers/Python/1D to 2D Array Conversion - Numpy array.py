"""
Objective: 

To work with Array reshape

Problem Description: 

You are working on an image processing project that requires transforming a 1D NumPy array into a 2D NumPy array to represent an image and also finding the pixel values of the top left corner, bottom right corner, and mean pixel value. The number of pixels is 8, and the pixel value should be less than and equal to 256. Using a numpy array in Python to transform an image

Process flow: 

Get all 8 pixel values from the user as input.
Check the pixel value, if it is greater than 256, then display the message "Invalid input! Enter a value between 0 and 256" and get the next input.
Convert the 1D array to a 2D array.
Find the pixel values of the top left corner, bottom right corner, and mean pixel value and display them as per the sample output statement.
 Note:

The input should be a integer value
Convert 1D array to 2D array and store it in a variable named "image_matrix"
Display the mean value of the pixel values in 2 decimal place


Sample Input 1:

Enter pixel values for the image (8 values):

Pixel 1: 23

Pixel 2: 45

Pixel 3: 67

Pixel 4: 89

Pixel 5: 256

Pixel 6: 78

Pixel 7: 123

Pixel 8: 200

 

Sample Output 1:

Original Array:

[ 23  45  67  89 256  78 123 200]

 

Image Matrix (2x4):

[[ 23  45  67  89]

 [256  78 123 200]]

 

Top-left 2x2 Region:

[[23 45]]

 

Bottom-right 2x2 Region:

[[123 200]]

 

Mean value of the pixel values in the Image Matrix: 110.12
"""


import numpy as np

pixels=[]
print('Enter pixel values for the image (8 values):')
for i in range(1,9):
    pixel=int(input(f'Pixel {i}:\n'))
    if pixel<0 or pixel>256:
        print('Invalid input! Enter a value between 0 and 256')
        continue
    pixels.append(pixel)
arr=np.array(pixels)
print(f'Original Array:\n{arr}')
image_matrix=arr.reshape(2,4)
print(f'\nImage Matrix (2x4):\n{image_matrix}')
print(f'\nTop-left 2x2 Region:\n{image_matrix[:1,:2]}')
print(f'\nBottom-right 2x2 Region:\n{image_matrix[1:,2:]}')
print('\nMean value of the pixel values in the Image matrix: {:.2f}'.format(np.mean(image_matrix)))
