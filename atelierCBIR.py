import numpy as np
# la fonction color_Moment retourne un vecteur descripteur de 6 valeurs
# contenant la moyenne et la déviation standard de chaque canal RGB
# utiliser np.mean et np.std
# il faut normaliser les moments en les divisant par la moyenne
def color_Moments(img):
    colorFeatures = []
    for i in range(3):
        colorFeatures.append(np.mean(img[:, :, i]))
        colorFeatures.append(np.std(img[: , :, i]))
    
    return colorFeatures

def getHsvHistogramFeatures(img):
    
    img_hsv=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    hist_hsv=cv2.calcHist(img_hsv,[0,1,2],None,[8,2,2],[0,360,0,255,0,255]) #il retourn un matrice de dimention 1x(8x2x2 =32)=>1x32
    return hist_hsv.flatten()
    #features=[]
    #for i in range(len(imgs_hsv)):
        #hist_hsv=cv2.calcHist(imgs_hsv[i],[0,1,2],None,[8,2,2],[0,360,0,255,0,255])
        #features.append(hist_hsv.flatten())
    #return features





def extractionMoments(img_originale):
    img_gray = cv2.cvtColor(img_originale, cv2.COLOR_BGR2GRAY)
    _,img=cv2.threshold(img_gray, 130, 255, cv2.THRESH_BINARY )
    
    moments = cv2.HuMoments(cv2.moments(img)).flatten()
    #print("ORIGINAL MOMENTS: {}".format(moments
    return moments

import math

def increaseValueMoments(moments):
    for i in range(0,7):
        moments[i] = -1* math.copysign(1.0, moments[i]) * math.log10(abs(moments[i]))
        #cv2.imwrite("ib.png",img)
    return moments

def getFeaturesShape(img):
    #featuresMoments=[]
    #for i in range(len(loaded_images)): # On parcours tous les images de base
        
    moments=extractionMoments(img)
    moments=increaseValueMoments(moments)
        
        #featuresMoments.append(moments)
    return moments




from skimage.feature import greycomatrix, greycoprops
from skimage import io, color, img_as_ubyte
import cv2




#matrix_coocurrence = greycomatrix(gray, [1], [0], levels=256, normed=False, symmetric=False) 

# GLCM properties
def contrast_feature(matrix_coocurrence):
    contrast = greycoprops(matrix_coocurrence, 'contrast')
    return  contrast

def dissimilarity_feature(matrix_coocurrence):
    dissimilarity = greycoprops(matrix_coocurrence, 'dissimilarity')    
    return  dissimilarity

def homogeneity_feature(matrix_coocurrence):
    homogeneity = greycoprops(matrix_coocurrence, 'homogeneity')
    return  homogeneity

def energy_feature(matrix_coocurrence):
    energy = greycoprops(matrix_coocurrence, 'energy')
    return  energy

def correlation_feature(matrix_coocurrence):
    correlation = greycoprops(matrix_coocurrence, 'correlation')
    return  correlation


def entropy_feature(matrix_coocurrence):
    entropy = greycoprops(matrix_coocurrence, 'entropy')
    return "Entropy = ", entropy


def getFeaturesTextur(img):
    freaturesTexturs=[]
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    matrix_coocurrence = greycomatrix(gray, [1], [0], levels=256, normed=False, symmetric=False) 
    
    freaturesTexturs.append(contrast_feature(matrix_coocurrence)[0][0])
    freaturesTexturs.append(homogeneity_feature(matrix_coocurrence)[0][0])
    freaturesTexturs.append(energy_feature(matrix_coocurrence)[0][0])
    freaturesTexturs.append(correlation_feature(matrix_coocurrence)[0][0])
    
    return freaturesTexturs






def indexation_base(loaded_images):
    features=[]
    for i in range(len(loaded_images)):
        features.append(np.concatenate((color_Moments(loaded_images[i]),getHsvHistogramFeatures(loaded_images[i]),getFeaturesShape(loaded_images[i])  , getFeaturesTextur(loaded_images[i])) )) #Concaténer les deux vecteurs descripteurs de moments et d’histogramme,form,texture 
    
    return features