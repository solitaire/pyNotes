from elixir import *

NAME = 0
class Notebook(Entity):

    id   = Field(Integer, primary_key=True)
    name = Field(String(100), required=True)

    using_options(tablename="notebooks")
    notes = OneToMany("Note")