# 主运行文件
import sys

from PyQt5.QtCore import QVariant
from qgis.core import *
import time
from LS import *
from LC import *
from CA import *
from Read_Shapefile import *

sys.path.append("D:\ApplicationData\PyCharm\Shortest path analysis")
Link_layer = "D:\张涵\过去的工作\大三上\地理信息系统\QGIS_python_shortest network\ChicagoSketch-ex1_lnk_s.shp"
Node_layer = "D:\张涵\过去的工作\大三上\地理信息系统\QGIS_python_shortest network\ChicagoSketch-ex1_nod_s.shp"
Node_filename = "ChicagoSketch-ex1_nod_s.shp"
Link_filename = "ChicagoSketch-ex1_lnk_s.shp"
LINK, NODE, NODE_COUNT, LINK_COUNT = read_shapefile(Link_layer, Node_layer, Node_filename, Link_filename)


def Test_SPP_LC(o_id, d_id):
    Lc_node = []
    shortestpath_p_list = SPP_LC(o_id, d_id, NODE)
    # print(shortestpath_p_list)
    if shortestpath_p_list[o_id] == -1:
        pass
    else:
        print(' shortestpath_p_list is wrong! ')
    shortestpath_link = []
    head_n = NODE[d_id]
    Lc_node.append(d_id)
    tail_n = shortestpath_p_list[d_id]
    while tail_n != -1:
        for l in head_n.l_in:
            if l.tail_node == tail_n.node_id:
                shortestpath_link.insert(0, l)
        head_n = tail_n
        Lc_node.append(tail_n.node_id)
        tail_n = shortestpath_p_list[head_n.node_id]
    Lc_node.reverse()
    return shortestpath_link, Lc_node


def Test_SPP_CA(o_id, d_id):
    node = CA(o_id, d_id, NODE, LINK, NODE_COUNT, LINK_COUNT)
    # print(node)
    print('length = {:.2f}\n'.format(node[d_id].u), end="")
    head_n = NODE[d_id]
    path = []
    shortestpath_link=[]
    while node[d_id].p != -1:
        tail_n=NODE[node[d_id].p]
        for l in head_n.l_in:
            if l.tail_node == tail_n.node_id:
                shortestpath_link.insert(0, l)
        head_n = tail_n
        path.append(d_id)
        d_id = node[d_id].p
    path.append(o_id)
    return shortestpath_link,path[::-1]


def Test_SPP_LS(o_id, d_id):
    Lc_node = []
    shortestpath_p_list = SPP_LS(o_id, d_id, NODE)
    # print(shortestpath_p_list)
    if shortestpath_p_list[o_id] == -1:
        pass
    else:
        print(' shortestpath_p_list is wrong! ')
    shortestpath_link = []
    head_n = NODE[d_id]
    Lc_node.append(d_id)
    tail_n = shortestpath_p_list[d_id]
    while tail_n != -1:
        for l in head_n.l_in:
            if l.tail_node == tail_n.node_id:
                shortestpath_link.insert(0, l)
        head_n = tail_n
        Lc_node.append(tail_n.node_id)
        tail_n = shortestpath_p_list[head_n.node_id]
    Lc_node.reverse()
    return shortestpath_link, Lc_node


def writeshp(splink, spnode,filename):
    # create fields
    layerFields = QgsFields()
    layerFields.append(QgsField('id', QVariant.Int))
    layerFields.append(QgsField('tail', QVariant.Int))
    layerFields.append(QgsField(' head ', QVariant.Int))
    # define the file path for the new shapefile
    # addr = sys.path[e]#当前目录
    file_path = "D:\张涵\过去的工作\大三上\地理信息系统\最短路径\{}".format(filename)
    writer = QgsVectorFileWriter(file_path, 'UTF-8 ', layerFields,
                                 QgsWkbTypes.LineString, QgsCoordinateReferenceSystem('EPSG:4326'), 'ESRI Shapefile')
    # create features
    count = 0
    for link in splink:
        count = count + 1
        # create an empty feature
        feat = QgsFeature()
        # Creates a new Linestring geometry from a list of QgsPoint points.
        tailnode = QgsPoint(NODE[link.tail_node].X, NODE[link.tail_node].Y)
        headnode = QgsPoint(NODE[link.head_node].X, NODE[link.head_node].Y)
        feat.setGeometry(QgsGeometry.fromPolyline([tailnode, headnode]))
        # set the attribute values
        feat.setAttributes([count, link.tail_node - 1, link.head_node - 1])
        # add the feature to the layer
        writer.addFeature(feat)
    del writer
    return "success for creating shpfile ! "


def result_LS(o_id, d_id):
    start = time.perf_counter()
    p, pnode = Test_SPP_LS(o_id, d_id)
    end = time.perf_counter()
    print(' run time =', end - start)
    print(pnode)
    print(writeshp(p, pnode,"LS_Route"))


def result_LC(o_id, d_id):
    start = time.perf_counter()
    p, pnode = Test_SPP_LC(o_id, d_id)
    end = time.perf_counter()
    print(' run time =', end - start)
    print(pnode)
    print(writeshp(p, pnode,"LC_Route"))


def result_CA(o_id, d_id):
    start = time.perf_counter()
    p,pnode = Test_SPP_CA(o_id, d_id)
    end = time.perf_counter()
    print(' run time =', end - start)
    print(pnode)
    print(writeshp(p, pnode,"CA_Route"))


result_LS(2, 289)
result_LC(2,289)
result_CA(2,289)

