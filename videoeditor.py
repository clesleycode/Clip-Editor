from moviepy.editor import *
import os
import sys

def callVideos(wildcard):
    for item in os.listdir(wildcard):
        #clip = VideoFileClip(item).subclip(50,60)
        #clip.write_videofile("clip",fps=24, codec='mpeg4')
        clip = VideoFileClip(item)
        print(item)
        print(clip.duration)
        

if __name__ == "__main__":
    wildcard = sys.argv[1]
    callVideos(wildcard)
