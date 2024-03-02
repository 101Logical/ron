from gtts import gTTS
import datetime
import os
import pygame

class Aru:


    def today(self):
        d = datetime.datetime.today().strftime("%d-%m-%Y-%H-%M").split('-')
        time = 'Сейчас {}, {}! часов'.format(d[3], d[4])
        w = datetime.date.today()
        week = datetime.datetime.weekday(w)
        weeks = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        today = 'Сегодня {}, месяц{}, год{}, день недели{}'.format(d[0], d[1], d[2], weeks[week])





        tts = gTTS(text=today, lang='ru')
        tts.save("output.mp3")

        pygame.mixer.init()  # Initialize pygame mixer here

        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()  # Close the pygame mixer

        # Remove the file now that it's no longer in use
        if os.path.exists("output.mp3"):
            os.remove("output.mp3")

# ron = Aru()
# ron.today()