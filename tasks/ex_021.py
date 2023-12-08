# Class link: https://www.youtube.com/watch?v=9FiEji_fzvk&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=30

from pygame import mixer, event

mixer.init()
mixer.music.load('tasks/ex_021_audio.mp3')
mixer.music.play()
input()
event.wait()