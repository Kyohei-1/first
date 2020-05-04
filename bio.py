from random import *
monster = ['タイラント','ネメシス','ゾンビ','フリッカー','ハンターα','ハンターγ']
print(len(monster))
monster.append('村長')
monster.append('ウェスカー')
print(len(monster))
Monster = monster[randint(0,int(len(monster)-1))]
print(Monster)

# やっぱ遊んでみるのが一番理解が深まるよね。

print('眠い')