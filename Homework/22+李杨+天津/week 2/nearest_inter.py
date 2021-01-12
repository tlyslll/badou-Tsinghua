import cv2
import numpy as np

class n_inter:
    def nearest_inter(self,img,out_dim):

        src_h,src_w,channel=img.shape
        new_h,new_w,new_c=out_dim[1],out_dim[0],out_dim[2]
        sh=new_h/src_h
        wh=new_w/src_w

        print("src_h=",src_h,"\nsrc_w=",src_w)
        print("new_h=",new_h, "\nnew_w=",new_w)

        if src_h==new_h and src_w==new_w:
            return img.copy()

        ner_img=np.zeros((new_h,new_w,new_c),dtype=np.uint8)

        for i in range(new_h):
            for j in range(new_w):
                x=int(i/sh)
                y=int(j/wh)
                ner_img[i,j]=img[x,y]
        return ner_img

if __name__=='__main__':
    img=cv2.imread("lenna.png")
    n_img=n_inter()
    ner_img=n_img.nearest_inter(img,(700,700,3))
    cv2.imshow("img",img)
    cv2.imshow("ner_img",ner_img)
    cv2.waitKey(0)