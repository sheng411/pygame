import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 設定視窗大小
screen = pygame.display.set_mode((800, 600))

# 設定標題
pygame.display.set_caption("21 點")

# 設定遊戲時鐘
clock = pygame.time.Clock()

# 設定字體
font = pygame.font.Font(None, 30)

# 設定背景顏色
screen.fill((255, 255, 255))

# 設定遊戲狀態
OVER = 0
RUNNING = 1
game_state = RUNNING

# 設定玩家和莊家的初始分數
player_score = 0
dealer_score = 0

# 設定玩家和莊家是否要牌
player_hit = False
dealer_hit = False

# 設定牌堆
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# 定義一個函數來繪製分數
def draw_score(player_score, dealer_score):
    player_text = font.render("Player: " + str(player_score), True, black)
    dealer_text = font.render("Dealer: " + str(dealer_score), True, black)
    screen.blit(player_text, (50, 50))
    screen.blit(dealer_text, (50, 100))

# 定義一個函數來抽牌
def draw_card():
    card = random.choice(deck)
    return card

# 設定字體顏色
black = (0, 0, 0)
red = (255, 0, 0)

# 遊戲主迴圈
while True:
    # 監聽事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 玩家還要牌
    if player_hit:
        player_card = draw_card()
        player_score += player_card

    # 繪製分數
    draw_score(player_score, dealer_score)

    # 如果玩家分數大於 21，設定遊戲結束
    if player_score > 21:
        game_state = OVER
        game_over_text = font.render("Game Over!", True, red)
        screen.blit(game_over_text, (300, 300))
        pygame.display.update()
    # 莊家還要牌
    if dealer_hit:
        dealer_card = draw_card()
        dealer_score += dealer_card

    # 如果莊家分數小於 17，莊家繼續還牌
    if dealer_score < 17:
        dealer_hit = True
    else:
        dealer_hit = False
    pygame.display.update()
    clock.tick(60)
