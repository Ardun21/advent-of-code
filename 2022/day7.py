from typing import Callable
from functools import reduce

class Node:
    def __init__(self, name, parent, is_dir):
        self.name: str = name
        self.parent: Node = parent
        self.is_dir: bool = is_dir
        self.children: list[Node] = []
        self.size: int = 0

class File(Node):
    def __init__(self, name, parent, size):
        Node.__init__(self, name, parent, False)
        self.size: int = size
        self.children: None = None

class Directory(Node):
    def __init__(self, name, parent):
        Node.__init__(self, name, parent, True)
        self.children: list[Node] = []
        self.size: int = 0

    def add_file(self, fl: File) -> None:
        self.children.append(fl)
        self.size += fl.size

        p = self.parent
        while p is not None:
            p.size += fl.size
            p = p.parent

class FileSystem:
    def __init__(self, root: Directory = Directory('/', None)):
        self.root: Directory = root
        self.cwd: Directory = root
        
FS = FileSystem()
with open('input/day7.txt') as f:
    for line in f:
        line_tokens = line.strip().split(' ')
        if line_tokens[0] == '$':
            if line_tokens[1] == 'cd':
                dname = line_tokens[2]
                if dname == FS.root.name:
                    pass
                elif dname == '..':
                    FS.cwd = FS.cwd.parent
                else:
                    d = Directory(dname, FS.cwd)
                    FS.cwd.children.append(d)
                    FS.cwd = d
        else:
            try:
                size = int(line_tokens[0])
                fname = line_tokens[1]
                fl = File(fname, FS.cwd, size)
                FS.cwd.add_file(fl)
            except ValueError:
                pass

def find_dirs_by_size(start: Node, size_minimum: int, comparator: Callable[[int, int], bool]):
    filtered_dirs = []
    if type(start) == Directory and comparator(start.size, size_minimum):
        filtered_dirs.append(start)
    if start.children is None:
        return filtered_dirs
    else:
        for c in start.children:
            filtered_dirs += find_dirs_by_size(c, size_minimum, comparator)
        return filtered_dirs

print(f"Part 1 Answer: {reduce(lambda x, y: x + y, [x.size for x in find_dirs_by_size(FS.root, 100000, lambda x, y: x <= y)])}")

dir_sizes = [x.size for x in find_dirs_by_size(FS.root, 30000000 - (70000000 - FS.root.size), lambda x, y: x >= y)]
dir_sizes.sort()
print(f"Part 2 Answer: {dir_sizes[0]}")