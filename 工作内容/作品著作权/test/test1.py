#encoding=utf-8

"""
#2019.4.4 将PASCAL VOC数据集转换成yolo数据集格式
"""
import xml.etree.ElementTree as ET
import os

pascal_Ann_path = "voc_data"
yolo_Output_txt = "yolo_data"


# 对voc中的坐标进行转换
def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


classes = {'罪': 1}  # 检测的内容类别


# 读出文件夹中XML文件，并寻找相应的尺寸
def convert_annotation(input_vocxml_file, output_yolo_txt):
    in_file = open(input_vocxml_file)
    out_file = open(output_yolo_txt, 'a')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')

    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes[cls]
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


def main():
    tempfilename = os.listdir(pascal_Ann_path)
    for file in tempfilename:  # 遍历文件夹
        (filename, extension) = os.path.splitext(file)
        pascal_ann_path = os.path.join(pascal_Ann_path + "\\" + file)  # 存放.XML的文件件
        yolo_output_txt = os.path.join(yolo_Output_txt + "\\" + filename + '.txt')

        if os.path.exists(yolo_output_txt):
            os.remove(yolo_output_txt)
        convert_annotation(pascal_ann_path, yolo_output_txt)


if __name__ == '__main__':
    main()