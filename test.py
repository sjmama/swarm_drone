import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
points=[]
# 초기 점 위치 설정
for i in range(20):
    tmp=[]
    for i in range(3):
        tmp.append(np.random.randint(low=-100,high=100))
    points.append(tmp)

# 점 표시
for point in points:
    ax.scatter3D(point[0], point[1], point[2], color='blue')
ax.scatter3D(points[3][0], points[3][1], points[3][2], color='red')
# 축 라벨 설정
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 축 제한 설정
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.set_zlim(-100, 100)

# 시각화 설정
plt.ion()  # 대화형 모드 설정
plt.show()

while True:
    # 새로운 점 위치 입력
    new_points = []
    print(f'3점위치 x: {points[3][0]} y: {points[3][1]} z: {points[3][2]}')
    num=input(f"어떤 점: ")
    if num=='q':
        break
    num=int(float(num))
    new_x = float(input(f"점 {num}의 X 좌표 입력: "))
    new_y = float(input(f"점 {num}의 Y 좌표 입력: "))
    new_z = float(input(f"점 {num}의 Z 좌표 입력: "))
    new_points.append([new_x, new_y, new_z])

    # 점 위치 업데이트
    points[num][0] = new_x
    points[num][1] = new_y
    points[num][2] = new_z

    # 캔버스 지우기
    ax.cla()

    # 업데이트된 점 표시
    for point in points:
        ax.scatter3D(point[0], point[1], point[2], color='blue')
    ax.scatter3D(points[3][0], points[3][1], points[3][2], color='red')
    # 축 라벨 및 제한 설정 재설정
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_zlim(-100, 100)

    plt.draw()