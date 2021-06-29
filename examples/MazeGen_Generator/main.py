from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''
StackLayout:
	canvas:
		Color: 
			rgba:700,300,0, 1
		Rectangle: 
			pos:700,300
			size:500,500
		Color: 
			rgba:900,1100,1100,100
		Line: 
			points: 900,1100,1100,100
			width: 2
		Line: 
			points: 900,1100,500,900
			width: 2
		Line: 
			points: 900,500,500,500
			width: 2
		Line: 
			points: 900,100,500,100
			width: 2
		Color: 
			rgba:200,1000,0, 1
		Rectangle: 
			pos:200,1000
			size:700,700
		Color: 
			rgba:200,700,0, 1
		Rectangle: 
			pos:200,700
			size:200,200
		Color: 
			rgba:800,600,200,800
		Line: 
			points: 800,600,200,800
			width: 7
		Line: 
			points: 800,600,800,800
			width: 7
		Line: 
			points: 800,800,800,800
			width: 7
		Line: 
			points: 800,800,800,800
			width: 7
		Color: 
			rgba:300,1100,0, 1
		Rectangle: 
			pos:300,1100
			size:600,600
		Color: 
			rgba:500,400,1100,1000
		Line: 
			points: 500,400,1100,1000
			width: 7
		Line: 
			points: 500,400,750,500
			width: 7
		Line: 
			points: 500,750,750,750
			width: 7
		Line: 
			points: 500,1000,750,1000
			width: 7
		Color: 
			rgba:500,100,700,400
		Line: 
			points: 500,100,700,400
			width: 3
		Line: 
			points: 500,100,450,500
			width: 3
		Line: 
			points: 500,450,450,450
			width: 3
		Line: 
			points: 500,400,450,400
			width: 3
		Color: 
			rgba:0, 1,100,200
		Line: 
			points: 100,200,100,250
			width: 5
		Line: 
			points: 100,200,150,200
			width: 5
		Color: 
			rgba:0, 1,800,1000
		Line: 
			points: 800,1000,800,1050
			width: 3
		Line: 
			points: 800,1000,850,1000
			width: 3
		Color: 
			rgba:200,600,0, 1
		Rectangle: 
			pos:200,600
			size:5,5
		Color: 
			rgba:0, 1,600,900
		Line: 
			points: 600,900,600,950
			width: 8
		Line: 
			points: 600,900,650,900
			width: 8
		Color: 
			rgba:1100,600,0, 1
		Rectangle: 
			pos:1100,600
			size:200,200
		Color: 
			rgba:1000,1100,0, 1
		Rectangle: 
			pos:1000,1100
			size:4,4
		Color: 
			rgba:600,500,100,1100
		Line: 
			points: 600,500,100,1100
			width: 6
		Line: 
			points: 600,500,850,600
			width: 6
		Line: 
			points: 600,850,850,850
			width: 6
		Line: 
			points: 600,1100,850,1100
			width: 6
		Color: 
			rgba:100,400,0, 1
		Rectangle: 
			pos:100,400
			size:1000,1000
		Color: 
			rgba:0, 1,300,800
		Line: 
			points: 300,800,300,850
			width: 1
		Line: 
			points: 300,800,350,800
			width: 1
		Color: 
			rgba:0, 1,400,600
		Line: 
			points: 400,600,400,650
			width: 3
		Line: 
			points: 400,600,450,600
			width: 3
		Color: 
			rgba:900,600,0, 1
		Rectangle: 
			pos:900,600
			size:400,400
		Color: 
			rgba:900,100,0, 1
		Rectangle: 
			pos:900,100
			size:8,8
		Color: 
			rgba:200,300,1100,800
		Line: 
			points: 200,300,1100,800
			width: 5
		Line: 
			points: 200,300,500,200
			width: 5
		Line: 
			points: 200,500,500,500
			width: 5
		Line: 
			points: 200,800,500,800
			width: 5
		Color: 
			rgba:0, 1,300,1100
		Line: 
			points: 300,1100,300,1150
			width: 7
		Line: 
			points: 300,1100,350,1100
			width: 7
		Color: 
			rgba:100,1100,600,100
		Line: 
			points: 100,1100,600,100
			width: 4
		Line: 
			points: 100,1100,100,100
			width: 4
		Line: 
			points: 100,100,100,100
			width: 4
		Line: 
			points: 100,100,100,100
			width: 4
		Color: 
			rgba:400,300,800,700
		Line: 
			points: 400,300,800,700
			width: 3
		Line: 
			points: 400,300,550,400
			width: 3
		Line: 
			points: 400,550,550,550
			width: 3
		Line: 
			points: 400,700,550,700
			width: 3
		Color: 
			rgba:0, 1,500,1100
		Line: 
			points: 500,1100,500,1150
			width: 5
		Line: 
			points: 500,1100,550,1100
			width: 5
		Color: 
			rgba:700,800,0, 1
		Rectangle: 
			pos:700,800
			size:300,300
		Color: 
			rgba:800,1000,0, 1
		Rectangle: 
			pos:800,1000
			size:200,200
		Color: 
			rgba:400,1100,0, 1
		Rectangle: 
			pos:400,1100
			size:7,7
		Color: 
			rgba:200,900,0, 1
		Rectangle: 
			pos:200,900
			size:900,900
		Color: 
			rgba:900,300,1000,200
		Line: 
			points: 900,300,1000,200
			width: 2
		Line: 
			points: 900,300,550,900
			width: 2
		Line: 
			points: 900,550,550,550
			width: 2
		Line: 
			points: 900,200,550,200
			width: 2
		Color: 
			rgba:300,500,0, 1
		Rectangle: 
			pos:300,500
			size:8,8
		Color: 
			rgba:0, 1,200,900
		Line: 
			points: 200,900,200,950
			width: 6
		Line: 
			points: 200,900,250,900
			width: 6
		Color: 
			rgba:0, 1,1100,700
		Line: 
			points: 1100,700,1100,750
			width: 7
		Line: 
			points: 1100,700,1150,700
			width: 7
		Color: 
			rgba:500,500,0, 1
		Rectangle: 
			pos:500,500
			size:1,1
		Color: 
			rgba:100,1000,0, 1
		Rectangle: 
			pos:100,1000
			size:3,3
		Color: 
			rgba:800,400,600,700
		Line: 
			points: 800,400,600,700
			width: 6
		Line: 
			points: 800,400,750,800
			width: 6
		Line: 
			points: 800,750,750,750
			width: 6
		Line: 
			points: 800,700,750,700
			width: 6
		Color: 
			rgba:800,1100,900,1000
		Line: 
			points: 800,1100,900,1000
			width: 3
		Line: 
			points: 800,1100,900,800
			width: 3
		Line: 
			points: 800,900,900,900
			width: 3
		Line: 
			points: 800,1000,900,1000
			width: 3
		Color: 
			rgba:0, 1,300,500
		Line: 
			points: 300,500,300,550
			width: 8
		Line: 
			points: 300,500,350,500
			width: 8
		Color: 
			rgba:700,300,0, 1
		Rectangle: 
			pos:700,300
			size:200,200
		Color: 
			rgba:0, 1,1100,400
		Line: 
			points: 1100,400,1100,450
			width: 4
		Line: 
			points: 1100,400,1150,400
			width: 4
		Color: 
			rgba:900,700,900,200
		Line: 
			points: 900,700,900,200
			width: 6
		Line: 
			points: 900,700,550,900
			width: 6
		Line: 
			points: 900,550,550,550
			width: 6
		Line: 
			points: 900,200,550,200
			width: 6
		Color: 
			rgba:1100,800,0, 1
		Rectangle: 
			pos:1100,800
			size:8,8
		Color: 
			rgba:0, 1,1100,300
		Line: 
			points: 1100,300,1100,350
			width: 4
		Line: 
			points: 1100,300,1150,300
			width: 4
		Color: 
			rgba:400,100,300,900
		Line: 
			points: 400,100,300,900
			width: 8
		Line: 
			points: 400,100,650,400
			width: 8
		Line: 
			points: 400,650,650,650
			width: 8
		Line: 
			points: 400,900,650,900
			width: 8
		Color: 
			rgba:600,800,0, 1
		Rectangle: 
			pos:600,800
			size:1,1
		Color: 
			rgba:0, 1,400,100
		Line: 
			points: 400,100,400,150
			width: 8
		Line: 
			points: 400,100,450,100
			width: 8
		Color: 
			rgba:0, 1,300,300
		Line: 
			points: 300,300,300,350
			width: 2
		Line: 
			points: 300,300,350,300
			width: 2
		Color: 
			rgba:400,800,400,100
		Line: 
			points: 400,800,400,100
			width: 5
		Line: 
			points: 400,800,250,400
			width: 5
		Line: 
			points: 400,250,250,250
			width: 5
		Line: 
			points: 400,100,250,100
			width: 5
		Color: 
			rgba:900,300,0, 1
		Rectangle: 
			pos:900,300
			size:600,600
		Color: 
			rgba:0, 1,600,100
		Line: 
			points: 600,100,600,150
			width: 2
		Line: 
			points: 600,100,650,100
			width: 2
		Color: 
			rgba:0, 1,900,800
		Line: 
			points: 900,800,900,850
			width: 6
		Line: 
			points: 900,800,950,800
			width: 6
		Color: 
			rgba:100,500,0, 1
		Rectangle: 
			pos:100,500
			size:2,2
		Color: 
			rgba:1000,200,0, 1
		Rectangle: 
			pos:1000,200
			size:1100,1100
		Color: 
			rgba:200,600,0, 1
		Rectangle: 
			pos:200,600
			size:900,900
		Color: 
			rgba:700,900,0, 1
		Rectangle: 
			pos:700,900
			size:700,700
		Color: 
			rgba:200,400,0, 1
		Rectangle: 
			pos:200,400
			size:1000,1000
		Color: 
			rgba:200,400,0, 1
		Rectangle: 
			pos:200,400
			size:800,800
		Color: 
			rgba:400,300,0, 1
		Rectangle: 
			pos:400,300
			size:1,1
		Color: 
			rgba:600,800,100,200
		Line: 
			points: 600,800,100,200
			width: 8
		Line: 
			points: 600,800,400,600
			width: 8
		Line: 
			points: 600,400,400,400
			width: 8
		Line: 
			points: 600,200,400,200
			width: 8
		Color: 
			rgba:400,600,800,700
		Line: 
			points: 400,600,800,700
			width: 2
		Line: 
			points: 400,600,550,400
			width: 2
		Line: 
			points: 400,550,550,550
			width: 2
		Line: 
			points: 400,700,550,700
			width: 2
		Color: 
			rgba:0, 1,200,400
		Line: 
			points: 200,400,200,450
			width: 7
		Line: 
			points: 200,400,250,400
			width: 7
		Color: 
			rgba:400,600,0, 1
		Rectangle: 
			pos:400,600
			size:600,600
		Color: 
			rgba:300,800,0, 1
		Rectangle: 
			pos:300,800
			size:4,4
		Color: 
			rgba:200,800,0, 1
		Rectangle: 
			pos:200,800
			size:1000,1000
		Color: 
			rgba:1100,700,0, 1
		Rectangle: 
			pos:1100,700
			size:400,400
		Color: 
			rgba:200,900,0, 1
		Rectangle: 
			pos:200,900
			size:800,800
		Color: 
			rgba:500,500,900,800
		Line: 
			points: 500,500,900,800
			width: 2
		Line: 
			points: 500,500,650,500
			width: 2
		Line: 
			points: 500,650,650,650
			width: 2
		Line: 
			points: 500,800,650,800
			width: 2
		Color: 
			rgba:300,900,0, 1
		Rectangle: 
			pos:300,900
			size:300,300
		Color: 
			rgba:0, 1,400,900
		Line: 
			points: 400,900,400,950
			width: 3
		Line: 
			points: 400,900,450,900
			width: 3
		Color: 
			rgba:800,1000,0, 1
		Rectangle: 
			pos:800,1000
			size:6,6
		Color: 
			rgba:100,1000,0, 1
		Rectangle: 
			pos:100,1000
			size:400,400
		Color: 
			rgba:800,300,0, 1
		Rectangle: 
			pos:800,300
			size:800,800
		Color: 
			rgba:900,1000,0, 1
		Rectangle: 
			pos:900,1000
			size:700,700
		Color: 
			rgba:800,100,700,900
		Line: 
			points: 800,100,700,900
			width: 2
		Line: 
			points: 800,100,850,800
			width: 2
		Line: 
			points: 800,850,850,850
			width: 2
		Line: 
			points: 800,900,850,900
			width: 2
		Color: 
			rgba:400,100,0, 1
		Rectangle: 
			pos:400,100
			size:2,2
		Color: 
			rgba:400,100,0, 1
		Rectangle: 
			pos:400,100
			size:700,700
		Color: 
			rgba:800,200,0, 1
		Rectangle: 
			pos:800,200
			size:100,100
		Color: 
			rgba:0, 1,200,1100
		Line: 
			points: 200,1100,200,1150
			width: 6
		Line: 
			points: 200,1100,250,1100
			width: 6
		Color: 
			rgba:400,800,0, 1
		Rectangle: 
			pos:400,800
			size:2,2
		Color: 
			rgba:700,400,300,500
		Line: 
			points: 700,400,300,500
			width: 6
		Line: 
			points: 700,400,600,700
			width: 6
		Line: 
			points: 700,600,600,600
			width: 6
		Line: 
			points: 700,500,600,500
			width: 6
		Color: 
			rgba:400,1000,0, 1
		Rectangle: 
			pos:400,1000
			size:500,500
		Color: 
			rgba:200,1100,0, 1
		Rectangle: 
			pos:200,1100
			size:2,2
		Color: 
			rgba:1000,400,1000,800
		Line: 
			points: 1000,400,1000,800
			width: 6
		Line: 
			points: 1000,400,900,1000
			width: 6
		Line: 
			points: 1000,900,900,900
			width: 6
		Line: 
			points: 1000,800,900,800
			width: 6
		Color: 
			rgba:700,1100,500,1100
		Line: 
			points: 700,1100,500,1100
			width: 1
		Line: 
			points: 700,1100,900,700
			width: 1
		Line: 
			points: 700,900,900,900
			width: 1
		Line: 
			points: 700,1100,900,1100
			width: 1
		Color: 
			rgba:900,900,800,800
		Line: 
			points: 900,900,800,800
			width: 8
		Line: 
			points: 900,900,850,900
			width: 8
		Line: 
			points: 900,850,850,850
			width: 8
		Line: 
			points: 900,800,850,800
			width: 8
		Color: 
			rgba:100,200,0, 1
		Rectangle: 
			pos:100,200
			size:5,5
		Color: 
			rgba:1000,300,0, 1
		Rectangle: 
			pos:1000,300
			size:500,500
		Color: 
			rgba:200,700,0, 1
		Rectangle: 
			pos:200,700
			size:200,200
		Color: 
			rgba:0, 1,800,400
		Line: 
			points: 800,400,800,450
			width: 6
		Line: 
			points: 800,400,850,400
			width: 6
		Color: 
			rgba:1100,200,100,400
		Line: 
			points: 1100,200,100,400
			width: 8
		Line: 
			points: 1100,200,750,1100
			width: 8
		Line: 
			points: 1100,750,750,750
			width: 8
		Line: 
			points: 1100,400,750,400
			width: 8
		Color: 
			rgba:1100,600,0, 1
		Rectangle: 
			pos:1100,600
			size:800,800
		Color: 
			rgba:700,200,0, 1
		Rectangle: 
			pos:700,200
			size:5,5
		Color: 
			rgba:800,1000,0, 1
		Rectangle: 
			pos:800,1000
			size:500,500
		Color: 
			rgba:300,1000,800,600
		Line: 
			points: 300,1000,800,600
			width: 8
		Line: 
			points: 300,1000,450,300
			width: 8
		Line: 
			points: 300,450,450,450
			width: 8
		Line: 
			points: 300,600,450,600
			width: 8
		Color: 
			rgba:600,800,0, 1
		Rectangle: 
			pos:600,800
			size:7,7
		Color: 
			rgba:1100,400,0, 1
		Rectangle: 
			pos:1100,400
			size:7,7
		Color: 
			rgba:900,900,0, 1
		Rectangle: 
			pos:900,900
			size:800,800
		Color: 
			rgba:0, 1,800,200
		Line: 
			points: 800,200,800,250
			width: 5
		Line: 
			points: 800,200,850,200
			width: 5
		Color: 
			rgba:0, 1,1000,700
		Line: 
			points: 1000,700,1000,750
			width: 4
		Line: 
			points: 1000,700,1050,700
			width: 4
		Color: 
			rgba:800,100,0, 1
		Rectangle: 
			pos:800,100
			size:2,2
		Color: 
			rgba:0, 1,800,500
		Line: 
			points: 800,500,800,550
			width: 1
		Line: 
			points: 800,500,850,500
			width: 1
		Color: 
			rgba:500,1100,1000,100
		Line: 
			points: 500,1100,1000,100
			width: 4
		Line: 
			points: 500,1100,300,500
			width: 4
		Line: 
			points: 500,300,300,300
			width: 4
		Line: 
			points: 500,100,300,100
			width: 4
		Color: 
			rgba:1000,200,900,100
		Line: 
			points: 1000,200,900,100
			width: 8
		Line: 
			points: 1000,200,550,1000
			width: 8
		Line: 
			points: 1000,550,550,550
			width: 8
		Line: 
			points: 1000,100,550,100
			width: 8
		Color: 
			rgba:600,400,0, 1
		Rectangle: 
			pos:600,400
			size:3,3
		Color: 
			rgba:400,700,0, 1
		Rectangle: 
			pos:400,700
			size:5,5
		Color: 
			rgba:500,600,0, 1
		Rectangle: 
			pos:500,600
			size:5,5
		Color: 
			rgba:500,600,0, 1
		Rectangle: 
			pos:500,600
			size:1000,1000
		Color: 
			rgba:700,300,0, 1
		Rectangle: 
			pos:700,300
			size:100,100
		Color: 
			rgba:0, 1,300,500
		Line: 
			points: 300,500,300,550
			width: 6
		Line: 
			points: 300,500,350,500
			width: 6
		Color: 
			rgba:700,400,1000,700
		Line: 
			points: 700,400,1000,700
			width: 1
		Line: 
			points: 700,400,700,700
			width: 1
		Line: 
			points: 700,700,700,700
			width: 1
		Line: 
			points: 700,700,700,700
			width: 1
		Color: 
			rgba:0, 1,1000,900
		Line: 
			points: 1000,900,1000,950
			width: 7
		Line: 
			points: 1000,900,1050,900
			width: 7
		Color: 
			rgba:100,700,0, 1
		Rectangle: 
			pos:100,700
			size:400,400
		Color: 
			rgba:0, 1,500,600
		Line: 
			points: 500,600,500,650
			width: 6
		Line: 
			points: 500,600,550,600
			width: 6
		Color: 
			rgba:500,200,500,300
		Line: 
			points: 500,200,500,300
			width: 4
		Line: 
			points: 500,200,400,500
			width: 4
		Line: 
			points: 500,400,400,400
			width: 4
		Line: 
			points: 500,300,400,300
			width: 4
		Color: 
			rgba:600,400,500,1100
		Line: 
			points: 600,400,500,1100
			width: 3
		Line: 
			points: 600,400,850,600
			width: 3
		Line: 
			points: 600,850,850,850
			width: 3
		Line: 
			points: 600,1100,850,1100
			width: 3
		Color: 
			rgba:0, 1,900,500
		Line: 
			points: 900,500,900,550
			width: 5
		Line: 
			points: 900,500,950,500
			width: 5
		Color: 
			rgba:1000,700,0, 1
		Rectangle: 
			pos:1000,700
			size:600,600
		Color: 
			rgba:800,1100,300,1000
		Line: 
			points: 800,1100,300,1000
			width: 1
		Line: 
			points: 800,1100,900,800
			width: 1
		Line: 
			points: 800,900,900,900
			width: 1
		Line: 
			points: 800,1000,900,1000
			width: 1
		Color: 
			rgba:300,400,400,500
		Line: 
			points: 300,400,400,500
			width: 2
		Line: 
			points: 300,400,400,300
			width: 2
		Line: 
			points: 300,400,400,400
			width: 2
		Line: 
			points: 300,500,400,500
			width: 2
		Color: 
			rgba:1000,800,1000,300
		Line: 
			points: 1000,800,1000,300
			width: 5
		Line: 
			points: 1000,800,650,1000
			width: 5
		Line: 
			points: 1000,650,650,650
			width: 5
		Line: 
			points: 1000,300,650,300
			width: 5
		Color: 
			rgba:600,200,0, 1
		Rectangle: 
			pos:600,200
			size:4,4
		Color: 
			rgba:500,600,0, 1
		Rectangle: 
			pos:500,600
			size:800,800
		Color: 
			rgba:100,1100,0, 1
		Rectangle: 
			pos:100,1100
			size:300,300
		Color: 
			rgba:600,300,100,200
		Line: 
			points: 600,300,100,200
			width: 3
		Line: 
			points: 600,300,400,600
			width: 3
		Line: 
			points: 600,400,400,400
			width: 3
		Line: 
			points: 600,200,400,200
			width: 3
		Color: 
			rgba:800,400,0, 1
		Rectangle: 
			pos:800,400
			size:3,3
		Color: 
			rgba:500,900,400,1000
		Line: 
			points: 500,900,400,1000
			width: 5
		Line: 
			points: 500,900,750,500
			width: 5
		Line: 
			points: 500,750,750,750
			width: 5
		Line: 
			points: 500,1000,750,1000
			width: 5
		Color: 
			rgba:800,200,0, 1
		Rectangle: 
			pos:800,200
			size:800,800
		Color: 
			rgba:200,300,1100,100
		Line: 
			points: 200,300,1100,100
			width: 6
		Line: 
			points: 200,300,150,200
			width: 6
		Line: 
			points: 200,150,150,150
			width: 6
		Line: 
			points: 200,100,150,100
			width: 6
		Color: 
			rgba:500,300,0, 1
		Rectangle: 
			pos:500,300
			size:1100,1100
		Color: 
			rgba:0, 1,200,800
		Line: 
			points: 200,800,200,850
			width: 1
		Line: 
			points: 200,800,250,800
			width: 1
		Color: 
			rgba:700,800,0, 1
		Rectangle: 
			pos:700,800
			size:500,500
		Color: 
			rgba:400,200,0, 1
		Rectangle: 
			pos:400,200
			size:1,1
		Color: 
			rgba:0, 1,1000,800
		Line: 
			points: 1000,800,1000,850
			width: 7
		Line: 
			points: 1000,800,1050,800
			width: 7
		Color: 
			rgba:600,400,300,200
		Line: 
			points: 600,400,300,200
			width: 8
		Line: 
			points: 600,400,400,600
			width: 8
		Line: 
			points: 600,400,400,400
			width: 8
		Line: 
			points: 600,200,400,200
			width: 8
		Color: 
			rgba:800,900,0, 1
		Rectangle: 
			pos:800,900
			size:600,600
		Color: 
			rgba:300,600,0, 1
		Rectangle: 
			pos:300,600
			size:1,1
		Color: 
			rgba:1000,1000,0, 1
		Rectangle: 
			pos:1000,1000
			size:4,4
		Color: 
			rgba:400,800,0, 1
		Rectangle: 
			pos:400,800
			size:400,400
		Color: 
			rgba:0, 1,100,400
		Line: 
			points: 100,400,100,450
			width: 7
		Line: 
			points: 100,400,150,400
			width: 7
		Color: 
			rgba:1100,1100,0, 1
		Rectangle: 
			pos:1100,1100
			size:4,4
		Color: 
			rgba:500,1000,0, 1
		Rectangle: 
			pos:500,1000
			size:1,1
		Color: 
			rgba:200,700,0, 1
		Rectangle: 
			pos:200,700
			size:5,5
		Color: 
			rgba:100,800,700,800
		Line: 
			points: 100,800,700,800
			width: 8
		Line: 
			points: 100,800,450,100
			width: 8
		Line: 
			points: 100,450,450,450
			width: 8
		Line: 
			points: 100,800,450,800
			width: 8
		Color: 
			rgba:200,800,0, 1
		Rectangle: 
			pos:200,800
			size:5,5
		Color: 
			rgba:0, 1,1100,100
		Line: 
			points: 1100,100,1100,150
			width: 8
		Line: 
			points: 1100,100,1150,100
			width: 8
		Color: 
			rgba:1100,500,0, 1
		Rectangle: 
			pos:1100,500
			size:6,6
		Color: 
			rgba:900,500,300,600
		Line: 
			points: 900,500,300,600
			width: 5
		Line: 
			points: 900,500,750,900
			width: 5
		Line: 
			points: 900,750,750,750
			width: 5
		Line: 
			points: 900,600,750,600
			width: 5
		Color: 
			rgba:800,600,0, 1
		Rectangle: 
			pos:800,600
			size:2,2
		Color: 
			rgba:800,400,0, 1
		Rectangle: 
			pos:800,400
			size:1100,1100
		Color: 
			rgba:400,700,0, 1
		Rectangle: 
			pos:400,700
			size:300,300
		Color: 
			rgba:0, 1,500,400
		Line: 
			points: 500,400,500,450
			width: 5
		Line: 
			points: 500,400,550,400
			width: 5
		Color: 
			rgba:0, 1,400,300
		Line: 
			points: 400,300,400,350
			width: 4
		Line: 
			points: 400,300,450,300
			width: 4
		Color: 
			rgba:400,800,0, 1
		Rectangle: 
			pos:400,800
			size:5,5
		Color: 
			rgba:200,1100,100,300
		Line: 
			points: 200,1100,100,300
			width: 7
		Line: 
			points: 200,1100,250,200
			width: 7
		Line: 
			points: 200,250,250,250
			width: 7
		Line: 
			points: 200,300,250,300
			width: 7
		Color: 
			rgba:0, 1,600,700
		Line: 
			points: 600,700,600,750
			width: 5
		Line: 
			points: 600,700,650,700
			width: 5
		Color: 
			rgba:1100,1100,0, 1
		Rectangle: 
			pos:1100,1100
			size:200,200
		Color: 
			rgba:200,1100,0, 1
		Rectangle: 
			pos:200,1100
			size:900,900
		Color: 
			rgba:700,100,500,100
		Line: 
			points: 700,100,500,100
			width: 7
		Line: 
			points: 700,100,400,700
			width: 7
		Line: 
			points: 700,400,400,400
			width: 7
		Line: 
			points: 700,100,400,100
			width: 7
		Color: 
			rgba:900,300,200,600
		Line: 
			points: 900,300,200,600
			width: 2
		Line: 
			points: 900,300,750,900
			width: 2
		Line: 
			points: 900,750,750,750
			width: 2
		Line: 
			points: 900,600,750,600
			width: 2
		Color: 
			rgba:700,200,0, 1
		Rectangle: 
			pos:700,200
			size:4,4
		Color: 
			rgba:200,600,0, 1
		Rectangle: 
			pos:200,600
			size:7,7
		Color: 
			rgba:700,400,600,300
		Line: 
			points: 700,400,600,300
			width: 4
		Line: 
			points: 700,400,500,700
			width: 4
		Line: 
			points: 700,500,500,500
			width: 4
		Line: 
			points: 700,300,500,300
			width: 4
		Color: 
			rgba:700,500,0, 1
		Rectangle: 
			pos:700,500
			size:5,5
		Color: 
			rgba:700,500,500,100
		Line: 
			points: 700,500,500,100
			width: 8
		Line: 
			points: 700,500,400,700
			width: 8
		Line: 
			points: 700,400,400,400
			width: 8
		Line: 
			points: 700,100,400,100
			width: 8
		Color: 
			rgba:200,100,700,1000
		Line: 
			points: 200,100,700,1000
			width: 5
		Line: 
			points: 200,100,600,200
			width: 5
		Line: 
			points: 200,600,600,600
			width: 5
		Line: 
			points: 200,1000,600,1000
			width: 5
		Color: 
			rgba:1100,700,0, 1
		Rectangle: 
			pos:1100,700
			size:4,4
		Color: 
			rgba:600,200,300,200
		Line: 
			points: 600,200,300,200
			width: 3
		Line: 
			points: 600,200,400,600
			width: 3
		Line: 
			points: 600,400,400,400
			width: 3
		Line: 
			points: 600,200,400,200
			width: 3
		Color: 
			rgba:400,700,0, 1
		Rectangle: 
			pos:400,700
			size:4,4
		Color: 
			rgba:1000,1100,300,700
		Line: 
			points: 1000,1100,300,700
			width: 8
		Line: 
			points: 1000,1100,850,1000
			width: 8
		Line: 
			points: 1000,850,850,850
			width: 8
		Line: 
			points: 1000,700,850,700
			width: 8
		Color: 
			rgba:700,700,0, 1
		Rectangle: 
			pos:700,700
			size:1000,1000
		Color: 
			rgba:500,400,0, 1
		Rectangle: 
			pos:500,400
			size:300,300
		Color: 
			rgba:200,700,0, 1
		Rectangle: 
			pos:200,700
			size:8,8
		Color: 
			rgba:500,600,0, 1
		Rectangle: 
			pos:500,600
			size:1,1
		Color: 
			rgba:100,700,0, 1
		Rectangle: 
			pos:100,700
			size:6,6
		Color: 
			rgba:0, 1,500,300
		Line: 
			points: 500,300,500,350
			width: 3
		Line: 
			points: 500,300,550,300
			width: 3
		Color: 
			rgba:300,400,0, 1
		Rectangle: 
			pos:300,400
			size:400,400
		Color: 
			rgba:100,1100,0, 1
		Rectangle: 
			pos:100,1100
			size:500,500
		Color: 
			rgba:200,700,0, 1
		Rectangle: 
			pos:200,700
			size:400,400
		Color: 
			rgba:0, 1,900,200
		Line: 
			points: 900,200,900,250
			width: 8
		Line: 
			points: 900,200,950,200
			width: 8
		Color: 
			rgba:900,800,0, 1
		Rectangle: 
			pos:900,800
			size:400,400
		Color: 
			rgba:600,100,200,400
		Line: 
			points: 600,100,200,400
			width: 2
		Line: 
			points: 600,100,500,600
			width: 2
		Line: 
			points: 600,500,500,500
			width: 2
		Line: 
			points: 600,400,500,400
			width: 2
		Color: 
			rgba:200,300,100,700
		Line: 
			points: 200,300,100,700
			width: 3
		Line: 
			points: 200,300,450,200
			width: 3
		Line: 
			points: 200,450,450,450
			width: 3
		Line: 
			points: 200,700,450,700
			width: 3
		Color: 
			rgba:900,900,0, 1
		Rectangle: 
			pos:900,900
			size:500,500
		Color: 
			rgba:0, 1,600,1000
		Line: 
			points: 600,1000,600,1050
			width: 6
		Line: 
			points: 600,1000,650,1000
			width: 6
		Color: 
			rgba:1100,800,200,1000
		Line: 
			points: 1100,800,200,1000
			width: 3
		Line: 
			points: 1100,800,1050,1100
			width: 3
		Line: 
			points: 1100,1050,1050,1050
			width: 3
		Line: 
			points: 1100,1000,1050,1000
			width: 3
		Color: 
			rgba:800,1000,0, 1
		Rectangle: 
			pos:800,1000
			size:6,6
		Color: 
			rgba:200,500,1100,1100
		Line: 
			points: 200,500,1100,1100
			width: 6
		Line: 
			points: 200,500,650,200
			width: 6
		Line: 
			points: 200,650,650,650
			width: 6
		Line: 
			points: 200,1100,650,1100
			width: 6
		Color: 
			rgba:300,1100,1000,400
		Line: 
			points: 300,1100,1000,400
			width: 1
		Line: 
			points: 300,1100,350,300
			width: 1
		Line: 
			points: 300,350,350,350
			width: 1
		Line: 
			points: 300,400,350,400
			width: 1
		Color: 
			rgba:700,700,900,200
		Line: 
			points: 700,700,900,200
			width: 5
		Line: 
			points: 700,700,450,700
			width: 5
		Line: 
			points: 700,450,450,450
			width: 5
		Line: 
			points: 700,200,450,200
			width: 5
		Color: 
			rgba:800,700,0, 1
		Rectangle: 
			pos:800,700
			size:5,5
		Color: 
			rgba:0, 1,500,900
		Line: 
			points: 500,900,500,950
			width: 3
		Line: 
			points: 500,900,550,900
			width: 3
		Color: 
			rgba:300,300,300,900
		Line: 
			points: 300,300,300,900
			width: 7
		Line: 
			points: 300,300,600,300
			width: 7
		Line: 
			points: 300,600,600,600
			width: 7
		Line: 
			points: 300,900,600,900
			width: 7
		Color: 
			rgba:1100,500,100,1100
		Line: 
			points: 1100,500,100,1100
			width: 8
		Line: 
			points: 1100,500,1100,1100
			width: 8
		Line: 
			points: 1100,1100,1100,1100
			width: 8
		Line: 
			points: 1100,1100,1100,1100
			width: 8
		Color: 
			rgba:0, 1,600,1000
		Line: 
			points: 600,1000,600,1050
			width: 4
		Line: 
			points: 600,1000,650,1000
			width: 4
		Color: 
			rgba:0, 1,900,500
		Line: 
			points: 900,500,900,550
			width: 5
		Line: 
			points: 900,500,950,500
			width: 5
		Color: 
			rgba:0, 1,800,500
		Line: 
			points: 800,500,800,550
			width: 3
		Line: 
			points: 800,500,850,500
			width: 3
		Color: 
			rgba:800,500,0, 1
		Rectangle: 
			pos:800,500
			size:4,4
		Color: 
			rgba:800,1100,0, 1
		Rectangle: 
			pos:800,1100
			size:8,8
		Color: 
			rgba:0, 1,700,400
		Line: 
			points: 700,400,700,450
			width: 4
		Line: 
			points: 700,400,750,400
			width: 4
		Color: 
			rgba:500,700,600,100
		Line: 
			points: 500,700,600,100
			width: 6
		Line: 
			points: 500,700,300,500
			width: 6
		Line: 
			points: 500,300,300,300
			width: 6
		Line: 
			points: 500,100,300,100
			width: 6
		Color: 
			rgba:500,500,0, 1
		Rectangle: 
			pos:500,500
			size:8,8
		Color: 
			rgba:0, 1,100,200
		Line: 
			points: 100,200,100,250
			width: 6
		Line: 
			points: 100,200,150,200
			width: 6
		Color: 
			rgba:500,100,0, 1
		Rectangle: 
			pos:500,100
			size:900,900
		Color: 
			rgba:500,1000,0, 1
		Rectangle: 
			pos:500,1000
			size:1,1
		Color: 
			rgba:400,100,0, 1
		Rectangle: 
			pos:400,100
			size:4,4
		Color: 
			rgba:1000,100,700,900
		Line: 
			points: 1000,100,700,900
			width: 5
		Line: 
			points: 1000,100,950,1000
			width: 5
		Line: 
			points: 1000,950,950,950
			width: 5
		Line: 
			points: 1000,900,950,900
			width: 5
		Color: 
			rgba:800,1000,0, 1
		Rectangle: 
			pos:800,1000
			size:7,7
		Color: 
			rgba:800,1100,900,200
		Line: 
			points: 800,1100,900,200
			width: 8
		Line: 
			points: 800,1100,500,800
			width: 8
		Line: 
			points: 800,500,500,500
			width: 8
		Line: 
			points: 800,200,500,200
			width: 8
		Color: 
			rgba:400,700,0, 1
		Rectangle: 
			pos:400,700
			size:700,700
		Color: 
			rgba:200,100,0, 1
		Rectangle: 
			pos:200,100
			size:1,1
		Color: 
			rgba:0, 1,600,1100
		Line: 
			points: 600,1100,600,1150
			width: 5
		Line: 
			points: 600,1100,650,1100
			width: 5
		Color: 
			rgba:0, 1,100,100
		Line: 
			points: 100,100,100,150
			width: 6
		Line: 
			points: 100,100,150,100
			width: 6
		Color: 
			rgba:200,800,0, 1
		Rectangle: 
			pos:200,800
			size:8,8
		Color: 
			rgba:0, 1,100,700
		Line: 
			points: 100,700,100,750
			width: 4
		Line: 
			points: 100,700,150,700
			width: 4
		Color: 
			rgba:300,1100,600,900
		Line: 
			points: 300,1100,600,900
			width: 3
		Line: 
			points: 300,1100,600,300
			width: 3
		Line: 
			points: 300,600,600,600
			width: 3
		Line: 
			points: 300,900,600,900
			width: 3
		Color: 
			rgba:100,500,0, 1
		Rectangle: 
			pos:100,500
			size:4,4
		Color: 
			rgba:0, 1,500,600
		Line: 
			points: 500,600,500,650
			width: 3
		Line: 
			points: 500,600,550,600
			width: 3
		Color: 
			rgba:500,300,900,800
		Line: 
			points: 500,300,900,800
			width: 7
		Line: 
			points: 500,300,650,500
			width: 7
		Line: 
			points: 500,650,650,650
			width: 7
		Line: 
			points: 500,800,650,800
			width: 7
		Color: 
			rgba:500,400,0, 1
		Rectangle: 
			pos:500,400
			size:6,6
		Color: 
			rgba:0, 1,1000,800
		Line: 
			points: 1000,800,1000,850
			width: 6
		Line: 
			points: 1000,800,1050,800
			width: 6
		Color: 
			rgba:200,800,0, 1
		Rectangle: 
			pos:200,800
			size:5,5
		Color: 
			rgba:200,1000,0, 1
		Rectangle: 
			pos:200,1000
			size:3,3
		Color: 
			rgba:0, 1,600,400
		Line: 
			points: 600,400,600,450
			width: 4
		Line: 
			points: 600,400,650,400
			width: 4
		Color: 
			rgba:0, 1,900,1000
		Line: 
			points: 900,1000,900,1050
			width: 8
		Line: 
			points: 900,1000,950,1000
			width: 8
		Color: 
			rgba:400,1000,0, 1
		Rectangle: 
			pos:400,1000
			size:6,6
		Color: 
			rgba:500,700,100,900
		Line: 
			points: 500,700,100,900
			width: 4
		Line: 
			points: 500,700,700,500
			width: 4
		Line: 
			points: 500,700,700,700
			width: 4
		Line: 
			points: 500,900,700,900
			width: 4
		Color: 
			rgba:0, 1,300,100
		Line: 
			points: 300,100,300,150
			width: 6
		Line: 
			points: 300,100,350,100
			width: 6
		Color: 
			rgba:600,1000,0, 1
		Rectangle: 
			pos:600,1000
			size:4,4
		Color: 
			rgba:0, 1,700,800
		Line: 
			points: 700,800,700,850
			width: 7
		Line: 
			points: 700,800,750,800
			width: 7
		Color: 
			rgba:1000,1100,800,200
		Line: 
			points: 1000,1100,800,200
			width: 2
		Line: 
			points: 1000,1100,600,1000
			width: 2
		Line: 
			points: 1000,600,600,600
			width: 2
		Line: 
			points: 1000,200,600,200
			width: 2
		Color: 
			rgba:500,1100,0, 1
		Rectangle: 
			pos:500,1100
			size:800,800
		Color: 
			rgba:1100,700,0, 1
		Rectangle: 
			pos:1100,700
			size:3,3
		Color: 
			rgba:1000,600,0, 1
		Rectangle: 
			pos:1000,600
			size:8,8
		Color: 
			rgba:600,100,0, 1
		Rectangle: 
			pos:600,100
			size:6,6
		Color: 
			rgba:900,800,0, 1
		Rectangle: 
			pos:900,800
			size:600,600
		Color: 
			rgba:1000,1100,0, 1
		Rectangle: 
			pos:1000,1100
			size:7,7
		Color: 
			rgba:0, 1,200,700
		Line: 
			points: 200,700,200,750
			width: 3
		Line: 
			points: 200,700,250,700
			width: 3
		Color: 
			rgba:800,800,0, 1
		Rectangle: 
			pos:800,800
			size:1100,1100
		Color: 
			rgba:1000,900,0, 1
		Rectangle: 
			pos:1000,900
			size:5,5
		Color: 
			rgba:800,1000,400,600
		Line: 
			points: 800,1000,400,600
			width: 2
		Line: 
			points: 800,1000,700,800
			width: 2
		Line: 
			points: 800,700,700,700
			width: 2
		Line: 
			points: 800,600,700,600
			width: 2
		Color: 
			rgba:200,500,1100,1000
		Line: 
			points: 200,500,1100,1000
			width: 8
		Line: 
			points: 200,500,600,200
			width: 8
		Line: 
			points: 200,600,600,600
			width: 8
		Line: 
			points: 200,1000,600,1000
			width: 8
		Color: 
			rgba:100,700,0, 1
		Rectangle: 
			pos:100,700
			size:1,1
		Color: 
			rgba:500,600,100,700
		Line: 
			points: 500,600,100,700
			width: 5
		Line: 
			points: 500,600,600,500
			width: 5
		Line: 
			points: 500,600,600,600
			width: 5
		Line: 
			points: 500,700,600,700
			width: 5
		Color: 
			rgba:800,400,900,400
		Line: 
			points: 800,400,900,400
			width: 8
		Line: 
			points: 800,400,600,800
			width: 8
		Line: 
			points: 800,600,600,600
			width: 8
		Line: 
			points: 800,400,600,400
			width: 8
		Color: 
			rgba:0, 1,300,600
		Line: 
			points: 300,600,300,650
			width: 1
		Line: 
			points: 300,600,350,600
			width: 1
		Color: 
			rgba:900,100,800,800
		Line: 
			points: 900,100,800,800
			width: 8
		Line: 
			points: 900,100,850,900
			width: 8
		Line: 
			points: 900,850,850,850
			width: 8
		Line: 
			points: 900,800,850,800
			width: 8
		Color: 
			rgba:300,1100,0, 1
		Rectangle: 
			pos:300,1100
			size:4,4
		Color: 
			rgba:300,300,0, 1
		Rectangle: 
			pos:300,300
			size:1000,1000
		Color: 
			rgba:1000,800,700,200
		Line: 
			points: 1000,800,700,200
			width: 2
		Line: 
			points: 1000,800,600,1000
			width: 2
		Line: 
			points: 1000,600,600,600
			width: 2
		Line: 
			points: 1000,200,600,200
			width: 2
		Color: 
			rgba:0, 1,300,300
		Line: 
			points: 300,300,300,350
			width: 3
		Line: 
			points: 300,300,350,300
			width: 3
		Color: 
			rgba:800,300,0, 1
		Rectangle: 
			pos:800,300
			size:800,800
		Color: 
			rgba:0, 1,200,1100
		Line: 
			points: 200,1100,200,1150
			width: 4
		Line: 
			points: 200,1100,250,1100
			width: 4
		Color: 
			rgba:500,900,0, 1
		Rectangle: 
			pos:500,900
			size:3,3
		Color: 
			rgba:1100,500,400,600
		Line: 
			points: 1100,500,400,600
			width: 8
		Line: 
			points: 1100,500,850,1100
			width: 8
		Line: 
			points: 1100,850,850,850
			width: 8
		Line: 
			points: 1100,600,850,600
			width: 8
		Color: 
			rgba:1100,200,1100,400
		Line: 
			points: 1100,200,1100,400
			width: 7
		Line: 
			points: 1100,200,750,1100
			width: 7
		Line: 
			points: 1100,750,750,750
			width: 7
		Line: 
			points: 1100,400,750,400
			width: 7
		Color: 
			rgba:0, 1,400,400
		Line: 
			points: 400,400,400,450
			width: 1
		Line: 
			points: 400,400,450,400
			width: 1
		Color: 
			rgba:300,700,200,100
		Line: 
			points: 300,700,200,100
			width: 8
		Line: 
			points: 300,700,200,300
			width: 8
		Line: 
			points: 300,200,200,200
			width: 8
		Line: 
			points: 300,100,200,100
			width: 8
		Color: 
			rgba:900,600,400,100
		Line: 
			points: 900,600,400,100
			width: 7
		Line: 
			points: 900,600,500,900
			width: 7
		Line: 
			points: 900,500,500,500
			width: 7
		Line: 
			points: 900,100,500,100
			width: 7
		Color: 
			rgba:900,900,1100,100
		Line: 
			points: 900,900,1100,100
			width: 5
		Line: 
			points: 900,900,500,900
			width: 5
		Line: 
			points: 900,500,500,500
			width: 5
		Line: 
			points: 900,100,500,100
			width: 5
		Color: 
			rgba:600,600,0, 1
		Rectangle: 
			pos:600,600
			size:900,900
		Color: 
			rgba:200,200,100,900
		Line: 
			points: 200,200,100,900
			width: 2
		Line: 
			points: 200,200,550,200
			width: 2
		Line: 
			points: 200,550,550,550
			width: 2
		Line: 
			points: 200,900,550,900
			width: 2
		Color: 
			rgba:1100,300,700,700
		Line: 
			points: 1100,300,700,700
			width: 1
		Line: 
			points: 1100,300,900,1100
			width: 1
		Line: 
			points: 1100,900,900,900
			width: 1
		Line: 
			points: 1100,700,900,700
			width: 1
		Color: 
			rgba:0, 1,700,700
		Line: 
			points: 700,700,700,750
			width: 1
		Line: 
			points: 700,700,750,700
			width: 1
		Color: 
			rgba:300,100,0, 1
		Rectangle: 
			pos:300,100
			size:300,300
		Color: 
			rgba:100,600,0, 1
		Rectangle: 
			pos:100,600
			size:100,100
		Color: 
			rgba:200,600,0, 1
		Rectangle: 
			pos:200,600
			size:5,5
		Color: 
			rgba:500,1000,0, 1
		Rectangle: 
			pos:500,1000
			size:3,3
		Color: 
			rgba:1100,200,0, 1
		Rectangle: 
			pos:1100,200
			size:2,2
		Color: 
			rgba:300,900,0, 1
		Rectangle: 
			pos:300,900
			size:100,100
		Color: 
			rgba:400,1000,0, 1
		Rectangle: 
			pos:400,1000
			size:7,7
		Color: 
			rgba:600,300,200,1000
		Line: 
			points: 600,300,200,1000
			width: 4
		Line: 
			points: 600,300,800,600
			width: 4
		Line: 
			points: 600,800,800,800
			width: 4
		Line: 
			points: 600,1000,800,1000
			width: 4
		Color: 
			rgba:1100,1100,0, 1
		Rectangle: 
			pos:1100,1100
			size:200,200
		Color: 
			rgba:200,900,0, 1
		Rectangle: 
			pos:200,900
			size:6,6
		Color: 
			rgba:700,800,500,700
		Line: 
			points: 700,800,500,700
			width: 5
		Line: 
			points: 700,800,700,700
			width: 5
		Line: 
			points: 700,700,700,700
			width: 5
		Line: 
			points: 700,700,700,700
			width: 5
		Color: 
			rgba:0, 1,800,1000
		Line: 
			points: 800,1000,800,1050
			width: 2
		Line: 
			points: 800,1000,850,1000
			width: 2
		Color: 
			rgba:400,500,0, 1
		Rectangle: 
			pos:400,500
			size:3,3
		Color: 
			rgba:1000,200,1100,1000
		Line: 
			points: 1000,200,1100,1000
			width: 2
		Line: 
			points: 1000,200,1000,1000
			width: 2
		Line: 
			points: 1000,1000,1000,1000
			width: 2
		Line: 
			points: 1000,1000,1000,1000
			width: 2
		Color: 
			rgba:700,600,0, 1
		Rectangle: 
			pos:700,600
			size:1000,1000
		Color: 
			rgba:900,700,0, 1
		Rectangle: 
			pos:900,700
			size:1100,1100
		Color: 
			rgba:1100,1100,900,100
		Line: 
			points: 1100,1100,900,100
			width: 1
		Line: 
			points: 1100,1100,600,1100
			width: 1
		Line: 
			points: 1100,600,600,600
			width: 1
		Line: 
			points: 1100,100,600,100
			width: 1
		Color: 
			rgba:1000,400,0, 1
		Rectangle: 
			pos:1000,400
			size:2,2
		Color: 
			rgba:500,1100,0, 1
		Rectangle: 
			pos:500,1100
			size:7,7
		Color: 
			rgba:700,1100,900,300
		Line: 
			points: 700,1100,900,300
			width: 6
		Line: 
			points: 700,1100,500,700
			width: 6
		Line: 
			points: 700,500,500,500
			width: 6
		Line: 
			points: 700,300,500,300
			width: 6
		Color: 
			rgba:200,700,0, 1
		Rectangle: 
			pos:200,700
			size:500,500
		Color: 
			rgba:800,1100,0, 1
		Rectangle: 
			pos:800,1100
			size:500,500
		Color: 
			rgba:0, 1,200,1100
		Line: 
			points: 200,1100,200,1150
			width: 7
		Line: 
			points: 200,1100,250,1100
			width: 7
		Color: 
			rgba:100,1000,400,300
		Line: 
			points: 100,1000,400,300
			width: 6
		Line: 
			points: 100,1000,200,100
			width: 6
		Line: 
			points: 100,200,200,200
			width: 6
		Line: 
			points: 100,300,200,300
			width: 6
		Color: 
			rgba:100,700,0, 1
		Rectangle: 
			pos:100,700
			size:4,4
		Color: 
			rgba:0, 1,600,100
		Line: 
			points: 600,100,600,150
			width: 4
		Line: 
			points: 600,100,650,100
			width: 4
		Color: 
			rgba:400,900,1100,500
		Line: 
			points: 400,900,1100,500
			width: 1
		Line: 
			points: 400,900,450,400
			width: 1
		Line: 
			points: 400,450,450,450
			width: 1
		Line: 
			points: 400,500,450,500
			width: 1
		Color: 
			rgba:800,400,0, 1
		Rectangle: 
			pos:800,400
			size:6,6
		Color: 
			rgba:200,100,0, 1
		Rectangle: 
			pos:200,100
			size:600,600
		Color: 
			rgba:600,700,0, 1
		Rectangle: 
			pos:600,700
			size:7,7
		Color: 
			rgba:600,800,700,200
		Line: 
			points: 600,800,700,200
			width: 3
		Line: 
			points: 600,800,400,600
			width: 3
		Line: 
			points: 600,400,400,400
			width: 3
		Line: 
			points: 600,200,400,200
			width: 3
		Color: 
			rgba:0, 1,400,500
		Line: 
			points: 400,500,400,550
			width: 4
		Line: 
			points: 400,500,450,500
			width: 4
		Color: 
			rgba:1100,900,0, 1
		Rectangle: 
			pos:1100,900
			size:3,3
		Color: 
			rgba:200,800,0, 1
		Rectangle: 
			pos:200,800
			size:2,2
		Color: 
			rgba:1100,1100,0, 1
		Rectangle: 
			pos:1100,1100
			size:1000,1000
		Color: 
			rgba:800,500,1000,400
		Line: 
			points: 800,500,1000,400
			width: 3
		Line: 
			points: 800,500,600,800
			width: 3
		Line: 
			points: 800,600,600,600
			width: 3
		Line: 
			points: 800,400,600,400
			width: 3
		Color: 
			rgba:0, 1,1100,500
		Line: 
			points: 1100,500,1100,550
			width: 6
		Line: 
			points: 1100,500,1150,500
			width: 6
		Color: 
			rgba:400,100,0, 1
		Rectangle: 
			pos:400,100
			size:6,6
		Color: 
			rgba:900,900,0, 1
		Rectangle: 
			pos:900,900
			size:200,200
		Color: 
			rgba:500,600,0, 1
		Rectangle: 
			pos:500,600
			size:8,8
		Color: 
			rgba:300,200,0, 1
		Rectangle: 
			pos:300,200
			size:1100,1100
		Color: 
			rgba:300,1100,700,800
		Line: 
			points: 300,1100,700,800
			width: 3
		Line: 
			points: 300,1100,550,300
			width: 3
		Line: 
			points: 300,550,550,550
			width: 3
		Line: 
			points: 300,800,550,800
			width: 3
		Color: 
			rgba:0, 1,900,200
		Line: 
			points: 900,200,900,250
			width: 1
		Line: 
			points: 900,200,950,200
			width: 1
		Color: 
			rgba:800,400,0, 1
		Rectangle: 
			pos:800,400
			size:6,6
		Color: 
			rgba:1100,100,0, 1
		Rectangle: 
			pos:1100,100
			size:900,900
		Color: 
			rgba:0, 1,500,1100
		Line: 
			points: 500,1100,500,1150
			width: 8
		Line: 
			points: 500,1100,550,1100
			width: 8
		Color: 
			rgba:800,200,100,1000
		Line: 
			points: 800,200,100,1000
			width: 2
		Line: 
			points: 800,200,900,800
			width: 2
		Line: 
			points: 800,900,900,900
			width: 2
		Line: 
			points: 800,1000,900,1000
			width: 2
		Color: 
			rgba:0, 1,800,900
		Line: 
			points: 800,900,800,950
			width: 3
		Line: 
			points: 800,900,850,900
			width: 3
		Color: 
			rgba:0, 1,1100,1100
		Line: 
			points: 1100,1100,1100,1150
			width: 8
		Line: 
			points: 1100,1100,1150,1100
			width: 8
		Color: 
			rgba:900,700,0, 1
		Rectangle: 
			pos:900,700
			size:500,500
		Color: 
			rgba:0, 1,100,500
		Line: 
			points: 100,500,100,550
			width: 7
		Line: 
			points: 100,500,150,500
			width: 7
		Color: 
			rgba:100,200,0, 1
		Rectangle: 
			pos:100,200
			size:2,2
		Color: 
			rgba:0, 1,400,1100
		Line: 
			points: 400,1100,400,1150
			width: 6
		Line: 
			points: 400,1100,450,1100
			width: 6
		Color: 
			rgba:0, 1,500,900
		Line: 
			points: 500,900,500,950
			width: 6
		Line: 
			points: 500,900,550,900
			width: 6
		Color: 
			rgba:200,600,0, 1
		Rectangle: 
			pos:200,600
			size:5,5
		Color: 
			rgba:0, 1,600,900
		Line: 
			points: 600,900,600,950
			width: 2
		Line: 
			points: 600,900,650,900
			width: 2
		Color: 
			rgba:700,700,0, 1
		Rectangle: 
			pos:700,700
			size:500,500
		Color: 
			rgba:800,500,0, 1
		Rectangle: 
			pos:800,500
			size:1100,1100
		Color: 
			rgba:400,400,0, 1
		Rectangle: 
			pos:400,400
			size:200,200
		Color: 
			rgba:800,600,300,600
		Line: 
			points: 800,600,300,600
			width: 2
		Line: 
			points: 800,600,700,800
			width: 2
		Line: 
			points: 800,700,700,700
			width: 2
		Line: 
			points: 800,600,700,600
			width: 2
		Color: 
			rgba:1100,500,600,700
		Line: 
			points: 1100,500,600,700
			width: 6
		Line: 
			points: 1100,500,900,1100
			width: 6
		Line: 
			points: 1100,900,900,900
			width: 6
		Line: 
			points: 1100,700,900,700
			width: 6
		Color: 
			rgba:900,600,0, 1
		Rectangle: 
			pos:900,600
			size:1,1
		Color: 
			rgba:1000,1100,0, 1
		Rectangle: 
			pos:1000,1100
			size:700,700
		Color: 
			rgba:0, 1,400,1000
		Line: 
			points: 400,1000,400,1050
			width: 7
		Line: 
			points: 400,1000,450,1000
			width: 7
		Color: 
			rgba:500,800,1100,700
		Line: 
			points: 500,800,1100,700
			width: 3
		Line: 
			points: 500,800,600,500
			width: 3
		Line: 
			points: 500,600,600,600
			width: 3
		Line: 
			points: 500,700,600,700
			width: 3
		Color: 
			rgba:300,800,500,1000
		Line: 
			points: 300,800,500,1000
			width: 3
		Line: 
			points: 300,800,650,300
			width: 3
		Line: 
			points: 300,650,650,650
			width: 3
		Line: 
			points: 300,1000,650,1000
			width: 3
		Color: 
			rgba:800,1000,0, 1
		Rectangle: 
			pos:800,1000
			size:3,3
		Color: 
			rgba:600,800,0, 1
		Rectangle: 
			pos:600,800
			size:4,4
		Color: 
			rgba:0, 1,500,600
		Line: 
			points: 500,600,500,650
			width: 8
		Line: 
			points: 500,600,550,600
			width: 8
		Color: 
			rgba:900,300,0, 1
		Rectangle: 
			pos:900,300
			size:1000,1000
		Color: 
			rgba:0, 1,100,800
		Line: 
			points: 100,800,100,850
			width: 8
		Line: 
			points: 100,800,150,800
			width: 8
		Color: 
			rgba:0, 1,1000,700
		Line: 
			points: 1000,700,1000,750
			width: 5
		Line: 
			points: 1000,700,1050,700
			width: 5
		Color: 
			rgba:0, 1,100,1100
		Line: 
			points: 100,1100,100,1150
			width: 8
		Line: 
			points: 100,1100,150,1100
			width: 8
		Color: 
			rgba:0, 1,700,400
		Line: 
			points: 700,400,700,450
			width: 5
		Line: 
			points: 700,400,750,400
			width: 5
		Color: 
			rgba:0, 1,700,200
		Line: 
			points: 700,200,700,250
			width: 6
		Line: 
			points: 700,200,750,200
			width: 6
		Color: 
			rgba:0, 1,400,900
		Line: 
			points: 400,900,400,950
			width: 5
		Line: 
			points: 400,900,450,900
			width: 5
		Color: 
			rgba:1100,400,1000,600
		Line: 
			points: 1100,400,1000,600
			width: 3
		Line: 
			points: 1100,400,850,1100
			width: 3
		Line: 
			points: 1100,850,850,850
			width: 3
		Line: 
			points: 1100,600,850,600
			width: 3
		Color: 
			rgba:1100,600,0, 1
		Rectangle: 
			pos:1100,600
			size:1100,1100
		Color: 
			rgba:0, 1,600,100
		Line: 
			points: 600,100,600,150
			width: 3
		Line: 
			points: 600,100,650,100
			width: 3
		Color: 
			rgba:700,900,500,800
		Line: 
			points: 700,900,500,800
			width: 5
		Line: 
			points: 700,900,750,700
			width: 5
		Line: 
			points: 700,750,750,750
			width: 5
		Line: 
			points: 700,800,750,800
			width: 5
		Color: 
			rgba:200,400,0, 1
		Rectangle: 
			pos:200,400
			size:6,6
		Color: 
			rgba:400,1100,0, 1
		Rectangle: 
			pos:400,1100
			size:7,7
		Color: 
			rgba:0, 1,200,100
		Line: 
			points: 200,100,200,150
			width: 6
		Line: 
			points: 200,100,250,100
			width: 6
		Color: 
			rgba:0, 1,900,400
		Line: 
			points: 900,400,900,450
			width: 7
		Line: 
			points: 900,400,950,400
			width: 7
		Color: 
			rgba:800,500,0, 1
		Rectangle: 
			pos:800,500
			size:7,7
		Color: 
			rgba:0, 1,200,1000
		Line: 
			points: 200,1000,200,1050
			width: 6
		Line: 
			points: 200,1000,250,1000
			width: 6
		Color: 
			rgba:800,400,800,700
		Line: 
			points: 800,400,800,700
			width: 2
		Line: 
			points: 800,400,750,800
			width: 2
		Line: 
			points: 800,750,750,750
			width: 2
		Line: 
			points: 800,700,750,700
			width: 2
		Color: 
			rgba:400,600,100,100
		Line: 
			points: 400,600,100,100
			width: 6
		Line: 
			points: 400,600,250,400
			width: 6
		Line: 
			points: 400,250,250,250
			width: 6
		Line: 
			points: 400,100,250,100
			width: 6
		Color: 
			rgba:0, 1,700,900
		Line: 
			points: 700,900,700,950
			width: 8
		Line: 
			points: 700,900,750,900
			width: 8
		Color: 
			rgba:200,400,0, 1
		Rectangle: 
			pos:200,400
			size:8,8
		Color: 
			rgba:300,500,0, 1
		Rectangle: 
			pos:300,500
			size:200,200
		Color: 
			rgba:500,400,400,600
		Line: 
			points: 500,400,400,600
			width: 8
		Line: 
			points: 500,400,550,500
			width: 8
		Line: 
			points: 500,550,550,550
			width: 8
		Line: 
			points: 500,600,550,600
			width: 8
		Color: 
			rgba:400,1100,1100,700
		Line: 
			points: 400,1100,1100,700
			width: 7
		Line: 
			points: 400,1100,550,400
			width: 7
		Line: 
			points: 400,550,550,550
			width: 7
		Line: 
			points: 400,700,550,700
			width: 7
		Color: 
			rgba:200,500,0, 1
		Rectangle: 
			pos:200,500
			size:5,5
		Color: 
			rgba:600,500,0, 1
		Rectangle: 
			pos:600,500
			size:5,5
		Color: 
			rgba:600,1000,0, 1
		Rectangle: 
			pos:600,1000
			size:400,400
		Color: 
			rgba:400,300,0, 1
		Rectangle: 
			pos:400,300
			size:900,900
		Color: 
			rgba:0, 1,900,500
		Line: 
			points: 900,500,900,550
			width: 8
		Line: 
			points: 900,500,950,500
			width: 8
		Color: 
			rgba:100,600,500,100
		Line: 
			points: 100,600,500,100
			width: 5
		Line: 
			points: 100,600,100,100
			width: 5
		Line: 
			points: 100,100,100,100
			width: 5
		Line: 
			points: 100,100,100,100
			width: 5
		Color: 
			rgba:100,300,1000,1000
		Line: 
			points: 100,300,1000,1000
			width: 6
		Line: 
			points: 100,300,550,100
			width: 6
		Line: 
			points: 100,550,550,550
			width: 6
		Line: 
			points: 100,1000,550,1000
			width: 6
		Color: 
			rgba:700,900,900,600
		Line: 
			points: 700,900,900,600
			width: 7
		Line: 
			points: 700,900,650,700
			width: 7
		Line: 
			points: 700,650,650,650
			width: 7
		Line: 
			points: 700,600,650,600
			width: 7
		Color: 
			rgba:0, 1,600,800
		Line: 
			points: 600,800,600,850
			width: 5
		Line: 
			points: 600,800,650,800
			width: 5
		Color: 
			rgba:1000,500,0, 1
		Rectangle: 
			pos:1000,500
			size:5,5
		Color: 
			rgba:1000,900,1100,500
		Line: 
			points: 1000,900,1100,500
			width: 1
		Line: 
			points: 1000,900,750,1000
			width: 1
		Line: 
			points: 1000,750,750,750
			width: 1
		Line: 
			points: 1000,500,750,500
			width: 1
		Color: 
			rgba:0, 1,600,500
		Line: 
			points: 600,500,600,550
			width: 1
		Line: 
			points: 600,500,650,500
			width: 1
		Color: 
			rgba:200,300,0, 1
		Rectangle: 
			pos:200,300
			size:5,5
		Color: 
			rgba:0, 1,600,500
		Line: 
			points: 600,500,600,550
			width: 2
		Line: 
			points: 600,500,650,500
			width: 2
		Color: 
			rgba:200,600,200,300
		Line: 
			points: 200,600,200,300
			width: 3
		Line: 
			points: 200,600,250,200
			width: 3
		Line: 
			points: 200,250,250,250
			width: 3
		Line: 
			points: 200,300,250,300
			width: 3
		Color: 
			rgba:400,500,0, 1
		Rectangle: 
			pos:400,500
			size:200,200
		Color: 
			rgba:1000,1000,0, 1
		Rectangle: 
			pos:1000,1000
			size:700,700
		Color: 
			rgba:500,900,700,200
		Line: 
			points: 500,900,700,200
			width: 2
		Line: 
			points: 500,900,350,500
			width: 2
		Line: 
			points: 500,350,350,350
			width: 2
		Line: 
			points: 500,200,350,200
			width: 2
		Color: 
			rgba:800,600,100,600
		Line: 
			points: 800,600,100,600
			width: 5
		Line: 
			points: 800,600,700,800
			width: 5
		Line: 
			points: 800,700,700,700
			width: 5
		Line: 
			points: 800,600,700,600
			width: 5
		Color: 
			rgba:0, 1,200,300
		Line: 
			points: 200,300,200,350
			width: 8
		Line: 
			points: 200,300,250,300
			width: 8
		Color: 
			rgba:1000,900,0, 1
		Rectangle: 
			pos:1000,900
			size:1000,1000
		Color: 
			rgba:400,1100,0, 1
		Rectangle: 
			pos:400,1100
			size:1100,1100
		Color: 
			rgba:1000,1000,0, 1
		Rectangle: 
			pos:1000,1000
			size:4,4
		Color: 
			rgba:0, 1,100,1100
		Line: 
			points: 100,1100,100,1150
			width: 8
		Line: 
			points: 100,1100,150,1100
			width: 8
		Color: 
			rgba:900,1000,0, 1
		Rectangle: 
			pos:900,1000
			size:200,200
		Color: 
			rgba:800,1100,0, 1
		Rectangle: 
			pos:800,1100
			size:5,5
		Color: 
			rgba:800,600,600,1100
		Line: 
			points: 800,600,600,1100
			width: 4
		Line: 
			points: 800,600,950,800
			width: 4
		Line: 
			points: 800,950,950,950
			width: 4
		Line: 
			points: 800,1100,950,1100
			width: 4
		Color: 
			rgba:1100,200,0, 1
		Rectangle: 
			pos:1100,200
			size:4,4
		Color: 
			rgba:700,300,600,800
		Line: 
			points: 700,300,600,800
			width: 3
		Line: 
			points: 700,300,750,700
			width: 3
		Line: 
			points: 700,750,750,750
			width: 3
		Line: 
			points: 700,800,750,800
			width: 3
		Color: 
			rgba:1000,400,600,500
		Line: 
			points: 1000,400,600,500
			width: 4
		Line: 
			points: 1000,400,750,1000
			width: 4
		Line: 
			points: 1000,750,750,750
			width: 4
		Line: 
			points: 1000,500,750,500
			width: 4
		Color: 
			rgba:200,1100,0, 1
		Rectangle: 
			pos:200,1100
			size:900,900
		Color: 
			rgba:800,900,900,1000
		Line: 
			points: 800,900,900,1000
			width: 2
		Line: 
			points: 800,900,900,800
			width: 2
		Line: 
			points: 800,900,900,900
			width: 2
		Line: 
			points: 800,1000,900,1000
			width: 2
		Color: 
			rgba:100,400,0, 1
		Rectangle: 
			pos:100,400
			size:2,2
		Color: 
			rgba:400,500,100,700
		Line: 
			points: 400,500,100,700
			width: 5
		Line: 
			points: 400,500,550,400
			width: 5
		Line: 
			points: 400,550,550,550
			width: 5
		Line: 
			points: 400,700,550,700
			width: 5
		Color: 
			rgba:0, 1,100,100
		Line: 
			points: 100,100,100,150
			width: 1
		Line: 
			points: 100,100,150,100
			width: 1
		Color: 
			rgba:0, 1,900,1100
		Line: 
			points: 900,1100,900,1150
			width: 6
		Line: 
			points: 900,1100,950,1100
			width: 6
		Color: 
			rgba:800,300,200,1100
		Line: 
			points: 800,300,200,1100
			width: 8
		Line: 
			points: 800,300,950,800
			width: 8
		Line: 
			points: 800,950,950,950
			width: 8
		Line: 
			points: 800,1100,950,1100
			width: 8
		Color: 
			rgba:1100,300,0, 1
		Rectangle: 
			pos:1100,300
			size:300,300
		Color: 
			rgba:600,1100,0, 1
		Rectangle: 
			pos:600,1100
			size:7,7
		Color: 
			rgba:100,1100,100,700
		Line: 
			points: 100,1100,100,700
			width: 2
		Line: 
			points: 100,1100,400,100
			width: 2
		Line: 
			points: 100,400,400,400
			width: 2
		Line: 
			points: 100,700,400,700
			width: 2
		Color: 
			rgba:0, 1,300,800
		Line: 
			points: 300,800,300,850
			width: 3
		Line: 
			points: 300,800,350,800
			width: 3
		Color: 
			rgba:0, 1,1100,600
		Line: 
			points: 1100,600,1100,650
			width: 7
		Line: 
			points: 1100,600,1150,600
			width: 7
		Color: 
			rgba:800,400,0, 1
		Rectangle: 
			pos:800,400
			size:300,300
		Color: 
			rgba:0, 1,400,1100
		Line: 
			points: 400,1100,400,1150
			width: 3
		Line: 
			points: 400,1100,450,1100
			width: 3
		Color: 
			rgba:700,600,0, 1
		Rectangle: 
			pos:700,600
			size:600,600
		Color: 
			rgba:1100,200,0, 1
		Rectangle: 
			pos:1100,200
			size:7,7
		Color: 
			rgba:1000,400,0, 1
		Rectangle: 
			pos:1000,400
			size:1,1
		Color: 
			rgba:1000,100,0, 1
		Rectangle: 
			pos:1000,100
			size:5,5
		Color: 
			rgba:200,200,0, 1
		Rectangle: 
			pos:200,200
			size:1,1
		Color: 
			rgba:0, 1,800,800
		Line: 
			points: 800,800,800,850
			width: 1
		Line: 
			points: 800,800,850,800
			width: 1
		Color: 
			rgba:400,800,0, 1
		Rectangle: 
			pos:400,800
			size:6,6
		Color: 
			rgba:0, 1,1000,300
		Line: 
			points: 1000,300,1000,350
			width: 1
		Line: 
			points: 1000,300,1050,300
			width: 1
		Color: 
			rgba:0, 1,500,1000
		Line: 
			points: 500,1000,500,1050
			width: 8
		Line: 
			points: 500,1000,550,1000
			width: 8
		Color: 
			rgba:200,300,0, 1
		Rectangle: 
			pos:200,300
			size:5,5
		Color: 
			rgba:600,300,0, 1
		Rectangle: 
			pos:600,300
			size:200,200
		Color: 
			rgba:600,400,0, 1
		Rectangle: 
			pos:600,400
			size:400,400
		Color: 
			rgba:500,400,0, 1
		Rectangle: 
			pos:500,400
			size:400,400
		Color: 
			rgba:300,1100,700,100
		Line: 
			points: 300,1100,700,100
			width: 1
		Line: 
			points: 300,1100,200,300
			width: 1
		Line: 
			points: 300,200,200,200
			width: 1
		Line: 
			points: 300,100,200,100
			width: 1
		Color: 
			rgba:300,200,800,100
		Line: 
			points: 300,200,800,100
			width: 7
		Line: 
			points: 300,200,200,300
			width: 7
		Line: 
			points: 300,200,200,200
			width: 7
		Line: 
			points: 300,100,200,100
			width: 7
		Color: 
			rgba:200,300,0, 1
		Rectangle: 
			pos:200,300
			size:900,900
		Color: 
			rgba:1100,500,0, 1
		Rectangle: 
			pos:1100,500
			size:1,1
		Color: 
			rgba:0, 1,1000,100
		Line: 
			points: 1000,100,1000,150
			width: 8
		Line: 
			points: 1000,100,1050,100
			width: 8
		Color: 
			rgba:300,200,0, 1
		Rectangle: 
			pos:300,200
			size:5,5
		Color: 
			rgba:300,400,0, 1
		Rectangle: 
			pos:300,400
			size:600,600
		Color: 
			rgba:0, 1,800,600
		Line: 
			points: 800,600,800,650
			width: 6
		Line: 
			points: 800,600,850,600
			width: 6
		Color: 
			rgba:900,200,800,700
		Line: 
			points: 900,200,800,700
			width: 7
		Line: 
			points: 900,200,800,900
			width: 7
		Line: 
			points: 900,800,800,800
			width: 7
		Line: 
			points: 900,700,800,700
			width: 7
		Color: 
			rgba:100,300,0, 1
		Rectangle: 
			pos:100,300
			size:900,900
		Color: 
			rgba:300,300,0, 1
		Rectangle: 
			pos:300,300
			size:300,300
		Color: 
			rgba:1100,300,0, 1
		Rectangle: 
			pos:1100,300
			size:200,200
		Color: 
			rgba:500,600,0, 1
		Rectangle: 
			pos:500,600
			size:3,3
		Color: 
			rgba:0, 1,300,1000
		Line: 
			points: 300,1000,300,1050
			width: 4
		Line: 
			points: 300,1000,350,1000
			width: 4
		Color: 
			rgba:0, 1,900,200
		Line: 
			points: 900,200,900,250
			width: 7
		Line: 
			points: 900,200,950,200
			width: 7
		Color: 
			rgba:600,300,0, 1
		Rectangle: 
			pos:600,300
			size:900,900
		Color: 
			rgba:700,700,500,300
		Line: 
			points: 700,700,500,300
			width: 8
		Line: 
			points: 700,700,500,700
			width: 8
		Line: 
			points: 700,500,500,500
			width: 8
		Line: 
			points: 700,300,500,300
			width: 8
		Color: 
			rgba:1100,400,1100,500
		Line: 
			points: 1100,400,1100,500
			width: 5
		Line: 
			points: 1100,400,800,1100
			width: 5
		Line: 
			points: 1100,800,800,800
			width: 5
		Line: 
			points: 1100,500,800,500
			width: 5
		Color: 
			rgba:700,600,0, 1
		Rectangle: 
			pos:700,600
			size:5,5
		Color: 
			rgba:500,400,0, 1
		Rectangle: 
			pos:500,400
			size:6,6
		Color: 
			rgba:200,900,700,100
		Line: 
			points: 200,900,700,100
			width: 2
		Line: 
			points: 200,900,150,200
			width: 2
		Line: 
			points: 200,150,150,150
			width: 2
		Line: 
			points: 200,100,150,100
			width: 2
		Color: 
			rgba:400,1100,0, 1
		Rectangle: 
			pos:400,1100
			size:800,800
		Color: 
			rgba:500,400,0, 1
		Rectangle: 
			pos:500,400
			size:1000,1000
		Color: 
			rgba:600,900,0, 1
		Rectangle: 
			pos:600,900
			size:100,100
		Color: 
			rgba:0, 1,900,700
		Line: 
			points: 900,700,900,750
			width: 8
		Line: 
			points: 900,700,950,700
			width: 8
		Color: 
			rgba:200,300,0, 1
		Rectangle: 
			pos:200,300
			size:700,700
		Color: 
			rgba:800,800,400,1000
		Line: 
			points: 800,800,400,1000
			width: 5
		Line: 
			points: 800,800,900,800
			width: 5
		Line: 
			points: 800,900,900,900
			width: 5
		Line: 
			points: 800,1000,900,1000
			width: 5
		Color: 
			rgba:0, 1,300,1000
		Line: 
			points: 300,1000,300,1050
			width: 6
		Line: 
			points: 300,1000,350,1000
			width: 6
		Color: 
			rgba:1000,1000,0, 1
		Rectangle: 
			pos:1000,1000
			size:4,4
		Color: 
			rgba:500,900,1100,1000
		Line: 
			points: 500,900,1100,1000
			width: 5
		Line: 
			points: 500,900,750,500
			width: 5
		Line: 
			points: 500,750,750,750
			width: 5
		Line: 
			points: 500,1000,750,1000
			width: 5
		Color: 
			rgba:300,100,0, 1
		Rectangle: 
			pos:300,100
			size:5,5
		Color: 
			rgba:200,1000,500,200
		Line: 
			points: 200,1000,500,200
			width: 7
		Line: 
			points: 200,1000,200,200
			width: 7
		Line: 
			points: 200,200,200,200
			width: 7
		Line: 
			points: 200,200,200,200
			width: 7
		Color: 
			rgba:600,800,1000,300
		Line: 
			points: 600,800,1000,300
			width: 7
		Line: 
			points: 600,800,450,600
			width: 7
		Line: 
			points: 600,450,450,450
			width: 7
		Line: 
			points: 600,300,450,300
			width: 7
		Color: 
			rgba:100,900,0, 1
		Rectangle: 
			pos:100,900
			size:7,7
		Color: 
			rgba:0, 1,900,200
		Line: 
			points: 900,200,900,250
			width: 2
		Line: 
			points: 900,200,950,200
			width: 2
		Color: 
			rgba:300,800,0, 1
		Rectangle: 
			pos:300,800
			size:100,100
		Color: 
			rgba:500,200,300,1000
		Line: 
			points: 500,200,300,1000
			width: 2
		Line: 
			points: 500,200,750,500
			width: 2
		Line: 
			points: 500,750,750,750
			width: 2
		Line: 
			points: 500,1000,750,1000
			width: 2
		Color: 
			rgba:400,800,0, 1
		Rectangle: 
			pos:400,800
			size:400,400
		Color: 
			rgba:600,100,0, 1
		Rectangle: 
			pos:600,100
			size:8,8
		Color: 
			rgba:800,900,0, 1
		Rectangle: 
			pos:800,900
			size:600,600
		Color: 
			rgba:400,300,700,1000
		Line: 
			points: 400,300,700,1000
			width: 2
		Line: 
			points: 400,300,700,400
			width: 2
		Line: 
			points: 400,700,700,700
			width: 2
		Line: 
			points: 400,1000,700,1000
			width: 2
		Color: 
			rgba:1000,800,0, 1
		Rectangle: 
			pos:1000,800
			size:1,1
		Color: 
			rgba:1100,100,0, 1
		Rectangle: 
			pos:1100,100
			size:5,5
		Color: 
			rgba:500,1100,200,400
		Line: 
			points: 500,1100,200,400
			width: 8
		Line: 
			points: 500,1100,450,500
			width: 8
		Line: 
			points: 500,450,450,450
			width: 8
		Line: 
			points: 500,400,450,400
			width: 8
		Color: 
			rgba:300,300,800,800
		Line: 
			points: 300,300,800,800
			width: 7
		Line: 
			points: 300,300,550,300
			width: 7
		Line: 
			points: 300,550,550,550
			width: 7
		Line: 
			points: 300,800,550,800
			width: 7
		Color: 
			rgba:100,1100,100,700
		Line: 
			points: 100,1100,100,700
			width: 1
		Line: 
			points: 100,1100,400,100
			width: 1
		Line: 
			points: 100,400,400,400
			width: 1
		Line: 
			points: 100,700,400,700
			width: 1
		Color: 
			rgba:1100,100,0, 1
		Rectangle: 
			pos:1100,100
			size:100,100
		Color: 
			rgba:100,400,0, 1
		Rectangle: 
			pos:100,400
			size:900,900
		Color: 
			rgba:700,700,0, 1
		Rectangle: 
			pos:700,700
			size:8,8
		Color: 
			rgba:200,800,1000,100
		Line: 
			points: 200,800,1000,100
			width: 8
		Line: 
			points: 200,800,150,200
			width: 8
		Line: 
			points: 200,150,150,150
			width: 8
		Line: 
			points: 200,100,150,100
			width: 8
		Color: 
			rgba:900,900,700,200
		Line: 
			points: 900,900,700,200
			width: 2
		Line: 
			points: 900,900,550,900
			width: 2
		Line: 
			points: 900,550,550,550
			width: 2
		Line: 
			points: 900,200,550,200
			width: 2
		Color: 
			rgba:1100,900,0, 1
		Rectangle: 
			pos:1100,900
			size:300,300
		Color: 
			rgba:400,100,0, 1
		Rectangle: 
			pos:400,100
			size:1,1
		Color: 
			rgba:0, 1,600,700
		Line: 
			points: 600,700,600,750
			width: 1
		Line: 
			points: 600,700,650,700
			width: 1
		Color: 
			rgba:600,800,0, 1
		Rectangle: 
			pos:600,800
			size:7,7
		Color: 
			rgba:100,100,0, 1
		Rectangle: 
			pos:100,100
			size:3,3
		Color: 
			rgba:0, 1,800,200
		Line: 
			points: 800,200,800,250
			width: 4
		Line: 
			points: 800,200,850,200
			width: 4
		Color: 
			rgba:100,1000,0, 1
		Rectangle: 
			pos:100,1000
			size:3,3
		Color: 
			rgba:500,900,0, 1
		Rectangle: 
			pos:500,900
			size:7,7
		Color: 
			rgba:0, 1,600,1100
		Line: 
			points: 600,1100,600,1150
			width: 5
		Line: 
			points: 600,1100,650,1100
			width: 5
		Color: 
			rgba:300,1000,0, 1
		Rectangle: 
			pos:300,1000
			size:1000,1000
		Color: 
			rgba:200,700,0, 1
		Rectangle: 
			pos:200,700
			size:7,7
		Color: 
			rgba:200,1000,0, 1
		Rectangle: 
			pos:200,1000
			size:200,200
		Color: 
			rgba:700,1000,0, 1
		Rectangle: 
			pos:700,1000
			size:200,200
		Color: 
			rgba:900,500,0, 1
		Rectangle: 
			pos:900,500
			size:5,5
		Color: 
			rgba:0, 1,900,1000
		Line: 
			points: 900,1000,900,1050
			width: 2
		Line: 
			points: 900,1000,950,1000
			width: 2
		Color: 
			rgba:700,100,900,300
		Line: 
			points: 700,100,900,300
			width: 2
		Line: 
			points: 700,100,500,700
			width: 2
		Line: 
			points: 700,500,500,500
			width: 2
		Line: 
			points: 700,300,500,300
			width: 2
		Color: 
			rgba:200,1100,0, 1
		Rectangle: 
			pos:200,1100
			size:7,7
		Color: 
			rgba:600,500,0, 1
		Rectangle: 
			pos:600,500
			size:300,300
		Color: 
			rgba:800,1100,0, 1
		Rectangle: 
			pos:800,1100
			size:4,4
		Color: 
			rgba:900,500,400,1000
		Line: 
			points: 900,500,400,1000
			width: 7
		Line: 
			points: 900,500,950,900
			width: 7
		Line: 
			points: 900,950,950,950
			width: 7
		Line: 
			points: 900,1000,950,1000
			width: 7
		Color: 
			rgba:0, 1,300,800
		Line: 
			points: 300,800,300,850
			width: 4
		Line: 
			points: 300,800,350,800
			width: 4
		Color: 
			rgba:700,500,0, 1
		Rectangle: 
			pos:700,500
			size:2,2
		Color: 
			rgba:400,900,0, 1
		Rectangle: 
			pos:400,900
			size:1,1
		Color: 
			rgba:0, 1,100,1000
		Line: 
			points: 100,1000,100,1050
			width: 8
		Line: 
			points: 100,1000,150,1000
			width: 8
		Color: 
			rgba:700,300,0, 1
		Rectangle: 
			pos:700,300
			size:3,3
		Color: 
			rgba:800,300,0, 1
		Rectangle: 
			pos:800,300
			size:4,4
		Color: 
			rgba:100,400,800,300
		Line: 
			points: 100,400,800,300
			width: 5
		Line: 
			points: 100,400,200,100
			width: 5
		Line: 
			points: 100,200,200,200
			width: 5
		Line: 
			points: 100,300,200,300
			width: 5
		Color: 
			rgba:0, 1,100,300
		Line: 
			points: 100,300,100,350
			width: 4
		Line: 
			points: 100,300,150,300
			width: 4
		Color: 
			rgba:700,800,800,100
		Line: 
			points: 700,800,800,100
			width: 2
		Line: 
			points: 700,800,400,700
			width: 2
		Line: 
			points: 700,400,400,400
			width: 2
		Line: 
			points: 700,100,400,100
			width: 2
		Color: 
			rgba:0, 1,500,900
		Line: 
			points: 500,900,500,950
			width: 4
		Line: 
			points: 500,900,550,900
			width: 4
		Color: 
			rgba:1000,1000,0, 1
		Rectangle: 
			pos:1000,1000
			size:6,6
		Color: 
			rgba:600,500,0, 1
		Rectangle: 
			pos:600,500
			size:4,4
		Color: 
			rgba:200,500,0, 1
		Rectangle: 
			pos:200,500
			size:1100,1100
		Color: 
			rgba:400,700,0, 1
		Rectangle: 
			pos:400,700
			size:1100,1100
		Color: 
			rgba:300,300,0, 1
		Rectangle: 
			pos:300,300
			size:900,900
		Color: 
			rgba:0, 1,800,1100
		Line: 
			points: 800,1100,800,1150
			width: 4
		Line: 
			points: 800,1100,850,1100
			width: 4
		Color: 
			rgba:0, 1,700,700
		Line: 
			points: 700,700,700,750
			width: 4
		Line: 
			points: 700,700,750,700
			width: 4
		Color: 
			rgba:200,900,0, 1
		Rectangle: 
			pos:200,900
			size:800,800
		Color: 
			rgba:500,200,0, 1
		Rectangle: 
			pos:500,200
			size:8,8
		Color: 
			rgba:100,500,800,400
		Line: 
			points: 100,500,800,400
			width: 1
		Line: 
			points: 100,500,250,100
			width: 1
		Line: 
			points: 100,250,250,250
			width: 1
		Line: 
			points: 100,400,250,400
			width: 1
		Color: 
			rgba:1100,700,0, 1
		Rectangle: 
			pos:1100,700
			size:700,700
		Color: 
			rgba:1000,400,0, 1
		Rectangle: 
			pos:1000,400
			size:3,3
		Color: 
			rgba:0, 1,800,300
		Line: 
			points: 800,300,800,350
			width: 7
		Line: 
			points: 800,300,850,300
			width: 7
		Color: 
			rgba:700,1000,0, 1
		Rectangle: 
			pos:700,1000
			size:2,2
		Color: 
			rgba:900,500,100,900
		Line: 
			points: 900,500,100,900
			width: 2
		Line: 
			points: 900,500,900,900
			width: 2
		Line: 
			points: 900,900,900,900
			width: 2
		Line: 
			points: 900,900,900,900
			width: 2
		Color: 
			rgba:800,800,0, 1
		Rectangle: 
			pos:800,800
			size:1000,1000
		Color: 
			rgba:300,900,500,500
		Line: 
			points: 300,900,500,500
			width: 4
		Line: 
			points: 300,900,400,300
			width: 4
		Line: 
			points: 300,400,400,400
			width: 4
		Line: 
			points: 300,500,400,500
			width: 4
		Color: 
			rgba:1000,800,0, 1
		Rectangle: 
			pos:1000,800
			size:700,700
		Color: 
			rgba:1000,300,0, 1
		Rectangle: 
			pos:1000,300
			size:1100,1100
		Color: 
			rgba:600,1000,500,400
		Line: 
			points: 600,1000,500,400
			width: 2
		Line: 
			points: 600,1000,500,600
			width: 2
		Line: 
			points: 600,500,500,500
			width: 2
		Line: 
			points: 600,400,500,400
			width: 2
		Color: 
			rgba:0, 1,400,100
		Line: 
			points: 400,100,400,150
			width: 2
		Line: 
			points: 400,100,450,100
			width: 2
		Color: 
			rgba:400,700,1100,1100
		Line: 
			points: 400,700,1100,1100
			width: 3
		Line: 
			points: 400,700,750,400
			width: 3
		Line: 
			points: 400,750,750,750
			width: 3
		Line: 
			points: 400,1100,750,1100
			width: 3
		Color: 
			rgba:400,200,0, 1
		Rectangle: 
			pos:400,200
			size:8,8
		Color: 
			rgba:0, 1,300,500
		Line: 
			points: 300,500,300,550
			width: 1
		Line: 
			points: 300,500,350,500
			width: 1
		Color: 
			rgba:0, 1,500,200
		Line: 
			points: 500,200,500,250
			width: 3
		Line: 
			points: 500,200,550,200
			width: 3
		Color: 
			rgba:800,300,0, 1
		Rectangle: 
			pos:800,300
			size:5,5
		Color: 
			rgba:1100,200,0, 1
		Rectangle: 
			pos:1100,200
			size:4,4
		Color: 
			rgba:100,500,0, 1
		Rectangle: 
			pos:100,500
			size:800,800
		Color: 
			rgba:600,400,900,400
		Line: 
			points: 600,400,900,400
			width: 2
		Line: 
			points: 600,400,500,600
			width: 2
		Line: 
			points: 600,500,500,500
			width: 2
		Line: 
			points: 600,400,500,400
			width: 2
		Color: 
			rgba:100,400,500,500
		Line: 
			points: 100,400,500,500
			width: 6
		Line: 
			points: 100,400,300,100
			width: 6
		Line: 
			points: 100,300,300,300
			width: 6
		Line: 
			points: 100,500,300,500
			width: 6
		Color: 
			rgba:300,600,0, 1
		Rectangle: 
			pos:300,600
			size:500,500
		Color: 
			rgba:1100,800,0, 1
		Rectangle: 
			pos:1100,800
			size:400,400
		Color: 
			rgba:200,1000,0, 1
		Rectangle: 
			pos:200,1000
			size:3,3
		Color: 
			rgba:600,900,0, 1
		Rectangle: 
			pos:600,900
			size:2,2
		Color: 
			rgba:900,1100,0, 1
		Rectangle: 
			pos:900,1100
			size:400,400
		Color: 
			rgba:600,100,0, 1
		Rectangle: 
			pos:600,100
			size:800,800
		Color: 
			rgba:800,1000,0, 1
		Rectangle: 
			pos:800,1000
			size:5,5
		Color: 
			rgba:500,600,0, 1
		Rectangle: 
			pos:500,600
			size:4,4
		Color: 
			rgba:100,400,100,1000
		Line: 
			points: 100,400,100,1000
			width: 5
		Line: 
			points: 100,400,550,100
			width: 5
		Line: 
			points: 100,550,550,550
			width: 5
		Line: 
			points: 100,1000,550,1000
			width: 5
		Color: 
			rgba:800,600,1100,800
		Line: 
			points: 800,600,1100,800
			width: 4
		Line: 
			points: 800,600,800,800
			width: 4
		Line: 
			points: 800,800,800,800
			width: 4
		Line: 
			points: 800,800,800,800
			width: 4
''')


class MainApp(App):

    def build(self):
        return root

if __name__ == '__main__':
    MainApp().run()

