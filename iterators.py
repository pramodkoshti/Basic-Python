# iterations if Python

class MyIterator:
	
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		x = self.a
		self.a += 1
		return x

myiteratorclass = MyIterator()

myiter = iter(myiteratorclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration


class Counter:
	
	def __iter__(cnt):
		cnt.x = 1
		return cnt

	def __next__(cnt):
		if cnt.x < 10:
			y = cnt.x
			cnt.x += 1
			return y
		else:
			raise StopIteration	

counter = Counter()

count_iter = iter(counter)		

for z in count_iter:
	print(z)



