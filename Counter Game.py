def counterGame(n):
    n = bin(n)[2:]
    n = n.split('1')
    turns = len(n)+len(n[-1])-2
    return 'Louise' if turns&1 else 'Richard'
