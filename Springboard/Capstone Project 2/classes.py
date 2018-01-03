import skimage
import numpy as np

from skimage import data, io
from skimage.transform import rotate
from skimage.color import rgb2gray, rgb2grey

#image editing
from skimage import feature, filters
#from skimage import *
import cPickle as pickle

import matplotlib.pyplot as plt


class ImageProcessor():
    '''Class used to stack and convert images into grayscale
    args: 
        image: ndarray image of the flappybird state representation
    '''
    def __init__(self, orig_image):
        self._orig_image = orig_image
        
        #convert into grayscale, crop out the bottom and downsample
        self._gray_image = skimage.color.rgb2gray(
            orig_image[:,:405][::3,::3])
        
    @property
    def gray_image(self):
        return self._gray_image
    
    @gray_image.setter
    def gray_image(self, image):
        self._orig_image = image
        self._gray_image = skimage.color.rgb2gray(image)
        
    @property 
    def orig_image(self):
        return self._orig_image
    
    @orig_image.setter
    def orig_image(self, image):
        self._orig_image = image
        self._gray_image = skimage.color.rgb2gray(image)
        
    def show_image(self, gray=True):
        if gray:
            io.imshow(self._gray_image)
        else:
            io.imshow(self._orig_image)
        plt.show()
        
    def shape(self):
        print('original image shape:', self._orig_image.shape)
        print('gray image eshape:', self._gray_image.shape)
        return self._gray_image.shape
        
    def matrix(self, gray=True):
        return self._gray_image
    
    def is_first_frame(self):
        '''seems first frame is always dark. Used to detect
        if the state value is all 0 or not'''
        return np.max(self._gray_image) == 0

class StackedImages():
    '''object to keep the stacked frames together for organization.
    organized as a list of stacked ndarrays'''
    def __init__(self, image_processors = None, num_per_stack = None):
        if type(image_processors) is not list:
            if num_per_stack is not None: ##
                print('images need to be a list')
        else:
            self._stacked_images = []
            self._images = image_processors
            for i in range(0, len(image_processors), num_per_stack):
                list_images = [image_processors[i].gray_image for i in 
                              range(i, i+num_per_stack)]
                stacked = np.stack(list_images, axis=0)
                self._stacked_images = stacked
#             self._images = [i.gray_image for i in images]
#             self._stacked_images = np.stack(self._images, axis=0)
    
    def plot(self):
        for image in self._images:
            io.imshow(image.gray_image)
            plt.show()
            #io.imshow(image)
            #plt.show()
        
    def get_stacked_images(self):
        return self._stacked_images
    
    
    def get_shape(self):
        return self._stacked_images.shape
    
    def save(self, file_name):
        handle = open(file_name, 'w')
        pickle.dump(self.__dict__, handle, 2)
        handle.close()
        
    def load(self, file_name):
        handle = open(file_name, 'r')
        tmp_dict = pickle.load(handle)
        self.__dict__.clear()
        self.__dict__.update(tmp_dict)
        handle.close()
        
        