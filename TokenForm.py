import cv2

def calculate_blurriness(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate the Laplacian
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    
    # Calculate the variance of the Laplacian
    variance = laplacian.var()
    
    return variance

def main():
    image_path = 'Known_Faces/ART LISBOA/14.png'  # Replace with the path to your image
    
    # Calculate the blurriness
    blurriness = calculate_blurriness(image_path)
    
    # Define a threshold to determine if the image is blurry or not
    threshold = 100  # You can adjust this threshold
    print(blurriness)


if __name__ == "__main__":
    main()
