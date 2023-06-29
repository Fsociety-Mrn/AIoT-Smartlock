import os

# Specify the directory path
directory = "Known_Faces/Art Lisboa"  # Replace with the actual path to your folder

# Get the list of files in the directory
files = os.listdir(directory)

# Filter the list to include only image files
image_files = [file for file in files if file.endswith((".png", ".jpg", ".jpeg"))]

# Sort the image file names numerically
sorted_image_files = sorted(image_files, key=lambda x: int(os.path.splitext(x)[0]))

# Print the sorted image file names
for image_file in sorted_image_files:
    print(image_file)
