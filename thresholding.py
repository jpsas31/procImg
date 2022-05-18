import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_otsu,threshold_isodata,threshold_li,threshold_local,threshold_mean
from skimage import io
def applyThreshold(img,threshold=0):
    thresholds=[threshold_otsu,threshold_isodata,threshold_li,threshold_local,threshold_mean]
    image = io.imread(img)
    thresh = thresholds[threshold](image)
    binary = image > thresh

    fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
    ax = axes.ravel()
    ax[0] = plt.subplot(1, 3, 1)
    ax[1] = plt.subplot(1, 3, 2)
    ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])

    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].set_title('Original')
    ax[0].axis('off')

    ax[1].hist(image.ravel(), bins=256)
    ax[1].set_title('Histogram')
    ax[1].axvline(thresh, color='r')

    ax[2].imshow(binary, cmap=plt.cm.gray)
    ax[2].set_title('Thresholded')
    ax[2].axis('off')

    plt.show()
def applyBinaryThreshold(img,threshold):
    imgF=numpy.zeros(numpy.shape(img))
    for i in range(numpy.shape(img)[0]):
        for j in range(numpy.shape(img)[1]):
            imgF[i][j]= 0 if img[i][j]<threshold else 255
    return imgF
# applyThreshold("400px-Bikesgray.jpg",0)