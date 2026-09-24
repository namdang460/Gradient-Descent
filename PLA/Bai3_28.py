import numpy as np
w = np.array([[-2], [1], [0]])
x = np.array([[2], [3], [1]])
y = 1

# Ham du doan
def h(w, x):
    return np.sign(np.dot(w.T, x))

# 1. Kiem tra mau co bi phan lop sai khong
wTx = np.dot(w.T, x)
y_pred = h(w, x)[0][0]
print("wTx truoc cap nhat =", wTx[0][0])
print("Nhan du doan =", y_pred)

if y_pred != y:
    print("Mau bi phan lop sai")

    # 2. Cap nhat Perceptron
    w = w + y*x
    print("w sau cap nhat:")
    print(w)

    # 3. Tinh lai wTx
    wTx_new = np.dot(w.T, x)
    print("wTx sau cap nhat =", wTx_new[0][0])

else:
    print("Mau duoc phan lop dung")