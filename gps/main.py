import numpy as np

'''
np.dot(a, b) # 计算矩阵a和矩阵b的点积
np.linalg.inv(a) # 矩阵a的逆矩阵
'''

# GPS定位
def main():
    i = 0
    c = 0.299792458
    x = np.zeros((6, 4)) # 存储6个卫星的(x, y, z, t)参数
    while i < 6:
        temp = input()
        x[i - 1] = temp.split()
        j = 0
        while j < 4:
            x[i-1][j] = float(x[i-1][j])
            j = j + 1
        i = i + 1
    a = np.zeros((4, 4)) # 系数矩阵
    b = np.zeros((4, 1)) # 常数项
    j = 0
    while j < 4:
        a[j][0] = 2 * (x[5][0] - x[j][0])
        a[j][1] = 2 * (x[5][1] - x[j][1])
        a[j][2] = 2 * (x[5][2] - x[j][2])
        a[j][3] = 2 * c * c * (x[j][3] - x[5][3])
        b[j][0] = x[5][0] * x[5][0] - x[j][0] * x[j][0] + \
            x[5][1] * x[5][1] - x[j][1] * x[j][1] + \
            x[5][2] * x[5][2] - x[j][2] * x[j][2] + \
            c * c * (x[j][3] * x[j][3] - x[5][3] * x[5][3])
        j = j + 1

    a = np.linalg.inv(a) # 系数矩阵求逆

    print(np.dot(a, b))

if __name__ == "__main__":
    main()