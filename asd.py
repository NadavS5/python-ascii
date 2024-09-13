from PIL import Image
import cv2
import os

def image_to_ascii(img):
    color = ' .;≡:!>7?CO$░▒▓█'

    width, height = img.size
    
    for y in range(height):
        for x in range(width)   :
            pixel = img.getpixel((x,y))
            pixel_Color = (pixel[0] + pixel[1] + pixel[2])/3
            pixel_Color = int((pixel_Color/256)*16)
            print (color[pixel_Color],end="")
        print()


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot access the camera")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        pil_image = Image.fromarray(rgb_frame)

        pil_image = pil_image.resize((200, 100))

        os.system("cls")
        image_to_ascii(pil_image)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()


if __name__ == '__main__':
    main()