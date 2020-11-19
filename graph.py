from graphviz import Digraph

dot = Digraph(comment='The Round Table')  # 別にコメント付けなくても良い
print(dot)  # 何も入れてないので当然　空

dot.node('0', '人間の')
dot.node('1', '知的能力を')
dot.node('2', 'コンピュータ上で')
dot.node('3', '実現する')
dot.node('4','様々な')
dot.node('5', '技術・ソフトウェア・コンピュータシステム')

# dot.edges(['12', '34', '06'])
dot.edge('1', '3')
dot.edge('2', '3')
dot.edge('3', '5')
dot.edge('4', '5')

print(dot.source)
dot.render('test-output/round-table.gv', view=True)
