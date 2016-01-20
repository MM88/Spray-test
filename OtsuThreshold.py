import sys
import numpy as np
import cv2


def main(argv):

    img = cv2.imread('wetta2.jpg')
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("original img",gray_image)
    cv2.waitKey(0)
    ret, otsu = cv2.threshold(gray_image,0,255,cv2.THRESH_OTSU)
    cv2.imshow("otsu img",otsu)
    cv2.waitKey(0)

    blur = cv2.GaussianBlur(gray_image,(7,7),0)
    cv2.imshow("blur img",blur)
    cv2.waitKey(0)

    ret, otsu = cv2.threshold(blur,0,255,cv2.THRESH_OTSU)
    cv2.imshow("otsu blur img",otsu)
    cv2.waitKey(0)

    pass

if __name__ == "__main__":
    main(sys.argv)




