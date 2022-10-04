from googletrans import Translator
import easyocr
from gtts import gTTS
from IPython.display import Audio

import playsound as ps

import os
import glob

reader = easyocr.Reader(['ta', 'en'])
reader = easyocr.Reader(['en'])

translator = Translator()

import PIL
from PIL import ImageDraw

path = os.getcwd()
fileSystem = glob.glob(path + '/*')
latestFile = max(fileSystem, key = os.path.getctime)
fileName = latestFile.split('\\')[-1]
print(fileName)

im = PIL.Image.open(fileName)

bounds = reader.readtext(fileName, add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch',blocklist='=-')

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

draw_boxes(im, bounds)

text_list = reader.readtext(fileName, add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch',blocklist='=-', detail=0)

text_comb=' '.join(text_list)
print(translator.detect(text_comb))

text_en=translator.translate(text_comb, src='en')
print(text_en.text)

ta_tts=gTTS(text_en.text)
ta_tts.save('trans.mp3')


text_hi=translator.translate(text_comb, src='en',dest='hi')
print(text_hi.text)

ta_tts_hi=gTTS(text_hi.text, lang='hi')
ta_tts_hi.save('trans_hi.mp3')

# Audio('trans.mp3' , autoplay=True)
# Audio('trans_hi.mp3' , autoplay=True)

ps.playsound("trans.mp3")
ps.playsound("trans_hi.mp3")

