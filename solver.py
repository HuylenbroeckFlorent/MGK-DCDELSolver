import random
import itertools

def generate_lceb_game():
	return (random.sample([100,75,50,25,10,10,9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1], k=6), random.randrange(1,1000))

solution = []
best_solution = [1,1,1,1,1,1,1]
number=0

def solve_lceb_game(plates, goal):
	global number, best_solution
	if goal in plates:
		number=number+1
		#print(solution)
		if len(solution) < len(best_solution):
			best_solution = deepcopy(solution)
		return
	plates.sort(reverse=True)
	couples = itertools.combinations(plates, 2)
	for couple in couples:
		plates_rec = deepcopy(plates)
		x = couple[0]
		y = couple[1]
		plates_rec.remove(x)
		plates_rec.remove(y)
		if x != y:
			plate_new = x-y
			plates_rec_tmp=deepcopy(plates_rec)
			plates_rec_tmp.append(plate_new)
			solution.append(str(x)+"-"+str(y)+"="+str(x-y))
			solve_lceb_game(plates_rec_tmp, goal)
			solution.pop()
		if x !=1 and y!=1:
			plate_new = x*y
			plates_rec_tmp=deepcopy(plates_rec)
			plates_rec_tmp.append(plate_new)
			solution.append(str(x)+"*"+str(y)+"="+str(x*y))
			solve_lceb_game(plates_rec_tmp, goal)
			solution.pop()
		if x%y == 0:
			plate_new = int(x/y)
			plates_rec_tmp=deepcopy(plates_rec)
			plates_rec_tmp.append(plate_new)
			solution.append(str(x)+"/"+str(y)+"="+str(int(x/y)))
			solve_lceb_game(plates_rec_tmp, goal)
			solution.pop()
		plate_new = x+y
		plates_rec_tmp=deepcopy(plates_rec)
		plates_rec_tmp.append(plate_new)
		solution.append(str(x)+"+"+str(y)+"="+str(x+y))
		solve_lceb_game(plates_rec_tmp, goal)
		solution.pop()

def deepcopy(l):
	return [x for x in l]
	

(tiles, goal) = generate_lceb_game()
solve_lceb_game(tiles, goal)
if len(best_solution)<7:
	print("Best solution for computing "+str(goal)+" with "+str(tiles)+" found amongst "+str(number)+" solutions :", sep='')
	for i in range(len(best_solution)):
		print(best_solution[i], end='')
		if i != len(best_solution)-1:
			print(" ; ", end='')
else:
	print("No solution for computing "+str(goal)+ " with "+str(tiles)+".", sep='')
print()

