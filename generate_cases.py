import os
import random
path = os.getcwd() 
path2 = [ '/inputs/' , '/outputs/' ]
print("Quantidade de casos de testes: " , end='')
qt_cases = int(input())

for i in range(qt_cases):
	
	size = random.randint(30,100)
	matrix = []

	for _ in range(size):
		matrix.append( [0] * size )

	way = []
	dist = []

	while len(way) < size:
		w = random.randint(0,size-1)
		d = random.randint(70,80)
		if not w in way:
			way += [w]
			dist += [d]

	for j in range(size):
		u = way[j]
		v = way[(j+1)%size]
		matrix[ u ][ v ] = dist[j]
		matrix[ v ][ u ] = dist[j]

	for j in range(size):
		for k in range(size):
			if not matrix[j][k] and ( j != k) :
				d = random.randint(81,90)
				matrix[ j ][ k ] = d
				matrix[ k ][ j ] = d

	file_in = open( path + path2[0] + str(i) + '.in' , 'w' )
	file_out = open( path + path2[1] + str(i) + '.out' , 'w' )

	file_in.write( str(size) + '\n' )
	for j in range(size):
		for k in range(size):
			file_in.write( str(matrix[j][k]) + ' ' )
		file_in.write('\n')

	file_out.write( str( sum(dist) ) + '\n' )

	file_in.close()
	file_out.close()