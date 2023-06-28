from __future__ import annotations

import sys
from typing import Tuple


class Letter:
    def __init__(self, letter: str, freq: int):
        self.letter: str = letter
        self.freq: int = freq
        self.bitstring: dict[str, str] = {}

    def __str__(self):
        return f"{self.letter}:{self.freq}"

    def __repr__(self) -> str:
        return self.__str__()


class TreeNode:
    def __init__(self, freq: int, left: Letter | TreeNode, right: Letter | TreeNode):
        self.freq: int = freq
        self.left: Letter | TreeNode = left
        self.right: Letter | TreeNode = right

    def __str__(self):
        return f"( {self.freq} ) -left: {self.left} right: {self.right}"

    def __repr__(self):
        return self.__str__()


def parse_file(file_path: str) -> list[Letter]:
    """
    Read the file and build a dict of all letters and their
    frequencies, then convert the dict into a list of Letters.
    """
    chars: dict[str, int] = {}
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            chars[c] = chars[c] + 1 if c in chars else 1
    return sorted((Letter(c, f) for c, f in chars.items()), key=lambda x: x.freq)


def build_tree(letters: list[Letter]) -> Letter | TreeNode:
    """
    Run through the list of Letters and build the min heap
    for the Huffman Tree.
    """
    response: list[Letter | TreeNode] = letters  # type: ignore
    while len(response) > 1:
        left = response.pop(0)
        right = response.pop(0)
        total_freq = left.freq + right.freq
        node = TreeNode(total_freq, left, right)
        response.append(node)
        response.sort(key=lambda x: x.freq)
    return response[0]


def traverse_tree(root: Letter | TreeNode, bitstring: str) -> list[Letter]:
    """
    Recursively traverse the Huffman Tree to set each
    Letter's bitstring dictionary, and return the list of Letters
    """
    if isinstance(root, Letter):
        root.bitstring[root.letter] = bitstring
        return [root]
    treenode: TreeNode = root  # type: ignore
    letters = []
    letters += traverse_tree(treenode.left, bitstring + "0")
    letters += traverse_tree(treenode.right, bitstring + "1")
    return letters


def huffman(file_path: str, char_list: dict[str, int] = None) -> tuple[Letter | TreeNode, dict]:
    """
    Parse the file, build the tree, then run through the file
    again, using the letters dictionary to find and print out the
    bitstring for each letter.
    """
    letters_list = []
    if char_list is None:
        letters_list = parse_file(file_path)
    else:
        letters_list = [Letter(char, freq) for char, freq in char_list.items()]
    root = build_tree(letters_list)
    letters = {
        k: v for letter in traverse_tree(root, "") for k, v in letter.bitstring.items()
    }

    if char_list is not None:
        return root, letters

def encode(letters: dict[Letter, str], string: str) -> str:
    out = ""
    for letter in string:
        out += letters[letter]
    return out




if __name__ == "__main__":
    # pass the file path to the huffman function
    tree, letters = huffman("", {
        "a": 500,
        "b": 400,
        "c": 300,
        "d": 250,
        "e": 200,
        "f": 150,
    })

    print(tree)
    print(letters)

    encoded = encode(letters, "caffebad")
    print(f"encoded length={len(encoded)} result= {encoded}")
