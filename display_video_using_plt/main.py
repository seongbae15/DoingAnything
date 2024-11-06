import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def main():
    video_path = "IMG_2639.MOV"
    cap = cv2.VideoCapture(video_path)

    fig, ax = plt.subplots()
    ret, frame = cap.read()
    if not ret:
        cap.release()
        exit()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    im = ax.imshow(frame)

    def update(i):
        ret, frame = cap.read()
        if not ret:
            return (im,)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im.set_array(frame)

    ani = FuncAnimation(fig, update, interval=30)
    plt.show()
    cap.release()


if __name__ == "__main__":
    main()
