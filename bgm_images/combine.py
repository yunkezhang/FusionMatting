import glob
import cv2 as cv
import os
fnlist = glob.glob('*_matting.png')

for mfn in fnlist:
    ifn = os.path.splitext(mfn)[0][:-8]
    print (ifn)
    img = cv.imread(ifn+'.png')
    mat = cv.imread(mfn, cv.IMREAD_COLOR)
    if mat.shape[0] != img.shape[0] or mat.shape[1] != img.shape[1]:
        mat = cv.resize(mat, img.shape[:2][::-1], interpolation=cv.INTER_AREA)
    con = cv.hconcat([img, mat])
    cv.imwrite(ifn+'_concat.jpg', con)