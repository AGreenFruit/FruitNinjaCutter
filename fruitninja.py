import numpy as np
import cv2
from mss import mss
from PIL import Image
import time
import pyautogui

def process_img(original_image):
	processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
	#processed_img = cv2.GaussianBlur(processed_img, (5,5), 0)
	#processed_img = cv2.Canny(processed_img, threshold1=160, threshold2=200)


	circles = cv2.HoughCircles(processed_img, 
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
               param2 = 35, minRadius = 20, maxRadius = 60)
  
	if circles is not None:
		circles = np.uint16(np.around(circles))
		for pt in circles[0, :]:
			a, b, r = pt[0], pt[1], pt[2]
			pyautogui.click(a, b)
			#cv2.circle(processed_img, (a, b), r, (0, 255, 0), 2)
			#pyautogui.moveTo(a, b)
			#pyautogui.dragRel(30, 0, duration = .15)

	#vertices = np.array([[10,500], [10,300], [300,200], [500,200], [800, 300], [800,500]], np.int32)
	return processed_img

def main():
	bounding_box = {'top': 0, 'left': 0, 'width': 1500, 'height': 600} #Get dimensions of screen

	sct = mss()

	while True:
		sct_img = sct.grab(bounding_box)
		#cv2.imshow('screen2', process_img(np.array(sct_img)))
		process_img(np.array(sct_img))
		if (cv2.waitKey(1) & 0xFF) == ord('q'):
			cv2.destroyAllWindows()
			break
main() 