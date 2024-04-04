from PySide6 import QtCore, QtWidgets
from instructdata import DataLoader
from .LabelWindow import Ui_Widget

class Sorter(QtWidgets.QWidget):
    def __init__(self, modelOrPath):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.dataloader = DataLoader(modelOrPath, modelOrPath.split('.')[-1])

        self.ui.jump_button.clicked.connect(self.jumpTo)
        self.ui.save_button.clicked.connect(self.saveToJson)
        self.ui.prev_button.clicked.connect(self.changeToPrev)
        self.ui.next_button.clicked.connect(self.changeToNext)

        self.lastData = self.dataloader.get()
        self.ansNum = min(len(self.lastData["output"]), 4)
        self.updateData(self.lastData)

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
        if not self.check_val_result():
            return
        data = self.dataloader.getPrev()
        if data:
            self.updateData(data)
        else:
            self.ui.idx_show.setText("No more data")

    @QtCore.Slot()
    def changeToNext(self):
        if not self.check_val_result():
            return
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
        for i in range(self.ansNum):
            self.lastData['score'][i] = self.ui.lineEdits[i].text() if self.ui.lineEdits[i].text() != '' else None

        self.ansNum = min(len(data['output']), 4)
        self.ui.idx_show.setText(str(self.dataloader.idx))
        self.ui.progressBar.setValue(self.dataloader.idx / self.dataloader.length * 100)
        self.ui.material_browser.setText(data['instruction'])
        self.ui.instruct_browser.setText(data['input'])
        for i in range(self.ansNum):
            self.ui.textBrowsers[i].setText(data['output'][i])
            self.ui.lineEdits[i].setText(data['score'][i])
        self.lastData = data

    def check_val_result(self):
        for i in range(self.ansNum):
            if not self.ui.lineEdits[i].text().isdigit() and self.ui.lineEdits[i].text() != '':
                self.ui.idx_show.setText("Invalid score")
                return False
        return True
        