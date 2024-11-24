import pyecharts
from nonebot_plugin_htmlrender import html_to_pic


async def build_pystats_chart(pypi_data: dict) -> bytes:
    """
    Build pypi stats chart
    """
    chart = pyecharts.charts.Line(
        pyecharts.options.InitOpts(
            animation_opts=pyecharts.options.AnimationOpts(animation=False)
        )
    )
    chart.add_xaxis(list(pypi_data.keys()))
    chart.add_yaxis("Downloads", list(pypi_data.values()))
    chart.set_global_opts(
        title_opts=pyecharts.options.TitleOpts(title="PyPI Stats"),
    )
    html = chart.render_embed()
    return await html_to_pic(html, viewport={"width": 512, "height": 512}, wait=5)
