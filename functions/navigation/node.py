import sys


class Node:
    def __init__(self, name):
        self.name = name
        self.dist = sys.maxsize
        self.edges = []
        self.parent = None
        self.added_to_opened_list = False

    def __lt__(self, other):
        return self.dist < other.dist
