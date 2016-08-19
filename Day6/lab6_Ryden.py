def gcd(num1, num2, divisor = None):
	if divisor is None:
		divisor = min(num1, num2)
	if num1%divisor == 0 and num2%divisor == 0:
		return divisor
	else:
		return gcd(num1, num2, divisor)


def primes(num = 121, prime_list = None):
	if prime_list is None:
		prime_list = []
	if num < 2:
		return 'Not a prime.'
	if num == 2:
		prime_list.insert(0,2)
		return prime_list
	divisors = range(2,num)
	for div in divisors:
		if num%div == 0:
			return primes(num - 1, prime_list)
	prime_list.insert(0,num)	
	return primes(num - 1, prime_list)

def hanoi(rings, Current_Towers = None):
	if Current_Towers is None:
		T1 = []
		T2 = []
		T3 = []
		Rings = range(1,rings+1)
		T1.extend(Rings)
		Current_Towers = [T1, T2, T3]
	mins = []
	for tower in Current_Towers:
		if not tower:
			mins.append(0)
		else:
			mins.append(min(tower))
	biggest_tower = mins.index(max(mins))
	move_this = min(Current_Towers[biggest_tower])
	Current_Towers[biggest_tower].remove(move_this)
	new_tower = mins.index(min(mins))
	if move_this > min(mins):
		smallest_tower = mins.index(min(mins))
		move_this = min(Current_Towers[smallest_tower])
		new_tower = 
	Current_Towers[new_tower].append(move_this)
	return Current_Towers
	if min(Current_Towers[0][0])

	return maxes, mins
	max(mins).index(max(mins))
	if not Current_Towers[]
	for tow in Current_Towers:
		'min_%d' % tow  
	min(Current_Towers[1])




