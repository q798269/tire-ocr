import cv2
import fastdeploy as fd

rec_label_file = "en_dict.txt"


det_model = fd.vision.ocr.DBDetector(r"G:\tire-ocr\en_PP-OCRv3_det_infer\inference.pdmodel", r"G:\tire-ocr\en_PP-OCRv3_det_infer\inference.pdiparams")
cls_model = fd.vision.ocr.Classifier(r"G:\tire-ocr\ch_ppocr_mobile_v2.0_cls_infer\inference.pdmodel", r"G:\tire-ocr\ch_ppocr_mobile_v2.0_cls_infer\inference.pdiparams")
rec_model = fd.vision.ocr.Recognizer(r"G:\tire-ocr\en_PP-OCRv3_rec_infer\inference.pdmodel", r"G:\tire-ocr\en_PP-OCRv3_rec_infer\inference.pdiparams", rec_label_file)

ppocrv3 = fd.vision.ocr.PPOCRv3(det_model=det_model, cls_model=cls_model, rec_model=rec_model)

img = cv2.imread("1.jpg")
result = ppocrv3.predict(img)
print(result)
vis_im = fd.vision.vis_ppocr(img, result)
cv2.imwrite("visualized_result.jpg", vis_im)
