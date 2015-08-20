from moviepy.editor import *
import os, os.path
import sys


def main(args):
    wildcard = args[1]
    for item in os.listdir(wildcard): 
        clip = VideoFileClip(os.path.join(wildcard, item)) 
        newVid(clip).to_videofile("./desktop/" + wildcard, fps=24, codec='mpeg4')
        video.without_audio().to_videofile("./desktop/noaudio/" + wildcard, fps=24, codec='mpeg4')


def newVid(vid):
    dur = vid.duration 
    firstHalf = (dur/2.0) - 7.5
    secHalf = (dur/2.0) + 7.5
    end = dur - 15.0
    clip1 = clip.subclip(0, 15.0)
    clip2 = clip.subclip(firstHalf, secHalf)
    clip3 = clip.subclip(end, dur)
    video = concatenate([clip1, clip2, clip3])
    return video


if __name__ == "__main__": 
    main(sys.argv) 
