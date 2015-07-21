from moviepy.editor import *
import os, os.path
import sys


wildcard = '/Users/lesleycordero/Desktop/Videos'
for item in os.listdir(wildcard):

    clip = VideoFileClip(os.path.join(wildcard, item))
    dur = clip.duration
    firstHalf = (dur/2.0) - 7.5
    secHalf = (dur/2.0) + 7.5
    end = dur - 15.0
    clip1 = clip.subclip(0, 15.0)
    clip2 = clip.subclip(firstHalf, secHalf)
    clip3 = clip.subclip(end, dur)
    video = concatenate([clip1, clip2, clip3])
    video.to_videofile("./desktop/hi.avi", fps=24, codec='mpeg4')


if __name__ == "__main__":
    wildcard = sys.argv[1]
    callVideos(wildcard)
