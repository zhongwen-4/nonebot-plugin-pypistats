import httpx

from typing import Dict,Any

plugin_client = httpx.AsyncClient()

async def got_statistics(package_name: str)-> Dict[str,Any]:
    """
    获取包的统计信息
    :param package_name: 包名
    :return: 包的统计信息
    """
    stats = await plugin_client.get(f"https://pypistats.org/api/packages/{package_name}/recent")

    if stats.status_code == 200:
        return stats.json()
    else:
        return {"data": -1}
