from nonebot import require
from nonebot.plugin import inherit_supported_adapters

require("nonebot_plugin_alconna")
require("nonebot_plugin_htmlrender")
require("nonebot_plugin_localstore")
from nonebot_plugin_alconna import Alconna, Args, on_alconna, Match, Option
from nonebot.plugin import PluginMetadata
from nonebot.matcher import Matcher
from nonebot_plugin_alconna.uniseg import UniMessage, Image, Text

from .utils import PyPiStats, val_name
from .render import build_pystats_chart
from .uasge import usage

__plugin_meta__ = PluginMetadata(
    name="PyPi下载统计",
    description="查询结果由pypistats提供， 数据是否可信需自己判断",
    usage=usage,
    type="application",
    homepage="https://github.com/zhongwen-4/nonebot-plugin-pypistats",
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_alconna"
    ),
)

pypistats = PyPiStats()

get_stats = on_alconna(
    Alconna(
        "下载统计",
        Args["name?", str],
        Option("-n|--nb", Args["nb", str]),
        Option("-t|--type", Args["t", str]),
    ),
    use_cmd_start=True,
    block=True,
    priority=1,
)


@get_stats.handle()
async def _(matcher: Matcher, name: Match[str], nb: Match[str], t: Match[str]):
    if not name.available:
        await get_stats.finish(usage, reply_message= True)

    _name = await val_name(matcher, name, nb)

    d = {}
    msg = UniMessage("pypistats查询信息：\n")

    if t.result == "overall":
        stats = await pypistats.get_overall_stats(_name)
        for i in stats["data"]:
            if i["category"] == "without_mirrors":
                d[i["date"]] = i["downloads"]
        msg += Image(raw= await build_pystats_chart(d))

    else:
        stats = await pypistats.get_recent_stats(_name)
        try:
            last_day = stats["data"]["last_day"]
            last_week = stats["data"]["last_week"]
            last_month = stats["data"]["last_month"]
        except KeyError:
            await get_stats.finish("查询失败，请检查包名是否正确", reply_message= True)

        msg += Text(
            "\n".join(
                [
                    f"{_name}的下载统计：",
                    f"昨日下载：{last_day}次",
                    f"近7日下载：{last_week}次",
                    f"近30日下载：{last_month}次",
                ]
            )
        )

    await msg.finish(reply=True)
