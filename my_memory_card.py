from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox, QRadioButton, QHBoxLayout,QButtonGroup
from random import shuffle

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(600,400)

text = QLabel('Сколько всего стран?')

RadioGroupBox = QGroupBox('Варианты ответов')

btn1 = QRadioButton('193')
btn2 = QRadioButton('195')
btn3 = QRadioButton('150')
btn4 = QRadioButton('200')

knopka = QPushButton('Ответить')
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

lineHor1 = QHBoxLayout()
lineHor2 = QVBoxLayout()
lineHor3 = QVBoxLayout()


lineHor2.addWidget(btn1)
lineHor2.addWidget(btn2)
lineHor3.addWidget(btn3)
lineHor3.addWidget(btn4)
lineHor1.addLayout(lineHor2)
lineHor1.addLayout(lineHor3)

RadioGroupBox.setLayout(lineHor1)

line1 = QHBoxLayout()
line1.addWidget(text, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line2 = QHBoxLayout()
line2.addWidget(RadioGroupBox)


line3 = QHBoxLayout()
line3.addWidget(knopka, alignment=(Qt.AlignHCenter | Qt.AlignVCenter),stretch = 2)

glav = QVBoxLayout()
glav.addLayout(line1)
glav.addLayout(line2)
glav.addLayout(line3)

main_win.setLayout(glav)


AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
itog = QLabel('Правильный ответ')

class Question():
    def __init__(self,question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    knopka.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    knopka.setText('Ответить')
    RadioGroup = QButtonGroup()
    RadioGroup.addButton(btn1)
    RadioGroup.addButton(btn2)
    RadioGroup.addButton(btn3)
    RadioGroup.addButton(btn4)
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)
def test():
    if 'Ответить' == knopka.text():
        show_result()
    else:
        show_question()
answer = [btn1, btn2, btn3, btn4]   
def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    itog.setText(q.right_answer)
    show_question()
def show_correct(res):
    result.setText(res)
    show_result()
def scheck_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно')
def next_question():
    main_win.cur_question += 1#переход на следующий слайд
    if main_win.cur_question > len(question_list):
        main_win.cur_question = 0 #если список вопросов больше , то сначала 
    q = question_list[main_win.cur_question] 
    ask(q)
def click_ok():
    if knopka.text() == 'Ответить':
        scheck_answer()
    else:
        next_question()

main_win.cur_question = -1
question_list = []
q7= Question('Сколько всего стран?', '195', '193', '150', '200')
question_list.append(q7)
q1 = Question('Кто мало платит губке Бобу?', 'Мистер Крабс', 'Сенди', 'Гери', 'Патрик')
question_list.append(q1)
q2 = Question('Сколько мне лет?', '15', '14', '12', '16')
question_list.append(q2)
q3 = Question('Сколько пероснажей в Dota 2?', '124', '119', '150', '200')
question_list.append(q3)
q4 = Question('Сколько денег вы мне скинете?', '1000', '300', '100', '500')
question_list.append(q4)
q5 = Question('Сколько длилась 2 мировая война?', '6', '10', '1', '2')
question_list.append(q5)
q6 = Question('Какая моя любима видеоигра?', 'Майнкрафт', 'Роблокс', 'Дота2', 'Субнатика')
question_list.append(q6)
q8 = Question('Когда появился Ютуб?', '2004', '2005', '2009', '2010')
question_list.append(q8)
q9 = Question('Сколько скилов в Дота2?', '431', '4004', '150', '300')
question_list.append(q9)
q10 = Question('Когда майнкрафт был создан?', '2009', '2011', '2010', '2003')
question_list.append(q10)
q11 = Question('Когда был создан роблокс?', '2005', '2011', '2003', '2007')
question_list.append(q11)
q12 = Question('Год отмены крепостного права?', '1861', '1823', '1890', '2000')
question_list.append(q12)
q13 = Question('Год крещения Руси?', '988', '982', '990', '984')
question_list.append(q13)
q14 = Question('Насколько хорош этот опрос?', '10/10', '8/10', '3/10', '1/10')
question_list.append(q14)


layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(itog, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line2.addWidget(AnsGroupBox)
RadioGroupBox.setLayout(lineHor1)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
knopka.clicked.connect(click_ok)

main_win.show()
app.exec_()