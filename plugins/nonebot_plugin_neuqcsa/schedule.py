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
        poster_path = "CTF海报.png"
        
        text_content = (
            "🎉 网络空间安全协会招新开始啦！🎉\n"
            "\n"
            "😎 加入我们，开启黑客之旅！😎\n"
            "💪 从Web攻防到算法破解，技能树全面点亮\n"
            "🧨 从漏洞挖掘到渗透测试，实战经验满满\n"
            "🕹️ 从竞赛获奖到科创加分，收获超乎想象\n"
            "\n"
            "🎭 参加黑客夏令营，揭开网络安全的神秘面纱\n"
            "⚔️ 本轮招新将在军训后正式启动，期待在赛场上见证你的锋芒！\n"
            "\n"
            "⚠️ 进群后请密切关注群公告，不错过任何重要通知！\n"
            f"👉 加群开启黑客之旅：{config.neuqcsa_group_id}\n"
            "🌐 官网了解更多：https://www.neuqcsa.cn\n"
            "\n"
            "✨ 无论零基础还是大佬，我们都欢迎你的加入！✨"
        )
        
        from nonebot.adapters.onebot.v11 import Message, MessageSegment
        
        msg = Message([
            MessageSegment.text(text_content),
            MessageSegment.image(file=resource(poster_path))
        ])
        
        await bot.send_group_msg(group_id=schedule_group_id, message=msg)
<<<<<<< HEAD
        # for superuser in config.superusers:
        #     await bot.send_private_msg(user_id=superuser, message=str(datetime.now()) + " 已向群 " + str(schedule_group_id) + " 发送 " + poster_path)
=======
        for superuser in config.superusers:
            await bot.send_private_msg(user_id=superuser, message=str(datetime.now()) + " 已向群 " + str(
            schedule_group_id) + " 发送 " + poster_path)
>>>>>>> parent of 0a8c2e5 (Chore: reformat code)

# 定时任务，基于装饰器的方式
# @scheduler.scheduled_job("cron", hour=8, id="job_8", misfire_grace_time=None)
async def task_8():
    await send_poster()
# @scheduler.scheduled_job("cron", hour=14, id="job_14", misfire_grace_time=None)
async def task_14():
    await send_poster()
# @scheduler.scheduled_job("cron", hour=19, id="job_19", misfire_grace_time=None)
async def task_19():
    await send_poster()

# 在每天的 11、13、15、17、19、21 点发一次
@scheduler.scheduled_job("cron", hour="11-21/2", id="cron_job", misfire_grace_time=None)
async def cron_task():
    await send_poster()

# 启动时输出定时任务
for job in scheduler.get_jobs():
    logger.info(job)
