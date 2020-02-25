class parkingFloor():
    def __init__(self,name):
        self.name = name
        self.spotTotal = {'compact':0,'large':0,'bike':0,'electric':0}

        self.spotTaken = {'compact':0,'large':0,'bike':0,'electric':0}

        self.freeSpot = {'compact':set(),'large':set(),'bike':set(),'electric':set()}
        self.takenSpot = {'compact':{},'large':{},'bike':{},'electric':{}}

    def assignSpot(self,tickt):
        if self.spotTaken[tickt.veh.type] >= self.spotTotal[tickt.veh.type]:
            return False
        for s in self.freeSpot[tickt.veh.type]:
            if s.id not in self.takenSpot[tickt.veh.type]:
                self.takenSpot[tickt.veh.type][s.id] = tickt
            self.spotTaken[tickt.veh.type]+=1
            self.freeSpot[tickt.veh.type].remove(s)
            tickt.allocateSpot(s)
            return True
        return False

    def addSpot(self,type,v):
        for v in range(v):
            s = spot(type)
            self.freeSpot[type].add(s)
        self.spotTotal[type] += v

class entryPanel():
    def __init__(self,id):
        self.id = id

    def printTicket(self,tickt):
        print('Vehicle ID ',tickt.veh.id)
        print('Spot ID ',tickt.spot.id)
        print('Ticket ID ',tickt.id)
        print('Date Time',tickt.DateTime)

    def display(self,message):
        print(message)


class vehicle():
    def __init__(self,id,vehType):
        self.id = id
        self.type = vehType


class spot():
    def __init__(self,spotType):
        def generateId():
            # some mechanism to generate spot id
            return 1
        self.id = generateId()
        self.type = spotType



class ticket():
    def __init__(self,v1):
        self.id = self.generateId()
        self.veh = v1

        self.spot = None
        self.DateTime = self.getTime()
        self.amount = 0
        self.status = 'Active'
        self.payment = None

    def getTime(self):
        time = 1234
        return time

    def generateId(self):
        # some mechanism to generate new ticket id
        new_ticket  = 1
        return new_ticket

    def allocateSpot(self,spot):
        self.spot = spot

    def addPayment(self,pay):
        self.status = 'Complete'
        self.payment = pay

class parkingLot():
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.level = []

    def addLevel(self,floor):
        self.level.append(floor)

    def processEntry(self,t1,gate):
        for l in self.level:
            if l.assignSpot(t1):
                gate.printTicket(t1)
                return
        gate.display('No Spot Empty')

    def processExit(self,tickt,gate):
        def getTime():
            # Gives the current time
            return 3
        currTime = getTime()
        print('Processing fare',tickt.veh.type,tickt.spot.id,tickt.DateTime,currTime)
        amountCalculated = 7
        tickt.addPayment(Payment(amountCalculated))
        gate.display('Payment Successful')

class Payment():
    def __init__(self,amount):
        self.id = 'paymentid2'
        self.type = 'credit' # debit
        self.time = 'paymet time'

class displayBoard():
    def show(self,p):
        for l in p.level:
            print(l.name)
            for k in l.spotTotal.keys():
                print(k, l.spotTotal[k] - l.spotTaken[k])


P = parkingLot('Chandan','Mumbai')
floor1 = parkingFloor('floor1')
P.addLevel(floor1)
floor1.addSpot('compact',5)

board = displayBoard()
board.show(P)

entryPanel1 = entryPanel('1')

v1 = vehicle(1,'compact')
t1 = ticket(v1)

P.processEntry(t1,entryPanel1)
P.processExit(t1,entryPanel1)
