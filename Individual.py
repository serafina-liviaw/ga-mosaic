class Individual:
    def __init__(self, size):
        # ukuran papan game mosaic
        self.size = size

        # kromosom berupa array 2d berukuran size*size
        # melambangkan pewarnaan papan
        # 0: sel berwarna putih
        # 1: sel berwarna hitam
        self.chromosome = [[0 for _ in range(size)] for _ in range(size)]

        # untuk menandai pewarnaan yang sudah pasti benar, misal berdasarkan heuristik
        # fungsi: agar warna yang sudah sesuai tidak terwarna ulang
        self.isCertain = [[False for _ in range(size)] for _ in range(size)]


    # method untuk menghasilkan kromosom pada satu individual
    def generate_chromosome(self, board):

        # warnai papan berdasarkan aturan heuristik 1-3 
        self.fill_by_heu1to3(board)

        # selain itu pewarnaan dilakukan secara acak dengan memerhatikan heuristik 4
        self.fill_randomly_w_heu4(board)


    # method untuk melakukan pewarnaan berdasarkan heuristik 1-3 (penjelasan pada dokumen)
    # Warna akan ditandai sebagai TRUE pada isCertain
    def fill_by_heu1to3(self, board):
        for i in range(self.size):
            for j in range(self.size):

                # jika pada sel tidak ada clue, skip
                if board[i][j] == -1: #sementara -1
                    continue

                # untuk clue di sudut papan
                if i == 0 and j == 0:  # kiri atas
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i][j+1] = 0  # kanan
                        self.chromosome[i+1][j] = 0  # bawah
                        self.chromosome[i+1][j+1] = 0 # kanan bawah
                        self.isCertain[i][j] = True
                        self.isCertain[i][j+1] = True
                        self.isCertain[i+1][j] = True
                        self.isCertain[i+1][j+1] = True
                    elif board[i][j] == 4:
                        self.chromosome[i][j] = 1
                        self.chromosome[i][j+1] = 1 
                        self.chromosome[i+1][j] = 1  
                        self.chromosome[i+1][j+1] = 1
                        self.isCertain[i][j] = True
                        self.isCertain[i][j+1] = True
                        self.isCertain[i+1][j] = True
                        self.isCertain[i+1][j+1] = True  
                
                elif i == 0 and j == self.size - 1:  # kanan atas
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i][j-1] = 0 # kiri
                        self.chromosome[i+1][j] = 0  # bawah
                        self.chromosome[i+1][j-1] = 0  # kiri bawah
                        self.isCertain[i][j] = True
                        self.isCertain[i][j-1] = True
                        self.isCertain[i+1][j] = True
                        self.isCertain[i+1][j-1] = True
                    elif board[i][j] == 4:
                        self.chromosome[i][j] = 1
                        self.chromosome[i][j-1] = 1 
                        self.chromosome[i+1][j] = 1 
                        self.chromosome[i+1][j-1] = 1
                        self.isCertain[i][j] = True
                        self.isCertain[i][j-1] = True
                        self.isCertain[i+1][j] = True
                        self.isCertain[i+1][j-1] = True  
                
                elif i == self.size - 1 and j == 0:  # kiri bawah
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i][j+1] = 0  # kanan
                        self.chromosome[i-1][j] = 0  # atas
                        self.chromosome[i-1][j+1] = 0 # kanan atas
                        self.isCertain[i][j] = True
                        self.isCertain[i][j+1] = True
                        self.isCertain[i-1][j] = True
                        self.isCertain[i-1][j+1] = True
                    elif board[i][j] == 4:
                        self.chromosome[i][j] = 1
                        self.chromosome[i][j+1] = 1  
                        self.chromosome[i-1][j] = 1  
                        self.chromosome[i-1][j+1] = 1
                        self.isCertain[i][j] = True
                        self.isCertain[i][j+1] = True
                        self.isCertain[i-1][j] = True
                        self.isCertain[i-1][j+1] = True 
                
                elif i == self.size - 1 and j == self.size - 1:  # kanan bawah
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i][j-1] = 0  # kiri
                        self.chromosome[i-1][j] = 0  # atas
                        self.chromosome[i-1][j-1] = 0   # kiri atas
                        self.isCertain[i][j] = True
                        self.isCertain[i][j-1] = True
                        self.isCertain[i-1][j] = True
                        self.isCertain[i-1][j-1] = True
                    elif board[i][j] == 4:
                        self.chromosome[i][j] = 1
                        self.chromosome[i][j-1] = 1  
                        self.chromosome[i-1][j] = 1  
                        self.chromosome[i-1][j-1] = 1
                        self.isCertain[i][j] = True
                        self.isCertain[i][j-1] = True
                        self.isCertain[i-1][j] = True
                        self.isCertain[i-1][j-1] = True  


                # untuk clue di tepi papan (tidak termasuk sudut)
                elif i == 0 and 0 < j < self.size - 1:  # tepi atas
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i][j-1] = 0  # kiri
                        self.chromosome[i][j+1] = 0  # kanan
                        self.chromosome[i+1][j-1] = 0  # bawah kiri
                        self.chromosome[i+1][j] = 0  # bawah
                        self.chromosome[i+1][j+1] = 0  # bawah kanan
                        self.isCertain[i][j] = True
                        self.isCertain[i][j-1] = True
                        self.isCertain[i][j+1] = True
                        self.isCertain[i+1][j-1] = True
                        self.isCertain[i+1][j] = True
                        self.isCertain[i+1][j+1] = True
                    elif board[i][j] == 6:
                        self.chromosome[i][j] = 1
                        self.chromosome[i][j-1] = 1 
                        self.chromosome[i][j+1] = 1  
                        self.chromosome[i+1][j-1] = 1  
                        self.chromosome[i+1][j] = 1  
                        self.chromosome[i+1][j+1] = 1
                        self.isCertain[i][j] = True
                        self.isCertain[i][j-1] = True
                        self.isCertain[i][j+1] = True
                        self.isCertain[i+1][j-1] = True
                        self.isCertain[i+1][j] = True
                        self.isCertain[i+1][j+1] = True  
                
                elif i == self.size - 1 and 0 < j < self.size - 1:  # tepi bawah
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i][j-1] = 0 # kiri
                        self.chromosome[i][j+1] = 0  # kanan
                        self.chromosome[i-1][j-1] = 0  # atas kiri
                        self.chromosome[i-1][j] = 0  # atas
                        self.chromosome[i-1][j+1] = 0  # atas kanan
                        self.isCertain[i][j] = True
                        self.isCertain[i][j-1] = True
                        self.isCertain[i][j+1] = True
                        self.isCertain[i-1][j-1] = True
                        self.isCertain[i-1][j] = True
                        self.isCertain[i-1][j+1] = True
                    elif board[i][j] == 6:
                        self.chromosome[i][j] = 1
                        self.chromosome[i][j-1] = 1  
                        self.chromosome[i][j+1] = 1  
                        self.chromosome[i-1][j-1] = 1  
                        self.chromosome[i-1][j] = 1  
                        self.chromosome[i-1][j+1] = 1
                        self.isCertain[i][j] = True
                        self.isCertain[i][j-1] = True
                        self.isCertain[i][j+1] = True
                        self.isCertain[i-1][j-1] = True
                        self.isCertain[i-1][j] = True
                        self.isCertain[i-1][j+1] = True  
                
                elif j == 0 and 0 < i < self.size - 1:  # tepi kiri
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0
                        self.chromosome[i-1][j] = 0  # atas
                        self.chromosome[i+1][j] = 0  # bawag
                        self.chromosome[i-1][j+1] = 0  # atas kanan
                        self.chromosome[i][j+1] = 0  # kanan
                        self.chromosome[i+1][j+1] = 0  # bawah kanan
                        self.isCertain[i][j] = True
                        self.isCertain[i-1][j] = True
                        self.isCertain[i+1][j] = True
                        self.isCertain[i-1][j+1] = True
                        self.isCertain[i][j+1] = True
                        self.isCertain[i+1][j+1] = True
                    elif board[i][j] == 6:
                        self.chromosome[i][j] = 1
                        self.chromosome[i-1][j] = 1 
                        self.chromosome[i+1][j] = 1 
                        self.chromosome[i-1][j+1] = 1  
                        self.chromosome[i][j+1] = 1  
                        self.chromosome[i+1][j+1] = 1
                        self.isCertain[i][j] = True
                        self.isCertain[i-1][j] = True
                        self.isCertain[i+1][j] = True
                        self.isCertain[i-1][j+1] = True
                        self.isCertain[i][j+1] = True
                        self.isCertain[i+1][j+1] = True 
                
                elif j == self.size - 1 and 0 < i < self.size - 1:  # tepi kanan
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i-1][j] = 0  # atas
                        self.chromosome[i+1][j] = 0  # bawah
                        self.chromosome[i-1][j-1] = 0  # atas kiri
                        self.chromosome[i][j-1] = 0  # kiri
                        self.chromosome[i+1][j-1] = 0  # bawah kiri
                        self.isCertain[i][j] = True
                        self.isCertain[i-1][j] = True
                        self.isCertain[i+1][j] = True
                        self.isCertain[i-1][j-1] = True
                        self.isCertain[i][j-1] = True
                        self.isCertain[i+1][j-1] = True
                    elif board[i][j] == 6:
                        self.chromosome[i][j] = 1 # diri 
                        self.chromosome[i-1][j] = 1  # atas
                        self.chromosome[i+1][j] = 1  # bawah
                        self.chromosome[i-1][j-1] = 1  # atas kiri
                        self.chromosome[i][j-1] = 1  # kiri
                        self.chromosome[i+1][j-1] = 1  # bawah kiri
                        self.isCertain[i][j] = True
                        self.isCertain[i-1][j] = True
                        self.isCertain[i+1][j] = True
                        self.isCertain[i-1][j-1] = True
                        self.isCertain[i][j-1] = True
                        self.isCertain[i+1][j-1] = True
                

                # untuk clue yang tidak berada tepi maupun sudut
                else:  
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0  # diri sendiri
                        self.chromosome[i-1][j-1] = 0  # atas kiri
                        self.chromosome[i-1][j] = 0  # atas
                        self.chromosome[i-1][j+1] = 0  # atas kanan
                        self.chromosome[i][j-1] = 0  # kiri
                        self.chromosome[i][j+1] = 0  # kanan
                        self.chromosome[i+1][j-1] = 0  # bawah kiri
                        self.chromosome[i+1][j] = 0  # bawah
                        self.chromosome[i+1][j+1] = 0  # bawah kanan
                        self.isCertain[i][j] = True
                        self.isCertain[i-1][j-1] = True
                        self.isCertain[i-1][j] = True
                        self.isCertain[i-1][j+1] = True
                        self.isCertain[i][j-1] = True
                        self.isCertain[i][j+1] = True
                        self.isCertain[i+1][j-1] = True
                        self.isCertain[i+1][j] = True
                        self.isCertain[i+1][j+1] = True
                    elif board[i][j] == 9:
                        self.chromosome[i][j] = 1  
                        self.chromosome[i-1][j-1] = 1 
                        self.chromosome[i-1][j] = 1 
                        self.chromosome[i-1][j+1] = 1 
                        self.chromosome[i][j-1] = 1  
                        self.chromosome[i][j+1] = 1  
                        self.chromosome[i+1][j-1] = 1 
                        self.chromosome[i+1][j] = 1  
                        self.chromosome[i+1][j+1] = 1
                        self.isCertain[i][j] = True
                        self.isCertain[i-1][j-1] = True
                        self.isCertain[i-1][j] = True
                        self.isCertain[i-1][j+1] = True
                        self.isCertain[i][j-1] = True
                        self.isCertain[i][j+1] = True
                        self.isCertain[i+1][j-1] = True
                        self.isCertain[i+1][j] = True
                        self.isCertain[i+1][j+1] = True  
                

    def fill_randomly_w_heu4(self, board):
        # pilih sel secara iteratif, sel harus memiliki nilai isCertain FALSE
        # cek apakah elligible untuk heuristik 4
        # jika tidak isi random
        pass