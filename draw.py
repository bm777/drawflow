""" Drawing with Opencv library and customizing drawing with different types
"""
# MIT License
# 
# Copyright (c) 2020 Bayangmbe Mounmo
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
    
def draw(frame, x, y, w, h):
    #8 line
    frame = cv2.line(frame, (x,y), (x+w, y), (0,255,0), 1)
    frame = cv2.line(frame, (x,y), (x, y+h), (0,255,0), 1)
    frame = cv2.line(frame, (x,y+h), (x+w, y+h), (0,255,0), 1)
    frame = cv2.line(frame, (x+w,y), (x+w, y+h), (0,255,0), 1)

    return frame
