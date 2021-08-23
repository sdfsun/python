# -*- coding: utf-8 -*-
#根据单张图片的xml文件，在图片上标注出目标
import xml.etree.ElementTree as ET
import cv2




xml_file = 'voc_data/1.xml'
tree = ET.parse(xml_file)
root = tree.getroot()
imgfile = 'images/1.jpg'
im = cv2.imread(imgfile)
for object in root.findall('object'):
    object_name = object.find('name').text
    print(object_name)
    Xmin = int(object.find('bndbox').find('xmin').text)
    Ymin = int(object.find('bndbox').find('ymin').text)
    Xmax = int(object.find('bndbox').find('xmax').text)
    Ymax = int(object.find('bndbox').find('ymax').text)
    color = (4, 250, 7)
    cv2.rectangle(im, (Xmin, Ymin), (Xmax, Ymax), color, 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(im, object_name, (Xmin, Ymin - 7), font, 0.5, (6, 230, 230), 2)
    # cv2.imshow('1', im)
    # cv2.waitKey(100)
cv2.imwrite('1.jpg', im)
