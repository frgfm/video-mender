#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Frame ordering
'''

import numpy as np
import cv2
from scipy.spatial import distance


def chain_frames(dist_matrix, first_frame=0, valid_idxs=None):
    """Chain together frames that are similar

    Args:
        dist_matrix (numpy.ndarray[N, N]): frame codistance matrix
        first_frame (int, optional): index of the first frame
        valid_idxs (list<int>, optional): list of valid frame indices

    Returns:
        list<int>: ordered frame indices
    """

    current_frame = first_frame
    used_frames = [current_frame]

    # For each frame, find the best match that has not been used yet
    for _ in range(dist_matrix.shape[0] - 1):
        sorted_candidates = dist_matrix[current_frame].argsort()
        for frame in sorted_candidates:
            # Skip invalid frames
            if isinstance(valid_idxs, list) and frame not in valid_idxs:
                continue
            if frame not in used_frames:
                used_frames.append(frame)
                current_frame = frame
                break

    return used_frames


def get_chain_split(used_frames, dist_matrix):
    """Filter noisy frames out

    Args:
        used_frames (list<int>): ordered frame indices
        dist_matrix (numpy.ndarray[N, N]): frame codistance matrix

    Returns:
        tuple<int, int>: pair of frame indices around the sequence split
    """

    max_dist = 0
    for prev_idx, current_idx in zip([used_frames[-1]] + used_frames[:-1], used_frames):
        # Take the maximum distance between consecutive frames
        if dist_matrix[prev_idx][current_idx] > max_dist:
            max_dist = dist_matrix[prev_idx][current_idx]
            # Take the frame before and after the split
            split = (prev_idx, current_idx)

    return split


def reorder_frames(frames, metric='cosine', target_size=(128, 128), denoise=False):
    """Reorder frames in a coherent fashion

    Args:
        frames (list<numpy.ndarray[H, W, 3]>): video frames
        metric (str, optional): matrix used for codistance matrix
        target_size (tuple<int, int>, optional): frame size used for codistance computation
        denoise (bool, optional): whether the frames need to be denoised

    Returns:
        list<numpy.ndarray[H, W, 3]>: video frames
    """

    # Don't use full resolution images if not needed
    resized_frames = np.asarray([cv2.resize(f.copy(), target_size).flatten() for f in frames])

    dist_matrix = distance.cdist(resized_frames, resized_frames, metric)

    # Take the closest unused frame and add it to the chain
    frame_chain = chain_frames(dist_matrix, 0)

    # Remove frames with consecutive frame distance much higher than the median value
    if denoise:
        consec_dist = [dist_matrix[prev_idx, current_idx]
                       for prev_idx, current_idx in zip(frame_chain[:-1], frame_chain[1:])]
        frame_chain = [elt for elt, dist in zip(frame_chain[:-1], consec_dist) if dist < 5 * np.median(consec_dist)]

    # Since we most likely didn't start with the actual first frame, there are at least two continuous sequences here
    # Let's spot the sequence split using the maximum distance between consecutive frames
    last_frame, first_frame = get_chain_split(frame_chain, dist_matrix)

    # Check both orders
    first_chain = chain_frames(dist_matrix, first_frame, valid_idxs=frame_chain)
    second_chain = chain_frames(dist_matrix, last_frame, valid_idxs=frame_chain)

    # Take the optimum in terms of sum of consecutive frame distance
    first_loss = sum(dist_matrix[prev_idx, current_idx]
                     for prev_idx, current_idx in zip(first_chain[:-1], first_chain[1:]))
    second_loss = sum(dist_matrix[prev_idx, current_idx]
                      for prev_idx, current_idx in zip(second_chain[:-1], second_chain[1:]))
    frame_chain = first_chain if first_loss < second_loss else second_chain

    return [frames[idx] for idx in frame_chain]
