import pygame as pg
pg.init()

color={
    "white":(255,255,255),
    "black":(0,0,0),
    "red":(220,20,60),
    "pink":(255,250,205),
    "lemon_y":(255,250,205),
    "green":(91,231,196),
    "sky_b":(135,206,250),
    "lc_b":(224,255,255),  #lightcyan
    "midn_b":(25,25,112),   #midnightblue
    "mid_p":(147,112,219),
    "blue_p":(138,43,226),  #blueviolet
    "pium_p":(221,160,221),
    
    }
#name=input("enter name-->")
name="tessst"

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
windows.fill(color["lc_b"])     #白色底

#顯示文字
font=pg.font.SysFont("simhei",50) #名字/尺寸
text=font.render("Hello "+name,True,color["midn_b"],color["pium_p"]) #內容/平滑值/文字顏色/背景顏色
windows.blit(text, (w/2-70,10)) 

#*輸入
font = pg.font.Font(None, 32)
input_box = pg.Rect(100, 100, 140, 32)

#畫線/方形/員
pg.draw.line(windows,color["midn_b"],(50,50),(200,50)) #起始/終點
pg.draw.rect(windows,color["green"],(150,200,170,150))  #(橫軸位置/縱軸位置/橫長/縱長)
pg.draw.circle(windows,color["blue_p"],(w/2+50,h/2),100) #圓心座標/半徑

#介面刷新及視窗判斷
screen.blit(windows, (0,0))
pg.display.update()     #介面刷新
bye()
pg.quit() 