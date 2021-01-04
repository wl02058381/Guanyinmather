# -*- coding: utf-8 -*-
from flask import Flask, request
import pygame
import os
from PIL import Image
app = Flask(__name__)

@app.route('/', methods=['POST'])
def handler():
    file_name = request.values.get('id')
    name = request.values.get('name')
    
    # 步驟一：信徒名字文字轉圖片
    text_to_picture(file_name,name)
    blend_two_images2(file_name)
    # 步驟二：圖片合成

    return {'status':'Ok'}
    
# 文字轉圖片
def text_to_picture(file_name,name):
    pygame.init()
    #設定視窗
    width, height = 698, 898
    # screen = pygame.display.set_mode((width, height))
    #建立畫布bg
    bg = pygame.Surface((width, height))
    # bg = bg.convert()
    bg.fill((255, 255, 255))  # 白色
    # 待轉換文字
    text = str(name)
    #設定字型和字號
    font_type = 'stxihei'
    
    if (len(text) == 3):
        font_size = 120
        font = pygame.font.SysFont(font_type, font_size)
        #渲染圖片，設定背景顏色和字型樣式,前面的顏色是字型顏色
        font_text = font.render(text, True, (0, 0, 0))
        bg.blit(font_text, (172, 680))
    elif len(text) == 4:
        font_size = 100
        font = pygame.font.SysFont(font_type, font_size)
        #渲染圖片，設定背景顏色和字型樣式,前面的顏色是字型顏色
        font_text = font.render(text, True, (0, 0, 0))
        bg.blit(font_text, (148, 680))
    elif len(text) == 5:
        font_size = 86
        font = pygame.font.SysFont(font_type, font_size)
        #渲染圖片，設定背景顏色和字型樣式,前面的顏色是字型顏色
        font_text = font.render(text, True, (0, 0, 0))
        bg.blit(font_text, (142, 680))
    #儲存圖片
    pygame.image.save(bg, os.path.join('.', 'images', str(file_name) + '.png'))#圖片儲存地址


def blend_two_images2(file_name):
    img1 = Image.open('./images/'+str(file_name) + '.png')
    img1 = img1.convert('RGBA')

    img2 = Image.open('./images/'+"light.jpg")
    img2 = img2.convert('RGBA')

    r, g, b, alpha = img2.split()
    alpha = alpha.point(lambda i: i > 0 and 204)

    img = Image.composite(img2, img1, alpha)
    img.show()
    img.save("./images/blend2.png")

    return

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8888',debug=True)
