# -*- coding: utf-8 -*-
#根据单张图片的xml文件，在图片上标注出目标
import time
import xml.etree.ElementTree as ET
import cv2

def chaijian(i):
    xml_file = 'F:/PycharmProjects/CnkjProjects/zpzzq/test/voc_data//'+str(i)+'.xml'
    tree = ET.parse(xml_file)
    root = tree.getroot()
    imgfile = 'F:/PycharmProjects/CnkjProjects/zpzzq/test/images//'+str(i)+'.jpg'
    im = cv2.imread(imgfile)
    for hanzi_obj in root.findall('object'):
        hanzi = hanzi_obj.find('name').text
        Xmin = int(hanzi_obj.find('bndbox').find('xmin').text)
        Ymin = int(hanzi_obj.find('bndbox').find('ymin').text)
        Xmax = int(hanzi_obj.find('bndbox').find('xmax').text)
        Ymax = int(hanzi_obj.find('bndbox').find('ymax').text)
        hanzi_slip=im[Ymin:Ymax,Xmin:Xmax]

        return hanzi,hanzi_slip

if __name__=='__main__':
    hanzi_dict={}
    for i in range(3):
        xml_file = 'F:/PycharmProjects/CnkjProjects/zpzzq/test/voc_data//' + str(i) + '.xml'
        tree = ET.parse(xml_file)
        root = tree.getroot()
        imgfile = 'F:/PycharmProjects/CnkjProjects/zpzzq/test/images//' + str(i) + '.jpg'
        im = cv2.imread(imgfile)
        for hanzi_obj in root.findall('object'):
            hanzi = hanzi_obj.find('name').text
            Xmin = int(hanzi_obj.find('bndbox').find('xmin').text)
            Ymin = int(hanzi_obj.find('bndbox').find('ymin').text)
            Xmax = int(hanzi_obj.find('bndbox').find('xmax').text)
            Ymax = int(hanzi_obj.find('bndbox').find('ymax').text)
            hanzi_slip = im[Ymin:Ymax, Xmin:Xmax]
        # hanzi,hanzi_slip=chaijian(i)
            if hanzi in hanzi_dict.keys():
                hanzi_dict[hanzi]=hanzi_dict[hanzi]+1
                cv2.imencode('.jpg', hanzi_slip)[1].tofile(str(hanzi_dict[hanzi]) + '_' + hanzi + '.jpg')
            else:
                hanzi_dict[hanzi] = 1
                cv2.imencode('.jpg', hanzi_slip)[1].tofile(str(hanzi_dict[hanzi]) + '_' + hanzi + '.jpg')