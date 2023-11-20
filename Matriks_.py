import os

# 1. penjumlahan dan pengurangan matriks
os.system('cls')
import numpy as np

matriks1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriks2 = np.array([[11, 12, 13], [14, 15, 16], [17, 18, 19]])

print("==== Penjumlahan dan Pengurangan ====")
for x in range(0, len(matriks1)):
    for y in range(0, len(matriks1[0])):
        print (matriks1[x][y] + matriks2[x][y], end=' '),
print()

# 2. perkalian matriks
matriks1 = np.array([[1, 2], [3, 4]])
matriks2 = np.array([[5, 6], [7, 8]])

print("\n==== Perkalian matriks ====".upper())
print("Hasil perkalian matriks: ", np.dot(matriks1, matriks2))
print()

# 3. transpose matriks
matriks = np.array([[6, 5], [1, 3], [2, 4]])
print("==== Transpose matriks ====")
print(np.transpose(matriks))
print()

# 4. invers matriks
matriks = np.array([[6, 1, 1], [4, -2, 8], [2, 8, 7]])
print("==== Invers matriks ====")
print(np.linalg.inv(matriks))
print()

# 5. Matriks indentasi
matriks_indentasi = np.eye(4)
print("==== Matriks indentasi ====")
print(matriks_indentasi)
print()

# 6.Reshape Matriks
matriks = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 10, 11], [12, 13, 14, 15]])
matriks_reshape = np.reshape(matriks, (2, 8))
print("==== Matriks Reshape ===")
print(matriks_reshape) 

