#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Video mixing script
'''

import argparse
import random
import numpy as np
from reparo.utils import read_video, write_video


def main(args):

    frames, fps_setting, frame_setting = read_video(args.video, max_frames=200)

    # Add noise inbetween them
    for _ in range(int(args.noise * len(frames))):
        frames.append((255 * np.random.rand(*frame_setting, 3)).astype(np.uint8))

    # Mix frames up
    random.shuffle(frames)

    # Write video
    write_video(frames, args.outfile, fps=fps_setting, frame=frame_setting)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Video mixer script',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("video", type=str, help="The path to the corrupted video")
    parser.add_argument("--outfile", type=str, default='result.mp4', help="Path to output file")
    parser.add_argument("--noise", type=float, default=0.05, help="Proportion of noisy frames added")

    args = parser.parse_args()

    main(args)
