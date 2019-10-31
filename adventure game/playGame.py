import pygame
import sys

pygame.init()

# 尺寸
size = width, height = 800, 600

# 创建指定大小的窗口
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("欢迎来到狂三真爱团，角色大冒险游戏！！！")



while 1:

    # 判断是否点击关闭按钮
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()