from pydantic import BaseModel
from nonebot import get_driver, get_plugin_config


class ScopedConfig(BaseModel):
    visualization: bool = True
    image_scale: float = 1.0


class Config(BaseModel):
    pypistats: ScopedConfig = ScopedConfig()


global_config = get_driver().config
plugin_config = get_plugin_config(Config).pypistats
