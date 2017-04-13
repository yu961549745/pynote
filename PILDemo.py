"""
PIL Demo
Ref: http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320027235877860c87af5544f25a8deeb55141d60c5000
"""
#%%
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rndChar():
    return chr(random.randint(65, 90))  # 根据随机ascii码，返回对应字符


def rndColor():
    # 返回随机颜色
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def line():
    # 返回一个随机tuple
    return (random.random() * 240, random.random() * 60, random.random() * 240, random.random() * 60)


# 创建图片，尺寸240x60，颜色模式RGB，填充色纯白色
img = Image.new('RGBA', (240, 60), (255, 255, 255))
# 设置字体的类型，font-family和font-size
font = ImageFont.truetype('Times New Roman', 36)
draw = ImageDraw.Draw(img)  # 新建一个画板实例，传入参数刚刚创建的img对象作为画板
for x in range(0, img.size[0], 2):  # 画板添加杂色
    for y in range(0, img.size[1]):
        draw.point((x, y), fill=rndColor())
for i in range(4):
    img1 = Image.new('RGBA', (55, 55), (255, 255, 255, 0))  # 新建一个透明图片img1
    img_font = ImageDraw.Draw(img1)  # img1作为画板
    img_font.text((15, 8), rndChar(), font=font, fill=rndColor2())  # img1上写字
    img1 = img1.rotate(random.randint(-30, 30))  # img1旋转
    img.paste(img1, (10 + i * 60, 10), mask=img1)  # 把img1粘贴到img上面
draw.line(line(), rndColor2())  # 添加干扰杂线
draw.line(line(), rndColor2())
draw.line(line(), rndColor2())
draw.line(line(), rndColor2())
img.show()  # 预览img
