#---------------------------------------
#	Tri à bulles | Complexité : Téta (n^2) en moyenne
#---------------------------------------

def tri_bulle(L):
	T = []+L
	echange = True
	i = len(T)
	while i>0 and echange != False:
		echange = False
		for e in range(0,i-1):
			if T[e] > T[e+1]:
				temp = T[e]
				T[e] = T[e+1]
				T[e+1] = temp
				echange = True
		i -= 1
	return T

#---------------------------------------
#	Tri sélection | Complexité : Téta (n^2) dans tous les cas
#---------------------------------------

def tri_selection(L):
	res = []
	T = []+L
	while(T != []):
		m = min(T)
		T.remove(m)
		res.append(m)
	return res

def tri_selection_en_place(L): 
	T = []+L
	for i in range(len(T)):
		m = indice_minimum(T,i)
		T[i], T[m] = T[m], T[i]
	return T

def indice_minimum(T,i):
	m = T[i]
	for e in range(i,len(T)):
		if T[e] < m:
			m = T[e]
	return T.index(m)

#---------------------------------------
#	Tri insertion | Complexité : Téta (n^2) au pire
#---------------------------------------

def tri_insertion(T):
	for i in range(1,len(T)):
		for j in range(i,0,-1):
			if T[j-1] > T[j]:
				T[j-1], T[j] = T[j], T[j-1]
			else : break
	return T

#---------------------------------------
#	Tri fusion | Complexité : Téta (n log n) dans tous les cas
#---------------------------------------

def fusion(L1,L2):
	if len(L1) == 0 : return L2
	elif len(L2) == 0 : return L1
	elif L1[0] < L2[0]:
		return [L1[0]] + fusion(L1[1:], L2)
	else:
		return [L2[0]] + fusion(L1, L2[1:])

def tri_fusion(L, debut, fin):
	T = []+L
	if fin-debut < 2 : return T[debut:fin]
	else:
		milieu = (debut+fin)//2
		gauche = tri_fusion(T, debut, milieu)
		droite = tri_fusion(T, milieu, fin)
		return fusion(gauche,droite)

#---------------------------------------
#	Tri rapide V.1 | Complexité : Téta (n log n) en moyenne
#---------------------------------------

def partition(T):
	pivot = T[0]
	gauche = [elt for elt in T if elt < pivot]
	droite = [elt for elt in T if elt > pivot]
	return pivot, gauche, droite

def tri_rapide(L):
	T = []+L
	if len(T) < 2 : return T
	pivot, gauche, droite = partition(T)
	return tri_rapide(gauche) + [pivot] + tri_rapide(droite)


tab = [4,2,5,1,6,3]

print("-"*40)
print("Bulles          : " + str(tri_bulle(tab)))
print("Sélection       : " + str(tri_selection(tab)))
print("Sélect en place : " + str(tri_selection_en_place(tab)))
print("Insertion       : " + str(tri_insertion(tab)))
print("Fusion          : " + str(tri_fusion(tab,0, len(tab))))
print("QuickSort       : " + str(tri_rapide(tab)))
print("-"*40)
