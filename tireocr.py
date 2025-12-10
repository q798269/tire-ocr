import os
import glob
import pytesseract
from PIL import Image

# 图片文件夹路径
folder_path = '/1'

# 获取文件夹中的所有图片文件路径
image_files = glob.glob(os.path.join(folder_path, '*.jpg'))  # 根据实际图片格式进行调整

# 遍历图片文件并进行识别
for image_file in image_files:
    # 读取图片
    image = Image.open(image_file)

    # 进行字体识别
    result = pytesseract.image_to_string(image)

    # 打印识别结果
    print('Image:', image_file)
    print('Result:', result)
    print('---')
    1231231232131233333s33ss1231231232121312312312312312321333123
			12101606
                         
