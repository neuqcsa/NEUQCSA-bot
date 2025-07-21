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
        await bot.send_group_msg(group_id=schedule_group_id, message="网络空间安全协会欢迎你的加入！群号：" + str(config.neuqcsa_group_id) + resource(poster_path))
        await bot.send_private_msg(user_id=config.admin_id, message=str(datetime.now()) + " 已向群 " + str(schedule_group_id) +" 发送 " + poster_path)

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