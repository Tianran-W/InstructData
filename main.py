import sys
from PySide6 import QtCore, QtWidgets, QtGui
from utils.DataLoader import DataLoader
from configs.colors import get_rgb
from gui.LabelWindow import Ui_Widget

class DiscreteScore(QtWidgets.QWidget):
    def __init__(self, data_path):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.dataloader = DataLoader(data_path, data_path.split('.')[-1])

        self.ui.jump_button.clicked.connect(self.jumpTo)
        self.ui.save_button.clicked.connect(self.saveToJson)
        self.ui.prev_button.clicked.connect(self.changeToPrev)
        self.ui.next_button.clicked.connect(self.changeToNext)

    @QtCore.Slot()
    def jumpTo(self):
        if not self.ui.lineEdit.text().isdigit():
            self.ui.idx_show.setText("Invalid index")
            return
        idx = int(self.ui.lineEdit.text())
        data = self.dataloader.get(idx)
        if data is not None:
            self.updateData(data)
            self.ui.lineEdit.setText("")
        else:
            self.ui.idx_show.setText("Index out of range")

    @QtCore.Slot()
    def saveToJson(self):
        self.dataloader.save()

    @QtCore.Slot()
    def changeToPrev(self):
        data = self.dataloader.getPrev()
        if data:
            self.updateData(data)
        else:
            self.ui.idx_show.setText("No more data")

    @QtCore.Slot()
    def changeToNext(self):
        data = self.dataloader.getNext()
        if data:
            self.updateData(data)
        else:
            self.ui.idx_show.setText("No more data")

    @QtCore.Slot()
    def refresh(self):
        data = self.dataloader.get()
        if data:
            self.updateData(data)
        else:
            self.ui.idx_show.setText("No more data")

    def updateData(self, data):
        self.ui.idx_show.setText(str(self.dataloader.idx))
        self.ui.progressBar.setValue(self.dataloader.idx / self.dataloader.length * 100)
        self.ui.material_browser.setText(data['instruction'])
        self.ui.instruct_browser.setText(data['input'])
        self.ui.textBrowser_1.setText(data['output'])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = DiscreteScore("./data/train.json")
    widget.resize(800, 600)
    widget.show()
    app.exec()
    print("idx: ", widget.dataloader.idx)
    sys.exit()