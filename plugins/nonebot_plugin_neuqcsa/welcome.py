from nonebot import on_notice
from nonebot.rule import is_type
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.adapters.onebot.v11.event import GroupIncreaseNoticeEvent
from .utils import config

welcome = on_notice(rule=is_type(GroupIncreaseNoticeEvent))

@welcome.handle()
async def handle_welcome(event: GroupIncreaseNoticeEvent):
    if event.group_id == config.neuqcsa_group_id:
        await welcome.finish(MessageSegment.at(event.user_id) +
                             " 🎉欢迎来到NEUQCSA2025招新群～🎉\n"
                             "加群后请按照年级-专业-姓名的格式修改群昵称\n"
                             "招新计划即将开始。\n"
                             "想对网安/CTF有更多了解的，可以B站搜索并关注我们协会官方账号NEUQCSA，里面有往期的暑期课。虽然今年课程内容可能较往年不同，但是大体方向还是一致的。")