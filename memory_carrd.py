from PyQt5.QtCore import Qt 
from PyQt5.OtWidget import( 
    QApplication, QWidget, QTableWidget, QListWidget, 
     QLineEdit, QFormLoyout, QHBoxLayout, 
      QVBoxLayout, QGroupBox, QButtonGroup, 
      QPushButton, QLabel, QRadioButton, QSpinBox)
from Ryabii import *

list_question = QListView()
widget_ans= QWidget()
widget.setLayout(layout_form)
btn_add = QPushButton("New Question")
btn_del = QPushButton("del question")
btn_start=QPushButton("START")

qst_col= QVBoxLayout()
qst_col.addWidget(list_question)
qst_col.addWidget(btn_add)

ans_col = QVBoxLayout()
ans_col.addWidget(widget_ans)
ans_col.addWidget(btn_del)

btn_line = QHBoxLayout
btn_line.addLayout(qst_col)
btn_line.addLayout(ans_col)

test_line=QHBoxLayout()
test_line.addWidget((btn_start, alignment=(QT.AlignHCentre|Qt.AlignVCenter)))

Layout_screen = QVBoxLayout()
Layout_screen.addLayout(btn_line)
Layout_screen.addLayout(test_line)