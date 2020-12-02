import PySimpleGUI as sg
from src.Router import Router

import time

COLOR_LINE = 'black'
COLOR_CIRCLE = 'BLACK'

class App:

    def __init__(self):
        # endpoints for search
        self.start = 0
        self.end   = 0

        self.layout = [
            [
                sg.Graph(
                    canvas_size=(625,500),
                    graph_bottom_left=(0,0),
                    graph_top_right=(625, 500),
                    background_color="#ffffff",
                    key="graph"
                ),
            ],
            [ sg.Text("Rementente") ,sg.Input(key="nodeIn",size=(10,10)), 
              sg.Text("Destinatário"), sg.Input(key="nodeOut",size=(10,10)), sg.Button("Enviar", key="submit"),
              sg.Text("Custo Total: ", key="weight",size=(15, 1))
            ]
            
        ]
        
        #initialize the graph
        self.theGraph = Router()
        self.prepare_graph()
    
        self.window = sg.Window('Simulação de Rede', self.layout)
        self.window.Finalize()
        self.graph = self.window.Element('graph')

        self.lineList   = self.prepare_lines()
        self.circleList = self.prepare_circles()
        self.prepare_labels()
        self.prepare_weight()

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
        lineList['DE'] =  self.graph.DrawLine((400,330), (300,120), width=2, color=COLOR_LINE)   # 0
        lineList['EG'] =  self.graph.DrawLine((400,330), (500,140), width=2, color=COLOR_LINE)   # 0
        lineList['DG'] =  self.graph.DrawLine((300,120), (500,140), width=2, color=COLOR_LINE)   # 0
        return lineList

    def prepare_weight(self):
        self.graph.DrawText(text= '14', location=(150,400), color="black", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= '12', location=(100,268), color="black", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= '7',  location=(330,390), color="black", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= '24', location=(240,270), color="black", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= '9',  location=(180,310), color="black", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= '38', location=(230,140), color="black", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= '13', location=(340,250), color="black", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= '29', location=(430,230), color="black", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= '9',  location=(405,115), color="black", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= '9',  location=(475,343), color="black", font=16, angle=0, text_location="center")
     

    def prepare_circles(self):
        circleList = {}
        circleList['A'] =  self.graph.DrawImage(filename="computer.png", location=(50,365))   # 0
        circleList['B'] =  self.graph.DrawImage(filename="computer.png", location=(135,225))  # 1
        circleList['C'] =  self.graph.DrawImage(filename="computer.png", location=(200,450))  # 2
        circleList['D'] =  self.graph.DrawImage(filename="computer.png", location=(275,145))  # 3
        circleList['E'] =  self.graph.DrawImage(filename="computer.png", location=(375,355))  # 4 
        circleList['F'] =  self.graph.DrawImage(filename="computer.png", location=(525,345))  # 5 
        circleList['G'] =  self.graph.DrawImage(filename="computer.png", location=(475,165))  # 6 
        return circleList
    
    def prepare_labels(self):
        self.graph.DrawText(text= 'A', location=(70,345),   color="white", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= 'B', location=(155,205),  color="white", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= 'C', location=(220,430),  color="white", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= 'D', location=(295, 125), color="white", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= 'E', location=(395, 335), color="white", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= 'F', location=(545, 325), color="white", font=16, angle=0, text_location="center")
        self.graph.DrawText(text= 'G', location=(495, 145), color="white", font=16, angle=0, text_location="center")

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
                self.clean_routes()
                self.start = values['nodeIn'].upper()
                self.end = values['nodeOut'].upper()
                
                if self.start not in self.babel.keys() or self.end not in self.babel.keys():
                    sg.popup_ok('Estado(s) informado(s) não existe(m)', title="Erro",auto_close=False) 
                    continue
                elif self.start == self.end:
                    self.window['weight'].update("Custo Total: 0")
                    continue
                result = self.theGraph.ucs(self.babel[self.start],self.babel[self.end])
                if(len(result) > 0):
                    path   = result[0]
                    weight = result[1]
                    self.window['weight'].update("Custo Total: %d"%(weight))
                    for i in range(len(path) -1):
                        if path[i] < path[i+1]:
                            name = path[i] + path[i+1]
                        else:
                            name = path[i+1] + path[i]
                        self.graph.TKCanvas.itemconfig(self.lineList[name], fill="green", width=4)  
                
        self.window.close()

    def clean_routes(self):
        for line in self.lineList:
            self.graph.TKCanvas.itemconfig(self.lineList[line], fill=COLOR_LINE, width=2)

