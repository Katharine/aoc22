# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

import functools
from typing import Optional


class Node:
    def __init__(self, parent: Optional['Node'], name: str):
        self.parent = parent
        self.name = name

    @property
    def size(self):
        raise NotImplemented


class Folder(Node):
    def __init__(self, parent: Optional['Folder'], name: str):
        super().__init__(parent, name)
        self.children: dict[str, Node] = {}

    @property
    @functools.cache
    def size(self):
        return sum(x.size for x in self.children.values())


class File(Node):
    def __init__(self, parent: Folder, name: str, size: int):
        super().__init__(parent, name)
        self._size = size

    @property
    def size(self):
        return self._size


def up_to_root(node: Node) -> Node:
    while node.parent is not None:
        node = node.parent

    return node


def read_cmd(lines: list[str], index: int, tree: Folder) -> (Node, int):
    if lines[index][0] != '$':
        raise Exception(f"Expected a command on line {index}, but didn't get one.")
    cmd = lines[index][2:].split()
    if cmd[0] == 'cd':
        if cmd[1] == '..':
            tree = tree.parent
        elif cmd[1] == '/':
            tree = up_to_root(tree)
        else:
            if cmd[1] not in tree.children:
                tree.children[cmd[1]] = Folder(tree, cmd[1])
            tree = tree.children[cmd[1]]
        return tree, index + 1
    elif cmd[0] == 'ls':
        index += 1
        while index < len(lines) and lines[index][0] != '$':
            size, name = lines[index].split(' ')
            if size == 'dir':
                tree.children[name] = Folder(tree, name)
            else:
                tree.children[name] = File(tree, name, int(size))
            index += 1

    return tree, index


def total_small_folder_size(tree: Folder):
    total_size = 0
    if tree.size <= 100000:
        total_size += tree.size
    for child in tree.children.values():
        if isinstance(child, Folder):
            total_size += total_small_folder_size(child)
    return total_size


def main():
    with open('day7.dat') as f:
        content = [x.strip() for x in f.readlines()]
        root = Folder(None, '/')
        tree = root
        index = 0
        while index < len(content):
            tree, index = read_cmd(content, index, tree)

        print(total_small_folder_size(root))

main()
