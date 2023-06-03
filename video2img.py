import cv2


def save_image(addr, image, num):
    address = addr + str(num) + '.jpg'
    cv2.imwrite(address, image)


video_path = ""
out_path = ""

is_all_frame = False
sta_frame = 1
end_frame = 1000

time_interval = 8


videocapture = cv2.VideoCapture(video_path)
success, frame = videocapture.read()


i = 0
j = 0
while success:
    if is_all_frame:
        if i % time_interval == 0:
            save_image(out_path, frame, j)
            j += 1
    else:
        if i >= sta_frame and i <= end_frame and (i - sta_frame) % time_interval == 0:
            save_image(out_path, frame, j)
            j += 1
        elif i > end_frame:
            break
    # i += 1
    success, frame = videocapture.read()