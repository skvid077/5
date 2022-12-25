import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sqlite3


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.btn.clicked.connect(self.btn_click)
        self.add.clicked.connect(self.add_click)
        self.edit.clicked.connect(self.edit_click)

    def btn_click(self):
        db = sqlite3.connect('data/coffee.sqlite')
        cur = db.cursor()
        coffee = cur.execute("""SELECT * FROM cof""").fetchall()
        for i in coffee:
            self.lst.addItem(' '.join(list(map(str, list(i)))))

    def add_click(self):
        self.a = Add_entry()
        self.a.show()

    def edit_click(self):
        self.a = Edit_entry()
        self.a.show()


class Add_entry(QMainWindow):

    def __init__(self):
        super(Add_entry, self).__init__()
        self.setWindowTitle('add')
        uic.loadUi('UI/untitled1.ui', self)
        self.add.clicked.connect(self.add_click)

    def add_click(self):
        db = sqlite3.connect('data/coffee.sqlite')
        cur = db.cursor()
        cur.execute('INSERT INTO cof(sort, roast, price, volume, flavor, type) VALUES(?, ?, ?, ?, ?, ?);',
                    (str(self.sort.text()), str(self.roast.text()), int(self.price.text()),
                     int(self.volume.text()), str(self.flavor.text()), str(self.type.text()),))
        db.commit()


class Edit_entry(QMainWindow):

    def __init__(self):
        super(Edit_entry, self).__init__()
        self.setWindowTitle('edit')
        uic.loadUi('UI/untitled2.ui', self)
        self.edit.clicked.connect(self.edit_click)
        self.search.clicked.connect(self.search_click)

    def edit_click(self):
        db = sqlite3.connect('data/coffee.sqlite')
        cur = db.cursor()
        cur.execute('UPDATE cof SET sort = ?, roast = ?, price = ?, volume = ?, flavor = ?, type = ? WHERE ID = ?;',
                    (str(self.sort.text()), str(self.roast.text()), int(self.price.text()),
                     int(self.volume.text()), str(self.flavor.text()), str(self.type.text()), int(self.ID.text())))
        db.commit()

    def search_click(self):
        db = sqlite3.connect('data/coffee.sqlite')
        cur = db.cursor()
        z = cur.execute(f'SELECT * FROM cof WHERE ID = {int(self.ID.text())};').fetchone()
        z = z[1:]
        self.sort.setText(str(z[0]))
        self.roast.setText(str(z[1]))
        self.price.setText(str(z[2]))
        self.volume.setText(str(z[3]))
        self.flavor.setText(str(z[4]))
        self.type.setText(str(z[5]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
