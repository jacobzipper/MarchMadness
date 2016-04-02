import random
round64 = open("Bracket.txt").read().split("\n\n")
round64 = round64[:len(round64)-1]
round64 = [a.split("\n") for a in round64]
round64 = [[b.split(" ") for b in a] for a in round64]
round32 = []
for match in round64:
	probabilityUpset = float(int(match[0][1]))/(int(match[0][1])+int(match[1][1]))
	if random.random() < probabilityUpset:
		round32.append(match[1])
	else:
		round32.append(match[0])

for i in xrange(0,len(round32)/2):
	round32[i] = list(round32[i]+round32[i+1])
	round32.pop(i+1)
print "___________"
print
print "ROUND OF 32"
print "___________"
print
for match in round32:
	print match[0] + " " + match[1]
	print match[2] + " " + match[3]
	print
sweet16 = []
for match in round32:
	probabilityUpset = float(int(match[1]))/(int(match[1])+int(match[3]))
	if random.random() < probabilityUpset:
		sweet16.append(match[2:])
	else:
		sweet16.append(match[:2])
for i in xrange(0,len(sweet16)/2):
	sweet16[i] = list(sweet16[i]+sweet16[i+1])
	sweet16.pop(i+1)
print "________"
print
print "SWEET 16"
print "________"
print
for match in sweet16:
	print match[0] + " " + match[1]
	print match[2] + " " + match[3]
	print
elite8 = []
for match in sweet16:
	probabilityUpset = float(int(match[1]))/(int(match[1])+int(match[3]))
	if random.random() < probabilityUpset:
		elite8.append(match[2:])
	else:
		elite8.append(match[:2])
for i in xrange(0,len(elite8)/2):
	elite8[i] = list(elite8[i]+elite8[i+1])
	elite8.pop(i+1)
print "_______"
print
print "ELITE 8"
print "_______"
print
for match in elite8:
	print match[0] + " " + match[1]
	print match[2] + " " + match[3]
	print
final4 = []
for match in elite8:
	probabilityUpset = float(int(match[1]))/(int(match[1])+int(match[3]))
	if random.random() < probabilityUpset:
		final4.append(match[2:])
	else:
		final4.append(match[:2])
for i in xrange(0,len(final4)/2):
	final4[i] = list(final4[i]+final4[i+1])
	final4.pop(i+1)
print "_______"
print
print "FINAL 4"
print "_______"
print
for match in final4:
	print match[0] + " " + match[1]
	print match[2] + " " + match[3]
	print
championship = []
for match in final4:
	probabilityUpset = float(int(match[1]))/(int(match[1])+int(match[3]))
	if random.random() < probabilityUpset:
		championship.append(match[2:])
	else:
		championship.append(match[:2])
for i in xrange(0,len(championship)/2):
	championship[i] = list(championship[i]+championship[i+1])
	championship.pop(i+1)
print "_____________________"
print
print "NATIONAL CHAMPIONSHIP"
print "_____________________"
print
for match in championship:
	print match[0] + " " + match[1]
	print match[2] + " " + match[3]
	print
champion = []
for match in championship:
	probabilityUpset = float(int(match[1]))/(int(match[1])+int(match[3]))
	if random.random() < probabilityUpset:
		champion.append(match[2:])
	else:
		champion.append(match[:2])
print "_________________"
print
print "NATIONAL CHAMPION"
print "_________________"
print
print champion[0][0] +"!!!!!!!"
