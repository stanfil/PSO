# -*- coding: utf-8 -*-

import numpy as np
import functions
# particle


class Particle:
    def __int__(self):
        self.pos = 0  # present position
        self.speed = 0
        self.pbest = 0  # best position


# PSO
class PSO:
    def __int__(self):
        self.w = 0.5  # 惯性因子
        self.c1 = 1 # 自我认知学习因子
        self.c2 = 1 # 社会认知学习因子
        self.gbest = 0 # 种群当前最好位置
        self.N = 20 # 种群中粒子数量
        self.POP = [] # 种群
        self.iter_N = 100 # 迭代次数


        # 适应度计算函数
        def fitness(self, x, y):
            return fitness1(x, y)