"""  
finding HCF
"""

def hcfLoop(x : int, y : int) -> int:
    """  
    finding hinghest common factor using loop
    returns int
    """
    while (x % y) > 0:
        remainder = x % y
        x = y
        y = remainder
    
    return y

def hcfRecurs(x : int, y : int) -> int:
    """  
    find highest common factor using recursion
    """
    if y == 0 :
        return x
    else:
        return hcfRecurs(y, x % y)
    
def lcm(x : int, y : int) -> int:
    """  
    given x : int and y : int
    returns int : lowest common multiple for x and y
    """
    return (x * (y / hcfRecurs(x,y))) if y > x else (y * (x / hcfRecurs(x,y)))

def solution(s):
    i = 0
    m = ""
    braille = {
    " " : "000000",
    "^" : "000001",
    "a" :   "100000",
    "b" :   "110000",
    "c" :   "100100",
    "d" :   "100110",
    "e" :   "100010",
    "f" :   "110100",
    "g" :   "110110",
    "h" :   "110010",
    "i" :   "010100",
    "j" :   "010110",
    "k" :   "101000",
    "l" :   "111000",
    "m" :   "101100",
    "n" :   "101110",
    "o" :   "101010",
    "p" :   "111100",
    "q" :   "111110",
    "r" :   "111010",
    "s" :   "011100",
    "t" :   "011110",
    "u" :   "101001",
    "v" :   "111001",
    "w" :   "010111",
    "x" :   "101101",
    "y" :   "101111",
    "z" :   "101011"
    }

    
    for k in s: # change i to k as index in for loop
        if k.isupper() == True:
            m += braille["^"]+braille[k.lower()]
        else:
            m += braille[k]
        
    
    print(m)

solution("hello")

x = 1220
y = 516
print(f"the HCF for {x} and {y} using loop: {hcfLoop(x,y)}")
print(f"the HCF for {x} and {y} using recursion: {hcfRecurs(x,y)}")