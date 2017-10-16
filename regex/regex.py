import re

"""
Character classes provide a way to match only one of a specific set of characters.
A character class is created by putting the characters it matches inside square brackets.
"""
print("-"*8,"Character classes","-"*8)
pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
   print("Match 1")

if re.search(pattern, "E3"):
   print("Match 2")

if re.search(pattern, "1ab"):
   print("Match 3")


print("-"*8,"Inverting character classes","-"*8)
"""
^ inversts the characters inside of the [character class]
"""
pattern = r"[^A-Z]" 

if re.search(pattern, "this is all quiet"):
   print("Match 1")

if re.search(pattern, "AbCdEfG123"):
   print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
   print("Match 3")


print("-"*8,"Metacharacter *","-"*8)
"""
* means 0 or more time repetition
"""
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")


print("-"*8,"Metacharacter +","-"*8)
"""
+ means 1 or more time repetition
"""
pattern = r"g+"

if re.match(pattern, "g"):
   print("Match 1")

if re.match(pattern, "gggggggggggggg"):
   print("Match 2")

if re.match(pattern, "abc"):
   print("Match 3")


print("-"*8,"Metacharacter ?","-"*8)
"""
? means 0 or 1 repetition
"""
pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
   print("Match 1")

if re.match(pattern, "icecream"):
   print("Match 2")

if re.match(pattern, "sausages"):
   print("Match 3")

if re.match(pattern, "ice--ice"):
   print("Match 4")


print("-"*8,"Metacharacter {}","-"*8)
"""
Curly braces can be used to represent the number of repetitions between two numbers.
The regex {x,y} means "between x and y repetitions of something".
Hence {0,1} is the same thing as ?.
If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.
"""
pattern = r"9{1,3}$"

if re.match(pattern, "9"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")

if re.match(pattern, "9999"):
   print("Match 3")


print("-"*8,"Groups","-"*8)
"""
The content of groups in a match can be accessed using the group function.
A call of group(0) or group() returns the whole match.
A call of group(n), where n is greater than 0, returns the nth group from the left.
The method groups() returns all groups up from 1.
"""
pattern = r"a(bc)(de)(f(g)h)i"

the_match = re.match(pattern, "abcdefghijklmnopqrstuvwxyz")

if the_match:
	print(the_match.group()) # prints the entire match
	print(the_match.group(0)) # prints the entire match

	print(the_match.group(1))
	print(the_match.group(2))
	print(the_match.group(3))
	print(the_match.group(4))

	print(the_match.groups()) # prints all groups
	print(the_match.groups()[0]) # equivalent match.group(1)


"""
There are several kinds of special groups.
Two useful ones are named groups and non-capturing groups.
Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering.
"""
"""
Using named/numbered groups is only necessary if you want to be able to refer back to that group again. 
For instance, if you were using RE to rename a bunch of files, you could use a named group to find a portion of the filename and then use it in the renaming process. 
In the filename, say there is some extra information in the name that you want to get rid of. For instance, you want to remove the band name from a bunch of mp3 filenames.
You could use a non-capturing group to find that group but not include it in the renaming process. All of the files have the band name, so you want to search for it. 
But you don't want to use it in the rename, so you don't capture it.
"""
pattern = r"(?P<first>abc)(?:def)(ghi)"

the_match = re.match(pattern, "abcdefghijklmnopqrstuvwxyz")

if the_match:
	print(the_match.group("first")) # the first group, in this case, gets printed, because it is a named group
	print(the_match.groups()) # the group (?:def) does not get printed, because it is a non-capturing group


print("-"*8,"Metacharacter |","-"*8)
"""
Another important metacharacter is |.
This means "or", so red|blue matches either "red" or "blue".
"""
pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
   print ("Match 1")

match = re.match(pattern, "grey")
if match:
   print ("Match 2")    

match = re.match(pattern, "griy")
if match:
    print ("Match 3")



print("-"*8,"Special sequences","-"*8)
"""
There are various special sequences you can use in regular expressions. They are written as a backslash followed by another character.
One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17. This matches the expression of the group of that number.
"""
pattern = r"(.+) (.+) (.+) \1" 

match = re.match(pattern, "abc bca cab abc") 
if match:
	print ("Match 1") 

match = re.match(pattern, "abc bca cab bca") 
if match: 
	print ("Match 2") 

match = re.match(pattern, "abc bca cab cab") 
if match: 
	print ("Match 3") 



print("-"*8,"Email extraction","-"*8)
"""
Email extraction
"""
str = "Please contact info-test@sololearn.co.jp or info-slate@sololearn.co.jp for assistance"

pattern = r"(\w+[\.-]*\w*@\w+[\.-]\w*\.[\w\.]+)"


match = re.findall(pattern, str)

if match:
	print(match)
