# pip install moviepy

try: from moviepy.editor import VideoFileClip
except ModuleNotFoundError: print("Please run \"pip install moviepy\"")
from sys import argv, exit


if argv.count == 1:
    print('FileName required in arguments!')
    exit(127)

original = VideoFileClip(argv[1])
new: VideoFileClip = original.without_audio()
new.write_videofile("out.mp4") 