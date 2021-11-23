import pygame
import numpy
from copy import deepcopy


#declaring colors using RGB

BROWN = (130, 160,136)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
                                #declare the variable we ll need next
ROWS, COLLUMS = 8, 8
squarewidth = 480//COLLUMS


king = pygame.transform.scale(pygame.image.load('king.jpg'), (44, 25))  #loading picture for crown on the table
WIN = pygame.display.set_mode((480, 480))
pygame.display.set_caption('Checkers with minMax Project')


def get_mouse_position(position):   #to use mouse
    x, y = position
    row = y // squarewidth
    collum = x // squarewidth
    return row, collum


class Table:                    #class for the board
    def __init__(self):         #constuctor
        self.table = []
        self.BROWN_left = self.white_left = 12
        self.BROWN_kings = self.white_kings = 0
        self.create_table()
    
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for collum in range(row % 2, COLLUMS, 2):
                pygame.draw.rect(win, BROWN, (row*squarewidth, collum *squarewidth, squarewidth, squarewidth))

    def evaluate(self):
        return self.white_left - self.BROWN_left + (self.white_kings * 0.5 - self.BROWN_kings * 0.5)

    def get_disks(self, couleur):
        pieces = []
        for row in self.table:
            for disk in row:
                if disk != 0 and disk.couleur == couleur:
                    pieces.append(disk)
        return pieces

    def move(self, disk, row, collum):
        self.table[disk.row][disk.collum], self.table[row][collum] = self.table[row][collum], self.table[disk.row][disk.collum]
        disk.move(row, collum)

        if row == ROWS - 1 or row == 0:
            disk.disk_king()
            if disk.couleur == WHITE:
                self.white_kings += 1
            else:
                self.BROWN_kings += 1 

    def get_disk(self, row, collum):
        return self.table[row][collum]

    def create_table(self):
        for row in range(ROWS):
            self.table.append([])
            for collum in range(COLLUMS):
                if collum % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.table[row].append(Disk(row, collum, WHITE))
                    elif row > 4:
                        self.table[row].append(Disk(row, collum, BROWN))
                    else:
                        self.table[row].append(0)
                else:
                    self.table[row].append(0)
        
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for collum in range(COLLUMS):
                disk = self.table[row][collum]
                if disk != 0:
                    disk.draw(win)

    def remove(self, pieces):
        for disk in pieces:
            self.table[disk.row][disk.collum] = 0
            if disk != 0:
                if disk.couleur == BROWN:
                    self.BROWN_left -= 1
                else:
                    self.white_left -= 1
    
    def winner(self):
        if self.BROWN_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return BROWN
        
        return None 
    
    def get_allowed_move(self, disk):
        moves = {}
        left = disk.collum - 1
        right = disk.collum + 1
        row = disk.row

        if disk.couleur == BROWN or disk.king:
            moves.update(self.move_left(row -1, max(row-3, -1), -1, disk.couleur, left))
            moves.update(self.move_right(row -1, max(row-3, -1), -1, disk.couleur, right))
        if disk.couleur == WHITE or disk.king:
            moves.update(self.move_left(row +1, min(row+3, ROWS), 1, disk.couleur, left))
            moves.update(self.move_right(row +1, min(row+3, ROWS), 1, disk.couleur, right))
    
        return moves


    def move_right(self, start, stop, step, couleur, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLLUMS:
                break
            
            current = self.table[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self.move_left(r+step, row, step, couleur, right-1,skipped=last))
                    moves.update(self.move_right(r+step, row, step, couleur, right+1,skipped=last))
                break
            elif current.couleur == couleur:
                break
            else:
                last = [current]

            right += 1
        
        return moves

    def move_left(self, start, stop, step, couleur, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.table[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self.move_left(r+step, row, step, couleur, left-1,skipped=last))
                    moves.update(self.move_right(r+step, row, step, couleur, left+1,skipped=last))
                break
            elif current.couleur == couleur:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    



class Disk:  # class for disks
    thickness = 15    #choosing size of pieces

    def __init__(self, row, collum, couleur):       #constuctor
        self.row = row
        self.collum = collum
        self.couleur = couleur
        self.king = 0
        self.x = 0
        self.y = 0
        self.position()

    def position(self):
        self.x = squarewidth * self.collum + squarewidth // 2
        self.y = squarewidth * self.row + squarewidth // 2

    
    def draw(self, win):
        circleSize = squarewidth//2 - self.thickness
        pygame.draw.circle(win, self.couleur, (self.x, self.y), circleSize)
        if self.king:
            win.blit(king, (self.x - king.get_width()//2, self.y - king.get_height()//2))

    def move(self, row, collum):
        self.row = row
        self.collum = collum
        self.position()

    def disk_king(self):
        self.king = 1

class Game:                     #class to create a game between player and AI
    def __init__(self, win):        #constuctor
        self._init()
        self.win = win
    
    def update(self):
        self.table.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.table = Table()
        self.turn = BROWN
        self.valid_moves = {}

    def winner(self):
        return self.table.winner()

    def reset(self):
        self._init()

    def select(self, row, collum):
        if self.selected:
            result = self.move(row, collum)
            if not result:
                self.selected = None
                self.select(row, collum)
        
        disk = self.table.get_disk(row, collum)
        if disk != 0 and disk.couleur == self.turn:
            self.selected = disk
            self.valid_moves = self.table.get_allowed_move(disk)
            return 1
            
        return 0

    def move(self, row, collum):
        disk = self.table.get_disk(row, collum)
        if self.selected and disk == 0 and (row, collum) in self.valid_moves:
            self.table.move(self.selected, row, collum)
            skipped = self.valid_moves[(row, collum)]
            if skipped:
                self.table.remove(skipped)
            self.swtich_turn()
        else:
            return 0

        return 1


    def swtich_turn(self):
        self.valid_moves = {}
        if self.turn == BROWN:
            self.turn = WHITE
        else:
            self.turn = BROWN

    def get_table(self):
        return self.table

    def ai_move(self, table):
        self.table = table
        self.swtich_turn()
    

def minMax(position, deepness, max_player, game):  #minmax algo
    if deepness == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        optimal_move = None
        for move in get_moves(position, WHITE, game):
            evaluation = minMax(move, deepness-1, 0, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                optimal_move = move
        
        return maxEval, optimal_move
    else:
        minEval = float('inf')
        optimal_move = None
        for move in get_moves(position, BROWN, game):
            evaluation = minMax(move, deepness-1, 1, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                optimal_move = move
        
        return minEval, optimal_move


def future_moves(disk, move, table, game, skip):
    table.move(disk, move[0], move[1])
    if skip:
        table.remove(skip)

    return table


def get_moves(table, couleur, game):
    moves = []

    for disk in table.get_disks(couleur):
        valid_moves = table.get_allowed_move(disk)
        for move, skip in valid_moves.items():
            temp_table = deepcopy(table)
            temp_piece = temp_table.get_disk(disk.row, disk.collum)
            new_table = future_moves(temp_piece, move, temp_table, game, skip)
            moves.append(new_table)
    
    return moves



def main(): #main to execute the classes
    run = 1
    game = Game(WIN)

    while run:
        if game.turn == WHITE:
            value, new_table = minMax(game.get_table(), 3, WHITE, game)
            game.ai_move(new_table)

        if game.winner() != None:
            print(game.winner())
            run = 0

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, collum = get_mouse_position(position)
                game.select(row, collum)
            elif event.type == pygame.QUIT:
                run = 0
            
        game.update()
    
    pygame.quit()

main()
