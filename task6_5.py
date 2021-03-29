class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Drawing now.")


class Pen(Stationery):

    def __init__(self, title: str):
        super().__init__(title)
        self.title = title

    def draw(self):
        print(f"Drawing with a {self.title} now. Enjoy!")


class Pencil(Stationery):

    def __init__(self, title: str):
        super().__init__(title)
        self.title = title

    def draw(self):
        print(f"Drawing with a {self.title} now. Have fun!")


class Handle(Stationery):

    def __init__(self, title: str):
        super().__init__(title)
        self.title = title

    def draw(self):
        print(f"Drawing with a {self.title} now. Great work!")


test_draw_1 = Pen("pen")
test_draw_1.draw()
test_draw_2 = Pencil("pencil")
test_draw_2.draw()
test_draw_3 = Handle("handle")
test_draw_3.draw()
