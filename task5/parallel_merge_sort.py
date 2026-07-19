import threading

lock = threading.Lock()


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def parallel_merge_sort(array):

    if len(array) <= 1:
        return array

    middle = len(array) // 2

    left = array[:middle]
    right = array[middle:]

    left_result = []
    right_result = []

    def sort_left():
        nonlocal left_result
        left_result = parallel_merge_sort(left)

    def sort_right():
        nonlocal right_result
        right_result = parallel_merge_sort(right)

    thread1 = threading.Thread(target=sort_left)
    thread2 = threading.Thread(target=sort_right)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    with lock:
        return merge(left_result, right_result)