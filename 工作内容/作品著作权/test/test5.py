#coding=utf-8
import cv2 as cv
import numpy as np
import math
from skimage import morphology
from skimage import img_as_float
from skimage import img_as_ubyte
import  matplotlib.pyplot as plt

#1、加载图片
image = cv.imread("F:\\PycharmProjects\\CnkjProjects\\zpzzq\\test\\hanzi\\0_0_3.jpg")  #你的图片路径
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# 2、图像灰度化
#gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)   #加权平均法 Gray(i,j) = 0.299R(i,j) + 0.578G(i,j) + 0.114B(i,j)  可尝试其他方法，但目前此方法最优

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)   #加权平均法 Gray(i,j) = 0.299R(i,j) + 0.578G(i,j) + 0.114B(i,j)  可尝试其他方法，但目前此方法最优
cv.imshow('show', gray)

#3、中值滤波  （论文中用的是中值滤波，但我采的图片没有很多椒盐噪声，所以换为高斯滤波器，名字懒得改了-v-）
# median = cv.GaussianBlur(gray, (3, 3), 0)     #sigmaX = 0时，标准差大小由高斯核大小自动确定
# cv.imshow('Gaus', median)
# (mh, mw) = median.shape
median = cv.medianBlur(gray,5)     #sigmaX = 0时，标准差大小由高斯核大小自动确定
cv.imshow('Median', median)
(mh, mw) = median.shape
print("medianwidth={}, medianheight={}".format(mw, mh))

#4、局部自适应二值化(递归法)
(gh, gw) = gray.shape
print("graywidth={}, grayheight={}".format(gw, gh))
# for i in range(gh):
#     for j in range(gw):
#         print(gray[i][j])

#--------划分窗口---------
#窗口大小
window_w = 30
window_h = 30
window_size = window_w * window_h
window_w_num = math.floor(mw/window_w)
window_h_num = math.floor(mh/window_h)
print(window_w_num,window_h_num)
#窗口总数
window_num = window_w_num * window_h_num
print(window_num)

windows = []
#print(windows,windows.shape)

for m in range(window_h_num):
    for k in range(window_w_num):
        for i in range(window_h):
            for j in range(window_w):
                windows.append(median[i+window_h*m][j+window_w*k])
arr_windows = np.array(windows)
print(arr_windows.shape)
reshape_arr = arr_windows.reshape(window_num,window_size)
print(reshape_arr.shape)
F_max = np.amax(reshape_arr, axis=1)
print(reshape_arr[0,:])
#print(F_max[0],F_max.shape)   #713

F_min = np.min(reshape_arr, axis=1)
print(F_min[0])

#-----------确定各个窗口的最佳阈值-----------
Ts = np.zeros(window_num)
for i in range(window_num):
   Ts[i] = round((int(F_max[i]) + int(F_min[i])) / 2)
T_uint = np.array(Ts,dtype='uint8')
print(T_uint.shape,T_uint.dtype,F_max.dtype)

# temp = np.zeros(window_size,dtype='uint8')
#print(reshape_arr.shape,temp.shape)
# ground = np.empty(window_size,dtype='uint8')
# crack = np.empty(window_size,dtype='uint8')
ground = []
crack = []
for i in range(window_num):
    T = 0
    temp = reshape_arr[i,:]
    temp = np.array(temp,dtype='uint8')
    T1 = T_uint[i]    #一般T都不会是零
    #print(T1)
    while T1 != T :
        T = T1
        for j in range(window_size):
            if temp[j]>= T1:
                ground.append(temp[j])
            else:
                crack.append(temp[j])
        R1 = int(np.mean(crack))
        R2 = int(np.mean(ground))
        T1 = int((R1 + R2) / 2)
    #print(T,T1)
    T_uint[i] = T1 - 5
print(T_uint.shape,T_uint.dtype) #713个窗口

#---------局部自适应二值化-----------
binary_gray = np.zeros((window_num,window_size),dtype='uint8')
for i in range(window_num):
    temp = reshape_arr[i, :]
    temp = np.array(temp, dtype='uint8')
    #temp_reshape = np.reshape(temp,(window_h,window_w))
    ret, th = cv.threshold(temp, T_uint[i], 255, cv.THRESH_BINARY)
    thresh = np.array(th, dtype='uint8')
    thresh = np.squeeze(thresh)
    binary_gray[i, :] = thresh
print(binary_gray.shape,thresh.shape)

#---------图像重构输出显示-------------
binary_gray = np.reshape(binary_gray,window_num*window_size)
print(binary_gray.shape)
c = 0
gray_binary = np.zeros((window_h_num*window_h,window_w_num*window_w),dtype='uint8')
for m in range(window_h_num):
    for k in range(window_w_num):
        for i in range(window_h):
            for j in range(window_w):
                gray_binary[i+window_h*m][j+window_w*k] = binary_gray[c]
                c = c + 1
print(c)
cv.imshow('binary_gray',gray_binary)
plt.imsave('1.jpg',gray_binary)

while True:
    key = cv.waitKey(10)
    if key == 27:
        cv.destroyAllWindows()    #按Esc键退出
