from datetime import datetime, timedelta, date
import os, sys, time, random, math, json, collections, itertools, functools, pathlib
from collections import Counter, defaultdict, namedtuple
from itertools import combinations, permutations, count

#-----------OS Modules-----------#
print(os.getcwd()) #Current Working Directory
print(os.listdir(".")) #List of files and directories in the current directory
print(os.path.exists(".")) #Check if a path exists
# os.mkdir("demo_folder") #Create a new directory
# os.rmdir("demo_folder") #Remove a directory
# print(os.environ.get("PATH"))
os.system("echo Hello from OS!") #Run system command
# for root, dirs, files in os.walk("."): #Walk through the directory
#     print(root)
#     print(dirs)
#     print(files)

for item in os.listdir("."):#List of files and directories in the current directory
    print(item)

#-----------System Modules-----------#
print(sys.argv) #Command-line arguments
print(sys.version) #Python version
print(sys.maxsize) #Maximum integer size
print(sys.platform) #Platform
print(sys.path)
# data = sys.stdin.readline() #Read from standard input
# print(data)

#-----------DateTime Modules-----------#
print(datetime.now())
print(date.today())
print(datetime.now().strftime("%Y-%m-%d %H:%M"))
print(datetime.now() + timedelta(days=1))

#-----------Random Modules-----------#
print(random.randint(1, 100)) #Random integer
print(random.random()) #Random float from 0 to 1
print(random.choice(["apple", "banana"])) #Random choice
numbers = [1, 2, 3, 4]
print(random.choices(numbers, k=3)) #Random choices
random.shuffle(numbers)
print(numbers)
print(random.sample(numbers, k=2)) #Random sample
print(random.uniform(1, 10)) #Random float from 1 to 10
print(random.gauss(0, 1)) #Random float from normal distribution

#-----------Math Modules-----------#
print(math.pi)
print(math.sqrt(16))
print(math.factorial(5))
print(math.sin(math.radians(30)))
print(math.ceil(4.1))
print(math.floor(4.9))

#-----------JSON Modules-----------#
data = {"name": "John", "age": 30, "city": "New York"}
json_str = json.dumps(data) #Python → JSON string
print(json_str)
back_to_dict = json.loads(json_str) #JSON → Python
print(back_to_dict["name"])


#-----------Collections Modules-----------#
c = Counter("abracadabra")
print(c)                        # Counter({'a': 5, 'b': 2, ...})
print(c.most_common(2))         # Top 2
d = defaultdict(int)
d["a"] += 1
print(d["b"])                   # 0 (instead of error)
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)
