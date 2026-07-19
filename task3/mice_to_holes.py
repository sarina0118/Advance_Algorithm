def assign_mice_to_holes(mice, holes):

    mice.sort()
    holes.sort()

    maximum_time = 0

    for i in range(len(mice)):

        time = abs(mice[i] - holes[i])

        maximum_time = max(maximum_time, time)

    return maximum_time