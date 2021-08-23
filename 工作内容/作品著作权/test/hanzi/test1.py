# -*- coding: utf-8 -*-
# 修改图片尺寸大小  注意cv2读取中文路径问题
import numpy as np
import cv2
import pathlib

# 读取图像，解决imread不能读取中文路径的问题
def readimg(filename, mode):
    raw_data = np.fromfile(filename, dtype=np.uint8)  # 先用numpy把图片文件存入内存：raw_data，把图片数据看做是纯字节数据
    img = cv2.imdecode(raw_data, mode)  # 从内存数据读入图片
    return img


if __name__ == '__main__':
    data_dir = 'F:\\PycharmProjects\\CnkjProjects\\zpzzq\\test\\hanzi\\'
    data_dir = pathlib.Path(data_dir)

    pictures_paths = list(data_dir.glob('*.jpg'))
    pictures_paths = [str(path) for path in pictures_paths]
    k = 0
    for i in pictures_paths:

        i = i.replace('\\', '\\\\')
        img = readimg(i,1)
        x, y = img.shape[0:2]
        x1,y1=30/x,30/y
        img = cv2.resize(img,(int(x*x1),int(y*y1)))
        print(img.shape)
        cv2.imwrite('F:\\hanzishibie\\111\\'+str(k)+'.jpg',img)
        k=k+1
