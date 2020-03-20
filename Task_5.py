import sys
import cv2
import numpy as np


def main(path):
    cap = cv2.VideoCapture(path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = int(cap.get(5))
    path = path[:-4]
    out = cv2.VideoWriter(path + "_fg.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps,
                          (frame_width, frame_height))

    threshold = 10
    frame_old = np.zeros((frame_height, frame_width , 3), np.uint8)

    while (cap.isOpened()):
        ret, frame_new = cap.read()
        # img2gray_new = cv2.cvtColor(frame_new, cv2.COLOR_BGR2GRAY)
        if ret:

            # check for difference in frame

            dif = np.array((abs(frame_old - frame_new) > threshold) * 255, np.uint8)
            frame_old = frame_new
            out.write(dif)
            cv2.imshow("dif", dif)
            cv2.imshow("img", frame_new)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # if len(sys.argv != 2):
    #    print("Wrong number of of parameters. Was {}, but should be 1".format(len(sys.argv)))
    # path= sys.argv[1]
    path = "videos/random_dot.avi"
    path2 = "videos/Pexels Videos 2881.mp4"
    main(path)
