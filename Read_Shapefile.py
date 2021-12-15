from qgis.core import *

from Node import Node
from Link import Link

"""读取shapefile文件"""


def read_shapefile(Link_layer, Node_layer, Nfilename, Lfilename):
    Link_layer = QgsVectorLayer(Link_layer, Lfilename, "ogr")
    Node_layer = QgsVectorLayer(Node_layer, Nfilename, "ogr")
    Link_features = Link_layer.getFeatures()
    Node_features = Node_layer.getFeatures()

    NODE_COUNT = 0
    list2 = []
    # 获取每个点的X,Y坐标
    for feature in Node_features:
        NODE_COUNT += 1
        # 获取shapefile中的点
        geom = feature.geometry()
        x = geom.asPoint()
        list2.append(x)
        # 将所有Node放入一个list中，并插入X,Y坐标
        NODE = [Node(i + 1, [], [], list2[i][0], list2[i][1]) for i in range(NODE_COUNT)]
        NODE.insert(0, 0)

    LINK_COUNT = 0
    list = []
    for feature in Link_features:
        LINK_COUNT += 1
        # 获取shapefile中的线段
        geom = feature.geometry()
        x = geom.asMultiPolyline()
        # 匹配一条线段的头尾节点的id
        find_head = False
        find_tail = False
        for node in NODE[1:]:
            # 第一个索引1表示线段取从头到尾的方向，第二个索引0表示取头节点，1表示取尾节点，第三个0索引表示取X坐标，1表示取Y坐标
            if x[0][0][0] == node.X and x[0][0][1] == node.Y:
                find_tail = True
                tail_id = node.node_id
            if x[0][1][0] == node.X and x[0][1][1] == node.Y:
                find_head = True
                head_id = node.node_id
            if find_tail and find_head:
                break
        # 获取到每一条线段的信息
        list.append([tail_id, head_id, geom.length()])
    LINK = [Link(i + 1, list[i][0], list[i][1], list[i][2]) for i in range(LINK_COUNT)]
    LINK.insert(0, 0)

    # 给每个Node插入入度和出度
    for i in range(1, LINK_COUNT + 1):
        NODE[LINK[i].tail_node].set_l_out(LINK[i])  # 流出对象
        NODE[LINK[i].head_node].set_l_in(LINK[i])  # 流入对象
    return LINK, NODE, NODE_COUNT, LINK_COUNT
