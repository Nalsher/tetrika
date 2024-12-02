def merge_intervals(intervals):
    intervals = sorted(intervals)
    merged = []
    for start, end in intervals:
        if merged and merged[-1][1] >= start:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def calculate_overlap(intervals1, intervals2):
    i, j = 0, 0
    overlap = 0
    while i < len(intervals1) and j < len(intervals2):
        start1, end1 = intervals1[i]
        start2, end2 = intervals2[j]
        start_overlap = max(start1, start2)
        end_overlap = min(end1, end2)
        if start_overlap < end_overlap:
            overlap += end_overlap - start_overlap
        if end1 < end2:
            i += 1
        else:
            j += 1
    return overlap


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = [[intervals['lesson'][0], intervals['lesson'][1]]]
    pupil_intervals = merge_intervals([[intervals['pupil'][i], intervals['pupil'][i + 1]]
                                       for i in range(0, len(intervals['pupil']), 2)])
    tutor_intervals = merge_intervals([[intervals['tutor'][i], intervals['tutor'][i + 1]]
                                       for i in range(0, len(intervals['tutor']), 2)])

    pupil_on_lesson = calculate_overlap(lesson, pupil_intervals)
    tutor_on_lesson = calculate_overlap(lesson, tutor_intervals)

    return calculate_overlap(
        merge_intervals([[intervals['lesson'][0], intervals['lesson'][1]]]),
        merge_intervals([[max(start1, start2), min(end1, end2)] for start1, end1 in pupil_intervals for start2, end2 in
                         tutor_intervals if start1 <= end2 and start2 <= end1])
    )
