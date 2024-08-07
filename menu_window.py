from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QRadioButton, \
    QPushButton, QLabel, QSpinBox, QButtonGroup, QGroupBox, QApplication, QLineEdit
from PyQt5.QtCore import Qt

menu_w = QWidget()
lb_question = QLabel("Введіть запитання:")
lb_right_ans = QLabel("Введіть вірну відповідь:")
lb_wrong1_ans = QLabel("Введіть першу хибну відповідь:")
lb_wrong2_ans = QLabel("Введіть другу хибну відповідь:")
lb_wrong3_ans = QLabel("Введіть третю хибну відповідь:")

le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong1_ans = QLineEdit()
le_wrong2_ans = QLineEdit()
le_wrong3_ans = QLineEdit()

lb_heat_stat = QLabel("Статистика")
lb_heat_stat.setStyleSheet("font-size: 19px; font-weight: bold;")

lb_statistic = QLabel()

v1_labels = QVBoxLayout()
v1_labels.addWidget(lb_question)
v1_labels.addWidget(lb_right_ans)
v1_labels.addWidget(lb_wrong1_ans)
v1_labels.addWidget(lb_wrong2_ans)
v1_labels.addWidget(lb_wrong3_ans)

v1_lineEdits = QVBoxLayout()
v1_lineEdits.addWidget(le_question)
v1_lineEdits.addWidget(le_right_ans)
v1_lineEdits.addWidget(le_wrong1_ans)
v1_lineEdits.addWidget(le_wrong2_ans)
v1_lineEdits.addWidget(le_wrong3_ans)

h1_question = QHBoxLayout()
h1_question.addLayout(v1_labels)
h1_question.addLayout(v1_lineEdits)

btn_back = QPushButton("Назад")
btn_add_ques = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")

h1_buttons = QHBoxLayout()
h1_buttons.addWidget(btn_add_ques)
h1_buttons.addWidget(btn_clear)

v1_res = QVBoxLayout()
v1_res.addLayout(h1_question)
v1_res.addLayout(h1_buttons)
v1_res.addWidget(lb_heat_stat)
v1_res.addWidget(lb_statistic)
v1_res.addWidget(btn_back)

menu_w.setLayout(v1_res)
menu_w.resize(400, 300)

