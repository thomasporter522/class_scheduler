import sys

# read in list of classes and conflicts from file
def load(filename):
	lines = [x[:-1] for x in open(filename).readlines() if x[0] != "#"][1:]

	split = lines.index("Conflicts:")
	classes = lines[:split]
	conflicts = lines[split+1:]

	classes = [[y.strip() for y in x] for x in [x.split("|") for x in classes]]
	conflicts = [[y.strip() for y in x] for x in [x.split("-") for x in conflicts]]

	return classes, conflicts
	
# generate a list of schedules, of length given by maximum, with no conflicts
def generate_schedules(classes, conflicts, single_tags, maximum):
	if maximum == 0: return [[]]
	long_list =  [schedule+[one_class] for one_class in classes for schedule in generate_schedules(classes, conflicts, single_tags, maximum - 1)]
	return [schedule for schedule in long_list if not conflicted(schedule, conflicts, single_tags)]
	
# determine whether a schedule has any conflicts
def conflicted(schedule, conflicts, single_tags):
	for i in range(len(schedule)):
		for j in range(len(schedule)):
			if j != i:
				a, b = schedule[i], schedule[j]
				if a[2] == b[2] and a[2] in single_tags:
					return True
				for conflict in conflicts:
					if a[1] in conflict and b[1] in conflict: 
						return True
	return False
	
# rate a schedule
def rate(schedule, critical_tags):
	rating = 0
	tags = [x[2] for x in schedule]
	for tag in critical_tags:
		if tag in tags: rating += 1
	bonus = sum([float(x[3]) for x in schedule])
	return rating + bonus
	
# pretty print a schedule
def nice_print(schedule):
	print("-"*30)
	for s in schedule:
		print(str(s[1])+": "+str(s[0]))
	
if __name__ == "__main__":
	
	filename = "classes_FA_20.txt"
	try: filename = sys.argv[1]
	except: pass
	
	num_classes = 5
	try: num_classes = int(sys.argv[2])
	except: pass
	
	minimal_rating = 5.0
	try: minimal_rating = float(sys.argv[3])
	except: pass
	
	critical_tags = ["M", "L", "CSC", "G"]
	try: critical_tags = eval(sys.argv[4])
	except: pass
	
	single_tags = critical_tags
	try: single_tags = eval(sys.argv[5])
	except: pass
			
	classes, conflicts = load(filename)
	schedules = generate_schedules(classes, conflicts, single_tags, num_classes)
	
	size = 0
	rated_schedule = []
	for schedule in schedules:
		rating = rate(schedule, critical_tags)
		if rating >= minimal_rating:
			rated_schedule.append((schedule, rating))
			size += 1
			
	rated_schedule.sort(key = (lambda x: x[1]))
	for schedule in rated_schedule:
		nice_print(schedule[0])
		print("Rating:",schedule[1])
	print("-"*30)
	print(size, "acceptable schedules")
