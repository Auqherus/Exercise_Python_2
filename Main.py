# Exc 1
helloMessage = "Hello %s!"
print(helloMessage % "Kate")
print(helloMessage % "Chris")

# Exc 2

helloMessage2 = "Hello {0:s}!"
print(helloMessage2.format("Kate"))
print(helloMessage2.format("Chris"))\

# Exc 3
helloMessage3 = "%s has %d %s"

print("%s has %d %s"%("Kate",1,"animal"))
print("%s has %d %s"%("Chris",100000,"$"))

# Exc 4

helloMessage4 = "{0:s} has {1:d} {2:s}"

print(helloMessage4.format("Kate",1,"animal"))
print(helloMessage4.format("Chris",100000,"$"))

# Exc 5

line = '{0:20s} cost {1:d}'


