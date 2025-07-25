# NEUQCSA-bot
用于协会招新宣传，兼具便民查询和娱乐功能的兔兔机器人

## 快速运行

1. 安装 [Python](https://www.python.org/) 3.9 及以上版本

   你可能还需要更换 pypi 源以获得更好的体验。可以参考：https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

2. 安装 NoneBot

   1. 确保已经卸载可能存在的 NoneBot v1：
      ```shell
      pip uninstall nonebot
      ```

   2. 安装 pipx：
      ```shell
      python -m pip install --user pipx
      python -m pipx ensurepath
      ```

      执行完后，请重新打开一个新的终端。

   3. 安装脚手架：
      ```shell
      pipx install nb-cli
      ```

3. 创建新项目

   选择一个工作目录打开终端，执行：
   ```shell
   nb create
   ```

   你将会看到一些询问，请如下输入：
   ```nb-cli
   [?] 选择一个要使用的模板: simple (插件开发者)
   [?] 项目名称: NEUQCSA-bot
   [?] 要使用哪些适配器? OneBot V11 (OneBot V11 协议)
   [?] 要使用哪些驱动器? websockets (websockets 驱动器)
   [?] 请输入插件存储位置: 2) 在 "src" 文件夹中
   [?] 立即安装依赖? Yes
   [?] 创建虚拟环境? n
   [?] 要使用哪些内置插件?
   ```

   在这里创建新项目只是为了自动安装所需的依赖。接下来请删除当前 `NEUQCSA-bot` 文件夹的全部内容，然后 Clone 本项目或 Download ZIP，将本项目的所有文件放置进来。

4. 安装 `nonebot-plugin-apscheduler` 插件至项目环境中

   在**本项目目录 `NEUQCSA-bot`** 下执行以下命令：

   ```shell
   nb plugin install nonebot-plugin-apscheduler
   ```

5. 修改 dotenv 配置文件

   配置文件为 `.env.prod`，请根据实际修改。默认配置如下：
   ```env
   DRIVER=~websockets
   
   SUPERUSERS=["123456789"] # 主人号
   NEUQCSA_GROUP_ID=101796777 # 招新群号
   SCHEDULE_GROUP_IDS=[102383053, 333291684] # 新生群号
   NO_QRCODE_GROUP_IDS=[333291684] # 禁止发送二维码的群号
   ```

6. [配置 OneBot 协议实现端与 NoneBot 的连接](https://onebot.adapters.nonebot.dev/docs/guide/setup/)

   协议实现端推荐使用 [LLOneBot](https://llonebot.com/zh-CN/guide/getting-started)。例如在 LLOneBot 的 `wsReverseUrls` 中添加 `ws://localhost:8080/onebot/v11/ws` 即可完成配置。

7. 启动
   ```shell
   cd NEUQCSA-bot
   nb run
   ```
