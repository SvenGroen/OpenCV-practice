import numpy as np
import matplotlib.pyplot as plt
import cv2

# DRAWING OVER PICTURES

# Load Image
# img = cv2.imread("images/blue-and-green-sky-and-mountain-3617500.jpg", -1)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
# Load Video
cap = cv2.VideoCapture("videos/Pexels Videos 2616637.mp4")


def click_event(event, x, y, flags, param):
    """
    :param event:
    :param x: x - coordinate where click occurred
    :param y: y - coordinate where click occurred
    :param flags:
    :param param:
    :return:
    """

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ", " + str(y)
        cv2.putText(img, strXY, (x, y), font, 0.5, (255, 255, 255), 1)
        cv2.imshow("image", img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ", " + str(green) + ", " + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (255, 255, 255), 1)
        cv2.imshow("image", img)


drawing = False
thickness = -1
radius = 5

color = (255, 255, 255)


def click_draw(event, x, y, flags, param):
    global ix, iy, drawing, color, thickness, radius

    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True
        cv2.circle(img, (x, y), radius, color, thickness)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img, (x, y), radius, color, thickness)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), radius, color, thickness)

    # elif event == cv2.EVENT_MOUSEWHEEL:
    #     if cv2.Mouse < 0:
    #         if radius > 0:
    #             radius -= 1
    #     else:
    #         radius +=1


cv2.setMouseCallback("image", click_draw)

# create black image
img = np.zeros((512, 512, 3), np.uint8)
while True:
    k = cv2.waitKey(1)
    cv2.imshow("image", img)
    if k == 27:
        break
    # cv2.setMouseCallback("image", click_event)

cv2.destroyAllWindows()
