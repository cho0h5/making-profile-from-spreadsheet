import numpy as np
import pandas as pd
import cv2

origin = pd.read_excel('./cho0h5.xlsx')
columns = origin.columns.values
data = origin.values
print(columns)
print(data)

