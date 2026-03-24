import turtle

DNA = {
    'Human':
    'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAG',
    'Rat':
    'ATGGTGCACCTGACTGATGCTGAGAAGGCTGCTGTTAATGGCCTGTGGGGAAAGGTGAACCCTGATGATGTTGGTGGCGAG',
    'Rhesus':
    'ATGGTGCATCTGACTCCTGAGGAGAAGAATGCCGTCACCACCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAG',
    'Chimpanzee':
    'ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAG'
}

DNA_TO_CODE_DICT = {
    'T': '00',
    'C': '01',
    'A': '10',
    'G': '11'
}


# Exercise 1
def dna_to_code(dna):
    """
    Return a coded sequence of 1's and 0's based on this mapping:
    T -> 00, C -> 01, A -> 10, G -> 11
    """
    coded = ''

    for base in dna:
        coded += DNA_TO_CODE_DICT[base]

    return coded


# Unit tests
assert dna_to_code('AATT') == '10100000'
assert dna_to_code('AA') == '1010'


# Time complexity answer:
# O(n), where n is the length of the dna string.


def draw_0(t):
    t.right(80)
    t.forward(20)
    t.left(80)


def draw_1(t):
    t.left(80)
    t.forward(20)
    t.right(80)


# Exercise 2
def draw_coded(coded, color):
    t = turtle.Turtle()
    t.penup()
    t.speed(0)
    t.goto(-300, -200)
    t.color(color)
    t.pendown()

    for bit in coded:
        if bit == '0':
            draw_0(t)
        else:
            draw_1(t)


# drawing_screen = turtle.Screen()
# draw_coded('10001101', 'red')
# drawing_screen.mainloop()


# Exercise 3
def visualize(dna, color):
    """
    Perform the entire operation of visualizing a DNA sequence.
    """
    code = dna_to_code(dna)
    draw_coded(code, color)


# if __name__ == "__main__":
#     drawing_screen = turtle.Screen()
#     visualize(DNA['Human'], 'red')
#     visualize(DNA['Rat'], 'green')
#     visualize(DNA['Rhesus'], 'blue')
#     visualize(DNA['Chimpanzee'], 'pink')
#     drawing_screen.mainloop()