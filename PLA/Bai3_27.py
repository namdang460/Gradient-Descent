import numpy as np
w = np.array([[1], [2], [-10]])
x = np.array([[3], [4], [1]])
y = -1
# tinh wT.x
wTx = np.dot(w.T, x)
print("wTx =", wTx[0][0])
# 2. Nhan du doan
y_pred = np.sign(wTx)[0][0]
print("Nhan du doan =", y_pred)
# 3. Kiem tra phan lop
if y_pred != y:
    print("Diem du lieu bi phan lop sai")
else:
    print("Diem du lieu duoc phan lop dung")