def decorator_function(original_function) :
	def wrapper() :
		print("this is the extra line of code")
		return original_function()
	return wrapper


@decorator_function
def display() :
	print("this is display function")

@decorator_function
def show() :
	print("this is show method")

def change(name, age, gender) :
	print(name, age, gender)


def args(*args, **kwargs) :
	print(*args)
	change(*args, **kwargs)


args("sravan", 40, gender ="male")

