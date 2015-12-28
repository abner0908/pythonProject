import cv2
from imtools import show_images, show_image, mirror_image


def recolorRC(src, dst):
    """Simulate conversion from BGR to RC (red, cyan).
    The source and destination images must both be in BGR format.
    Blues and greens are replaced with cyans.
    Pseudocode:
    dst.b = dst.g = 0.5 * (src.b + src.g)
    dst.r = src.r
    """
    b, g, r = cv2.split(src)
    cv2.addWeighted(b, 0.5, g, 0.5, 0, b)
    cv2.merge((b, b, r), dst)


def recolorRGV(src, dst):
    """Simulate conversion from BGR to RGV (red, green, value).
    The source and destination images must both be in BGR format.
    Blues are desaturated.
    Pseudocode:
    dst.b = min(src.b, src.g, src.r)
    dst.g = src.g
    dst.r = src.r
    """

    b, g, r = cv2.split(src)
    cv2.min(b, g, b)
    cv2.min(b, r, b)
    cv2.merge((b, g, r), dst)


def recolorCMV(src, dst):
    """Simulate conversion from BGR to CMV (cyan, magenta, value).
    The source and destination images must both be in BGR format.
    Yellows are desaturated.
    Pseudocode:
    dst.b = max(src.b, src.g, src.r)
    dst.g = src.g
    dst.r = src.r
    """
    b, g, r = cv2.split(src)
    cv2.max(b, g, b)
    cv2.max(b, r, b)
    cv2.merge((b, g, r), dst)


if __name__ == '__main__':
    file_path = './img/lena.jpg'
    img = cv2.imread(file_path)
    #img = mirror_image(img)

    b, g, r = cv2.split(img)
    img_rc = img.copy()
    img_rgv = img.copy()
    img_cmv = img.copy()
    img_gray = img.copy()

    recolorRC(img, img_rc)
    recolorRGV(img, img_rgv)
    recolorCMV(img, img_cmv)
    img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)
    img_gray_eq = cv2.equalizeHist(img_gray)

    images = [('lena origin', img),
              ('lena RC', img_rc),
              ('lena RGV', img_rgv),
              ('lena CMV', img_cmv),
              ('lena gray', img_gray),
              ('lena gray equalize', img_gray_eq)]
    show_images(images)
