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
                             "2025暑期夏令营课程已开始，欢迎大家到协会B站账号NEUQCSA学习~\n"
                             "更多信息请看群公告和群文件，如有疑问欢迎在群内交流~")