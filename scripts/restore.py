#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Video repairing script
'''

import argparse
from reparo import repair_video


def main(args):

    repair_video(args.video, args.outfile, args.chain_denoise)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Video repairing script',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("video", type=str, help="The path to the corrupted video")
    parser.add_argument("--outfile", type=str, default='result.mp4', help="Path to output file")
    parser.add_argument("--chain-denoise", dest='chain_denoise', action='store_true',
                        help="Should the denoising be performed using sequence coherence (rather than histograms)")

    args = parser.parse_args()

    main(args)
