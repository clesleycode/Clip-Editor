import moviepy.editor as mp
from moviepy.editor import *
import os
import sys


wildcard = './desktop/Videos'
vid = './desktop/Videos/'
for item in os.listdir(wildcard):
        # figure out length of video

    clip = VideoFileClip(vid + item)
    dur = clip.duration
    firstHalf = (dur/2.0) - 7.5
    secHalf = (dur/2.0) + 7.5
    end = dur - 15.0
    listt = []
    clip1 = clip.subclip(0, 15.0)
    clip2 = clip.subclip(firstHalf, secHalf)
    clip3 = clip.subclip(end, dur)
    listt.append(clip1)
    listt.append(clip2)
    listt.append(clip3)
    video = mp.concatenate(listt)
    video.write_videofile(wildcard, fps=24, codec='mpeg4')
    


if __name__ == "__main__":
    wildcard = sys.argv[1]
    callVideos(wildcard)
