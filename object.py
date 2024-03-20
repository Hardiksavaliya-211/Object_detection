import cv2
import cvlib as cv
from gtts import gTTS
from cvlib.object_detection import draw_bbox
from playsound import playsound
# cv2.resizeWindow('image', 1000, 1600)

def playy(text):
    language="en"
    output=gTTS(text=text,lang=language,slow=False)
    output.save("./sound/output.mp3")
    playsound("./sound/output.mp3")
video = cv2.VideoCapture(0)

while True:
    rep, frame=video.read()
    bbox,label,conf=cv.detect_common_objects(frame)
    output_imag=draw_bbox(frame,bbox,label,conf)
    
    cv2.imshow("image",output_imag)
    if cv2.waitKey(1) == ord("a"):
        break
    
sentenses=[]
i=0
for l in label:
    if(i==0):
        sentenses.append(f'hello sir,i found {l} and ')
    else:
        sentenses.append(f'{l}')
    i+=1
playy(" ".join(sentenses))    
print(label)
print(bbox)
print(conf)
     
    