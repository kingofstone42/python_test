import os
import msvcrt  # Windows 特有模块，用于捕获键盘输入

# 定义地图（7x7）
game_map = [
    list("#######"),
    list("#.....#"),
    list("#.....#"),
    list("#..P..#"),
    list("#.....#"),
    list("#.....#"),
    list("#######"),
]

# 玩家初始位置（行, 列）
player_pos = [3, 3]

def render():
    """渲染地图"""
    os.system("cls")  # Windows 清屏
    for row in game_map:
        print("".join(row))

def move_player(direction):
    """更新玩家位置"""
    global player_pos
    x, y = player_pos
    # 计算新位置
    if direction == "UP": x -= 1
    elif direction == "DOWN": x += 1
    elif direction == "LEFT": y -= 1
    elif direction == "RIGHT": y += 1
    else:
        return  # 无效输入

    # 检查是否能走
    if game_map[x][y] == ".":
        # 原位置清空
        game_map[player_pos[0]][player_pos[1]] = "."
        # 新位置放置玩家
        player_pos = [x, y]
        game_map[x][y] = "P"

# 游戏主循环
while True:
    render()
    print("使用箭头键移动...")
    key = msvcrt.getch()  # 获取按键

    # 方向键是两个字节组成的特殊码
    if key == b'\xe0':  # 箭头键前缀
        key2 = msvcrt.getch()
        if key2 == b'H':   # 上
            move_player("UP")
        elif key2 == b'P': # 下
            move_player("DOWN")
        elif key2 == b'K': # 左
            move_player("LEFT")
        elif key2 == b'M': # 右
            move_player("RIGHT")
