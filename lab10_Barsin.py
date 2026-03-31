import random
from PIL import Image

# ------------------------------
# Exercise 1 - Dim Image
# ------------------------------
def dim_eight_pixels_image():
    # Open original image
    im = Image.open("palette_more_pixels.png")
    
    # Create new image with same size
    im_dim = Image.new("RGB", (im.width, im.height))
    
    # Loop through each pixel
    for row in range(im.height):
        for col in range(im.width):
            (r, g, b) = im.getpixel((col, row))
            
            # Reduce brightness to half
            r = r // 2
            g = g // 2
            b = b // 2
            
            # Put new pixel
            im_dim.putpixel((col, row), (r, g, b))
    
    # Save result
    im_dim.save("img1_palette_dim.png")


# ------------------------------
# Exercise 2 - Blue Washed Image
# ------------------------------
def blue_washed_image():
    im = Image.open("rick_and_morty.png")
    im_blue = Image.new("RGB", (im.width, im.height))
    
    # Loop through pixels
    for row in range(im.height):
        for col in range(im.width):
            (r, g, b) = im.getpixel((col, row))
            
            # Keep only blue channel
            im_blue.putpixel((col, row), (0, 0, b))
    
    im_blue.save("img2_rick_blue_washed.png")


# ------------------------------
# Exercise 3 - Alternate Lines
# ------------------------------
def create_alternate_lines(width, height):
    im = Image.new("RGB", (width, height))
    
    for row in range(height):
        for col in range(width):
            # Even rows → white
            if row % 2 == 0:
                im.putpixel((col, row), (255, 255, 255))
            # Odd rows → black
            else:
                im.putpixel((col, row), (0, 0, 0))
    
    im.save("img3_alternate_lines.png")


# ------------------------------
# Exercise 4 - Random Noise
# ------------------------------
def create_random_noise(width, height):
    im = Image.new("RGB", (width, height))
    
    for row in range(height):
        for col in range(width):
            # 50% chance white or black
            if random.random() < 0.5:
                im.putpixel((col, row), (255, 255, 255))
            else:
                im.putpixel((col, row), (0, 0, 0))
    
    im.save("img4_random.png")


# ------------------------------
# Exercise 5 - Decode Image
# ------------------------------
def decode_image():
    im = Image.open("rick_encoded.png")
    im_secret = Image.new("RGB", (im.width, im.height))
    
    for row in range(im.height):
        for col in range(im.width):
            (r, g, b) = im.getpixel((col, row))
            
            # If red is odd → black
            if r % 2 == 1:
                im_secret.putpixel((col, row), (0, 0, 0))
            # If red is even → red
            else:
                im_secret.putpixel((col, row), (255, 0, 0))
    
    im_secret.save("img5_rick_secret.png")
