"""
属性:
    node id:节点编号;
    l_in:流入节点的路段对象构成的列表;
    l_out:流出节点的路段对象构成的列表;
    u:最短路中该节点cost标号;
    p:最短路中该节点前序节点标号
方法:
    set_l_in:向流入路段列表末尾添加一个路段对象;
    set_l _out:向流出路段列表末尾添加一个路段对象;
    set_SPP_u:设置cost标号;
    set_SPP_p:设置前序节点标号
"""


class Node:
    def __init__(self, node_id, l_in_empty, l_out_empty, X, Y):
        self.node_id = node_id
        self.l_in = l_in_empty
        self.l_out = l_out_empty
        self.X = X
        self.Y = Y

    def set_l_in(self, l_in):
        self.l_in.append(l_in)

    def set_l_out(self, l_out):
        self.l_out.append(l_out)

    def set_SPP_u(self, u):  # 𝐿_𝑖 相当于赋予节点 i 的一个“距离标号”，设置 𝐿_𝑖 的值
        self.u = u

    def set_SPP_p(self, p):  # 𝑃_𝑖 为节点 𝑖 在路径上的直接前驱节点，设置 𝑃_𝑖 的值
        self.p = p

    def set_X(self, X):
        self.X = X

    def set_Y(self, Y):
        self.Y = Y
