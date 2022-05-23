from treelib import Tree  # 建语法树所用包
import numpy as np


calcultate = ['sin', 'cos', 'tg', 'ctg', 'log', 'lg', 'In']
print("实验一输入的公式：", "x = 0.5*PI;y = E;z = 3;?1/3*(ln(y)+5*sin(x))+(7+z)^2;#")


class Stack(object):

    def __init__(self):  # 创建空列表实现栈
        self.__list = []

    def is_empty(self):  # 判断是否为空
        return self.__list == []

    def push(self, item):  # 压栈，添加元素
        self.__list.append(item)

    def pop(self):  # 弹栈，弹出最后压入栈的元素
        if self.is_empty():
            return
        else:
            return self.__list.pop()

    def top(self):  # 取最后压入栈的元素
        if self.is_empty():
            return
        else:
            return self.__list[-1]


stack = Stack()
stack.push('#')
stack.push('S')


def AnalyseColumn(s):  # 判断矩阵列的下标
    if s == 21:
        return 0
    elif s == 20:
        return 1
    elif s == 10:
        return 2
    elif s == 11:
        return 3
    elif s == 12:
        return 4
    elif s == 13:
        return 5
    elif s == 14:
        return 6
    elif s == 15:
        return 7
    elif s == 16:
        return 8
    elif s == 17:
        return 9
    elif (s >= 0 and s <= 4) or s == 6:
        return 10
    elif s == 5:
        return 11
    elif s == 23:
        return 12
    elif s == 24:
        return 13
    elif s == 19:
        return 14
    else:
        return -1


def AnalyseRow(s):  # 判断矩阵的行的下标
    if s == 'S':
        return 0
    elif s == 'L':
        return 1
    elif s == 'A':
        return 2
    elif s == 'B':
        return 3
    elif s == 'b':  # b 为B1
        return 4
    elif s == 'T':
        return 5
    elif s == 't':  # t为T1
        return 6
    elif s == 'F':
        return 7
    elif s == 'N':
        return 8
    elif s == 'M':
        return 9
    elif s == 'E':
        return 10
    else:
        return -1


def BuildPrediction():  # 构建预测分析表
    prediction = np.zeros([11, 15], dtype=(str, 16))
    prediction[0][0] = "L?B"
    prediction[0][2] = "S?B"
    prediction[0][12] = "k"  # k为空集
    prediction[1][0] = "A;L"
    prediction[1][2] = "k"
    prediction[2][0] = "id=B"
    prediction[3][0] = "Tb"
    prediction[3][1] = "Tb"
    prediction[3][7] = "Tb"
    prediction[3][10] = "Tb"
    prediction[3][11] = "Tb"
    prediction[3][12] = "Tb"
    prediction[4][3] = 'k'
    prediction[4][5] = "k"
    prediction[4][6] = "+Tb"
    prediction[4][7] = "-Tb"
    prediction[4][13] = "k"
    prediction[5][0] = "Ft"
    prediction[5][1] = "Ft"
    prediction[5][4] = "Ft"
    prediction[5][7] = "Ft"
    prediction[5][10] = "Ft"
    prediction[5][11] = "Ft"
    prediction[6][3] = "k"
    prediction[6][5] = "k"
    prediction[6][6] = "k"
    prediction[6][7] = "k"
    prediction[6][8] = "*Ft"
    prediction[6][9] = "/Ft"
    prediction[6][13] = "k"
    prediction[7][0] = "FN"
    prediction[7][1] = "FN"
    prediction[7][4] = "FN"
    prediction[7][7] = "FN"
    prediction[7][10] = "fF"
    prediction[7][11] = "logF"
    prediction[8][3] = "k"
    prediction[8][5] = "k"
    prediction[8][6] = "k"
    prediction[8][7] = "k"
    prediction[8][8] = "k"
    prediction[8][9] = "k"
    prediction[8][12] = "k"
    prediction[8][14] = "^E"
    prediction[9][0] = "B"
    prediction[9][1] = "B"
    prediction[9][4] = "(B,B)"
    prediction[9][7] = "B"
    prediction[9][10] = "B"
    prediction[9][11] = "B"
    prediction[10][0] = "id"
    prediction[10][1] = "num"
    prediction[10][4] = "(B)"
    prediction[10][7] = "-E"
    return prediction


prediction = BuildPrediction()
key = ['x', '=', '0.5', '*', 'PI', ';', 'y', '=', 'E', ';', '?', '1', '/', '3', '*', '(', 'In', '(', 'y', ')', '+',
       '5', '*', 'sin', '(', 'x', ')', ')', '+', '(', '7', '+', 'z', ')', ';', '#']
value = [21, 18, 20, 15, 8, 11, 21, 18, 9, 19, 10, 20, 17, 20, 16, 12, 7, 13, 21, 16, 14, 20, 16, 1, 12, 21, 13, 13,
         14, 12, 20, 14, 21, 13, 11, 23]


def process(k, v, prediction, stack):
    i1 = 0
    node = {}  # 可能存在值一样，位置不同的节点，该节点负责更新其值对应的最新的节点下标在哪
    j = 0
    tree = Tree()
    tree.create_node(stack.top(), i1)
    node[stack.top()] = i1
    i1 = i1+1
    while not stack.is_empty():
        if j < len(k):
            word = stack.pop()
            print("word:", word)
            column = AnalyseColumn(v[j])  # 匹配出分析表的列号
            print("column:", column)
            row = AnalyseRow(word)  # 匹配出分析表的行号
            print("row=", row)
            if column == -1 or row == -1:  # 任意一个为-1则说明该输入存在问题
                print("wrong input in ", word)
            print("row:", row)
            result = prediction[row][column]
            print("result:", result)
            if result == 'k':  # k为空
                continue
            elif result == 0:  # 此时说明该文法存在问题，无法从分析表中得到结果
                print("Wrong input for ", k[j])
                print("plz reput now")
                break
            elif word == k[j] or (word == 'id' and v[j] == 21) or (word == 'num' and v[j] == 20) or (word == 'f' and key[j] in calcultate):  # 匹配成功
                # 分为特殊符号终结符匹配成功，变量与实数匹配成功，函数匹配成功
                j = j+1
                for r in result:
                    if node.__contains__(r):  # 如果该节点已经存在，则进行寻找到最新的节点下标名进行建树
                        parent = node[r]
                        tree.create_node(r, i1, parent=parent)
                        node[r] = i1
                        i1 = i1 + 1
                    else:
                        tree.create_node(r, i1, parent=word)
                        node[r] = i1
                        i1 = i1+1
            else:
                if result != 'id' or result != 'num' or result != 'logF' or result != 'id=B':
                    for w in reversed(result):
                        stack.push(w)
                elif result == 'id' or 'num':
                    stack.push(result)
                elif result == 'id=B':
                    stack.push('B')
                    stack.push('=')
                    stack.push('id')
                else:
                    stack.push('log')
                    stack.push('F')
        else:
            print("文法错误！")  # 此时可能出现文法错误但匹配依旧出现的情况，需重新进行排查
            break
    return tree


tree = process(key, value, prediction, stack)
tree.show()  # 打印出语法树
