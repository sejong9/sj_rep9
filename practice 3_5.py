print "===================="
my_file = open('C:\Temp\sample.txt', 'r')
print my_file.read()
my_file = open('C:\Temp\sample.txt.', 'a')
my_file.write('\n4. Drink coffee')
my_file.close()
print "===================="
my_file = open('C:\Temp\sample.txt', 'r')
print my_file.read()

