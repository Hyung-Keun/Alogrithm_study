from dfs_implementation import dfs_recursive, dfs_stack


dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]
dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]