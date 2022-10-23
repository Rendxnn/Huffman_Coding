def readFrequencies(message):
    frequencies = {}
    for char in message:
        frequencies[char] = frequencies[char] + 1 if char in frequencies else 1
    return frequencies


def calculateCode(frequencies):
    t = [pair for pair in frequencies.items()]
    while len(t) > 1:
        m1, m2 = float('inf'), float('inf')
        char1, char2 = '', ''
        for frequency in t:
            if frequency[1] < m1:
                m2, m1 = m1, frequency[1]
                char2, char1 = char1, frequency[0]
            elif frequency[1] < m2:
                m2 = frequency[1]
                char2 = frequency[0]
        t = [((char1, char2), m1 + m2)] + [char for char in t if char[0] != char1 and char[0] != char2]
    return t


def calculateLength(frequencies):
    n = len(frequencies)
    array = [0] * (n * 2)
    i = 0
    for char in frequencies:
        array[n + i] = frequencies[char]
        array[i] = n + i
        i += 1
    h = n - 1
    array = buildMinHeap(array)
    while h > 0:
        m1 = array[0]
        array[0] = array[h]
        h = h - 1
        sift(array, h)
        m2 = array[0]
        array[h + 1] = array[m1] + array[m2]
        array[0] = h + 1
        array[m1] = h + 1
        array[m2] = h + 1
        sift(array, h)
    array[1] = 0
    for i in range(2, 2 * n):
        array[i] = array[array[i]] + 1
    i = 0
    lengths = []
    for char in frequencies:
        lengths.append(array[n + i])
        # print(char, array[n + i])
        i += 1
    # print(array)
    return lengths


def buildMinHeap(array):
    n = len(array)
    while True:
        mod = 0
        for i in range(n // 2):
            if i * 2 + 1 < n // 2:
                if array[array[i]] > array[array[i * 2 + 1]]:
                    array[i], array[i * 2 + 1] = array[i * 2 + 1], array[i]
                    mod += 1
                    break
            if i * 2 + 2 < n // 2:
                if array[array[i]] > array[array[i * 2 + 2]]:
                    array[i], array[i * 2 + 2] = array[i * 2 + 2], array[i]
                    mod += 1
                    break
        if mod == 0:
            return array


def sift(array, n):
    parent = 0
    minimum = 0
    while parent < n:
        if parent * 2 + 1 < n and array[array[parent]] > array[array[parent * 2 + 1]]:
            minimum = parent * 2 + 1
        if parent * 2 + 2 < n and array[array[parent]] > array[array[parent * 2 + 2]]:
            minimum = parent * 2 + 2
        if parent != minimum:
            array[parent], array[minimum] = array[minimum], array[parent]
            parent = minimum
        else:
            break
    return array


def assignCanonical(frequencies, lengths):
    n = len(lengths)
    maxlength = max(lengths)
    nums = [0] * maxlength
    print(nums, lengths)
    for length in lengths:
        nums[length - 1] += 1
    print(nums)


def main():
    message = input()
    frequencies = readFrequencies(message)
    lenghts = calculateLength(frequencies)
    assignCanonical(frequencies, lenghts)


main()
