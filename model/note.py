from elixir import *
import datetime

TITLE, NOTEBOOK, CREATED_AT, UPDATED_AT, BODY, TAGS = range(6)

class Note(Entity):

    id    = Field(Integer, primary_key=True)
    title = Field(String(100), default="title")
    body  = Field(Text, default="body")
    created_at = Field(DateTime, default=datetime.datetime.now)
    updated_at = Field(DateTime, default=datetime.datetime.now)

    using_options(tablename="notes")
    notebook = ManyToOne("Notebook")
    tags = ManyToMany("Tag")