class Collector:
    def __init__(self, collector):
        self.collect = collector

def tables(schema):
    table_list = []

    for table_name in schema.keys():
        table_list.append(table_name)

    return table_list

def columns(schema, table_names):
    column_dict = {}

    for table_name in table_names:
        column_list = []

        for column_name in schema[table_name]['columns'].keys():
            column_list.append(column_name)

        column_dict[table_name] = column_list

    return column_dict

def key_types(schema, table_names):
    key_type_dict = {}

    for table_name in table_names:
        key_type_dict[table_name] = schema[table_name]['key_type']

    return key_type_dict

def column_types(schema, table_names, column_names):
    column_type_dict = {}
    for table_name in table_names:
        column_type_dict[table_name] = {}
        for column_name in column_names[table_name]:
            column_type_dict[table_name][column_name] = schema[table_name]['columns'][column_name]['value_type']

    return column_type_dict

