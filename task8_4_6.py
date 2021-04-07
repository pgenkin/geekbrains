class Warehouse:
    def __init__(self, w_name: str):
        self.w_name = w_name


class Equipment:
    def __init__(self, manufacturer: str, model: str, color_mode: str, quantity_wh: int, quantity_office):
        self.manufacturer = manufacturer
        self.model = model
        self.color_mode = color_mode
        self.quantity_wh = quantity_wh
        self.quantity_office = quantity_office

    def received_in_wh(self, new_units: int):
        self.quantity_wh += new_units

    def sent_to_office(self, sent_units: int):
        self.quantity_wh -= sent_units


class Printer(Equipment):
    def __init__(self, manufacturer: str, model: str, pr_type: str, color_mode: str, quantity_wh: int, quantity_office: int):
        super().__init__(manufacturer, model, color_mode, quantity_wh, quantity_office)
        self.pr_type = pr_type


class Copier(Equipment):
    def __init__(self, manufacturer: str, model: str, color_mode: str, quantity_wh: int, quantity_office: int, copy_speed: int):
        super().__init__(manufacturer, model, color_mode, quantity_wh, quantity_office)
        self.copy_speed = copy_speed


class Scanner(Equipment):
    def __init__(self, manufacturer: str, model: str, color_mode: str, quantity_wh: int, quantity_office: int, scan_speed: int):
        super().__init__(manufacturer, model, color_mode, quantity_wh, quantity_office)
        self.scan_speed = scan_speed




