'''請你試著完成以下集合, 並印出內容:

set1: 在 zooA 而且也在 zooB 的動物集合
set2: zooA 和 zooB 所有動物集合
set3: 在 zooA 但不在 zooB 的動物集合
set4: 在 zooB 但不在 zooA 的動物集合
set5: 在 zooA 或是 zooB, 但不同時存在兩個動物園的動物集合'''

zooA = {'elephant', 'tiger', 'lion', 'giraffe', 'leopard', 'antelop'}
zooB = {'lion', 'cheetah', 'giraffe', 'zebra', 'wildebeest', 'elephant'}

print("zoo A:", zooA)
print("zoo B:", zooB)
print("zoo A and zoo B:", zooA & zooB)
print("zoo A or zoo B:", zooA | zooB)
print("zoo A - zoo B:",zooA - zooB)
print("zoo A xor zoo B:", zooA ^ zooB)