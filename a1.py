import pygame as pg
pg.init()

w,h=800,500
screen=pg.display.set_mode((w,h))
pg.display.set_caption("我還不知道")   #title

def bye():  #關閉程式
    running=True
    while running:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                running=False
windows=pg.Surface(screen.get_size())    #get_size()取得視窗尺寸
windows=windows.convert()
windows.fill((255,255,255))     #白色底



screen.blit(windows, (0,0))
pg.display.update()     #介面刷新

bye()
pg.quit() 