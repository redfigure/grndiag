#!/usr/bin/env python

from lib.collector import *

from lib import Loader
from lib import Collector
from lib import Converter
from lib import Designer
from lib import Cursor
from lib import Drawer, Agent


if __name__ == '__main__':
    load = Loader('http://localhost:10042/d/schema')

    tables = Collector(tables(load.schema))
    key_types = Collector(key_types(load.schema, tables.collect))
    columns = Collector(columns(load.schema, tables.collect))
    column_types = Collector(column_types(load.schema, tables.collect, columns.collect))

    converter = Converter(tables.collect,
                            key_types.collect,
                            columns.collect,
                            column_types.collect)
    element_box = converter.convert()

    design = Designer()
    cursor = Cursor(design)
    drawer = Drawer('sample')
    agent = Agent(drawer)

    for table_name in element_box:
        design.adjust(element_box[table_name])
        for table_element in element_box[table_name]:
            for text in table_element:
                agent.draw_element(drawer.get(), design, cursor, text)
                cursor.move('row', design.rect_height)
            cursor.move('column', design.name_width)
        cursor.move('table', design.type_width)


    agent.save()
