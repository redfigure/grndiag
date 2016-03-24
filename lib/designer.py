class Designer:
    def __init__(self):

        self.name_width = 0
        self.type_width = 0

        self.rect_height = 30

        self.text_padding_left = 5
        self.text_padding_top = self.rect_height / 2

        self.fill = 'white'
        self.stroke = 'black'
        self.rect_style = 'stroke-width: 2'

        self.text_style = 'font-size: 1em; dominant-baseline: middle;'

    def adjust(self, table_element):
        self.max_name_length = max([len(text) for text in table_element[0]])
        self.max_type_length = max([len(text) for text in table_element[1]])

        # TODO: fix the accurate size
        self.name_width = self.max_name_length * 10
        self.type_width = self.max_type_length * 10


