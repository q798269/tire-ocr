import paddleocr

ocr_engine = paddleocr.OCR()

# 读取图像
image_path = 'G:\\tire-ocr\\1\\1a3eb292c93d85d88ade6688b939668.jpg'
image = paddleocr.load_image(image_path)

# 进行字体识别
result = ocr_engine.ocr(image, use_gpu=False)

# 输出识别结果
for line in result:
    line_text = ' '.join([word_info[-1] for word_info in line])
    print(line_text)
