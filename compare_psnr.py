import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio
import cv2

ref_img = cv2.imread('picture1.jpg')
noisy_img = cv2.imread('picture1steg.jpg')

mse = np.mean((ref_img - noisy_img)**2)
PSNR = peak_signal_noise_ratio(ref_img, noisy_img)
print('MSE:', mse)
print('PSNR:', PSNR)
