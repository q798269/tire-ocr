import cv2
import pytesseract

# 读取图像
image = cv2.imread("G:\\tire-ocr\\1\\1a3eb292c93d85d88ade6688b939668.jpg")

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 对灰度图像进行二值化处理
# threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# 对二值化图像进行降噪处理
blur = cv2.medianBlur(threshold, 3)

# 对降噪后的图像进行平滑处理
smooth = cv2.GaussianBlur(blur, (5, 5), 0)

# 保存预处理后的图像
cv2.imwrite('preprocessed_image.png', smooth)

# 使用 Tesseract 进行识别
result = pytesseract.image_to_string(smooth,lang='eng', config='--psm 1')

# 打印识别结果
print(result)
