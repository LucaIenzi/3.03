import ui
from numpy import random

computer_op = random.randint(1,3)

user_ans = None
computer_ans = None

if (computer_op == 1) :
     computer_ans = 'rock'
elif (computer_op == 2):
    computer_ans = 'paper'
elif   (computer_op == 3):
    computer_ans = 'sizers'



def rock_touch_up_inside (sender):
    user_ans = str('rock')

def paper_touch_up_inside (sender):
    user_ans = str('paper')

def sizers_touch_up_inside (sender):
    user_ans = str('sizers')



if computer_ans == str('rock') and user_ans == str('rock'):
    view['answer_lable'].text = ("tie")
elif computer_ans == str('rock') and user_ans == str('paper'):
    view['answer_lable'].text = ("you win")
elif computer_ans == str('rock') and user_ans == str('sizers'):
    view['answer_lable'].text = ("you lose")
elif computer_ans == str('paper') and user_ans == str('paper'):
    view['answer_lable'].text = ("tie")
elif computer_ans == str('paper') and user_ans == str('rock'):
    view['answer_lable'].text = ("you lose")
elif computer_ans == str('paper') and user_ans == str('sizers'):
    view['answer_lable'].text = ("you win")
elif computer_ans == str('sizers') and user_ans == str('sizers'):
    view['answer_lable'].text = ("tie")
elif computer_ans == str('sizers') and user_ans == str('paper'):
    view['answer_lable'].text = ("you lose")
elif computer_ans == str('sizers') and user_ans == str('sizers'):
    view['answer_lable'].text = ("you win")


view = ui.load_view()
view.present('sheet')
