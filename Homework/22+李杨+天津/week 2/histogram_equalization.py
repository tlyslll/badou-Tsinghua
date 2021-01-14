# _*_ coding:utf-8 _*_
import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ =='__main__':
    img=cv2.imread("lenna.png",1)
    '''
        #灰度直方图
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hist=cv2.calcHist([img_gray],[0],None,[256],[0,256])
        plt.figure()
        plt.hist(img_gray.ravel(),256)
        plt.show()
    '''
    '''
    #彩色直方图画法
    chans=cv2.split(img)
    colors=('b','g','r')
    cv2.imshow("img",img)
    plt.figure()
    plt.title("Flattened Color Histogram")

    for (chan,color) in zip(chans,colors):
        hist=cv2.calcHist([chan],[0],None,[256],[0,256])
        plt.plot(hist,color=color)
    plt.show()#循环结束画出所有直方图
    cv2.waitKey(0)
    '''
    '''
        #灰度图像均衡化
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        print(img_gray)
        dst=cv2.equalizeHist(img_gray)
        print(dst)
        hist=cv2.calcHist(dst,[0],None,[256],[0,256])
    
        plt.figure()
        plt.hist(dst.ravel(),256)
        plt.show()
    
        cv2.imshow("img_gray",img_gray)
        cv2.imshow("dst",dst)
        cv2.waitKey(0)
    '''

    '''
        #彩色图像均衡化
        (b,g,r)=cv2.split(img)
        bh=cv2.equalizeHist(b)
        gh=cv2.equalizeHist(g)
        rh=cv2.equalizeHist(r)
        result=cv2.merge((bh,gh,rh))
        cv2.imshow("img",img)
        cv2.imshow("img_mean",result)
        cv2.waitKey(0)
    '''
