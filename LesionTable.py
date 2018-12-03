import numpy as np

def LesionTable():
    coord = np.zeros((6, 7, 3))
    lesionDiameter = np.zeros((6, 7, 1))

    coord[0, 0] = np.array([124, 151, 69])
    coord[0, 1] = np.array([135, 147, 60])
    coord[0, 2] = np.array([110, 153, 52])
    coord[0, 3] = np.array([99, 137, 49])
    coord[0, 6] = np.array([110, 156, 42])
    coord[0, 5] = np.array([124, 158, 40])
    coord[0, 6] = np.array([140, 135, 35])

    coord[1, 0] = np.array([123, 165, 87])
    coord[1, 1] = np.array([136, 152, 80])
    coord[1, 2] = np.array([108, 162, 75])
    coord[1, 3] = np.array([148, 142, 70])
    coord[1, 4] = np.array([107, 168, 63])
    coord[1, 5] = np.array([123, 162, 60])
    coord[1, 6] = np.array([141, 138, 61])

    coord[2, 0] = np.array([128, 153, 73])
    coord[2, 1] = np.array([144, 142, 66])
    coord[2, 2] = np.array([142, 153, 61])
    coord[2, 3] = np.array([149, 133, 58])
    coord[2, 4] = np.array([140, 162, 50])
    coord[2, 5] = np.array([128, 156, 46])
    coord[2, 6] = np.array([144, 131, 42])

    coord[3, 0] = np.array([126, 151, 68])
    coord[3, 1] = np.array([139, 140, 57])
    coord[3, 2] = np.array([114, 148, 55])
    coord[3, 3] = np.array([144, 133, 47])
    coord[3, 4] = np.array([140, 156, 45])
    coord[3, 5] = np.array([128, 155, 43])
    coord[3, 6] = np.array([112, 137, 43])

    coord[4, 0] = np.array([130, 167, 71])
    coord[4, 1] = np.array([142, 151, 62])
    coord[4, 2] = np.array([114, 160, 55])
    coord[4, 3] = np.array([153, 140, 55])
    coord[4, 4] = np.array([144, 158, 45])
    coord[4, 5] = np.array([130, 160, 40])
    coord[4, 6] = np.array([143, 139, 40])

    coord[5, 0] = np.array([128, 156, 67])
    coord[5, 1] = np.array([142, 146, 57])
    coord[5, 2] = np.array([142, 156, 48])
    coord[5, 3] = np.array([149, 142, 43])
    coord[5, 4] = np.array([140, 156, 41])
    coord[5, 5] = np.array([126, 163, 37])
    coord[5, 6] = np.array([144, 137, 32])

    lesionDiameter[0, 0] = 1.95
    lesionDiameter[0, 1] = 2.2
    lesionDiameter[0, 2] = 2
    lesionDiameter[0, 3] = 2
    lesionDiameter[0, 4] = 2.11
    lesionDiameter[0, 5] = 2.33
    lesionDiameter[0, 6] = 1.41

    lesionDiameter[1, 0] = 2.11
    lesionDiameter[1, 1] = 2.2
    lesionDiameter[1, 2] = 2.09
    lesionDiameter[1, 3] = 1.83
    lesionDiameter[1, 4] = 1.99
    lesionDiameter[1, 5] = 2.04
    lesionDiameter[1, 6] = 1.65

    lesionDiameter[2, 0] = 1.83
    lesionDiameter[2, 1] = 2
    lesionDiameter[2, 2] = 2.11
    lesionDiameter[2, 3] = 1.65
    lesionDiameter[2, 4] = 2
    lesionDiameter[2, 5] = 2.11
    lesionDiameter[2, 6] = 1.35

    lesionDiameter[3, 0] = 2.09
    lesionDiameter[3, 1] = 2.09
    lesionDiameter[3, 2] = 1.83
    lesionDiameter[3, 3] = 1.91
    lesionDiameter[3, 4] = 1.91
    lesionDiameter[3, 5] = 2.08
    lesionDiameter[3, 6] = 1.28

    lesionDiameter[4, 0] = 2.09
    lesionDiameter[4, 1] = 2.08
    lesionDiameter[4, 2] = 2.2
    lesionDiameter[4, 3] = 1.89
    lesionDiameter[4, 4] = 2.08
    lesionDiameter[4, 5] = 1.89
    lesionDiameter[4, 6] = 1.33

    lesionDiameter[5, 0] = 2.11
    lesionDiameter[5, 1] = 2.11
    lesionDiameter[5, 2] = 2.11
    lesionDiameter[5, 3] = 2.09
    lesionDiameter[5, 4] = 2.08
    lesionDiameter[5, 5] = 2.08
    lesionDiameter[5, 6] = 1.49

    return coord, lesionDiameter