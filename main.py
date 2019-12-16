import numpy as np
import pandas as pd
import cv2

origin = pd.read_excel('./cho0h5.xlsx')

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
[88, 170, 75]]

x, y = data.shape
img = np.zeros((x, y, 3), dtype='uint8')

for i in range(x):
    for j in range(y):
        img[i, j] = colors[data[i, j]]

print(colors)
print(data)
print(data.dtype)

cv2.imshow('data*123', data*123)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.imwrite('./cho0h5.png', img) #
cv2.destroyAllWindows()
