import nonebot
from nonebot import require, logger
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
from .utils import config, resource
from datetime import datetime

async def send_poster():
    logger.info("Sending poster...")
    bot = nonebot.get_bot()
    for schedule_group_id in config.schedule_group_ids:
        if schedule_group_id in config.no_qrcode_group_ids:
            poster_path = "2025招新海报-无二维码.png"
        else:
            poster_path = "2025招新海报.png"
        await bot.send_group_msg(group_id=schedule_group_id, message="🎉网络空间安全协会招新开始啦🎉\n"
                                                                     "😎加入我们，成为黑客！😎\n"
                                                                     "💪从网站攻击到算法破解应有尽有💪\n"
                                                                     "🧨从漏洞挖掘到漏洞利用样样满足🧨\n"
                                                                     "🕹️从竞赛奖项到科创加分拿到手软🕹️\n"
                                                                     "\n"
                                                                     "🎭参加黑客夏令营，解开黑客攻防的秘密🎭\n"
                                                                     "😋还有7.28日开始的彩蛋题活动，U盘、PCB尺子、限定贴纸等你来拿，一血甚至还有专属神秘奖励😋\n"
                                                                     "👉加群开启黑客之旅：" + str(config.neuqcsa_group_id) + "\n"
                                                                     "不管你是零基础还是大神都可以加入进来！详细信息可以到协会官网了解：www点neuqcsa点cn" + resource(poster_path))
        for superuser in config.superusers:
            await bot.send_private_msg(user_id=superuser, message=str(datetime.now()) + " 已向群 " + str(
            schedule_group_id) + " 发送 " + poster_path)

# 定时任务，基于装饰器的方式
@scheduler.scheduled_job("cron", hour=8, id="job_8", misfire_grace_time=None)
async def task_8():
    await send_poster()
@scheduler.scheduled_job("cron", hour=14, id="job_14", misfire_grace_time=None)
async def task_14():
    await send_poster()
@scheduler.scheduled_job("cron", hour=19, id="job_19", misfire_grace_time=None)
async def task_19():
    await send_poster()

# 启动时输出定时任务
for job in scheduler.get_jobs():
    logger.info(job)