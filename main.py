import sys
from PySide6 import QtWidgets
from instructdata import Sorter

data_path = "./data/train.json"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = Sorter(data_path)
    widget.resize(800, 600)
    widget.show()
    app.exec()
    print("idx: ", widget.dataloader.idx)
    sys.exit()