import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img, "sun", (20,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img, "mercury", (110,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img, "venus", (190,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img, "earth", (280,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img, "mars", (370,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img, "jupiter", (500,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img, "saturn", (800,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img, "Uranus", (930,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img, "Neptune", (1100,200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))




cv2.imshow("output",img)
cv2.waitKey(0)

