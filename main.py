import numpy as np
import pandas as pd
import cv2

def resize2x(img) :
    h, w, c = img.shape
    resized_img = np.zeros((h*2, w*2, c), dtype='uint8')

    for i in range(h) :
        for j in range(w) :
            resized_img[i*2, j*2] = img[i, j]
            resized_img[i*2+1, j*2] = img[i, j]
            resized_img[i*2, j*2+1] = img[i, j]
            resized_img[i*2+1, j*2+1] = img[i, j]

    return resized_img
    
def margin(img) :
    h, w, c = img.shape

    if w > h :
        start_point = int((w - h) / 2)
        resized_img = np.ones((w, w, c), dtype='uint8')
        resized_img = resized_img * 255
        for i in range(h) :
            for j in range(w) :
                resized_img[start_point + i, j] = img[i, j]
        
#    else :
#        resized_img = np.zeros((h*2, h*2, c), dtype='uint8')

    return resized_img


input_name = input("File Name : ")
output_name = input_name.split('.')[0] + ".png"
origin = pd.read_excel("./data/" + input_name)

columns = origin.columns.values
data = origin.values

colors = []
for i in columns:
    try :
        if i[0] == 'U' :
            break
    except:
        pass


    try :
        colors.append(hex(i))
    except :
        colors.append(i)

data = data.astype('uint8')

colors = [[255, 255, 255], #
[0, 0, 0],
[75, 170, 88]]

x, y = data.shape
img = np.zeros((x, y, 3), dtype='uint8')

for i in range(x):
    for j in range(y):
        img[i, j] = colors[data[i, j]]

img = resize2x(img)
img = resize2x(img)
img = resize2x(img)
img = resize2x(img)
img = resize2x(img)
img = resize2x(img)

img = margin(img)

#cv2.imshow('profile', img)
#cv2.waitKey(0)
cv2.imwrite("./data/" + output_name, img) #
#cv2.destroyAllWindows()
