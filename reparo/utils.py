#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Video utils
'''

import cv2
from tqdm import tqdm


def write_video(frames, outfile, fps, frame):
    """Write frames to video output file

    Args:
        frames (list<numpy.ndarray[H, W, 3]>): video frames
        outfile (string): path to output file
        fps (int): frames per second to write
        frame (tuple<int, int>): video spatial dimensions
    """

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(outfile, fourcc, fps, frame)

    for frame in tqdm(frames):
        out.write(frame)


def read_video(video_path, max_frames=None):
    """Read frames from video input file

    Args:
        video_path (str): path to input video file
        max_frames (int, optional): maximum number of frames to read

    Returns:
        list<numpy.ndarray[H, W, 3]>: video frames
        int: frames per second of the input video
        tuple<int, int>: video spatial dimensions
    """

    vidcap = cv2.VideoCapture(video_path)
    frames = []
    for idx in tqdm(range(int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)))):
        _, image = vidcap.read()
        frames.append(image)
        if isinstance(max_frames, int) and (idx + 1 == max_frames):
            break

    fps_setting = vidcap.get(cv2.CAP_PROP_FPS)
    vidframe_setting = (int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    vidcap.release()

    return frames, fps_setting, vidframe_setting
