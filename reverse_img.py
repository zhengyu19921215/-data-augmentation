def reverse_img(word_img):
    offset = np.random.randint(-10, 10)
    return 255 + offset - word_img
 
 
def apply_emboss(word_img):
    emboss_kernal = np.array([
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ])
    return cv2.filter2D(word_img, -1, emboss_kernal)
 
def apply_sharp(word_img):
    sharp_kernel = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ])
    return cv2.filter2D(word_img, -1, sharp_kernel)
