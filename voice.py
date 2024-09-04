from gtts import gTTS
from playsound import playsound
mytext="I m Maha Abdulraqib"
myjob =gTTS(text=mytext)
# myjob.save('pysound.mp4')
# playsound('pysound.mp4')
import os
file_path = os.path.abspath("pysound.mp3")
playsound(file_path)
