# -*- coding: utf-8 -*-  
#       Copyright 2010 Anna Stępień <solitaire at g.pl>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

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