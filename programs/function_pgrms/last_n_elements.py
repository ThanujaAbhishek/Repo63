sequence_1 = (1, 2, 3, 8, 4+5j)
sequence_2 = "Hello World"
sequence_3 = [10, True, 30+5j, 12.3]

n1 = 4
n2 = 7
n3 = 3


def seq(sequences_, num):
    length = len(sequences_)
    if num <= length:
        print(sequences_[-num::])
    else:
        print("n is greater than number of elements in sequence")


seq(sequence_1, n1)
seq(sequence_2, n2)
seq(sequence_3, n3)
