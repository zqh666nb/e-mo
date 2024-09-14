#创建游戏板
import random
def generate_blocks(patterns):
    blocks = []
    all_patterns = []
    for i in range(11):
        pattern = random.choice(patterns)
        all_patterns.extend([pattern] * 3)
    random.shuffle(all_patterns)
    for i in range(0, len(all_patterns), 3):
        block_patterns = all_patterns[i:i + 3]
        block = (block_patterns, 3)
        blocks.append(block)
    return blocks