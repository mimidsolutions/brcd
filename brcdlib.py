# K Opong-Mensah
# barcode 4

import numpy as np
from pyzbar.pyzbar import decode
import cv2
import imutils
import urllib.request as urllib
from skimage import io


def read_imei(file_id):

    file_link = 'https://drive.google.com/uc?id='+file_id+'&export=download'
    resp = urllib.urlopen(file_link)
    # image_file = np.asarray(bytearray(resp.read()), dtype="uint8")
    # img_in = cv2.imdecode(image_file, cv2.COLOR_BGR2GRAY)
    img_in = io.imread(file_link)
    
    yimg,ximg = np.shape(img_in)[0:2]
    side = int(2*(np.ceil(np.linalg.norm([yimg,ximg]))//2))
    xpad = int(2*(np.ceil(side - ximg)//2))
    ypad = int(2*(np.ceil(side - yimg)//2))
    
    x0 = np.floor(side/2 - ximg/2).astype(int)
    y0 = np.floor(side/2 - yimg/2).astype(int)
    
    bg = np.zeros((side,side,3)).astype('uint8')
    img_temp = bg
    img_temp[y0:(y0+yimg),x0:(x0+ximg),:] = img_in
    
    img_in = img_temp
    
    
    angle_initial=-20
    angle_delta = 0.5
    angle_final=20
    rotation_angles=np.arange(angle_initial,angle_final,angle_delta)
    step_total = len(rotation_angles)
    
    imei = []
    for step, rotation_angle in enumerate(rotation_angles):
    
        img = imutils.rotate(img_in, rotation_angle)
        x = decode(img)
        
        # cv2.imshow("IMG",img)
        # cv2.waitKey(0)
        
        imei_temp = []
        for xi in x:
            if len(str(int(xi.data))) == 15:
                imei_temp.append(xi.data)
        
        imei = np.unique(np.concatenate((imei, imei_temp), axis=0))
        # print('Progress: '+str(100*(step+1)/step_total)+'%')
        
    
    
    imei = [int(x) for x in imei]

    return ''.join([str(imei_n)+','+'\n' for imei_n in imei])


# you can potentially cross-reference with OCR


