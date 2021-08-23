# -*- coding: utf-8 -*-
# 裁剪图片，把每一个字提出来
import time
import xml.etree.ElementTree as ET
import cv2
import json

#读取字典中原来的内容
def get_dict():
    f = open('hanzi_dict.json', 'r')
    hanzi_dict=json.load(f)
    f.close()
    return hanzi_dict

#把更新的字典写到文件中
def write_dict(hanzi_dict):
    hanzi_json=json.dumps(hanzi_dict)
    f = open('hanzi_dict.json', 'w')
    f.write(hanzi_json)
    f.close()


if __name__ == '__main__':
    hanzi_dict = get_dict()
    for i in range(10):
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
            X = 30 / (Xmax - Xmin)
            Y = 30 / (Ymax - Ymin)
            hanzi_slip = cv2.resize(hanzi_slip,(int(30/(Xmax-Xmin)*X),int(30/(Ymax-Ymin)*Y)))
            if hanzi in hanzi_dict.keys():
                hanzi_dict[hanzi] = hanzi_dict[hanzi] + 1
                #cv2.imencode('.jpg', hanzi_slip)[1].tofile(str(hanzi_dict[hanzi]) + '_' + hanzi + '.jpg')
                cv2.imencode('.jpg', hanzi_slip)[1].tofile(str(hanzi_dict[hanzi]) + hanzi + '.jpg')
            else:
                hanzi_dict[hanzi] = 1
                #cv2.imencode('.jpg', hanzi_slip)[1].tofile(str(hanzi_dict[hanzi]) + '_' + hanzi + '.jpg')
                cv2.imencode('.jpg', hanzi_slip)[1].tofile(str(hanzi_dict[hanzi]) + hanzi + '.jpg')
        time.sleep(1)
    write_dict(hanzi_dict)