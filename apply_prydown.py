def apply_prydown(img):
    """
    模糊图像，模拟小图片放大的效果
    """
    scale = random.uniform(1, self.cfg.prydown.max_scale)
    height = img.shape[0]
    width = img.shape[1]
 
    out = cv2.resize(img, (int(width / scale), int(height / scale)), interpolation=cv2.INTER_AREA)
    return cv2.resize(out, (width, height), interpolation=cv2.INTER_AREA)
