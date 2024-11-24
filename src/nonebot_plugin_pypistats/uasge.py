import inspect

usage = inspect.cleandoc(
    """
快速开始：
/下载统计 <包名>
如：/下载统计 pillow

高级用法：
/下载统计 <包名> -n|--nb <p|a> -t|--type <overall|recent>

参数说明：
-n |--nb  : 包类型，p为插件，a为适配器
-t |--type : 统计类型，overall为总下载量，recent为最近下载量
"""
)
