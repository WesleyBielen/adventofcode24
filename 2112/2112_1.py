import os
import time
import itertools

def main():
    num_board = [['7', '8', '9'], ['4', '5', '6'], ['1','2','3'],['', '0', 'A']]
    dir_board = [['', '^', 'A'], ['<', 'v', '>']]
    os.chdir(os.path.dirname(__file__))
    file_path = "2112_input_sample.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    codes = [line.strip() for line in content]

    ax, ay = 3,2
    sx, sy = ax, ay
    total=0

    for code in codes:
        print(f'Scanning code {code}')
        code_comb = dict()
        sequence=''
        sx, sy = ax, ay
        for char in code:
            ex, ey = get_pos(num_board, char)
            diffx = ex - sx
            diffy = ey - sy

            seq = ''
            if diffx < 0:
                seq += ('^' * abs(diffx))
            elif diffx > 0:
                seq += ('v' * diffx)

            if diffy < 0:
                seq += ('<' * abs(diffy))
            elif diffy > 0:
                seq += ('>' * diffy)

            seq_poss = generate_all_possibilities_with_all_characters(seq)
            code_comb[char] = dict()
            i = 0
            for seq_string in seq_poss:
                i+=1
                #seq_string = seq_poss[i]
                seq_string+='A'
                code_comb[char][i] = seq_string
            sequence+=('A')
            sx, sy = ex, ey

        sequenceold = sequence
        sequencedisplay = sequence
        print(sequence)
        for i in range(2):
            sequencenew = ''
            sx, sy = 0, 2
            for char in sequenceold:
                ex, ey = get_pos(dir_board, char)
                diffx = ex - sx
                diffy = ey - sy

                if diffy < 0:
                    sequencenew += ('<' * abs(diffy))
                elif diffy > 0:
                    sequencenew += ('>' * diffy)

                if diffx < 0:
                    sequencenew += ('^' * abs(diffx))
                elif diffx > 0:
                    sequencenew += ('v' * diffx)


                if char == 'A':
                    sequencenew+='A'
                else:
                    sequencenew += ('A')

                sx, sy = ex, ey
            sequenceold = sequencenew
            print(sequenceold)
        print(sequencenew + " : " + str(len(sequencenew)))
        codenum = int(''.join(filter(str.isdigit, code)))
        total+=codenum * len(sequenceold)
    print(total)

def generate_all_possibilities_with_all_characters(string):
    return sorted(set(''.join(perm) for perm in itertools.permutations(string)))

def get_pos(matrix, char):
    for i in range(len(matrix)):
        for ii in range(len(matrix[0])):
            if matrix[i][ii] == char:
                return i, ii

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")