from collections import deque


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def readFrequency(message):
    frequencies = {}
    for char in message:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


def create(frequencies):
    nodes = []
    for char in frequencies:
        nodes.append(Node(char, frequencies[char]))
    nodes.sort(key=lambda x: x.freq)
    return nodes


def buildTree(nodes):
    if len(nodes) == 1:
        return nodes[0]
    new = Node(None, nodes[0].freq + nodes[1].freq)
    new.left = nodes[0]
    new.right = nodes[1]
    nodes = [new] + nodes[2:]
    nodes.sort(key=lambda x: x.freq)
    return buildTree(nodes)


def assignCodes(root, code='', codes=None):
    if not codes:
        codes = {}
    if root:
        if not root.left and not root.right:
            codes[root.char] = code
        codes = assignCodes(root.left, code + '0', codes)
        codes = assignCodes(root.right, code + '1', codes)
        return codes
    return codes


def writeCode(message, codes):
    newMessage = ''
    for char in message:
        newMessage += codes[char]
    return newMessage


def decode(coded, root):
    current = root
    message = ''
    for char in coded:
        if current.char:
            message += current.char
            current = root
        if char == '0':
            current = current.left
        elif char == '1':
            current = current.right
    message += current.char
    return message


def bfs(root):
    stack = deque([[root]])
    ans = []
    while stack:
        temp = []
        level = stack.popleft()
        if not level:
            break
        for node in level:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        stack.append(temp)
        ans.append([x.char for x in temp])
    return ans


def calculateLength(frequencies):
    n = len(frequencies)
    i = 0
    array = [0] * (n * 2)
    for char in frequencies:
        array[n + i] = frequencies[char]
        array[i] = n + i
        i += 1
    h = n
    array = siftMinHeap(array)
    newArr = []
    for x in range(len(array) // 2):
        newArr.append(array[array[x]])
    # print(newArr)


def siftMinHeap(array):
    n = len(array)
    while True:
        # print(array)
        mod = 0
        for i in range(n // 2):
            if i * 2 + 1 < n // 2:
                if array[array[i]] > array[array[i * 2 + 1]]:
                    array[array[i]], array[array[i * 2 + 1]] = array[array[i * 2 + 1]], array[array[i]]
                    mod += 1
                    break
            if i * 2 + 2 < n // 2:
                if array[array[i]] > array[array[i * 2 + 2]]:
                    array[array[i]], array[array[i * 2 + 2]] = array[array[i * 2 + 2]], array[array[i]]
                    mod += 1
                    break
        if mod == 0:
            return array


def main():
    message = input()
    frequencies = readFrequency(message)
    nodes = create(frequencies)
    root = buildTree(nodes)
    values = assignCodes(root)
    newMessage = writeCode(message, values)
    # print(f'values: {values}')
    print(f'old message: {"".join(bin(ord(c)) for c in message).replace("b","")}')
    print(f'new message: {newMessage}')
    # print(f'message decoded is: {decode(newMessage, root)}')
    # print(bfs(root))
    calculateLength(frequencies)


main()
