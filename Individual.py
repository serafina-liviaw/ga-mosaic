import random

# Individual adalah entitas yang merepresentasikan 1 solusi mosaic puzzle tertentu
# @author Serafina Livia Wardhana
class Individual:
    def __init__(self, size):
        # ukuran papan game mosaic
        self.size = size

        # kromosom berupa array 2d berukuran size*size
        # melambangkan pewarnaan papan
        # 0: sel berwarna putih
        # 1: sel berwarna hitam
        self.chromosome = [[0 for _ in range(size)] for _ in range(size)]

        # array untuk menandai pewarnaan sel yang sudah pasti benar, misal berdasarkan heuristik 1-3
        # fungsi: agar warna yang sudah sesuai tidak terwarna ulang
        self.certainCells = set()

        # array untuk menandai clue yang sudah terselesaikan dan hasilnya pasti bendar, misal berdasarkan heuristik 1-3
        # fungsi: agar clue yang sudah terselesaikan tidak di cek lagi
        self.solvedClues = set()


    # method untuk menghasilkan kromosom pada satu individual
    # solusi awal digenerate berdasarkan heuristik untuk mempercepat algoritma
    def generate_chromosome(self, board):

        # warnai papan berdasarkan aturan heuristik 1-3 
        self.fill_by_heu1to3(board)

        # selain itu pewarnaan dilakukan secara acak dengan memerhatikan heuristik 4
        self.fill_w_heu4(board)


    # method untuk melakukan pewarnaan berdasarkan heuristik 1-3 (penjelasan pada dokumen)
    # warna akan ditandai sebagai TRUE pada isCertain
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
                        self.certainCells.add((i, j))
                        self.certainCells.add((i, j+1))
                        self.certainCells.add((i+1, j))
                        self.certainCells.add((i+1, j+1))
                        self.solvedClues.add((i, j))

                    elif board[i][j] == 4:
                        self.chromosome[i][j] = 1
                        self.chromosome[i][j+1] = 1 
                        self.chromosome[i+1][j] = 1  
                        self.chromosome[i+1][j+1] = 1
                        self.certainCells.add((i, j))
                        self.certainCells.add((i, j+1))
                        self.certainCells.add((i+1, j))
                        self.certainCells.add((i+1, j+1))
                        self.solvedClues.add((i, j))  
                
                elif i == 0 and j == self.size - 1:  # kanan atas
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i][j-1] = 0 # kiri
                        self.chromosome[i+1][j] = 0  # bawah
                        self.chromosome[i+1][j-1] = 0  # kiri bawah
                        self.certainCells.add((i, j))
                        self.certainCells.add((i, j-1))
                        self.certainCells.add((i+1, j))
                        self.certainCells.add((i+1, j-1))
                        self.solvedClues.add((i, j))
                    elif board[i][j] == 4:
                        self.chromosome[i][j] = 1
                        self.chromosome[i][j-1] = 1 
                        self.chromosome[i+1][j] = 1 
                        self.chromosome[i+1][j-1] = 1
                        self.certainCells.add((i, j))
                        self.certainCells.add((i, j-1))
                        self.certainCells.add((i+1, j))
                        self.certainCells.add((i+1, j-1))
                        self.solvedClues.add((i, j))  
                
                elif i == self.size - 1 and j == 0:  # kiri bawah
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i][j+1] = 0  # kanan
                        self.chromosome[i-1][j] = 0  # atas
                        self.chromosome[i-1][j+1] = 0 # kanan atas
                        self.certainCells.add((i, j))
                        self.certainCells.add((i, j+1))
                        self.certainCells.add((i-1, j))
                        self.certainCells.add((i-1, j+1))
                        self.solvedClues.add((i, j))
                    elif board[i][j] == 4:
                        self.chromosome[i][j] = 1
                        self.chromosome[i][j+1] = 1  
                        self.chromosome[i-1][j] = 1  
                        self.chromosome[i-1][j+1] = 1
                        self.certainCells.add((i, j))
                        self.certainCells.add((i, j+1))
                        self.certainCells.add((i-1, j))
                        self.certainCells.add((i-1, j+1))
                        self.solvedClues.add((i, j)) 
                
                elif i == self.size - 1 and j == self.size - 1:  # kanan bawah
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i][j-1] = 0  # kiri
                        self.chromosome[i-1][j] = 0  # atas
                        self.chromosome[i-1][j-1] = 0   # kiri atas
                        self.certainCells.add((i, j))
                        self.certainCells.add((i, j-1))
                        self.certainCells.add((i-1, j))
                        self.certainCells.add((i-1, j-1))
                        self.solvedClues.add((i, j))
                    elif board[i][j] == 4:
                        self.chromosome[i][j] = 1
                        self.chromosome[i][j-1] = 1  
                        self.chromosome[i-1][j] = 1  
                        self.chromosome[i-1][j-1] = 1
                        self.certainCells.add((i, j))
                        self.certainCells.add((i, j-1))
                        self.certainCells.add((i-1, j))
                        self.certainCells.add((i-1, j-1))
                        self.solvedClues.add((i, j))  


                # untuk clue di tepi papan (tidak termasuk sudut)
                elif i == 0 and 0 < j < self.size - 1:  # tepi atas
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i][j-1] = 0  # kiri
                        self.chromosome[i][j+1] = 0  # kanan
                        self.chromosome[i+1][j-1] = 0  # bawah kiri
                        self.chromosome[i+1][j] = 0  # bawah
                        self.chromosome[i+1][j+1] = 0  # bawah kanan
                        self.certainCells.add((i, j))
                        self.certainCells.add((i, j-1))
                        self.certainCells.add((i, j+1))
                        self.certainCells.add((i+1, j-1))
                        self.certainCells.add((i+1, j))
                        self.certainCells.add((i+1, j+1))
                        self.solvedClues.add((i, j))
                    elif board[i][j] == 6:
                        self.chromosome[i][j] = 1
                        self.chromosome[i][j-1] = 1 
                        self.chromosome[i][j+1] = 1  
                        self.chromosome[i+1][j-1] = 1  
                        self.chromosome[i+1][j] = 1  
                        self.chromosome[i+1][j+1] = 1
                        self.certainCells.add((i, j))
                        self.certainCells.add((i, j-1))
                        self.certainCells.add((i, j+1))
                        self.certainCells.add((i+1, j-1))
                        self.certainCells.add((i+1, j))
                        self.certainCells.add((i+1, j+1))
                        self.solvedClues.add((i, j))  
                
                elif i == self.size - 1 and 0 < j < self.size - 1:  # tepi bawah
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i][j-1] = 0 # kiri
                        self.chromosome[i][j+1] = 0  # kanan
                        self.chromosome[i-1][j-1] = 0  # atas kiri
                        self.chromosome[i-1][j] = 0  # atas
                        self.chromosome[i-1][j+1] = 0  # atas kanan
                        self.certainCells.add((i, j))
                        self.certainCells.add((i, j-1))
                        self.certainCells.add((i, j+1))
                        self.certainCells.add((i-1, j-1))
                        self.certainCells.add((i-1, j))
                        self.certainCells.add((i-1, j+1))
                        self.solvedClues.add((i, j))
                    elif board[i][j] == 6:
                        self.chromosome[i][j] = 1
                        self.chromosome[i][j-1] = 1  
                        self.chromosome[i][j+1] = 1  
                        self.chromosome[i-1][j-1] = 1  
                        self.chromosome[i-1][j] = 1  
                        self.chromosome[i-1][j+1] = 1
                        self.certainCells.add((i, j))
                        self.certainCells.add((i, j-1))
                        self.certainCells.add((i, j+1))
                        self.certainCells.add((i-1, j-1))
                        self.certainCells.add((i-1, j))
                        self.certainCells.add((i-1, j+1))
                        self.solvedClues.add((i, j))  
                
                elif j == 0 and 0 < i < self.size - 1:  # tepi kiri
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0
                        self.chromosome[i-1][j] = 0  # atas
                        self.chromosome[i+1][j] = 0  # bawag
                        self.chromosome[i-1][j+1] = 0  # atas kanan
                        self.chromosome[i][j+1] = 0  # kanan
                        self.chromosome[i+1][j+1] = 0  # bawah kanan
                        self.certainCells.add((i, j))
                        self.certainCells.add((i-1, j))
                        self.certainCells.add((i+1, j))
                        self.certainCells.add((i-1, j+1))
                        self.certainCells.add((i, j+1))
                        self.certainCells.add((i+1, j+1))
                        self.solvedClues.add((i, j))
                    elif board[i][j] == 6:
                        self.chromosome[i][j] = 1
                        self.chromosome[i-1][j] = 1 
                        self.chromosome[i+1][j] = 1 
                        self.chromosome[i-1][j+1] = 1  
                        self.chromosome[i][j+1] = 1  
                        self.chromosome[i+1][j+1] = 1
                        self.certainCells.add((i, j))
                        self.certainCells.add((i-1, j))
                        self.certainCells.add((i+1, j))
                        self.certainCells.add((i-1, j+1))
                        self.certainCells.add((i, j+1))
                        self.certainCells.add((i+1, j+1))
                        self.solvedClues.add((i, j)) 
                
                elif j == self.size - 1 and 0 < i < self.size - 1:  # tepi kanan
                    if board[i][j] == 0:
                        self.chromosome[i][j] = 0 # diri sendiri
                        self.chromosome[i-1][j] = 0  # atas
                        self.chromosome[i+1][j] = 0  # bawah
                        self.chromosome[i-1][j-1] = 0  # atas kiri
                        self.chromosome[i][j-1] = 0  # kiri
                        self.chromosome[i+1][j-1] = 0  # bawah kiri
                        self.certainCells.add((i, j))
                        self.certainCells.add((i-1, j))
                        self.certainCells.add((i+1, j))
                        self.certainCells.add((i-1, j-1))
                        self.certainCells.add((i, j-1))
                        self.certainCells.add((i+1, j-1))
                        self.solvedClues.add((i, j))
                    elif board[i][j] == 6:
                        self.chromosome[i][j] = 1 # diri 
                        self.chromosome[i-1][j] = 1  # atas
                        self.chromosome[i+1][j] = 1  # bawah
                        self.chromosome[i-1][j-1] = 1  # atas kiri
                        self.chromosome[i][j-1] = 1  # kiri
                        self.chromosome[i+1][j-1] = 1  # bawah kiri
                        self.certainCells.add((i, j))
                        self.certainCells.add((i-1, j))
                        self.certainCells.add((i+1, j))
                        self.certainCells.add((i-1, j-1))
                        self.certainCells.add((i, j-1))
                        self.certainCells.add((i+1, j-1))
                        self.solvedClues.add((i, j))
                

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
                        self.certainCells.add((i, j))
                        self.certainCells.add((i-1, j-1))
                        self.certainCells.add((i-1, j))
                        self.certainCells.add((i-1, j+1))
                        self.certainCells.add((i, j-1))
                        self.certainCells.add((i, j+1))
                        self.certainCells.add((i+1, j-1))
                        self.certainCells.add((i+1, j))
                        self.certainCells.add((i+1, j+1))
                        self.solvedClues.add((i, j))
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
                        self.certainCells.add((i, j))
                        self.certainCells.add((i-1, j-1))
                        self.certainCells.add((i-1, j))
                        self.certainCells.add((i-1, j+1))
                        self.certainCells.add((i, j-1))
                        self.certainCells.add((i, j+1))
                        self.certainCells.add((i+1, j-1))
                        self.certainCells.add((i+1, j))
                        self.certainCells.add((i+1, j+1))
                        self.solvedClues.add((i, j))  
                

    def fill_w_heu4(self, board):
        # sel discan secara iteratif, sel harus memiliki nilai isCertain FALSE
        # cek apakah elligible untuk heuristik 4 sebagai berikut

        isAnyChangesCanBeMade = True # stop jika tidak ada sel baru yang dapat diganti
        while isAnyChangesCanBeMade:
            isAnyChangesCanBeMade = False
            
            # update solvedClues berdasarkan data terbaru
            for i in range(self.size):
                for j in range(self.size):
                    if board[i][j] == -1:  # skip jika bukan clue
                        continue
                    
                    neighbors = self.get_neighbors(i, j)
                    # cek apakah semua neighbors sudah pasti
                    all_determined = all((ni, nj) in self.certainCells for ni, nj in neighbors)
                    
                    if all_determined:
                        self.solvedClues.add((i, j))
            

            # scan semua sel pada board untuk mencari clue 
            for i in range(self.size):
                for j in range(self.size):
                    if board[i][j] == -1:  # skip jika bukan clue (sementara -1)
                        continue
                    
                    if (i, j) in self.solvedClues: # skip clue yang sudah solved
                        continue
                    
                    clue = board[i][j]
                    neighbors = self.get_neighbors(i, j) # cari koordinat tetangga
                    
                    black_count = 0
                    empty_cells = [] # untuk menyimpan sel kosong yang belum pasti warnanya
                    
                    # hitung sel hitam dan cari sel kosong di sekitar clue
                    for ni, nj in neighbors:
                        if self.chromosome[ni][nj] == 1:
                            black_count += 1
                        elif (ni, nj) not in self.certainCells:  # sel kosong yang belum pasti
                            empty_cells.append((ni, nj))
                    
                    # heuristik 4a: jika jumlah sel hitam sudah cukup, sel kosong tersebut pasti putih
                    if black_count == clue:
                        for ni, nj in empty_cells:
                            self.chromosome[ni][nj] = 0
                            self.certainCells.add((ni, nj))
                            isAnyChangesCanBeMade = True
                    
                    # jika jumlah sel hitam belum cukup 
                    else:
                        needed_black = clue - black_count
                        validCandidates = []
                        for ni, nj in neighbors: # cari kandidat valid dari sel kosong
                            if (ni, nj) not in self.certainCells and self.is_valid_if_black(ni, nj, board):
                                validCandidates.append((ni, nj))
                        
                        # heuristik 4b + 4c: jika jumlah sel kosong sama dengan jumlah sel hitam yang dibutuhkan, sel kosong tersebut pasti hitam
                        if len(validCandidates) == needed_black and needed_black > 0:
                            for ni, nj in validCandidates:
                                self.chromosome[ni][nj] = 1
                                self.certainCells.add((ni, nj))
                                isAnyChangesCanBeMade = True

            # random fill (hanya untuk sel not certain yang berada di sekitar clue unsolved)                 
            for i in range(self.size):
                for j in range(self.size):
                    if (i, j) not in self.certainCells:
                        # cek apakah sel berada di sekitar clue unsolved
                        neighbors = self.get_neighbors(i, j)
                        has_unsolved_clue = any(
                            board[ni][nj] != -1 and (ni, nj) not in self.solvedClues # true jika ada minimal 1 tetangga yang yang berupa clue (bukan -1/kosong) dan tidak termasuk di solvedClues
                            for ni, nj in neighbors
                        )
                        
                        if has_unsolved_clue:
                            self.chromosome[i][j] = random.randint(0, 1)
                            self.certainCells.add((i, j))

            # heuristik 4d: jika penandaan sel sebagai hitam melanggar constraint, tandai sebagai putih
            for i in range(self.size):
                for j in range(self.size):
                    if (i, j) not in self.certainCells:
                        # cek apakah pengisian sel valid
                        if not self.is_valid_if_black(i, j, board):
                            self.chromosome[i][j] = 0
                            self.certainCells.add((i, j))
                            isAnyChangesCanBeMade = True
            
            
    # method untuk mendapatkan koordinat semua sel tetangga termasuk diri sendiri
    def get_neighbors(self, i, j):
        neighbors = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ni, nj = i + di, j + dj
                if 0 <= ni < self.size and 0 <= nj < self.size:
                    neighbors.append((ni, nj))
        return neighbors
    
    # method untuk mengecek apakah pewarnaan sel hitam pada sel (i,j) melanggar constraint
    def is_valid_if_black(self, i, j, board):
        neighbors = self.get_neighbors(i, j)
        
        for ni, nj in neighbors:
            if board[ni][nj] == -1:  # skip jika bukan clue (sementara -1)
                continue
            
            clue = board[ni][nj]
            neighbor_neighbors = self.get_neighbors(ni, nj) # cari koordinat tetangga dari tetangga
            
            # hitung berapa hitam jika (i,j) diset hitam
            black_count = 0
            empty_count = 0
            for nni, nnj in neighbor_neighbors:
                if self.chromosome[nni][nnj] == 1 or (nni == i and nnj == j):
                    black_count += 1
                elif (nni, nnj) not in self.certainCells:
                    empty_count += 1
            
            # Validasi: black_count tidak boleh melebihi clue
            if black_count > clue:
                return False
            
            # Validasi: hitam yang tersisa + kosong yang bisa diisi harus >= kebutuhan
            remaining = clue - black_count
            if remaining < 0 or (empty_count < remaining):
                return False
        
        return True
  