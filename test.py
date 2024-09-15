import pygame
import random

# 初始化 Pygame
pygame.init()

# 常量
TILE_SIZE = 80
MAX_SLOTS = 7

# 加载图案图片（这里用简单的颜色填充代替图像）
patterns = [pygame.Surface((TILE_SIZE, TILE_SIZE)) for _ in range(3)]
for i, pat in enumerate(patterns):
    pat.fill((i * 100, i * 100, i * 100))  # 用不同颜色填充

def set_slots(test_scenario):
    global slots
    slots = test_scenario

def remove_matching():
    global slots
    new_slots = []
    i = 0
    while i < len(slots):
        if i <= len(slots) - 3 and slots[i] == slots[i + 1] == slots[i + 2]:
            i += 3
        else:
            new_slots.append(slots[i])
            i += 1
    slots = new_slots

def print_slots(slots):
    print([p.get_at((0,0)) for p in slots])

def test_remove_matching():
    global slots
    # 测试用例
    scenarios = {
        "test_case_1": [patterns[0], patterns[0], patterns[0], patterns[1], patterns[2]],  # 预期输出: [patterns[1], patterns[2]]
        "test_case_2": [patterns[0], patterns[1], patterns[2]],  # 预期输出: [patterns[0], patterns[1], patterns[2]]
        "test_case_3": [patterns[0], patterns[0], patterns[0], patterns[0], patterns[0]],  # 预期输出: [patterns[0], patterns[0]]
        "test_case_4": [patterns[1], patterns[2], patterns[0], patterns[0], patterns[0]],  # 预期输出: [patterns[1], patterns[2], patterns[0]]
        "test_case_5": [patterns[1], patterns[1], patterns[2], patterns[2], patterns[2]],  # 预期输出: [patterns[1], patterns[1]]
        "test_case_6": [patterns[0], patterns[0], patterns[1], patterns[1], patterns[0]],  # 预期输出: [patterns[1], patterns[1], patterns[0]]
        "test_case_7": [],  # 预期输出: []
    }

    for name, scenario in scenarios.items():
        set_slots(scenario)
        print(f"{name} - Before removal:")
        print_slots(slots)
        remove_matching()
        print(f"{name} - After removal:")
        print_slots(slots)

# 运行测试
test_remove_matching()

pygame.quit()
