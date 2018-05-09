import pygame as pyg
import sys
import numpy as np
from math import isnan
from random import randint
import matplotlib.pyplot as plt
def get_time(data):
    result = ''

    result += str(int(data//3600)) + 'h:' + str(int((data%3600)//60)) + 'm:' + str(int((data%3600)%60)) + 's'


    return result

def normalize(data):
    data = data - min(data)
    top = data - min(data)
    bottom = max(data) - min(data)
    if bottom != 0:
        return top/bottom
    else:
        return top
pyg.init()


window = pyg.display.set_mode((800,800))
pyg.mixer.music.load("bloodline.WAV")
song_data = pyg.mixer.Sound("bloodline.WAV")
raw_data = song_data.get_raw()
signal = np.fromstring(raw_data, 'Int16')
print(len(signal))
the_time = np.linspace(0,len(signal)/1024, num=len(signal))
print(song_data.get_length())
print(len(signal)/song_data.get_length())
test = signal / np.linalg.norm(signal)
pyg.mixer.music.play(1)
background =  [255, 255, 255]
button_font = pyg.font.SysFont('Arial', 25)
timer_font = pyg.font.SysFont('Arial', 12)

play_button = pyg.Rect(100, 100, 300, 100)
pause_button = pyg.Rect(450,100,300,100)
progress_holder =  pyg.Rect(100, 785, 600, 5)
current_sec = 0
begin = 0
end = 5879/100

while True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit(0)

        if event.type == pyg.MOUSEBUTTONDOWN:
            mouse_position = event.pos

            if play_button.collidepoint(mouse_position[0], mouse_position[1]):
                print("Music resumed at: %.0f seconds" %(pyg.mixer.music.get_pos()/1000 ))
                pyg.mixer.music.unpause()

            if pause_button.collidepoint(mouse_position[0],mouse_position[1]):
                print("Music Paused at: %.0f seconds" %(pyg.mixer.music.get_pos()/1000))
                pyg.mixer.music.pause()
    window.fill(background)

    #print(int(600*((pyg.mixer.music.get_pos()/1000) / song_data.get_length())))
    if (pyg.mixer.music.get_pos() / 1000)//.001 > current_sec:
        current_sec += .001
        #print(current_sec)
        res = sum(normalize(signal[int(begin):int(end)]))/(5879/100)
        if isnan(res) or res < 0:
            res = 0.01
        if res > 1:
            res = 1
        res = res * 399
        print(res)
        color = [0,255, 0]
        if res > 350:
            color = [randint(200,255),0,0]
        elif res <= 350 and res >=250:
            color = [randint(150, 255), randint(150,255), 0]
        else:
            color = [0, randint(150,255), randint(100,255)]


        try:
            pyg.draw.circle(window, color, (400, 400), int(res), 10)
        except:
            pyg.draw.circle(window, color, (400, 400), 390, 10)
        begin += 5879/100
        end += 5879/100
        #print(begin)
        #print(end)
    progress = int(600*((pyg.mixer.music.get_pos()/1000) / song_data.get_length()))
    pyg.draw.circle(window, [0,0,0],(400,400),100, 10)
    pyg.draw.rect(window, [255, 0, 0], pyg.Rect(100, 785, progress, 5))
    pyg.draw.rect(window, (0, 0, 0), progress_holder, 1)
    pyg.draw.rect(window, [0, 250, 0], play_button)  # draw button
    pyg.draw.rect(window, [0, 0, 250], pause_button)  # draw button
    window.blit(button_font.render('Play', True, [0,0,0]),(225,140))
    window.blit(button_font.render('Pause', True, [0, 0, 0]), (600, 140))
    window.blit(timer_font.render(get_time(pyg.mixer.music.get_pos()/1000) + ' /', True, [0, 0, 0]), (720, 763))
    window.blit(timer_font.render(get_time(song_data.get_length()), True, [0, 0, 0]), (720, 785))
    pyg.display.update()
