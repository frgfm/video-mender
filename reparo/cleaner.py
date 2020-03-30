#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Frame filtering
'''

import numpy as np
import cv2


def filter_frames(frames, method=cv2.HISTCMP_CORREL, target_size=(64, 64), threshold=0.85):
    """Filter noisy frames out

    Args:
        frames (list<numpy.ndarray[H, W, 3]>): video frames
        method (int, optional): histogram comparison method
        target_size (tuple<int, int>, optional): frame size used for histogram comparison
        threshold (float, optional): minimum correlation between histograms to keep frame

    Returns:
        list<numpy.ndarray[H, W, 3]>: video frames
    """

    resized_frames = [cv2.resize(f.copy(), target_size) for f in frames]

    histograms = []
    for f in resized_frames:
        hist = cv2.calcHist([f], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        histograms.append(cv2.normalize(hist, hist).flatten())

    # Find a reference histogram (median less sensitive to noise)
    med_hist = np.median(histograms, axis=0)

    filtered_frames = []
    # loop over the index
    for idx, hist in enumerate(histograms):
        # compute the distance between the two histograms
        if cv2.compareHist(med_hist, hist, method) > threshold:
            filtered_frames.append(frames[idx])

    return filtered_frames
