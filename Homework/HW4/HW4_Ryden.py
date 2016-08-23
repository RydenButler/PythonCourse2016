# O(n^2) average
def Insertion_Sort(num_list):
	for i in range(1,len(num_list)):
		if num_list[i] < num_list[i-1]:
			new = num_list.pop(i)
			num_list.insert(i-1, new)
			Insertion_Sort(num_list)
		else:
			continue
	return num_list

# O(n log(n)) average
def Merge_Sort(num_list):
	new_list = []
	num_list =list(num_list)
	if type(num_list[0]) is int:
		for i in range(len(num_list)):
			num_list[i] = [num_list[i]]
	if len(num_list) == 1:
		return num_list[0]
	if len(num_list) %2 == 1:
		new_list.append(num_list.pop(len(num_list)-1))
	for j in range(0,len(num_list),2):
		compare = num_list[j+1]
		middle = []
		restart = True
		while restart:
			for k in num_list[j]:
				if len(compare) is 0:
					if k not in middle:
						middle.append(k)
					restart = False
					continue
				if k not in middle and k <= compare[0]:
					middle.append(k)
					continue
				if k in middle and k != max(num_list[j]):
					continue
				else:
					middle.append(compare.pop(0))
					restart = True
					break
		new_list.append(middle)
	return Merge_Sort(new_list)