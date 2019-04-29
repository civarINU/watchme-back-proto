import cv2

def _draw_rect(frame, rect):
    (x, y, w, h) = rect
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)        
    return rect

def draw_dlib_rect(frame, rect):
    # dlib.rectangle을 frame에 cv2 rectangle로 표시
    x, y = rect.left(), rect.top()
    return _draw_rect(frame, (x, y, rect.right() - x, rect.bottom() - y))

def draw_ndarray_rect(frame, rect):
    # x, y, w, h 형태의 numpy.ndarray을 frame에 cv2 rectangle로 표시
    return _draw_rect(frame, rect)