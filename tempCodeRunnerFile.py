import numpy as np

# 행렬 A를 출력하는 함수
def pprint(msg, A):
    print("---", msg, "---")
    (n,m) = A.shape
    for i in range(0, n):
        line = ""
        for j in range(0, m):
            line += "{0:.2f}".format(A[i,j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")

A = np.array([[3., 0., 0.], [0., 2., 0.], [0., 0., 5.]])
B = np.array([[1., 0., 0.], [4., 2., 0.], [-1., 3., 4.]])
C = np.array([[10., 0., 0.], [1., 0., 0.], [2., 1., 5.]])
D = np.array([[2., 4., 1.], [0., 3., 4.], [0., 0., 7.]])
E = np.array([[9., 6., 3.], [0., -2., 4.], [0., 0., 11.]])
v = np.array([[10.], [20.], [30.]])

pprint("A+B", A+B) # 행렬의 합 A+B
pprint("A-B", A-B) # 행렬의 차 A-B

pprint("3*A ", 3*A) # 행렬의 스칼라배 3A
pprint("2*v", 2*v) # 행렬의 스칼라배 2v

pprint("matmul(B,A)", np.matmul(B,A)) # 행렬의 곱 AB
pprint("matmul(B,C)", np.matmul(B,C)) # 행렬의 곱 BC
pprint("matmul(D,E)", np.matmul(D,E)) # 행렬의 곱 DE

pprint("A*v", A*v)  # 행렬과 벡터의 곲 Av

pprint("matrix_power(A,2)", np.linalg.matrix_power(A,2)) # 행렬의 거듭제곱 A2
pprint("matrix_power(A,3)", np.linalg.matrix_power(A,3)) # 행렬의 거듭제곱 A3

pprint("A*B", A*B) # 행렬의 성분별 곱셈 A*B
#pprint("A/B", A/B) # 행렬의 성분별 나눗셈 A/B
pprint("A**2 == A*A", A**2) # 행렬의 성분별 거듭제곱 A**2

pprint("A.T", A.T) # 행렬의 전치 AT
pprint("v.T", v.T) # 벡터의 전치 vT
pprint("E.T", E.T) # 벡터의 전치 ET

M = np.diag([1, 2, 3]) # 대각행렬 diag(1,2,3) 생성
pprint("diag(1,2,3) =", M)

D11 = np.array([[1, 2], [3, 4]])
D12 = np.array([[5], [6]])
D21 = np.array([[7, 7]])
D22 = np.array([[8]])
D = np.block([[D11, D12], [D21, D22]]) # 블록행렬 D 생성
pprint("block matrix", D)