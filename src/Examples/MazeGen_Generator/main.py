from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
StackLayout:
	canvas:
		Color: 
			rgba: 1, 1, 1, 1
		Line: 
			points: 100,100,100,1150,1500,1150,1500,100,100,100
			width: 5
		Line: 
			points: 150,150,175,175,200,150
			width: 5
			close: True
		Color: 
			rgba: 1, 1, 1, 1
		Rectangle: 
			pos:700,100
			size:2,2
		Color: 
			rgba: 1, 1, 1, 1
		Line: 
			points: 600,300,100,600
			width: 8
		Line: 
			points: 600,300,600,600
			width: 8
		Line: 
			points: 600,600,600,600
			width: 8
		Line: 
			points: 600,600,600,600
			width: 8
		Color: 
			rgba: 1, 1, 1, 1
		Rectangle: 
			pos:200,500
			size:7,7
		Color: 
			rgba: 1, 1, 1, 1
		Line: 
			points: 300,300,300,350
			width: 5
		Line: 
			points: 300,300,350,300
			width: 5
		Color: 
			rgba: 1, 1, 1, 1
		Rectangle: 
			pos:100,700
			size:400,400
		Color: 
			rgba: 1, 1, 1, 1
		Rectangle: 
			pos:200,700
			size:3,3
		Color: 
			rgba: 1, 1, 1, 1
		Line: 
			points: 400,200,400,250
			width: 7
		Line: 
			points: 400,200,450,200
			width: 7
		Color: 
			rgba: 1, 1, 1, 1
		Rectangle: 
			pos:600,100
			size:4,4
		Color: 
			rgba: 1, 1, 1, 1
		Rectangle: 
			pos:200,300
			size:1,1
		Color: 
			rgba: 1, 1, 1, 1
		Line: 
			points: 400,700,800,500
			width: 1
		Line: 
			points: 400,700,450,400
			width: 1
		Line: 
			points: 400,450,450,450
			width: 1
		Line: 
			points: 400,500,450,500
			width: 1
''')


class MainApp(App):

    def build(self):
        return root

if __name__ == '__main__':
    MainApp().run()

