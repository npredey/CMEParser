import cv2
from PIL import Image
import pytesseract
import os
from pdf2image import convert_from_path

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#                 help="path to input image to be OCR'd")
# ap.add_argument("-p", "--preprocess", type=str, default="thresh",
#                 help="type of preprocessing to be done")
# args = vars(ap.parse_args())

# load the example image and convert it to grayscale
pdf = '/Users/nickpredey/EDF_MAN/data/CME/DailyBulletin_pdf_20180627123/Section01B_Summary_Volume_And_Open_Interest_FX_Futures_And_Options.pdf'
pdf_jpg = '/Users/nickpredey/EDF_MAN/data/CME/Section01_Exchange_Overall_Volume_And_Open_Interest-page-001.jpg'
pdf_path = r'C:\Users\npredey\Downloads\CME\DailyBulletin_pdf_20180627123\Section42_10YrNote_5yrNote_2yrNote_30YrBond_Options.pdf'
jpg = convert_from_path(pdf_path, 500)
image = cv2.imread(jpg)
print(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the
# image
# if args["preprocess"] == "thresh":
#     gray = cv2.threshold(gray, 0, 255,
#                          cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove
# noise
# elif args["preprocess"] == "blur":
#     gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
f = open("output_text.txt", "w+")
f.writelines(text)
f.close()


# show the output images
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)
