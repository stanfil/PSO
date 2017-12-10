# -*- coding: utf-8 -*-
import numpy as np

def fitness1(x, y):
    return x * x + y * y


def fitness2(x, y):
    return abs(x) + abs(y) + abs(x * y)


def fitness3(x, y):
    return x*x + (x+y)*(x+y)


def fitness4(x, y):
    return max(abs(x), abs(y))


def fitness5(x, y):
    return 100*(y-x*x)*(y-x*x)+(x-1)*(x-1)


def fitness6(x, y):
    return (int(x+0.5))*(int(x+0.5))+(int(y+0.5))*(int(y+0.5))


def fitness7(x, y):
    return pow(x,4)+2*pow(y,4) + np.random.random()


def fitness8(x, y):
    return -x*np.sin(np.sqrt(abs(x)))-y*np.sin(np.sqrt(abs(y)))+2*418.9829


def fitness9(x, y):
    return (int(x*x-10*np.cos(2*np.pi*x)+10)+int(y*y-10*np.cos(2*np.pi*y)+10))


def fitness10(x, y):
    return -20*np.exp(-0.2*np.sqrt(0.5*(x*x+y*y)))-np.exp(0.5*(np.cos(2*np.pi*x)+np.cos(2*np.pi*y)))+20+np.exp(1)


def fitness11(x, y):
    return 1.0/4000*(x*x+y*y)-np.cos(x*1.0/np.sqrt(1))*np.cos(y*1.0/np.sqrt(2))+1


def fitness12(x, y):
    return np.pi/2*((f1(x)-1)*(f1(x)-1)*(1+np.sin(np.pi*f1(x)+1))+(f1(y)-1)*(f1(y)-1)*(1+np.sin(np.pi*f1(y)+1))+pow(f1(y)-1,2)+10*np.sin(np.pi*x)*np.sin(np.pi*x))+f2(x,10,100,4)+f2(y,10,100,4)


def fitness13(x, y):
    return 0.1*(f2(x,10,100,4)+f2(y,10,100,4))*(np.sin(3*np.pi*x)*np.sin(3*np.pi*x)+(x-1)*(x-1)*(1+np.sin(3*np.pi*x)*np.sin(3*np.pi*x))+(y-1)*(y-1)*(1+np.sin(3*np.pi*y)*np.sin(3*np.pi*y)))


def f1(x):
    return 1+0.25*(x+1)


def f2(x,a,k,m):
    if x>a:
        return k*pow(x-a,m)
    elif x<-1*a:
        return k*pow(-1*x-a,m)
    else:
        return 0