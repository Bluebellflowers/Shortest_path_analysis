# link储存的是左右弧段的头尾结点信息胡弧长
# node储存的是左右结点的
def CA(o_id, d_id, node, link, node_count, link_count):
    for t in node[1:]:  # 遍历所有的节点
        t.set_SPP_p(-1)  # 初始化前驱节点为-1
        t.set_SPP_u(float("inf"))
    node[o_id].set_SPP_u(0)
    for k in range(1, node_count):
        for l in range(1, link_count + 1):
            if node[link[l].head_node].u > node[link[l].tail_node].u + link[l].length:
                node[link[l].head_node].u = node[link[l].tail_node].u + link[l].length
                node[link[l].head_node].p = link[l].tail_node
    return node

