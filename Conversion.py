from googletrans import Translator
import easyocr
from gtts import gTTS
from IPython.display import Audio
import PIL
from PIL import Image, ImageDraw
import playsound as ps
import os
import glob

reader = easyocr.Reader(['en'])

translator = Translator()

path = os.getcwd()
fileSystem = glob.glob(path + '/images/*')
latestFile = max(fileSystem, key = os.path.getctime)
fileName = latestFile.split('\\')[-1]
print(fileName)

fileName = path + '/images/' + fileName

img = Image.open(fileName)
contobw = img.convert("L")
contobw.save(path + '/bw_images/' + 'rdj-bw.jpg')
contobw.show()

path1 = os.getcwd()
fileSystem1 = glob.glob(path1 + '/bw_images/*')
latestFile1 = max(fileSystem1, key = os.path.getctime)
fileName1 = latestFile1.split('\\')[-1]
print(fileName1)

fileName = path + '/bw_images/' + fileName1

bounds = reader.readtext(fileName, add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch',blocklist='=-')

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

im = PIL.Image.open(fileName)
exl = draw_boxes(im, bounds)
exl.show()

text_list = reader.readtext(fileName, add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch',blocklist='=-', detail=0)

text_comb=' '.join(text_list)
print(translator.detect(text_comb))

text_en=translator.translate(text_comb, src='en')
print(text_en.text)

ta_tts=gTTS(text_en.text)
path += '/audio/trans.mp3'
ta_tts.save(path)


ps.playsound(path)

aud = path + '/audio/'
audlist = glob.glob(os.path.join(aud, "*"))
for f in audlist:
    os.remove(f)


bwimg = path + '/bw_images/'
imglist = glob.glob(os.path.join(bwimg, "*"))
for f in imglist:
    os.remove(f)
