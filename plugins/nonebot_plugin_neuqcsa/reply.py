from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from .utils import config, resource

map = on_fullmatch(("地图"))
calendar = on_fullmatch(("校历"))
address = on_fullmatch(("快递地址"))
register = on_fullmatch(("报到", "报到时间"))
train = on_fullmatch(("军训", "军训时间"))
poster = on_fullmatch(("网安海报"))

@map.handle()
async def handle_map():
    await map.finish(resource("学校地图.png"))
@calendar.handle()
async def handle_calendar():
    await calendar.finish(resource("东秦校历.jpg"))
@address.handle()
async def handle_address():
    await address.finish("河北省秦皇岛市海港区白塔岭街道泰山路143号东北大学秦皇岛分校工学馆东侧\n邮编：066004")
@register.handle()
async def handle_register():
    await register.finish("新生报到时间：8月30日至31日")
@train.handle()
async def handle_train():
    await train.finish("学校将按照国家有关规定开展新生军训，军训时间为2025年9月14日至27日，共14天。")
@poster.handle()
async def handle_poster(event: GroupMessageEvent): # 由于需要判断群号，该功能在私聊无效
    if event.group_id in config.no_qrcode_group_ids:
        await poster.finish(resource("2025招新海报-无二维码.png") + "群号：" + str(config.neuqcsa_group_id))
    else:
        await poster.finish(resource("2025招新海报.png"))