<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-pypistats

_✨ 通过机器人查看PyPi包的下载次数 ✨_

</div>

一个通过nonebot与pypistats对接实现的下载量查询插件

> [!IMPORTANT]
> 数据是否可信请自行判断


## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-pypistats

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-pypistats
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-pypistats
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-pypistats
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-pypistats
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_pypistats"]

</details>

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 下载统计 [包名] [类型] | all | 否 | all | 类型选项有p：nonebot-plugin-和a: nonebot-adapter-两种，如果不写参数的话那就是直接查询|

### 指令例子

<details>
<summary>点击展开</summary>

![图一](./img/stats1.png)
![图二](./img/stats2.png)

</details>