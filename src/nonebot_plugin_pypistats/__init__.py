import httpx

from nonebot import require
from nonebot.plugin import inherit_supported_adapters
require("nonebot_plugin_alconna")
from nonebot_plugin_alconna import Alconna, Args, on_alconna, Match
from nonebot.plugin import PluginMetadata


__plugin_meta__ = PluginMetadata(
    name="PyPi下载统计",
    description= "查询结果由pypistats提供， 数据是否可信需自己判断",
    usage= "发送：下载统计 [包名] [类型]即可获取",
    type= "application",
    homepage= "https://github.com/zhongwen-4/nonebot-plugin-pypistats",
    supported_adapters= inherit_supported_adapters("nonebot_plugin_alconna")
)


get_stats = on_alconna(
    Alconna(
        "下载统计", Args["name?", str]["nb?", str]
    )
)

@get_stats.handle()
async def _(name: Match[str], nb: Match[str]):
    if name.available:
        if nb.available:
            if nb.result == "p":
                _name = f"nonebot_plugin_{name.result}"
            
            elif nb.result == "a":
                _name = f"nonebot_adapter_{name.result}"

            else:
                _name = name.result

        else:
            _name = name.result

        async with httpx.AsyncClient() as client:
            stats = await client.get(f"https://pypistats.org/api/packages/{_name}/recent")
            if stats.status_code == 200:
                stats = stats.json()
            
            else:
                await get_stats.finish("获取失败，请检查包名是否正确")

        last_day = stats["data"]["last_day"]
        last_week = stats["data"]["last_week"]
        last_month = stats["data"]["last_month"]

        msg = [
            f"{_name}的下载统计：",
            f"昨日下载：{last_day}次",
            f"近7日下载：{last_week}次",
            f"近30日下载：{last_month}次"
        ]

        await get_stats.finish("\n".join(msg))
    
    await get_stats.finish("没有包名怎么查")