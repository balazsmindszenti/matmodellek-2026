import numpy as np


class PairwiseDistanceCalculator:
    def __init__(self, vectors_1: np.ndarray,
                 vectors_2: np.ndarray):
        self.vectors_1 = vectors_1
        self.vectors_2 = vectors_2

        # 4. óra
        self.__n_1 = 0  # láthatósági szint, public: vectors_1, private: __n_1
        self.__n_2 = 0

    @property  # dekorátor, az n_1 meghívásakor nem kell ()
    def n_1(self) -> int:
        self.__n_1 = len(self.vectors_1)
        return self.__n_1

    @property
    def n_2(self) -> int:
        self.__n_2 = len(self.vectors_2)
        return self.__n_2

    def compute_distance_no_loop(self) -> np.ndarray:
        v2 = np.sum(self.vectors_1 ** 2, axis=1).reshape((self.n_1, 1))
        # oszloppá alakítás, reshape sorfolytonosan alakítja át, self.n_1 helyett -1 is lehet
        vw = self.vectors_1 @ self.vectors_2.T # T egy property, nincs ()
        # @ is tartalmaz for ciklust, csak azt a numpy fordítja, nem tőlünk megy a gép kódra fordítás
        w2 = np.sum(self.vectors_2 ** 2, axis=1)
        result = v2 - 2 * vw + w2
        return np.sqrt(result)
