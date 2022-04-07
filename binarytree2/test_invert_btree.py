from binarytree2.prac import make_tree_by, make_lst_by


def test_invert_btree(lst):
    if not lst:
        return []

    def invert(parent):
        if parent:
            parent.left, parent.right = invert(parent.right), invert(parent.left)
            return parent

    root = make_tree_by(lst, 0)
    #root_inverted_tree = invert(root)
    return make_lst_by(invert(root))


assert test_invert_btree(lst=[]) == []
assert test_invert_btree(lst=[2]) == [2]
assert test_invert_btree(lst=[2, 1, 3, 5, 6, 2, 3]) == [2, 3, 1, 3, 2, 6, 5]
assert test_invert_btree(lst=[4, 2, 7, 1, 3, 6, 9]) == [4, 7, 2, 9, 6, 3, 1]