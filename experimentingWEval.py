

def ready():
    print "ready"

def set():
    print "set"

def go():
    print "go"

L = ["ready","set","go" ]

for command in L:
    eval(command)()
