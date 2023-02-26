from  const import *
from square import Square
from piece import *
from move import Move
class Board:
    def __init__(self):
        self.squares=[[0,0,0,0,0,0,0,0] for col in range(COLUMNS)]
        self._created()
        self.last_move=None
        self._add_pieces('white')
        self._add_pieces('black')



    def calc_moves(self,piece,row,col):
        
        '''calculate all the possible moves of an specific pos'''
        def knight_moves():
            possible_moves=[
                (row-2,col+1),
                (row-1,col+2),
                (row+1,col+2),
                (row+2,col+1),
                (row+2,col-1),
                (row+1,col-2),
                (row-1,col-2),
                (row-2,col-1),
            ]
            for possible_move in possible_moves:
                possible_move_row,possible_move_col=possible_move
                if Square.in_range(possible_move_row,possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_rival(piece.color):
                        #create new square
                        initial=Square(row,col)
                        final=Square(possible_move_row,possible_move_col)#piece=piece
                        #create new move
                        move=Move(initial,final)
                        piece.add_moves(move)
                        
        def pawn_moves():
            if piece.moved:
                steps=1
            else:
                steps=2   
            #verticle moves
            start=row+piece.dir
            end=row+(piece.dir*(1+steps))   
            for move_row in range (start,end,piece.dir):
                if Square.in_range(move_row):
                    if self.squares[move_row][col].isempty():
                        #create initial and final moves squares
                        initial=Square(row,col)
                        final=Square(move_row,col)
                        move=Move(initial,final)
                        piece.add_moves(move)
                    else:break    
                else:break        
            #diagonal moves
            possible_row=row+piece.dir
            possible_cols=[col-1,col+1]
            for possible_col in possible_cols:
                if Square.in_range(possible_row,possible_col):
                    if self.squares[possible_row][possible_col].has_rival_piece(piece.color):
                        initial=Square(row,col)
                        final=Square(possible_row,possible_col)
                        move=Move(initial,final)
                        piece.add_move(move)
                
        def straightline_moves(incrs):
            for incr in incrs:
                row_incr,col_incr=incr
                possible_move_row=row+row_incr
                possible_move_col=row+col_incr
                while True:
                    if Square.in_range(possible_move_row,possible_move_col):
                            initial=Square(row,col)
                            final=Square(possible_move_row,possible_move_col)
                            #create possible moves
                            move=Move(initial,final)
                            if self.squares [possible_move_row][possible_move_col].isempty():
                                #add new move
                                piece.add_moves(move)
                            # has enemy piece
                            if self.squares [possible_move_row][possible_move_col].has_rival_piece(piece.color):
                                piece.add_moves(move)
                                break
                            #has team pieced
                            if self.squares [possible_move_row][possible_move_col].has_team_piece(piece.color):
                                
                                break
                    else:break    
                            #incrementinf incrs    
                    possible_move_row,possible_move_col=possible_move_row+row_incr,possible_move_col+col_incr
        
        def king_moves():
            adjs=[
                (row-1,col+0),#up
                (row-1,col+1),#upright
                (row+0,col+1),#right
                (row+1,col+1),#downright
                (row+1,col+0),#down
                (row+1,col-1),#down-left
                (row+0,col-1),#-left
                (row-1,col-1),#up-left
            ]
            for possible_move in adjs:
                possible_move_row,possible_move_col=possible_move
                if Square.in_range(possible_move_row,possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_rival(piece.color):
                        #create new square
                        initial=Square(row,col)
                        final=Square(possible_move_row,possible_move_col)#piece=piece
                        #create new move
                        move=Move(initial,final)
                        piece.add_moves(move)
            #castling moves   
            # queen castling
            # king castling         
        if isinstance(piece,Pawn): pawn_moves()
            
        elif isinstance(piece,Knight):
            knight_moves()
        elif isinstance(piece,Bishop):straightline_moves([
            (-1,1),#upright
            (-1,-1),#upleft
            (1,1),#downright
            (1,-1)#down left
        ])
       
        elif isinstance(piece,Rook):
            straightline_moves([
            (-1,0), #up
            (0,1),#left
            (1,0),#down
            (0,-1)#left
        ])
        
        elif isinstance(piece,Queen):
            straightline_moves([
            (-1,1),#upright
            (-1,-1),#upleft
            (1,1),#downright
            (1,-1),#down left
            (-1,0), #up
            (0,1),#left
            (1,0),#down
            (0,-1)#left
            
        ])

        elif isinstance(piece,king):
            king_moves()    
    def _created(self):
       
        for row in range(ROWS):
            for col in range(COLUMNS):
                self.squares[row][col]=Square(row,col)
                
    def _add_pieces(self,color):
        if color=='white':
            row_pawn,row_other=(6,7)
        else:
            row_pawn,row_other=(1,0)
        for col  in range(COLUMNS):
            #Pawns
            self.squares[row_pawn][col]=Square(row_pawn,col,Pawn(color) )
        self.squares[row_other][1]=Square(row_other,1,Knight(color))
        self.squares[row_other][6]=Square(row_other,6,Knight(color))
        #bishops

        self.squares[row_other][2]=Square(row_other,2,Bishop(color))
        self.squares[row_other][5]=Square(row_other,5,Bishop(color))

        #rooks

        self.squares[row_other][0]=Square(row_other,0,Rook(color))
        self.squares[row_other][7]=Square(row_other,7,Rook(color))

        #quen
        self.squares[row_other][3]=Square(row_other,3,Queen(color))
        #king 
        self.squares[row_other][4]=Square(row_other,4,king(color))
    def move(self,piece,move):
        initial=move.initial
        final=move.final

        #console board move update
        self.squares[initial.row][initial.col].piece=None
        self.squares[final.row][final.col].piece=piece
        #move
        piece.moved=True
        # cleared valid moves
        piece.clear_moves()

        self.last_move=move
   

    def valid_move(self,piece,move):
        return  move in piece.moves
            