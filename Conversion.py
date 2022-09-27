from googletrans import Translator
import easyocr
from gtts import gTTS
from IPython.display import Audio

reader = easyocr.Reader(['ta'])
translator = Translator()

import PIL
from PIL import ImageDraw
im = PIL.Image.open("tm1.jpg")

bounds = reader.readtext('tm1.jpg', add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch',blocklist='=-')

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

draw_boxes(im, bounds)

text_list = reader.readtext('tm1.jpg', add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch',blocklist='=-', detail=0)

text_comb=' '.join(text_list)
print(translator.detect(text_comb))

text_en=translator.translate(text_comb, src='ta')
print(text_en.text)

ta_tts=gTTS(text_en.text)
ta_tts.save('trans.mp3')


text_hi=translator.translate(text_comb, src='ta',dest='hi')
print(text_hi.text)

ta_tts_hi=gTTS(text_hi.text, lang='hi')
ta_tts_hi.save('trans_hi.mp3')

Audio('trans.mp3' , autoplay=True)
Audio('trans_hi.mp3' , autoplay=True)

