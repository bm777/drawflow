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


def text(frame, string, x=0, y=0):
	font = cv2.FONT_HERSHEY_COMPLEX
	s = cv2.getTextSize(string, cv2.FONT_HERSHEY_COMPLEX, 0.5, 1)[0]
	frame = cv2.rectangle(frame, (x, y-2*s[1]), (x+s[0], y), (255, 255, 0), -1)
	frame = cv2.putText(frame, string, (x,y-int(s[1]/2)), font, 0.5, (0,0,0),1)

	return frame
