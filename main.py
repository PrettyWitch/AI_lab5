from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QStandardItemModel, QStandardItem
import xlrd as xlrd

class Search:
    def __init__(self):
        # Load UI definition from file
        qfile_stats = QFile('lab5.ui')
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        self.ui = QUiLoader().load(qfile_stats)
        self.model = QStandardItemModel(4, 10)
        self.ui.tableView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(['name', 'id', 'Import', 'weight', 'price',
                                              'discount', 'shelfLife', 'sweetness', 'hardness', 'food'])
        self.ui.button1.clicked.connect(self.search)

        date = self.readData()
        values = date[0]
        nrows = date[1]
        ncols = date[2]

        # 设置表格行高列宽
        self.ui.tableView.resizeRowsToContents()
        # self.ui.tableView.setColumnWidth(0, 30)
        for column in range(ncols - 4):
            self.ui.tableView.setColumnWidth(column, 70)
        self.ui.tableView.setColumnWidth(7, 120)
        self.ui.tableView.setColumnWidth(8, 100)
        self.ui.tableView.setColumnWidth(9, 70)


    def readData(self):
        # Read table data
        book = xlrd.open_workbook('fruit.xlsx')
        sheet1 = book.sheets()[0]
        nrows = sheet1.nrows
        ncols = sheet1.ncols
        values = []
        for row in range(nrows):
            row_values = sheet1.row_values(row)
            values.append(row_values)
        return values, nrows, ncols

    def search(self):
        # global history
        data = self.readData()
        nrows = data[1]
        values = data[0]
        ncols = data[2]
        # 获取搜索值
        price_floor = int(self.ui.lineEdit.text())
        price_cell = int(self.ui.lineEdit_2.text())
        discount_floor = int(self.ui.lineEdit_3.text())
        discount_cell = int(self.ui.lineEdit_4.text())
        print(price_floor, price_cell)

        # Use dictionary to store line number and price information
        dict = {}
        # 判断字典是否为空，如果空则扩大搜索范围
        price_floor_1 = price_floor
        price_cell_1 = price_cell
        discount_floor_1 = discount_floor
        discount_cell_1 = discount_cell
        while not bool(dict):
            for row in range(1, nrows):
                # 条件搜索，记录行号和价格
                if (values[row][5] > price_floor_1) & (values[row][5] < price_cell_1) & \
                        (values[row][6] > discount_floor_1) & (values[row][6] < discount_cell_1):
                    row_num = row
                    price_num = values[row][5]
                    discount_num = values[row][6]
                    dict[row_num] = [price_num, discount_num]
                else:
                    continue
            price_floor_1 -= 20
            price_cell_1 += 20
            discount_floor_1 -= 10
            discount_cell_1 += 10
        print(dict)
        # 记录有几个match
        newDis = {}
        for k, v in dict.items():
            # match = 0
            newDis[k] = 0
            if (v[0] > price_floor) & (v[0] < price_cell):
                # match += 1
                newDis[k] += 1
            if (v[1] > discount_floor) & (v[1] < discount_cell):
                # match += 1
                newDis[k] += 1
        print(newDis)
        # Dictionary sort 排序
        newDis_1 = sorted(newDis.items(), key=lambda d: d[1], reverse=True)
        print(newDis_1)
        # index记录下标（行号）
        index = {}
        for i in range(len(newDis_1)):
            index[i] = int(newDis_1[i][0])
        for row in range(len(index)):
            for col in range(1, ncols):
                item = QStandardItem('%s' % values[index[row]][col])
                self.model.setItem(row, col - 1, item)
                self.ui.tableView.resizeRowsToContents()


app = QApplication([])
search = Search()
search.ui.show()
app.exec_()