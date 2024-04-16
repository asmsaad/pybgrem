
from PIL import Image

def resize_image(image_path, window_width, window_height):
    # Open the image file
    image = Image.open(image_path)
    
    # Get the original dimensions of the image
    original_width, original_height = image.size
    
    # Calculate the aspect ratio of the original image
    original_aspect_ratio = original_width / original_height
    
    # Calculate the aspect ratio of the window
    window_aspect_ratio = window_width / window_height
    
    # Resize the image to fit within the window dimensions while maintaining aspect ratio
    if window_aspect_ratio > original_aspect_ratio:
        # Window is wider than the image, adjust height
        new_height = window_height
        new_width = int(new_height * original_aspect_ratio)
    else:
        # Window is taller than the image, adjust width
        new_width = window_width
        new_height = int(new_width / original_aspect_ratio)
    
    # Resize the image
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    
    return resized_image

# Example usage:
window_width = 40
window_height = 40
image_path = "sharamoni.png"

resized_image = resize_image(image_path, window_width, window_height)
resized_image.show()  # Display the resized image
