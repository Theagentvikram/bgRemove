from io import BytesIO
from PIL import Image
from rembg import remove

# Upload the file
uploaded_file = input("Upload an image (png, jpg, jpeg): ")

# If we've uploaded an image, open it and remove the background!
if uploaded_file:
    # Show the uploaded image
    image = Image.open(uploaded_file)
    image.show()

    # Remove the background
    fixed = remove(image)

    # Save the background removed image
    output_image = "BgRem.png"
    fixed.save(output_image)
    print("Background removed image saved as", output_image)
