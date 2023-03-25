from tqdm import tqdm, trange
from tinyec.ec import SubGroup, Curve


name = 'secp256k1'
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
h = 1

curve = Curve(a, b, SubGroup(p, g, n, h), name)
pubKey = curve.g*1

A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22, A23, A24, A25, A26, A27, A28, A29, A30, A31 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
multiples = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255)
lists = (A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22, A23, A24, A25, A26, A27, A28, A29, A30, A31)

for iter in trange(32,total=32,ascii=True,ncols=100,colour='#00ff00',unit='Rows',desc='Creating Key LookUp Table...Please Wait:'):
    B = (256** iter)%n
    for multiple in (multiples):
        DD = pubKey * multiple
        BB = type(pubKey*0)
        if isinstance(DD, BB) == True:
            C = 0
            lists[iter].append(C)
        else:
            C = (B*DD)
            lists[iter].append(C)
tuples = []
for list in lists:
    AA= tuple(list)
    tuples.append(AA)
grid = tuple(tuples)

def multiplyNum(number):
    N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    array = ((number)%N).to_bytes(32, "little")       
    list = []
    for byte in array:
        BBB = int(((hex(byte)))[2:], 16)
        list.append(BBB)
    tupleNumber = (tuple(list))
    posList = []
    for iteration, place in enumerate(tupleNumber):
        position = (grid[iteration][place])
        if position == 0:
            pass
        else:
            posList.append(position)
    tuplePos = tuple(posList)
    total = tuplePos[0]
    if len(tuplePos) < 1:
        print("Infinity and Beyond")
        exit()
    elif len(tuplePos) < 2:
        print(total)
        exit()
    else:
        for k in tuplePos[1:]:
            total = total + k
    print(total)
    exit()
multiplyNum(115792089237316195423570985008687907852837564279074904382605163141518161494336)


