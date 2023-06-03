from paddleocr import PaddleOCR

ocr = PaddleOCR()  # need to run only once to download and load model into memory
img_path = '1.jpg'
result = ocr.ocr(img_path, det=False)
for line in result:
    print(line)