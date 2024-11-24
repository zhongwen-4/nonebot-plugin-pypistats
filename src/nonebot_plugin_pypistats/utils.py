import httpx

from typing import Dict, Any
from nonebot.matcher import Matcher
from nonebot_plugin_alconna import Match


class PyPiStats:
    def __init__(self):
        self.client = httpx.AsyncClient()
        self.api_url = "https://pypistats.org/api/packages/"

    async def get_statistics(
        self, package_name: str, endpoint: str, **args
    ) -> Dict[str, Any]:
        """
        获取包的统计信息
        :param package_name: 包名
        :return: 包的统计信息
        """
        stats = await self.client.get(
            f"{self.api_url}{package_name}/{endpoint}", params=args
        )

        if stats.status_code == 200:
            return stats.json()
        else:
            raise Exception("获取包的统计信息失败")

    async def get_recent_stats(self, package_name: str) -> Dict[str, Any]:
        """
        获取包的最近统计信息
        :param package_name: 包名
        :return: 包的最近统计信息
        """
        return await self.get_statistics(package_name, "recent")

    async def get_overall_stats(
        self, package_name: str, mirros=False
    ) -> Dict[str, Any]:
        """
        获取最近的统计信息
        :param package_name: 包名
        :return: 包的一段时间内的统计信息
        """
        return await self.get_statistics(package_name, "overall", mirros=mirros)


async def val_name(matcher: Matcher, name: Match[str], nb: Match[str]) -> str:
    if not name.available:
        await matcher.finish("请输入包名")
    if nb.available:
        if nb.result == "p":
            _name = f"nonebot_plugin_{name.result}"

        elif nb.result == "a":
            _name = f"nonebot_adapter_{name.result}"

        else:
            _name = name.result

    else:
        _name = name.result

    return _name
