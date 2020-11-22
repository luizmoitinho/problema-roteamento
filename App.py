import PySimpleGUI as sg
import time
# import .Main

COLOR_LINE = 'RED'
COLOR_CIRCLE = 'BLACK'

class App:

    def __init__(self):
        
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
            [sg.Input(key="nodeIn")]
        ]
        
        self.window = sg.Window('Simulação de Rede', self.layout)
        self.window.Finalize()
        self.graph = self.window.Element('graph')

        self.lineList   = self.prepare_lines()
        self.circleList = self.prepare_circles()
        
    
    def prepare_lines(self):
        lineList = {}
        lineList['AC'] =  self.graph.DrawLine((75,340), (225,425),  width=2, color=COLOR_LINE)   # 0
        lineList['AB'] =  self.graph.DrawLine((75,340), (160,200),  width=2, color=COLOR_LINE)   # 0
        lineList['CE'] =  self.graph.DrawLine((225,425), (400,330), width=2, color=COLOR_LINE)   # 0
        lineList['CD'] =  self.graph.DrawLine((225,425), (300,120), width=2, color=COLOR_LINE)   # 0
        lineList['BD'] =  self.graph.DrawLine((160,200), (300,120), width=2, color=COLOR_LINE)   # 0
        lineList['EF'] =  self.graph.DrawLine((400,330), (550,320), width=2, color=COLOR_LINE)   # 0
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
    
    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
        self.window.close()





