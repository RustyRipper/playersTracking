from PySide6.QtCore import QObject, Slot


class MainController(QObject):

    def __init__(self, model):
        super().__init__()
        self.model = model

    @Slot()
    def doSomething(self):
        pass