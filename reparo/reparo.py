#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Video repairing function
'''

from .utils import read_video, write_video
from .cleaner import filter_frames
from .order import reorder_frames


def repair_video(video_path, output_path, chain_denoising=True):
    """Repair a video stream

    Args:
        video_path (str): path to input video file
        output_path (str): path to output video file
        chain_denoising (bool, optional): whether denoising should be performed during frame ordering
    """

    # Read video frames and settings
    frames, fps_setting, frame_setting = read_video(video_path)

    # Remove noise using histogram comparison
    if not chain_denoising:
        frames = filter_frames(frames)

    # Reorder frames
    frames = reorder_frames(frames, denoise=chain_denoising)

    # Write to video
    write_video(frames, output_path, fps=fps_setting, frame=frame_setting)
