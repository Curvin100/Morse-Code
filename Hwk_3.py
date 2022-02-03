def text_to_morse(translate):
    B = ('-...')
    E = ('.')
    I = ('..')
    K = ('-.-')
    N = ('-.')
    O = ('---')
    R = ('.-.')
    T = ('-')
    V = ('...')
    if Letter == 'B':
        return ('The morse code for {0} is, {1}'.format(Letter.upper(), B))
    elif Letter == 'E':
        return ('The morse code for {0} is, {1}'.format(Letter.upper(), E))
    elif Letter == 'I':
        return ('The morse code for {0} is, {1}'.format(Letter.upper(), I))
    elif Letter == 'K':
        return ('The morse code for {0} is, {1}'.format(Letter.upper(), K))
    elif Letter == 'N':
        return ('The morse code for {0} is, {1}'.format(Letter.upper(), N))
    elif Letter == 'R':
        return ('The morse code for {0} is, {1}'.format(Letter.upper(), R))
    elif Letter == 'O':
        return ('The morse code for {0} is, {1}'.format(Letter.upper(), O))
    elif Letter == 'T':
        return ('The morse code for {0} is, {1}'.format(Letter.upper(), T))
    elif Letter == 'V':
        return ('The morse code for {0} is, {1}'.format(Letter.upper(), V))
    else:
        return ('Unknown Character')


intro = ("""
      Welcome to a basic Morse Code Simulator. This will allow you to write 
      basic messages into Morse Code!
      """)

print(intro)

index = 10000000
while index > 0:
    Letter = input('Please enter an uppercase letter: ')
    morse_code = text_to_morse(Letter)
    print(morse_code)
    index -= 1
