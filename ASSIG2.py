# Write a program to implement Huffman Encoding using a greedy strategy.

import heapq

class HuffmanNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(symbol_freq_list):
    priority_queue = [HuffmanNode(symbol, freq) for symbol, freq in symbol_freq_list]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left, merged.right = left, right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_huffman_codes(root, current_code, huffman_codes):
    if root is not None:
        if root.symbol:
            huffman_codes[root.symbol] = current_code
        build_huffman_codes(root.left, current_code + "0", huffman_codes)
        build_huffman_codes(root.right, current_code + "1", huffman_codes)

def huffman_encoding(symbol_freq_list):
    if not symbol_freq_list:
        return {}, None

    huffman_tree = build_huffman_tree(symbol_freq_list)
    huffman_codes = {}
    build_huffman_codes(huffman_tree, "", huffman_codes)

    return huffman_codes, huffman_tree

def huffman_decoding(encoded_data, huffman_tree):
    if not encoded_data:
        return ""

    decoded_data = []
    current_node = huffman_tree

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.symbol:
            decoded_data.append(current_node.symbol)
            current_node = huffman_tree

    return "".join(decoded_data)

if __name__ == "__main__":
    symbol_freq_list = []
    num_symbols = int(input("Enter the number of symbols: "))
    for i in range(num_symbols):
        symbol = input(f"Enter symbol {i + 1}: ")
        freq = int(input(f"Enter frequency for {symbol}: "))
        symbol_freq_list.append((symbol, freq))

    huffman_codes, huffman_tree = huffman_encoding(symbol_freq_list)
    print("Huffman Codes:")
    for symbol, code in huffman_codes.items():
        print(f"{symbol}: {code}")

    encoded_data = input("Enter data to encode: ")
    encoded_data = "".join(huffman_codes[char] for char in encoded_data)
    print(f"Encoded data: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, huffman_tree)
    print(f"Decoded data: {decoded_data}")




'''
    symbol_freq_list = [("A", 5), ("B", 9), ("C", 12), ("D", 13), ("E", 16), ("F", 45)]
    encoded_data = ABCDEF
'''

