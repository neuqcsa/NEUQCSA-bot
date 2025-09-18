from nonebot import on_keyword, on_notice, on_regex, logger
from nonebot.rule import is_type, to_me
from nonebot.adapters.onebot.v11.event import PokeNotifyEvent
from .utils import random_image

greet = on_regex(r"(^兔兔$)|(兔兔在吗)")
persecute = on_keyword({"驴驴", "阿米驴", "驴子", "驴肉", "马户", "烧兔", "烧驴", "辣兔", "蒸兔", "炸兔"})
poke = on_notice(rule=is_type(PokeNotifyEvent) & to_me())

@greet.handle()
async def handle_greet():
    await greet.finish("兔兔在哦")
@persecute.handle()
async def handle_persecute():
    await persecute.finish("不准迫害兔兔！" + random_image("persecute_faces"))
@poke.handle()
async def handle_poke():
    await poke.finish(random_image("poke_faces"))