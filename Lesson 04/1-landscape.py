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

house = gr.Rectangle(gr.Point(150, 150), gr.Point(300, 300))
house.setWidth(5)
house.setFill("grey")
roof = gr.Polygon(gr.Point(130, 150), gr.Point(225, 75), gr.Point(320, 150))
roof.setWidth(5)
roof.setFill("red")
win = gr.Rectangle(gr.Point(185, 185), gr.Point(265, 265))
win.setWidth(5)
win.setFill("yellow")
win_line1 = gr.Line(gr.Point(225, 185), gr.Point(225, 265))
win_line1.setWidth(3)
win_line2 = gr.Line(gr.Point(185, 225), gr.Point(265, 225))
win_line2.setWidth(3)

tree_stem = gr.Rectangle(gr.Point(495, 300), gr.Point(505, 330))
tree_stem.setWidth(3)
tree_stem.setFill("brown")
tree1 = gr.Polygon(gr.Point(460, 300), gr.Point(500, 260), gr.Point(540, 300))
tree1.setWidth(3)
tree1.setFill("green")
tree2 = gr.Polygon(gr.Point(470, 270), gr.Point(500, 240), gr.Point(530, 270))
tree2.setWidth(3)
tree2.setFill("green")
tree3 = gr.Polygon(gr.Point(480, 245), gr.Point(500, 225), gr.Point(520, 245))
tree3.setWidth(3)
tree3.setFill("green")

# Отрисовка примитивов в окне window
sky.draw(window)
sun.draw(window)
cloud1.draw(window)
cloud2.draw(window)
cloud3.draw(window)
cloud4.draw(window)
cloud5.draw(window)
house.draw(window)
roof.draw(window)
win.draw(window)
win_line1.draw(window)
win_line2.draw(window)
tree_stem.draw(window)
tree1.draw(window)
tree2.draw(window)
tree3.draw(window)

#  Ожидание нажатия кнопки мыши по окну.
window.getMouse()

#  После того как мы выполнили все нужные операции, окно следует закрыть.
window.close()