
import cv2
import matplotlib.pyplot as plt
from threshold import threshold_optimal, threshold_otsu, binirize
from morphology import erode, dilate, opening, closing


def main():
    # load image
    img = cv2.imread('./assets/stationery.jpg', cv2.IMREAD_GRAYSCALE)

    # get thresold
    thOpti = threshold_optimal(img)
    thOtsu = threshold_otsu(img)

    # image binirization
    imgOptiBin = binirize(img, thOpti)
    imgOtsuBin = binirize(img, thOtsu)

    # mathematical morphology
    imgDilationOtsu = dilate(imgOtsuBin)
    imgErosionOtsu = erode(imgOtsuBin)
    imgOpeningOtsu = opening(imgOtsuBin)
    imgClosingOtsu = closing(imgOtsuBin)
    imgOC = closing(opening(imgOtsuBin))
    imgCO = opening(closing(imgOtsuBin))

    images = [imgDilationOtsu, imgErosionOtsu,
              imgOpeningOtsu, imgClosingOtsu, imgOC, imgCO]
    titles = ['Dilation', 'Erosion', 'Opening',
              'Closing', 'Opening-Closing', 'Closing-Opening']

    for i in range(2):
        plt.subplot(1, 2, i + 1), plt.title(titles[i])
        plt.imshow(images[i], 'gray')

if __name__ == '__main__':
    main()
