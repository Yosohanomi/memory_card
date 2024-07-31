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
