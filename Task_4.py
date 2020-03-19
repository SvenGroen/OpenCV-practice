import cv2
import numpy as np

# artificial video
out = cv2.VideoWriter('videos/random_dot.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25,
                      (512, 512))

# black canvas

img = np.zeros((512, 512, 3), np.uint8)

xyold = (100, 100)
xynew = (100, 100)


def get_rand_change(x, y):
    return x + np.random.choice([-1, 0, 1]), y + np.random.choice([-1, 0, 1])


while (True):
    xynew = get_rand_change(xyold[0],xyold[1])

    cv2.circle(img, xyold, 10, (0, 0, 0), -1)
    cv2.circle(img, xynew, 10, (255, 255, 255), -1)
    xyold = xynew

    out.write(img)
    k = cv2.waitKey(1)
    cv2.imshow("image", img)
    if k == 27:
        break
out.release()
cv2.destroyAllWindows()
