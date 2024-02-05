import qrcode
import cv2
import numpy as np
from PIL import Image

# Rest of your code remains the same...


# taking image which user wants 
# in the QR code center
Logo_link = 'Images/Untitled design.png'

logo = cv2.imread(Logo_link)

# taking base width
basewidth = 100

# adjust image size using OpenCV
scale_percent = basewidth / logo.shape[1]
width = int(logo.shape[1] * scale_percent)
height = int(logo.shape[0] * scale_percent)
dim = (width, height)
logo = cv2.resize(logo, dim, interpolation=cv2.INTER_AREA)

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# taking url or text
url = 'https://user-aiot-smartlocker.web.app/'

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from user
QRcolor = '#1A2A36'

# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.shape[1]) // 2,
       (QRimg.size[1] - logo.shape[0]) // 2)

# Convert OpenCV image to PIL image
logo_pil = Image.fromarray(cv2.cvtColor(logo, cv2.COLOR_BGR2RGB))

QRimg.paste(logo_pil, pos)

# save the QR code generated
QRimg.save('Images/USER_QR.png')

print('QR code generated!')
