# def square(x):
# 	return x*x

# def my_map(func, arg_list):
# 	result = []
# 	for i in arg_list:
# 		result.append(func(i))
# 	return result

# squares = my_map(square, [1,2,3,4,5,6,])

# print(squares)

# def logger(msg):

# 	def log_message():
# 		print('Log: ', msg)

# 	return log_message

# log_hi = logger("hi")
# log_hi()


# def html_tag(tag):

# 	def wrap_text(msg):
# 		print('<{0}>{1}</{0}>'.format(tag, msg))

# 	return wrap_text

# print_h1 = html_tag('h1')
# print_h1('Test Heading')
# print_h1('Another headline!')

# print_p = html_tag('p')
# print_p('This is a paragraph')

def removeDups(word):
	if len(word) <= 1:
		return word
	elif word[0] == word[1]:
		return removeDups(word[1:])
	else:
		return word[0] + removeDups(word[1:])


word = "aabbbbccccccdd"
print(removeDups(word))
