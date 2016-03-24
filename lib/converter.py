class Converter:
    def __init__(self, table_names, key_types, column_names, column_types):
        self.table_dict = {}
        self.table_names = table_names
        self.key_types = key_types
        self.column_names = column_names
        self.column_types = column_types

    def convert(self):
        for table_name in self.table_names:
            self.name_element = []
            self.type_element = []

            self.name_element.append(table_name)
            self.name_element.extend(self.column_names[table_name])
            self.type_element.append(self.key_types[table_name]['name'])

            for column_name in self.column_names[table_name]:
                self.type_element.append(self.column_types[table_name][column_name]['name'])

            self.table_dict[table_name] = [self.name_element, self.type_element]

        return self.table_dict


