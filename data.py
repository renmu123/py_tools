import types

def group_by(data: list, key):
    """
    :param data: [{},{}]
    :param key: 可以用 str 也可以用lambda
    :return:
    """
    group_data = defaultdict(list)
    if isinstance(key, types.FunctionType):
        for r in data:
            k = key(r)
            group_data[k].append(dict(r.items()))
    elif isinstance(key, (int, str, tuple)):
        for r in data:
            group_data[r[key]].append(dict(r.items()))
    else:
        raise KeyError('key既不是 str, int, tuple 也不是 function')
    return group_data

# 递归解析树形图
def nodes_from_tree(tree, nodes=[]):
    import copy
    if isinstance(tree, list):
        for child in tree:
            nodes_from_tree(child, nodes=nodes)
    elif isinstance(tree, dict) and tree.get('children'):
        new_child = copy.deepcopy(tree)
        new_child.pop('children')
        nodes.append(new_child)

        child = tree.get('children')
        nodes_from_tree(child, nodes=nodes)
    else:
        nodes.append(tree)
    return nodes