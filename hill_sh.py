import math
import numpy as np
def encryption(open_text: str, key: str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    key = list(key)
    key_num = []
    for i in range(len(key)):
        key_num.append(alphabet.index(key[i]))
        i += 1

    if(int(math.sqrt(len(key))) != math.sqrt(len(key))):
        return("Некорректный ключ")
    n = int(math.sqrt(len(key_num)))

    open_text = list(open_text)
    text_num = []
    for i in range(len(open_text)):
        text_num.append(alphabet.index(open_text[i]))
        i += 1

    while (True):
        if len(text_num)%n == 0:
            break
        text_num.append(0)

    c = 0
    mas = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            mas[i][j] = key_num[c]
            c += 1

    key_matrix = np.array(mas)
    if np.linalg.det(key_matrix) == 0:
        return("Некоррекктный ключ")

    def evklid_algorithm(a,b):
        if not b:
            return (1, 0, a)
        y, x, g = evklid_algorithm(b, a % b)
        return (x, y - (a // b) * x, g)

    det = int(round(np.linalg.det(key_matrix)))

    x, y, g = evklid_algorithm(det, 26)
    if g != 1:
        return("Некорректный ключ")

    m = int(len(text_num)/n)
    c = 0
    mas1 = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            mas1[i][j] = text_num[c]
            c += 1
    text_matrix = np.array(mas1)

    row, col = text_matrix.shape
    res = []
    for i in range(row):
        res.append(list(np.dot(key_matrix, text_matrix[i])))
        i += 1
    res = np.array(sum(res, [])) % 26
    encrypted_text = []
    for i in range(len(res)):
        encrypted_text.append(alphabet[res[i]])
        i += 1
    return "".join(encrypted_text)

print(encryption(input("Введите открытый текст:"), input("Введите ключ:") ))


def decryption(encrypted_text: str, key: str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    key = list(key)
    key_num = []
    for i in range(len(key)):
        key_num.append(alphabet.index(key[i]))
        i += 1

    if (int(math.sqrt(len(key))) != math.sqrt(len(key))):
        return ("Некорректный ключ")
    n = int(math.sqrt(len(key_num)))

    encrypted_text = list(encrypted_text)
    text_num = []
    for i in range(len(encrypted_text)):
        text_num.append(alphabet.index(encrypted_text[i]))
        i += 1

    c = 0
    mas = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            mas[i][j] = key_num[c]
            c += 1

    key_matrix = np.array(mas)

    if np.linalg.det(key_matrix) == 0:
        return("Некоррекктный ключ")

    m = int(len(text_num) / n)
    c = 0
    mas1 = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            mas1[i][j] = text_num[c]
            c += 1
    text_matrix = np.array(mas1)

    def evklid_algorithm(a,b):
        if not b:
            return (1, 0, a)
        y, x, g = evklid_algorithm(b, a % b)
        return (x, y - (a // b) * x, g)

    det = int(round(np.linalg.det(key_matrix)))

    x, y, g = evklid_algorithm(det, 26)
    if g != 1:
        return("Некорректный ключ")

    if det < 0 and x > 0:
        x = x
    elif det > 0 and x < 0:
        x = 26 + x
    elif det > 0 and x > 0:
        x = x
    elif det < 0 and x < 0:
        x = -x

    matrix_cofactor = np.round(np.linalg.inv(key_matrix).T * det)

    row, col = matrix_cofactor.shape
    for i in range(col):
        for j in range(row):
            if matrix_cofactor[i, j] < 0:
                matrix_cofactor[i, j] = -1 * (abs(matrix_cofactor[i, j]) % 26)
            else:
                matrix_cofactor[i, j] = matrix_cofactor[i, j] % 26
            j += 1
        i += 1

    matrix_cofactor = matrix_cofactor * x

    for i in range(col):
        for j in range(row):
            if matrix_cofactor[i, j] < 0:
                matrix_cofactor[i, j] = -1 * (abs(matrix_cofactor[i, j]) % 26)
            else:
                matrix_cofactor[i, j] = matrix_cofactor[i, j] % 26
            j += 1
        i += 1

    matrix_cofactor = matrix_cofactor.T

    for i in range(col):
        for j in range(row):
            if matrix_cofactor[i, j] < 0:
                matrix_cofactor[i, j] = matrix_cofactor[i, j] + 26
            j += 1
        i += 1

    key_matrix = matrix_cofactor

    row, col = text_matrix.shape
    res = []
    for i in range(row):
        res.append(list(np.dot(key_matrix, text_matrix[i])))
        i += 1
    res = np.array(sum(res, [])) % 26
    res = np.around(res)
    decrypted_text = []
    for i in range(len(res)):
        decrypted_text.append(alphabet[int(res[i])])
        i += 1

    return "".join(decrypted_text)



print(decryption(input("Введите шифрованный текст:"), input("Введите ключ:")))
