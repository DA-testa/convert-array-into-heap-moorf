import os

def build_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        heapify(data, i, swaps)
    return swaps

def heapify(data, i, swaps):
    size = len(data)
    min_index = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and data[left] < data[min_index]:
        min_index = left
    if right < size and data[right] < data[min_index]:
        min_index = right
    if min_index != i:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        heapify(data, min_index, swaps)
        
def main():
    input_str = input()
    if "I" in input_str:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif "F" in input_str:
        filename = input()
        with open(os.path.join('./tests/', filename), mode="r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    swaps = build_heap(data)
    print(len(swaps))
    print('\n'.join(f'{i} {j}' for i, j in swaps))
        
if __name__ == "__main__":
    main()
