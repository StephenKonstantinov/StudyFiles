from enum import Enum
import pygame
CELL_SIZE=50
FPS=60
class Cell(Enum):
    VOID=0
    CROSS=1
    ZERO=2

class Player:
    def __init__(self, name, cell_type):
        self.name=name
        self.cell_type=cell_type



class GameField:
    def __init__(self):
        self.height=3
        self.width=3
        self.cells=[[Cell.VOID]*self.width for i in range(self.height)]


class GameFieldView:
    def __init__(self, field):
        #загрузить картинки клеток, отобразить первичное поле
        self._field=field
        self._height= field.height * CELL_SIZE
        self._width=field.width * CELL_SIZE

    def draw(self):
        pass


    def check_coords_correct(self,x,y):
        return True #TODO self._height

    def get_coords(self, x, y):
        return (x,y) #TODO реально вычислить


class GameRoundManager:
    def __init__(self, player1: Player, player2: Player):
        self._players=[player1, player2]
        self.current_player=0
        self.field= GameField()

    def handle_click(self,x,y):
        player=self._players[self.current_player]
        print('click_handled')
        print (x,' ', y)



class GameWindow:
    def __init__(self):
        pygame.init()
        self._width=800
        self.height=600
        self._title="XO"
        self._screen=pygame.display.set_mode((self._width,self.height))
        pygame.display.set_caption(self._title)
        player1=Player('Петя', Cell.CROSS)
        player2 = Player('Вася', Cell.ZERO)
        self._game_manager=GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)


    def main_loop(self):
        finished=False
        clock=pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x,y = mouse_pos
                    if self._field_widget.check_coords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                    self._game_manager.handle_click(i, j)
            pygame.display.flip()
            clock.tick(FPS)

def main():
    window=GameWindow()
    window.main_loop()
    print('Game OVER')

main()