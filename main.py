import requests

# Import the required module for text
# to speech conversion
from gtts import gTTS
import pdfplumber
# This module is imported so that we can
# play the converted audio
import os

# ---------------------------------------------EXTRACT TEXT FROM PDF----------------------------------------------------
all_text = ''
pdf = pdfplumber.open('name_of_your_pdf.pdf')
for page in pdf.pages:
    single_page_text = page.extract_text()
    # print(single_page_text)
    all_text = all_text + '\n' + single_page_text
print(all_text)

# --------------------------------------------CONVERT TEXT INTO AUDIO---------------------------------------------------
# The text that you want to convert to audio
mytext = all_text
# mytext = 'There was once a hare who was friends with a tortoise. One day, he challenged the tortoise to a race. ' \
#          'Seeing how slow the tortoise was going, the hare thought he’ll win this easily. So he took a nap while the ' \
#          'tortoise kept on going. When the hare woke up, he saw that the tortoise was already at the finish line. ' \
#          'Much to his chagrin, the tortoise won the race while he was busy sleeping. There are actually a couple of ' \
#          'moral lessons we can learn from this story. The hare teaches that overconfidence can sometimes ruin you. ' \
#          'While the tortoise teaches us about the power of perseverance. Even if all the odds are stacked against ' \
#          'you, never give up. Sometimes life is not about who’s the fastest or the strongest, it’s about who is the ' \
#          'most consistent. '

# mytext = 'Я сейчас вам покажу, откуда на Беларусь готовилось нападение. И если бы за шесть часов до операции не был ' \
#          'нанесён превентивный удар по позициям — четыре позиции, я сейчас покажу карту, я принёс — они бы атаковали ' \
#          'наши войска Белоруссии и России... Не мы развязали эту [роскомнадзор], у нас совесть чиста. Хорошо, ' \
#          'что начали. '

# mytext = '上海市政府新闻办公室组织召开上海市新冠肺炎疫情防控工作第193场新闻发布会,介绍疫情防控有关情况。 上海市卫生健康委副主任赵丹丹介绍,5月23日,上海市新增58例新冠'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")
