def pick_peaks(array):
    pos, peaks = [], []
    start, peak = None, None
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            start = i - 1
            peak = i
        elif array[i - 1] > array[i]:
            if start is not None:
                pos.append(peak)
                peaks.append(array[peak])
                peak = None
                start = None

    return dict(zip(['pos', 'peaks'], [pos, peaks]))