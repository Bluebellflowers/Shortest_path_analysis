def SPP_LS(o_id, d_id, node):
    # initialize
    node[o_id].set_SPP_u(0)  # 初始化𝐿_𝑖=0
    for t in node[1:]:  # 遍历所有的节点
        t.set_SPP_p(-1)  # 初始化前驱节点为-1
        if t.node_id != o_id:
            t.set_SPP_u(float("inf"))
    # mainLoop
    Q = [node[o_id]]
    while len(Q) != 0:
        min = Q[0].u
        min_index = 0
        for i in range(len(Q) - 1):
            if len(Q) == 1:
                pass
            else:
                if Q[i + 1].u < min:
                    min = Q[i + 1].u
                    min_index = i + 1
        i = Q[min_index]
        del Q[min_index]
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

