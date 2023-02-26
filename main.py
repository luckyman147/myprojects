import pygame
import sys
from const import *
from game import *
from square import *
from move import *

class Main:
    def __init__(self) :
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("chess")
        self.game=Game()
       
    def mainloop(self):
        game=self.game
        screen=self.screen
        dragger=self.game.dragger
        board=self.game.board
        while True:
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            if dragger.dragging:
                dragger.update_blit(screen)
            for  event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_raw=dragger.mouseY//SQSIZE
                    clicked_col=dragger.mouseX//SQSIZE
                    if board.squares[clicked_raw][clicked_col].has_piece():
                        piece=board.squares[clicked_raw][clicked_col].piece
                        board.calc_moves(piece,clicked_raw,clicked_col)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                elif   event.type==pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_moves(screen )
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                elif event.type==pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_raw=dragger.mouseY //SQSIZE
                        released_col=dragger.mouseX //SQSIZE
                        #create possible move
                        initial=Square(dragger.initial_row,dragger.initial_col)
                        final=Square(released_raw,released_col)
                        move=Move(initial,final)
                        if board.valid_move(dragger.piece,move):
                            board.move(dragger.piece,move)
                            #draw methods
                            game.show_bg(screen)
                            game.show_pieces(screen)
                    dragger.undrag_piece()

                elif event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            pygame.display.update()

main=Main()  
main.mainloop()  
        