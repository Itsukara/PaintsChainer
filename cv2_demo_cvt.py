import cv2

image = cv2.imread("clouds.jpg")
image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
image_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)
image_bgr = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("Over the Clouds", image)
cv2.imshow("Over the Clouds - hsv", image_hsv)
cv2.imshow("Over the Clouds - rgb", image_rgb)
cv2.imshow("Over the Clouds - bgr", image_bgr)
cv2.waitKey(0)

cv2.imwrite("clouds_hsv.jpg", image_hsv)
cv2.imwrite("clouds_rgb.jpg", image_rgb)
cv2.imwrite("clouds_bgr.jpg", image_bgr)


cv2.destroyAllWindows()