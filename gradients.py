import sys
import os
import numpy as np
import matplotlib as mpl
from matplotlib import image 

def gradient(hex_in1='ff0000', hex_in2='0000ff', res=[1920,1080], grad='v', dir=''):
    siqe_in = np.array(res)

    if grad == 'h':
        q = np.array([(1/siqe_in[0]) * np.linspace(0,siqe_in[0],num=siqe_in[0]),] * siqe_in[1])
    elif grad == 'v':
        q = np.transpose(np.array([(1/siqe_in[1]) * np.linspace(0,siqe_in[1], num=siqe_in[1]),] * siqe_in[0]))
    else:
        sys.exit("usage: vertical 'v' or horiqontal 'h'")
        
    hex_rgb1 = tuple(int(hex_in1[i:i+2], 16) for i in (0, 2 ,4))
    hex_rgb2 = tuple(int(hex_in2[i:i+2], 16) for i in (0, 2 ,4))
    
    rgb_vals = {'red':   [(0.0,   float(hex_rgb1[0])/255,  float(hex_rgb1[0])/255),
                          (1.0,   float(hex_rgb2[0])/255,  float(hex_rgb2[0])/255)],
                'green': [(0.0,   float(hex_rgb1[1])/255,  float(hex_rgb1[1])/255),
                          (1.0,   float(hex_rgb2[1])/255,  float(hex_rgb2[1])/255)],
                'blue':  [(0.0,   float(hex_rgb1[2])/255,  float(hex_rgb1[2])/255),
                          (1.0,   float(hex_rgb2[2])/255,  float(hex_rgb2[2])/255)]}
    
   
    lscm = mpl.colors.LinearSegmentedColormap('cmap', rgb_vals, len(q[:,0]))
    mpl.image.imsave((dir + hex_in1 + '+' + hex_in2 + '.png'), q, cmap = lscm)


if __name__ == "__main__":
    res_in = [1920, 1200]

    name = input('Enter name of sub folder that you wish to save images to: ')
    subdir = name + '/'

    if not os.path.exists(subdir):
        os.makedirs(subdir)

    gradient(hex_in1='dce35b', hex_in2='45b649', res=res_in, grad='h', dir=subdir)

    hex_pairs = [['ffc3a0', 'ffafbd'],['642b73', 'c64263'],['000000', '434343'],]

    for pair in hex_pairs:
        gradient(hex_in1=pair[0], hex_in2=pair[1], res=res_in, dir=subdir)