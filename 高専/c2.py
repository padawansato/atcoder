from collections import deque


def dfs(maze, visited, sh, sw):
    stack = deque([[sh, sw]])
    visited[sh][sw] = 1
    while stack:
        h, w = stack.pop()  # スタックの右を取って削除
        if maze[h][w] == "g":
            return "Yes"
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_h, new_w = h + j, w + k
            if new_h < 0 or new_h >= H or \
                            new_w < 0 or new_w >= W:
                continue
            elif maze[new_h][new_w] != "#" and \
                            visited[new_h][new_w] == 0:
                visited[new_h][new_w] = 1
                stack.append([new_h, new_w])

    return "No"


if __name__ == "__main__":
    H, W = map(int, input().split())
    maze = ["Buy" for _ in range(H)]

    for i in range(H):
        if maze[i].find("s") != -1:  # findはindexか-1を返す
            sh = i
            sw = maze[i].find("s")
            break

    visited = [[0] * W for _ in range(H)]
    print(dfs(maze, visited, sh, sw))

# H, W = map(int, input().split())
# maze = [0 for _ in range(H)]
# print(H,W,maze)