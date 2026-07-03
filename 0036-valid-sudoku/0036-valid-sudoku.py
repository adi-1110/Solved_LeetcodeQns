class Solution(object):
    def isValidSudoku(self, board):
        
        for n in board:
            temp_r=set()

            for i in n:
                if i in temp_r:
                    return False
                if i != ".":
                    temp_r.add(i)

        for i in range(9):
            temp_c=set()
            for n in board:
                if n[i] in temp_c:
                    return False
                if n[i] != ".":    
                    temp_c.add(n[i])
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                temp = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] in temp:
                            return False

                        if board[i][j] != ".":
                            temp.add(board[i][j])

                        
        return True

            



                
                
                    
                    

        