import cv2
import fastdeploy as fd
import numpy as np

rec_label_file = "en_dict.txt"


det_model = fd.vision.ocr.DBDetector(r"G:\tire-ocr\en_PP-OCRv3_det_infer\inference.pdmodel", r"G:\tire-ocr\en_PP-OCRv3_det_infer\inference.pdiparams")
cls_model = fd.vision.ocr.Classifier(r"G:\tire-ocr\ch_ppocr_mobile_v2.0_cls_infer\inference.pdmodel", r"G:\tire-ocr\ch_ppocr_mobile_v2.0_cls_infer\inference.pdiparams")
rec_model = fd.vision.ocr.Recognizer(r"G:\tire-ocr\en_PP-OCRv3_rec_infer\inference.pdmodel", r"G:\tire-ocr\en_PP-OCRv3_rec_infer\inference.pdiparams", rec_label_file)

ppocrv3 = fd.vision.ocr.PPOCRv3(det_model=det_model, cls_model=cls_model, rec_model=rec_model)

img = cv2.imread(r"G:\tire-ocr\1\868a4608e165931a7d982f319d67100.jpg")
result = ppocrv3.predict(img)

# q：这个类fastdeploy.libs.fastdeploy_main.vision.OCRResult在哪里？
# a：这个类在fastdeploy.libs.fastdeploy_main.vision.ocr.py文件中，是一个类，OCRResult类的定义如下：
# class OCRResult:
# def __init__(self, text, score, box):
#         self.text = text
#         self.score = score
#         self.box = box
#     def __str__(self):
#         return "OCRResult(text=%s, score=%s, box=%s)" % (self.text, self.score, self.box)
#     def __repr__(self):
#         return "OCRResult(text=%s, score=%s, box=%s)" % (self.text, self.score, self.box)
print("这里是text", result.text)
# print("这里是score", result.score)
# print("这里是box", result.box)

# print(type(result))
# print(result)

vis_im = fd.vision.vis_ppocr(img, result)





cv2.imwrite("visualized_result.jpg", vis_im)
