#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@time: 2016/11/18 18:45
@author: Silence
'''
import cv2
import dlib
import numpy
import glob


PREDICTOR_PATH = "D:\py2.7.12\Lib\site-packages\dlib-19.2.0-py2.7-win-amd64.egg\shape_predictor_68_face_landmarks.dat"
SCALE_FACTOR = 1
FEATURE_AMOUNT = 11

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(PREDICTOR_PATH)


class NoFaces(Exception):
    pass

def get_landmarks(im):
    '''
    本方法主要是获得点的列表
    :param im: 输入一张图像
    :return: 返回68*2的列表
    '''
    rects = detector(im, 1)
    print("脸的个数: {}".format(len(rects)))
    if len(rects) > 1:
        for i in range(len(rects)):
            facepoint = numpy.array([[p.x, p.y] for p in predictor(im, rects[i]).parts()])
            for i in range(68):
                im[facepoint[i][1]][facepoint[i][0]] = [232, 28, 8]
        return im
    if len(rects) == 0:
        raise NoFaces
    else:
        return numpy.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])

def annote_landmarks(im, landmarks):
    '''
    在图像上将点表示出来，并且在点的旁边为点标号
    :param im:图像
    :param landmarks:点
    :return:返回图像
    '''
    im = im.copy()
    for idx, point in enumerate(landmarks):
        pos = (point[0, 0], point[0, 1])
        cv2.putText(im, str(idx), pos,
                    fontFace=cv2.FONT_HERSHEY_DUPLEX,
                    fontScale=0.5,
                    color=(0, 0, 255))
        cv2.circle(im, pos, 3, color=(0,255,255))
    return im

def read_im_and_landmarks(fname):
    '''
    读取图像并获得点
    :param fname: 图像路径
    :return: 图像和点列表
    '''
    im = cv2.imread(fname, cv2.IMREAD_COLOR)
    im = cv2.resize(im, (im.shape[1] * SCALE_FACTOR,
                         im.shape[0] * SCALE_FACTOR))
    s = get_landmarks(im)

    return im, s

def main(img,path):
    dealimg,landmarks = read_im_and_landmarks(img)
    fuseimg = annote_landmarks(dealimg,landmarks)

    a, b = img.split('.')
    newName = a + '_landmark.jpg'

    return cv2.imwrite(newName, fuseimg)

if __name__ == '__main__':

    main()
    # outputLandmarksImage(r'F:\image\imageData\positive\front\pre\his\*.jpg')

    # path = r'F:\image\imageData3\positive\front\pre\his\*.jpg'
    # for imgfile in glob.glob(path):
    #     img,landmarks = read_im_and_landmarks(imgfile)
    #     img1 = annote_landmarks(img,landmarks)
    #
    #     a,b = imgfile.split('.')
    #     newName = a + '_landmark.jpg'
    #     cv2.imwrite(newName,img1)
