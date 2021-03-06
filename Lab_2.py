import sys


def SybButes(mas, inv):
    if not inv:
        sbox = [
            0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
            0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
            0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
            0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
            0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
            0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
            0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
            0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
            0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
            0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
            0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
            0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
            0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
            0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
            0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
        ]
    else:
        sbox = [
            0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
            0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
            0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
            0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
            0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
            0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
            0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
            0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
            0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
            0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
            0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
            0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
            0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
            0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
            0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
        ]
    for i in range(4):
        mas[i] = sbox[mas[i]]
    return mas


def ShiftRows(mas, inv):
    if not inv:
        for i in range(4):
            for j in range(i):
                t = mas[i][0]
                for m in range(3):
                    mas[i][m] = mas[i][m + 1]
                mas[i][3] = t
    else:
        for i in range(4):
            for j in range(i):
                t = mas[i][3]
                for m in range(3, 0, -1):
                    mas[i][m] = mas[i][m - 1]
                mas[i][0] = t
    return mas


def mix_columns(mas, inv):
    if not inv:
        for i in range(4):
            m0 = mul_by_02(mas[0][i]) ^\
                mul_by_03(mas[1][i]) ^ mas[2][i] ^ mas[3][i]
            m1 = mas[0][i] ^ mul_by_02(mas[1][i]) ^ \
                mul_by_03(mas[2][i]) ^ mas[3][i]
            m2 = mas[0][i] ^ mas[1][i] ^ \
                mul_by_02(mas[2][i]) ^ mul_by_03(mas[3][i])
            m3 = mul_by_03(mas[0][i]) ^ mas[1][i] ^ \
                mas[2][i] ^ mul_by_02(mas[3][i])
            mas[0][i] = m0
            mas[1][i] = m1
            mas[2][i] = m2
            mas[3][i] = m3
    else:
        for i in range(4):
            m0 = mul_by_0e(mas[0][i]) ^ mul_by_0b(mas[1][i]) ^ \
                mul_by_0d(mas[2][i]) ^ mul_by_09(mas[3][i])
            m1 = mul_by_09(mas[0][i]) ^ mul_by_0e(mas[1][i]) ^ \
                mul_by_0b(mas[2][i]) ^ mul_by_0d(mas[3][i])
            m2 = mul_by_0d(mas[0][i]) ^ mul_by_09(mas[1][i]) ^ \
                mul_by_0e(mas[2][i]) ^ mul_by_0b(mas[3][i])
            m3 = mul_by_0b(mas[0][i]) ^ mul_by_0d(mas[1][i]) ^ \
                mul_by_09(mas[2][i]) ^ mul_by_0e(mas[3][i])
            mas[0][i] = m0
            mas[1][i] = m1
            mas[2][i] = m2
            mas[3][i] = m3
    return mas


def mul_by_02(num):
    if num < 0x80:
        num = (num << 1)
    else:
        num = ((num << 1) ^ 0x1b) % 0x100
    return num


def mul_by_03(num):
    return (mul_by_02(num) ^ num)


def mul_by_04(num):
    return mul_by_02(mul_by_02(num))


def mul_by_08(num):
    return mul_by_02(mul_by_04(num))


def mul_by_09(num):
    return mul_by_08(num) ^ num


def mul_by_0b(num):
    return mul_by_08(num) ^ mul_by_02(num) ^ num


def mul_by_0d(num):
    return mul_by_08(num) ^ mul_by_04(num) ^ num


def mul_by_0e(num):
    return mul_by_08(num) ^ mul_by_04(num) ^ mul_by_02(num)


def add_round_key(mas, rkey, round, inv):
    if not inv:
        for i in range(4):
            m0 = mas[0][i] ^ rkey[0][4 * round + i]
            m1 = mas[1][i] ^ rkey[1][4 * round + i]
            m2 = mas[2][i] ^ rkey[2][4 * round + i]
            m3 = mas[3][i] ^ rkey[3][4 * round + i]
            mas[0][i] = m0
            mas[1][i] = m1
            mas[2][i] = m2
            mas[3][i] = m3
    else:
        for i in range(4):
            m0 = mas[0][i] ^ rkey[0][(10 - round) * 4 + i]
            m1 = mas[1][i] ^ rkey[1][(10 - round) * 4 + i]
            m2 = mas[2][i] ^ rkey[2][(10 - round) * 4 + i]
            m3 = mas[3][i] ^ rkey[3][(10 - round) * 4 + i]
            mas[0][i] = m0
            mas[1][i] = m1
            mas[2][i] = m2
            mas[3][i] = m3
    return mas


def key_expansion(KEY):
    col = []
    key_schedule = []
    rcon = [[0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]]
    for i in range(4):
        col.append([])
    for i in range(4):
        key_schedule.append([])
        for j in range(11 * 4):
            key_schedule[i].append([])
    for i in range(4):
        for j in range(4):
            key_schedule[j][i] = ord(KEY[j + 4 * i])
    for i in range(4, 11 * 4):
        if not (i % 4):
            for j in range(3):
                col[j] = key_schedule[j + 1][i - 1]
            col[3] = key_schedule[0][i - 1]
            col = SybButes(col, False)
            for j in range(4):
                key_schedule[j][i] = key_schedule[j][i - 4] ^ \
                    col[j] ^ rcon[j][i / 4 - 1]
        else:
            for j in range(4):
                key_schedule[j][i] = key_schedule[j][i - 4] ^ \
                    key_schedule[j][i - 1]
    return key_schedule


def crypt(TXT, KEY, inv):
    TXTlen = len(TXT)
    KEYlen = len(KEY)
    if (KEYlen < 16):
        while(KEYlen != 16):
            KEY = KEY + chr(0x01)
            KEYlen = KEYlen + 1
    nb = 4
    round = 0
    rez = ''
	res2 = ""

    if not TXTlen % 0x10:
        cur_state = int(TXTlen / 0x10)
        state = []
        for i in range(cur_state):
            state.append([])
            for j in range(nb):
                state[i].append([])
                for m in range(nb):
                    state[i][j].append(ord(TXT[j + nb * m + 16 * i]))
    else:
        cur_state = TXTlen / 0x10 + 1
        state = []
        for i in range(cur_state):
            state.append([])
            for j in range(nb):
                state[i].append([])
                for m in range(nb):
                    state[i][j].append([])
        for i in range(TXTlen):
            state[i / 0x10][i % 4][(i % 0x10) / 4] = ord(TXT[i])
        for i in range(TXTlen, cur_state * 0x10 - 1):
            state[i / 0x10][i % 4][(i % 0x10) / 4] = 0
        state[cur_state - 1][3][3] = 0x01

    rkey = key_expansion(KEY)
    for i in range(cur_state):
            state[i] = add_round_key(state[i], rkey, round, inv)
    for i in range(9):
        round = round + 1
        for i in range(cur_state):
            for j in range(nb):
                state[i][j] = SybButes(state[i][j], inv)
        for i in range(cur_state):
            state[i] = ShiftRows(state[i], inv)
        if not inv:
            for i in range(cur_state):
                state[i] = mix_columns(state[i], inv)
            for i in range(cur_state):
                state[i] = add_round_key(state[i], rkey, round, inv)
        else:
            for i in range(cur_state):
                state[i] = add_round_key(state[i], rkey, round, inv)
            for i in range(cur_state):
                state[i] = mix_columns(state[i], inv)
    round = round + 1
    for i in range(cur_state):
        for j in range(nb):
            state[i][j] = SybButes(state[i][j], inv)
    for i in range(cur_state):
        state[i] = ShiftRows(state[i], inv)
    for i in range(cur_state):
        state[i] = add_round_key(state[i], rkey, round, inv)

    for i in range(cur_state * 0x10):
        rez = rez + chr(state[i / 0x10][i % 4][(i % 16) / 4])
    if inv:
        if ord(rez[len(rez) - 1]) == 0x01:
            resLen = len(rez) - 1
            point = len(rez) - 2
            while ord(rez[point]) == 0x00:
                point = point - 1
                resLen = resLen - 1
            for i in range(resLen):
                res2 += rez[i]
            return res2
    return rez


def main():
    print "Example of main string:"
    print "[*.py] [input file name] [key file name]\
        result file name] [encode or decode]"
    print "    ""-c"" - encode"
    print "    ""-d"" - decode"
    countPar = len(sys.argv)
    if (countPar != 5):
        print "There is wrong number of parameters."
        exit()
    if(sys.argv[4] != "-c" and sys.argv[4] != "-d"):
        print "irregular operation"
        exit()

    inFileName = sys.argv[1]
    keyFileName = sys.argv[2]
    rezFileName = sys.argv[3]
    fl = sys.argv[4]

    with open(inFileName, 'r') as inFile:
        TXT = inFile.read()
    with open(keyFileName, 'r') as keyFile:
        KEY = keyFile.read()
    if fl == '-c':
        rez = crypt(TXT, KEY, False)
    else:
        rez = crypt(TXT, KEY, True)
    with open(rezFileName, 'w') as rezFile:
        rezFile.write(rez)
if __name__ == "__main__":
    main()
