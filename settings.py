from pydantic import BaseModel
from cat.mad_hatter.decorators import plugin
from enum import Enum


class DataSource(Enum):
    a: str = 'sqlite'
    b: str = 'postgresql'
    c: str = 'mysql'


# settings
class DatabaseSettings(BaseModel):

    data_source: DataSource

    host: str
    port: str

    username: str
    password: str

    database: str

    allowed_tables: str

    character_encoding: str = "utf8"


@plugin
def settings_schema():
    return DatabaseSettings.schema()
