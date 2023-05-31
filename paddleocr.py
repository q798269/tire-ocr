import cv2
import fastdeploy as fd

det_model=fd.vision.ocr.DBDetector("en_PP-OCRv3_det_infer/inference.pdmodel","en_PP-OCRv3_det_infer/inference.pdiparams")
cls_model=fd.vision.ocr.Classifier("en_PP-OCRv3_cls_infer/inference.pdmodel","en_PP-OCRv3_cls_infer/inference.pdiparams")
rec_model=fd.vision.ocr.CRNNRecognizer("ch_ppocr_mobile_v2.0_cls_infer/inference.pdmodel","ch_ppocr_mobile_v2.0_cls_infer/inference.pdiparams","en_dict.txt")

ppocr_v3 = fd.vision.ocr.PPOCRv3(det_model=det_model, cls_model=cls_model, rec_model=rec_model)

# Read an image
img = cv2.imread("1.jpg")

# Predict and reutrn the results

result = ppocr_v3.predict(img)

print(result)

# Visuliaze the results.

vis_im = fd.vision.vis_ppocr(img, result)

cv2.imwrite("result.png",vis_im)
