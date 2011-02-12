from elixir import *
import datetime

NAME = 0
class Tag(Entity):
    id = Field(Integer, primary_key=True)
    name = Field(String(100), required=True)

    using_options(tablename="tags")
    notes = ManyToMany("Note")
