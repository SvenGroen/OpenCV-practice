import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load Image
img = cv2.imread("images/blue-and-green-sky-and-mountain-3617500.jpg", -1)

# Load Video
cap = cv2.VideoCapture("videos/Pexels Videos 2881.mp4")

'''
also:
    cv2.IMREAD_COLOR (1) RGB
    cv2.IMREAD_GRAYSCALE (0) GREY
    cv2.IMREAD_UNCHANGED (-1) RGB-alpha
'''
# Printing image
# using plt
# plt.imshow(img, interpolation="bicubic")
# draw a line on the image
# plt.plot([0,3000],[0,3000])
# plt.show()

# drawing on the image
# (image, start, stop, color(bgr), width
cv2.line(img, (0, 0), (1500, 2000), (0, 0, 255), 15)
# drawing a rectangle (top left, bottom right)
cv2.rectangle(img, (1000, 1000), (2000, 2000), (255, 0, 0), 15)
# circle (center position, radius, color, thickness (-1 to fill it))
cv2.circle(img, (3000, 3000), 100, (0, 255, 0), -1)

# polygons
# list of points
offset = [1000, 1000]
scale = 5
pts = np.array([[0, 0], [100, 100], [500, 700], [300, 500], [10, 600]], np.int32)
# pts=pts.reshape((-1,1,2))
pts = (pts * scale + offset)
# points, connect ends?, color
cv2.polylines(img, [pts], True, (255, 255, 255), 3)

# write text
font = cv2.FONT_HERSHEY_PLAIN
# text, position,font, scale, color, thickness, anti aliasing
cv2.putText(img, "Hello World", (2000, 2000), font, 10, (200, 100, 255), 10, cv2.LINE_AA)

# plot using cv2
# resizable window
cv2.namedWindow("Image of a Nature Scene", cv2.WINDOW_NORMAL)
# Display Image
cv2.imshow("Image of a Nature Scene", img)

# Waits indefinitely until key is pressed
cv2.waitKey(0)
# closes all windows
cv2.destroyAllWindows()

# Save Image
cv2.imwrite("images/blue-and-green-sky-and-mountain-3617500-altered.jpg", img)

# same for video
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('videos/Pexels Videos 2881-altered.avi', fourcc, 20.0, (1080, 1920))
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
print(frame_height, frame_width)
out = cv2.VideoWriter('videos/Pexels Videos 2881-altered.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25, (frame_width, frame_height))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # transform image to grey image
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.line(frame, (0, 0), (150, 200), (0, 0, 255), 15)
        h, w, _ = frame.shape
        cv2.circle(frame, (int(h / 2), int(w / 2)), 100, (255, 0, 0), -1)

        out.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
