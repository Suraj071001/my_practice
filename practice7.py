# import pytesseract
# from PIL import Image
#
# pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
# img=Image.open('1.webp')
# text=pytesseract.image_to_string(img,lang="eng")
# with open("ship.txt","a") as f :
#     f.write(text)
# print(text)
import pywhatkit
inp_img = input("Give full path of image")
out_img = input("Give full path of txt file")
pywhatkit.image_to_ascii_art(rf"{inp_img}",rf"{out_img}")