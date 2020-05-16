from src.sift import *
import math

scaling_pyramid_depths = [1, 2, 3, 4]
rotations = [0.0, 30.0, 60.0, 90.0, 120.0, 150.0, 180.0, 210.0, 240.0, 270.0, 300.0, 330.0]


def main():
    sift_training()


def sift_training():
    (keypoints, descriptors) = detect_keypoints("../img/fb.png", 1)
    print(keypoints.shape[0])

    img = cv2.imread("../img/fb.png")

    for i in range(0, keypoints.shape[0]):
        cv2.circle(img, (int(keypoints[i][1]), int(keypoints[i][0])), int(keypoints[i][2]), (0, 255, 0), thickness=1, lineType=8, shift=0)
        # int(keypoints[i][2]) is the orientation in degrees divided by 10
        angle = int(keypoints[i][3])*10
        length = int(keypoints[i][2])
        centerx = int(keypoints[i][1])
        centery = int(keypoints[i][0])
        x = int(centerx + length * math.cos(angle * 3.14 / 180.0))
        y = int(centery + length * math.sin(-angle * 3.14 / 180.0))

        start_point = (centerx, centery)
        end_point = (x, y)

        cv2.line(img, start_point, end_point, (0, 0, 255), thickness=2, lineType=8, shift=0)



    cv2.imshow("img", img)
    cv2.waitKey(0)


def sift_testing(directory):
    pass
    # todo sift testing


if __name__ == "__main__":
    main()
