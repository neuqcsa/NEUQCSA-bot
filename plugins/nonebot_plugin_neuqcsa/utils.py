import nonebot
from pathlib import Path
from nonebot.adapters.onebot.v11 import MessageSegment
import random

config = nonebot.get_driver().config

def resource(path: str):
    return MessageSegment.image(Path("Resources/" + path))

def random_image(path: str):
    folder = Path("Resources/" + path)
    # 获取文件夹中所有图片文件（可以根据需要添加更多扩展名）
    image_files = [f for f in folder.iterdir() if f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.gif', '.bmp')]
    return MessageSegment.image(random.choice(image_files))