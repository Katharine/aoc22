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


def smallest_big_folder(tree: Folder, required_size: int):
    small_name, small_size = tree.name, tree.size

    for child in tree.children.values():
        if isinstance(child, Folder):
            new_name, new_size = smallest_big_folder(child, required_size)
            if new_size < small_size and new_size >= required_size:
                small_name, small_size = new_name, new_size
    return small_name, small_size


def main():
    with open('day7.dat') as f:
        content = [x.strip() for x in f.readlines()]
        root = Folder(None, '/')
        tree = root
        index = 0
        while index < len(content):
            tree, index = read_cmd(content, index, tree)

        print(smallest_big_folder(root, 30000000 - (70000000 - root.size)))

main()
