class Cursor:
    def __init__(self, designer):
        self.draw_area = 'name'
        self.rect_pos_x = 0
        self.rect_pos_y = 0
        self.text_pos_x = 0
        self.text_pos_y = 0
        self.text_pos_base = 0
        self.table_height = 0

    def move(self, direction, amount):
        if direction == 'row':
            self.__move_row(amount)
        elif direction == 'column':
            self.__move_column(amount)
        elif direction == 'table':
            self.__move_table(amount)
        # else:
        #     raise

    def __move_row(self, amount):
        self.rect_pos_y += amount

    def __move_column(self, amount):
        self.draw_area = 'type'
        self.rect_pos_y = 0
        self.rect_pos_x += amount
        self.text_pos_x += amount
        self.text_pos_y = self.text_pos_base

    def __move_table(self, amount):
        self.draw_area = 'name'
        self.rect_pos_y = 0
        self.rect_pos_x += amount + 100
        self.text_pos_x += amount + 100
        self.text_pos_y = self.text_pos_base


