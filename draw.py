import cv2

def raw(frame, x, y, w, h):
    #8 line
    frame = cv2.line(frame, (x,y), (x+int(w/4), y), (0,255,0), 1)
    frame = cv2.line(frame, (x,y), (x, y+int(h/4)), (0,255,0), 1)
    frame = cv2.line(frame, (x,y+h), (x, y+int(3*h/4)), (0,255,0), 1)
    frame = cv2.line(frame, (x,y+h), (x+int(h/4), y+h), (0,255,0), 1)
    frame = cv2.line(frame, (x+w,y+h), (x+w, y+int(3*h/4)), (0,255,0), 1)
    frame = cv2.line(frame, (x+w,y+h), (x+int(3*w/4), y+h), (0,255,0), 1)
    frame = cv2.line(frame, (x+w,y), (x+w, y+int(h/4)), (0,255,0), 1)
    frame = cv2.line(frame, (x+w,y), (x+int(3*w/4), y), (0,255,0), 1)

    return frame
