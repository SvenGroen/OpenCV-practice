import sys
import cv2
import numpy as np


def main(path):
    # create background subtraction object
    fgbg1 = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25);

    cap = cv2.VideoCapture(path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = int(cap.get(5))
    path = path[:-4]
    out = cv2.VideoWriter(path + "_cv2_bg.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps,
                          (frame_width, frame_height))

    while (cap.isOpened()):
        ret, frame = cap.read()
        # img2gray_new = cv2.cvtColor(frame_new, cv2.COLOR_BGR2GRAY)
        if ret:
            fgmask1 = fgbg1.apply(frame)
            cv2.imshow("frame", fgmask1)
            out.write(fgmask1)
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
    path3 = "videos/Pexels Videos 2616637.mp4"
    path4 = "videos/Video Of People Walking.mp4"
    main(path4)
