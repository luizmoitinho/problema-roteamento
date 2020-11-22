import PySimpleGUI as sg
from src.Router import Router

import time
# import .Main

COLOR_LINE = 'RED'
COLOR_CIRCLE = 'BLACK'


class App:

    def __init__(self):
        # endpoints for search
        self.start = 0
        self.end   = 0

        self.layout = [
            [
                sg.Graph(
                    canvas_size=(650,500),
                    graph_bottom_left=(0,0),
                    graph_top_right=(650, 500),
                    background_color="#ffffff",
                    key="graph"
                ),
            ],
            [sg.Input(key="nodeIn"), sg.Input(key="nodeOut"), sg.Button(key="submit")]
        ]
        
        #initialize the graph
        self.theGraph = Router()
        self.prepare_graph()
    

        self.window = sg.Window('Simulação de Rede', self.layout)
        self.window.Finalize()
        self.graph = self.window.Element('graph')

        self.lineList   = self.prepare_lines()
        self.circleList = self.prepare_circles()

        self.babel = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3,
            'E': 4,
            'F': 5,
            'G': 6,
        }


    def get_value_babel(self, value ):
        for elem in self.babel.keys():
            if(self.babel[elem] == value):
                return elem
        return None

    def prepare_lines(self):
        lineList = {}
        lineList['AC'] =  self.graph.DrawLine((75,340), (225,425),  width=2, color=COLOR_LINE)   # 0
        lineList['AB'] =  self.graph.DrawLine((75,340), (160,200),  width=2, color=COLOR_LINE)   # 0
        lineList['CE'] =  self.graph.DrawLine((225,425), (400,330), width=2, color=COLOR_LINE)   # 0
        lineList['CD'] =  self.graph.DrawLine((225,425), (300,120), width=2, color=COLOR_LINE)   # 0
        lineList['BD'] =  self.graph.DrawLine((160,200), (300,120), width=2, color=COLOR_LINE)   # 0
        lineList['BC'] =  self.graph.DrawLine((160,200), (225,425), width=2, color=COLOR_LINE)   # 0
        lineList['EF'] =  self.graph.DrawLine((400,330), (550,320), width=2, color=COLOR_LINE)   # 0
        lineList['ED'] =  self.graph.DrawLine((400,330), (300,120), width=2, color=COLOR_LINE)   # 0
        lineList['EG'] =  self.graph.DrawLine((400,330), (500,140), width=2, color=COLOR_LINE)   # 0
        lineList['DG'] =  self.graph.DrawLine((300,120), (500,140), width=2, color=COLOR_LINE)   # 0
        return lineList

    def prepare_circles(self):
        circleList = {}
        circleList['A'] =  self.graph.DrawCircle((75,340), 25,  fill_color = COLOR_CIRCLE, line_color='white')  # 0
        circleList['B'] =  self.graph.DrawCircle((160,200), 25, fill_color = COLOR_CIRCLE, line_color='white')  # 1
        circleList['C'] =  self.graph.DrawCircle((225,425), 25, fill_color = COLOR_CIRCLE, line_color='white')  # 2
        circleList['D'] =  self.graph.DrawCircle((300,120), 25, fill_color = COLOR_CIRCLE, line_color='white')  # 3
        circleList['E'] =  self.graph.DrawCircle((400,330), 25, fill_color = COLOR_CIRCLE, line_color='white')  # 4 
        circleList['F'] =  self.graph.DrawCircle((550,320), 25, fill_color = COLOR_CIRCLE, line_color='white')  # 5 
        circleList['G'] =  self.graph.DrawCircle((500,140), 25, fill_color = COLOR_CIRCLE, line_color='white')  # 6 
        return circleList
    
    def prepare_graph(self):
        self.theGraph.addAccess('A') # 0
        self.theGraph.addAccess('B') # 1
        self.theGraph.addAccess('C') # 2
        self.theGraph.addAccess('D') # 3
        self.theGraph.addAccess('E') # 4
        self.theGraph.addAccess('F') # 5
        self.theGraph.addAccess('G') # 6

        self.theGraph.addLink(0, 2, 14)
        self.theGraph.addLink(0, 1, 12)

        self.theGraph.addLink(1, 2, 9)
        self.theGraph.addLink(1, 3, 38)
        
        self.theGraph.addLink(2, 4, 7)
        self.theGraph.addLink(2, 3, 24)
        
        self.theGraph.addLink(3, 6, 9)
        
        self.theGraph.addLink(4, 3, 13)
        self.theGraph.addLink(4, 6, 29)
        self.theGraph.addLink(4, 5, 9)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == "submit":
                self.start = values['nodeIn']
                self.end = values['nodeOut']
                # print(self.babel[self.start],self.babel[self.end])
                path = self.theGraph.ucs(self.babel[self.start],self.babel[self.end])
                # print(path) 
                for elem in path:
                    print(self.get_value_babel(elem))
                        
        self.window.close()
     
    def ucs(self, start, end):
        self.theGraph.ucs(start, end)




#  import PySimpleGUI as sg      

#     layout = [      
#                [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0,0), graph_top_right=(400, 400), background_color='red', key='graph')],      
#                [sg.T('Change circle color to:'), sg.Button('Red'), sg.Button('Blue'), sg.Button('Move')]      
#                ]      

#     window = sg.Window('Graph test', layout)      
#     window.Finalize()      
  
#     circle = graph.DrawCircle((75,75), 25, fill_color='black',line_color='white')      
#     point = graph.DrawPoint((75,75), 10, color='green')      
#     oval = graph.DrawOval((25,300), (100,280), fill_color='purple', line_color='purple'  )      
#     rectangle = graph.DrawRectangle((25,300), (100,280), line_color='purple'  )      
#     line = graph.DrawLine((0,0), (100,100))      

#     while True:      
#         event, values = window.read()      
#         if event == sg.WIN_CLOSED:      
#             break      
#         if event is 'Blue':      
#             graph.TKCanvas.itemconfig(circle, fill = "Blue")      
#         elif event is 'Red':      
#             graph.TKCanvas.itemconfig(circle, fill = "Red")      
#         elif event is 'Move':      
#             graph.MoveFigure(point, 10,10)      
#             graph.MoveFigure(circle, 10,10)      
#             graph.MoveFigure(oval, 10,10)      
#             graph.MoveFigure(rectangle, 10,10) 