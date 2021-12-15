"""
属性:
    link_id:路段编号,
    tail_node:路段起点（相当于from node) ,
    head_node:路段终点（相当于to node),
    length:路段长度,
"""


class Link:
    def __init__(self, link_id, tail_node, head_node, length):
        self.link_id = link_id
        self.tail_node = tail_node
        self.head_node = head_node
        self.length = length
