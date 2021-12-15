"""
    o_id:起始节点
    node:节点集合
"""


def SPP_LC(o_id, d_id, node):
    # initialize
    node[o_id].set_SPP_u(0)  # 初始化𝐿_𝑖=0
    for t in node[1:]:  # 遍历所有的节点
        t.set_SPP_p(-1)  # 初始化前驱节点为-1
        if t.node_id != o_id:
            t.set_SPP_u(float("inf"))
    # mainLoop
    Q = [node[o_id]]
    while len(Q) != 0:
        i = Q[0]  # 重新设置节点 j 的前驱节点，即： 𝑃_𝑗=i;
        del Q[0]
        for ij in i.l_out:
            j = node[ij.head_node]
            if j.u > (i.u + ij.length):
                j.u = (i.u + ij.length)
                j.p = i
                if j not in Q:
                    Q.append(j)
    shortestpath_p_list = [0]
    for t in node[1:]:
        shortestpath_p_list.append(t.p)
    print('length = {:.2f}\n'.format(node[d_id].u),end="")
    return shortestpath_p_list
