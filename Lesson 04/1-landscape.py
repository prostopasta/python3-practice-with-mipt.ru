# подключение библиотеки под синонимом gr
import graphics as gr

# Инициализация окна с названием и размером 600х400 пикселей
window = gr.GraphWin("Task 1 - Landscape", 600, 400)

sky = gr.Rectangle(gr.Point(0, 0), gr.Point(600, 200))
sky.setFill("blue")

sun = gr.Circle(gr.Point(450, 80), 50)
sun.setFill('yellow')

cloud1 = gr.Circle(gr.Point(90, 70), 20)
cloud2 = gr.Circle(gr.Point(110, 70), 20)
cloud3 = gr.Circle(gr.Point(120, 90), 20)
cloud4 = gr.Circle(gr.Point(100, 90), 20)
cloud5 = gr.Circle(gr.Point(80, 90), 20)
cloud1.setFill('white')
cloud2.setFill('white')
cloud3.setFill('white')
cloud4.setFill('white')
cloud5.setFill('white')

'''
eyebrow1 = gr.Line(gr.Point(100, 120), gr.Point(180, 170))
eyebrow2 = gr.Line(gr.Point(220, 170), gr.Point(300, 140))
eyebrow1.setWidth(10)
eyebrow2.setWidth(10)
eyebrow1.setOutline('black')
eyebrow2.setOutline('black')

mouth = gr.Line(gr.Point(150, 260), gr.Point(250, 260))
mouth.setWidth(20)
mouth.setOutline('black')
'''

# Отрисовка примитивов в окне window
sky.draw(window)
sun.draw(window)
cloud1.draw(window)
cloud2.draw(window)
cloud3.draw(window)
cloud4.draw(window)
cloud5.draw(window)

#  Ожидание нажатия кнопки мыши по окну.
window.getMouse()

#  После того как мы выполнили все нужные операции, окно следует закрыть.
window.close()