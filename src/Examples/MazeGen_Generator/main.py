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
			rgba: 0, 0, 1, 1
		Line: 
			points: 200,200,200,150
			width: 5
		Line: 
			points: 200,200,1000,200
			width: 5
		Line: 
			points: 1000,200,1000,150
			width: 5
		Color: 
			rgba: 1, 1, 1, 1
		Rectangle: 
			pos:400,400
			size: 50, 50
		Rectangle: 
			pos:400,450
			size: 50, 50
		Rectangle: 
			pos:400,500
			size: 50, 50
		Rectangle: 
			pos:400,550
			size: 50, 50
		Rectangle: 
			pos:400,600
			size: 50, 50
		Rectangle: 
			pos:400,650
			size: 50, 50
		Rectangle: 
			pos:400,700
			size: 50, 50
		Rectangle: 
			pos:400,750
			size: 50, 50
		Color: 
			rgba: 1, 1, 1, 1
		Rectangle: 
			pos:350,350
			size: 50, 50
		Rectangle: 
			pos:400,350
			size: 50, 50
		Rectangle: 
			pos:450,350
			size: 50, 50
		Rectangle: 
			pos:500,350
			size: 50, 50
		Rectangle: 
			pos:550,350
			size: 50, 50
		Rectangle: 
			pos:600,350
			size: 50, 50
		Rectangle: 
			pos:650,350
			size: 50, 50
		Rectangle: 
			pos:700,350
			size: 50, 50
		Color: 
			rgba: 0, 0, 1, 1
		Line: 
			points:400,400,425,425,450,400
			width: 5
		Color: 
			rgba: 0, 0, 1, 1
		Line: 
			points:150,150,175,175,200,150
			width: 5
		Color: 
			rgba: 0, 0, 1, 1
		Line: 
			points: 200,200,200,150
			width: 5
		Line: 
			points: 200,200,1000,200
			width: 5
		Line: 
			points: 1000,200,1000,150
			width: 5
''')


class MainApp(App):

    def build(self):
        return root

if __name__ == '__main__':
    MainApp().run()

