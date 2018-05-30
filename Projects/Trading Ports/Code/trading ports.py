import time
from random import randint

class Good:
    def __init__(self,name,production_cost,selling_price):
        self.name = name
        self.cost = production_cost
        self.price = selling_price
        self.maze = 1

    def pname(self):
        print('This good is called:',self.name)

    def pcost(self):
        print(self.name,"'s production cost:",self.cost,'Gold')

    def pprice(self):
        print(self.name,"'s current price:",self.price,'Gold')

    def pmaze(self):
        print('Every unit of goods has volume:',self.maze,'m³')

#Goods definition

goods_list = []
goods_names = []

dye = Good('Dye',370,525)
goods_list.append(dye)
wood = Good('Wood',465,770)
goods_list.append(wood)
marble = Good('Marble',370,525)
goods_list.append(marble)
wine = Good('Wine',465,770)
goods_list.append(wine)
cloth = Good('Cloth',465,770)
goods_list.append(cloth)
ebony = Good('Ebony',465,770)
goods_list.append(ebony)
iron = Good('Iron',465,770)
goods_list.append(iron)
jewelry = Good('Jewelry',370,525)
goods_list.append(jewelry)
brick = Good('Brick',370,525)
goods_list.append(brick)
glass = Good('Glass',370,525)
goods_list.append(glass)
dh = Good('Dried Herbs',465,770)
goods_list.append(dh)
salt = Good('Salt',465,770)
goods_list.append(salt)
alabaster = Good('Alabaster',465,770)
goods_list.append(alabaster)
gold = Good('Gold',370,525)
goods_list.append(gold)
honey = Good('Honey',465,770)
goods_list.append(honey)
granite = Good('Granite',465,770)
goods_list.append(granite)

for i in goods_list:
    goods_names.append(i.name)

class Ship:

    def __init__(self,name,speed,cargo_capacity,price):
        self.name = name
        self.mph = speed
        self.space = cargo_capacity
        self.price = price

    def pname(self):
        print('This ship is called:',self.name)

    def pspeed(self):
        print(self.name,"'s top speed:",self.mph,'mph')

    def pspace(self):
        print(self.name,"'s cargo capacity:",self.space,'m³')

    def pprice(self):
        print(self.name,"'s current price:",self.price,'Gold')

#Ships definition

ships_list = []
sh_names = []

bar = Ship('Barque',22.5,150,52000)
ships_list.append(bar)
fri = Ship('Frigate',40,90,15000)
ships_list.append(fri)
cor = Ship('Corvette',46,70,48000)
ships_list.append(cor)
ind = Ship('East Indiaman',8,270,92000)
ships_list.append(ind)
gal = Ship('Galleon',19.6,170,56000)
ships_list.append(gal)
sch = Ship('Schooner',70,50,120000)
ships_list.append(sch)
yac = Ship('Yacht',16,300,149000)
ships_list.append(yac)

for i in ships_list:
    sh_names.append(i.name)

class Port:

    def __init__(self,name,location,provides,demands):
        self.name = name
        self.location = (location)
        self.provides = provides
        self.demands = demands
        self.ships = []
        self.economy = 100000000
        self.scargos = {}
        self.inventory = []
        self.warehouse = 6000
        self.sh_count = {}
        for i in sh_names:
            self.sh_count[i] = 1


    def whcap(self):
        print("Port's current warehouse capacity:",self.warehouse,'m³')

    def pname(self):
        print("Port's name:",self.name)

    def plocation(self):
        print("Port's co-ordinates:\nx: ",self.location[0],'\ny: ',self.location[1])

    def prov(self):
        if len(self.provides) > 0:
            print('Port',self.name,'provides: ',end = '')
            for i in range(len(self.provides)):
                if i == len(self.provides) - 1:
                    print(self.provides[i])
                else:
                    print(self.provides[i], end = ', ')
        else:
            print('Port',self.name,'currently provides no good.')

    def dem(self):
        if len(self.demands) > 0:
            print('Port',self.name,'demands: ',end = '')
            for i in range(len(self.demands)):
                if i == len(self.demands) - 1:
                    print(self.demands[i])
                else:
                    print(self.demands[i], end = ', ')
        else:
            print('Port',self.name,'currently demands no good.')

    def buy_ship(self,name):
        if name not in sh_names:
            print('There is no ship called',name,'.')
        else:
            for i in range(len(sh_names)):
                if len(self.ships) < 10:
                    if name == sh_names[i]:
                            if self.economy >= ships_list[i].price:
                                self.scargos[name+' '+str(self.sh_count[name])] = []
                                self.sh_count[name] += 1
                                self.ships.append(name)
                                self.economy -= ships_list[i].price
                                print(name,'bought.\nGold:',self.economy)
                            else:
                                missing_gold = ships_list[i].price - self.economy
                                print('Port',self.name,'cannot afford a',name,'right now.\n\nMissing gold: ',missing_gold,"\nPort's gold: ",self.economy)
                else:
                    print('Port',self.name,"can't have any other ship anchored for now, it can only have a maximum of 10 ships docked at the same moment.")
                    break

    def sell_ship(self,name):
        tempcount = 0
        if len(name.split()) == 1:
            if name not in sh_names:
                print('There is no ship called',name+'.')
            elif name not in self.ships:
                print('Port',self.name,"hasn't any",name,'docked at the moment.')
            else:
                for i in range(len(self.scargos)):
                    if list(self.scargos)[i].split()[0] == name:
                        tempcount += 1
                        uniq = list(self.scargos)[i]
                        for i in range(len(ships_list)):
                            if name == sh_names[i]:
                                profit = ships_list[i].price * (75/100)
                                break
                if tempcount == 1:
                    self.scargos.pop(uniq)
                    self.economy += profit
                    self.ships.remove(uniq.split()[0])
                    print(uniq,'has been sold for: ',profit,"Gold.\nPort's gold: ",self.economy)
                else:
                    print('When a port has more than 1',name+'s docked, it is required to clarificate which one you want to sell.')

        else:
            if name in self.scargos:
                for i in range(len(ships_list)):
                    if name.split()[0] == sh_names[i]:
                        self.ships.remove(sh_names[i])
                        self.scargos.pop(name)
                        self.economy += ships_list[i].price * (75/100)
                        profit = ships_list[i].price * (75/100)
                        print(name,'has been sold for: ',profit,"Gold.\nPort's gold: ",self.economy)
            elif name.split()[0] not in sh_names:
                print('There is no ship called',name.split()[0]+'.')
            elif name.split()[0] not in self.ships:
                print('Port',self.name,"hasn't any",name.split()[0],'dock at the moment.')
            else:
                for i in self.scargos:
                    if i.split()[0] == name.split()[0]:
                        tempcount += 1
                    if tempcount >= 1:
                        print('Port',self.name,"hasn't any",name,'docked at the moment.')
                        break
                    else:
                        if len(self.scargos) == 1:
                            print('Port',self.name,"hasn't any",name.split()[0],'docked at the moment.')

    def buy_good(self,amount,good,storage):
        if good not in goods_names:
                print('There is no good called',good+'.')
        else:
            if storage in self.scargos:
                for i in range(len(goods_names)):
                    if good == goods_names[i]:
                        purchase_list = [amount,good]
                        if self.economy >= goods_list[i].price * amount:
                            if len(self.scargos[storage]) == 0:
                                self.scargos[storage].append(purchase_list)
                            else:
                                for j in range(len(self.scargos[storage])):
                                    if good == self.scargos[storage][j][1]:
                                        self.scargos[storage][j][0] += amount
                                        break
                                    else:
                                        if j == len(self.scargos[storage]) - 1:
                                            self.scargos[storage].append(purchase_list)
                                        else:
                                            continue
                            print(amount,good,'bought for', goods_list[i].price * amount,'Gold.\nYour Gold:',self.economy)
                            self.economy -= goods_list[i].price * amount
                        else:
                            missing_gold = goods_list[i].price * amount - self.economy
                            print('Port',self.name,'cannot afford',amount,good,'right now.\n\nMissing Gold:',missing_gold,'\nYour Gold:',self.economy)
            elif storage == 'Warehouse':
                for i in range(amount):
                    self.inventory.append(good)
            else:
                if storage in self.ships and self.ships.count(storage) > 1:
                    print('When a port has more than 1',storage+'s docked, it is required to clarificate which one you want to store the goods into.')
                elif storage in self.ships and self.ships.count(storage) == 1:
                    print('Buy the goods (In progress)')
                else:
                    print("Goods can be stored only in specific storages, like the port's warehouse or a ship's cargo.",storage,"isn't a warehouse, nor a ship.")

    def pships(self):
        if len(self.ships) > 0:
            print('Ships currently docked on port',self.name+': ', end = '')
            for i in sh_names:
                if self.ships.count(i) > 1:
                    if  i != sorted(self.ships)[len(self.ships)-1]:
                        print(self.ships.count(i),i + 's',end = ', ')
                    else:
                        print(self.ships.count(i),i + 's\n')
                elif self.ships.count(i) == 1:
                    if  i != sorted(self.ships)[len(self.ships)-1]:
                        print(self.ships.count(i),i,end = ', ')
                    else:
                        print(self.ships.count(i),i + '\n')
            for i in sorted(self.scargos):
                print('Cargo of',i+':', end = ' ')
                if len(self.scargos[i]) == 0:
                    print('Empty')
                else:
                    for j in range(len(self.scargos[i])):
                        if j != len(self.scargos[i]) - 1:
                            print(self.scargos[i][j][0],self.scargos[i][j][1], end = ', ')
                        else:
                            print(self.scargos[i][j][0],self.scargos[i][j][1])
        else:
            print('None of ships are currently docked on',self.name+'.')

#Port definition

port_list = []
port_names = []

liv = Port('Liverpool', (330,700), ['Dye', 'Lumber'],['Honey', 'Alabaster', 'Gold'])
port_list.append(liv)
ham = Port('Hamburg', (40,100), ['Marble', 'Wine'], ['Brick', 'Salt', 'Glass'])
port_list.append(ham)
pei = Port('Peireaus', (1000,450), ['Cloth', 'Ebony'], ['Honey', 'Gold', 'Granite'])
port_list.append(pei)
sev = Port('Seville', (600,50), ['Iron', 'Jewelry'], ['Brick', 'Glass', 'Dried Herbs'])
port_list.append(sev)
lis = Port('Lisbon', (1200,580), ['Brick', 'Glass'], ['Dye', 'Lumber', 'Marble'])
port_list.append(lis)
ams = Port('Amsterdam', (470,280), ['Dried Herbs', 'Salt'], ['Jewelry', 'Ebony', 'Iron'])
port_list.append(ams)
ven = Port('Venice', (900,630), ['Alabaster', 'Gold'], ['Marble', 'Wine', 'Dye'])
port_list.append(ven)
lon = Port('London', (510,120), ['Honey', 'Granite'], ['Jewelry', 'Iron', 'Cloth'])
port_list.append(lon)

for i in port_list:
    port_names.append(i.name)

# wh store failed print('Port',self.name,"warehouse hasn't enough capacity to store",amount,good+'.\n\n'+storage,'cargo capacity:',self.capacity,'m³ / 6000 m³')
# wh store successfull print(amount,good,'bought for', goods_list[i].price * amount,"Gold.\nPort's Gold:",self.economy,'\n\n'+storage,'cargo capacity:',self.capacity,'m³ / 6000 m³')
# ship store failed print('Cargo of',storage,"hasn't enough capacity to store",amount,good+'\n'+'Cargo Capacity of',storage+':',self.scargos[storage][0],'m³ /',ships_list[i].space,'m³')
# ship store successfull print(amount,good,'bought for', goods_list[i].price * amount,"Gold.\nPort's Gold:",self.economy,'\n\n'+'Cargo Capacity of',storage+':',self.scargos[storage][0],'m³ /',ships_list[i].space,'m³')
