import svgwrite

class Drawer:
    def __init__(self, file_name):
        self.drawer = svgwrite.Drawing(file_name + '.svg', profile='full')

    def get(self):
        return self.drawer

    def save(self):
        self.drawer.save()


class Agent(Drawer):
    def __init__(self, drawer):
        self.drawer = drawer

    def draw_element(self, drawer, design, cursor, text):
        if cursor.draw_area == 'name':
            self.width = design.name_width
        elif cursor.draw_area == 'type':
            self.width = design.type_width

        drawer.add(
            drawer.rect(
                insert=(cursor.rect_pos_x, cursor.rect_pos_y),
                size=(self.width, design.rect_height),
                fill=design.fill,
                stroke=design.stroke,
                style=design.rect_style))
        drawer.add(
            drawer.text(
                text,
                insert=(cursor.rect_pos_x + design.text_padding_left,
                        cursor.rect_pos_y + design.text_padding_top),
                style=design.text_style))


