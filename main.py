#lists vai saraksti
#['Sveika,', 100,' tu', 3.59, 'skaista', [1.26]]
myList = [1, 2, 3, 100,' tu', 3.59, 'skaista']
print(len(myList)) #saraksta garums

my_List=["viens", "divi", "tris", "četri"]
print(my_List[0]) #izdruka elementu at noradito indeksu
print(my_List[1:4]) #izdruka no noradita indeksa lidz beigam

#sarakstu apvienošana jeb konkatinācija
cits_list=["pieci", "seši"]
print(my_List+cits_list) #izdruka sarakstu ar abu mainigo elementiem
jauns_list=my_List+cits_list
print(jauns_list)

#sarakstu mainišana
jauns_list[0]=1
print(jauns_list)

jauns_list.append("septiņi")
print(jauns_list)
jauns_list.append(8)
print(jauns_list)

pop_elem=jauns_list.pop(3) #nonem pedejo elementu
print(jauns_list)
print(pop_elem)

#elementu kartošana
new_list = ['b', 'a', 'z', 'e']
print(new_list)
num_list = [4,1,8,3]
new_list.sort()
print(new_list)
num_list.sort()
print(num_list)
num_list.reverse() #sakarto preteja seciba
print(num_list)
myList = [1, 2, 3, 100, 3.59]
myList.sort()
print(myList)

#saraksts sarakstā (nested)
nested_list =[1, 5, [7, 2]]
print(nested_list[2][1])



augli=["ābols", "bananas", "ģūrķis"]
print(augli[2])
#aizstat elementu - gurķis ->apelsins
augli[2] = "apelsīns"
print(augli)
#pievienot "bumbieris"
augli.append("bumbieris")
print(augli)
#iespraust konkreta vieta jaunu elementu "citrons"
augli.insert(2,"citrons")
print(augli)
#izņemt no saraksta "banans"
augli.pop(1)
print(augli)
#izdrukat pilna teikuma, cik augli ir saraksta
print(f"saraksta ir {len(augli)} dažadi augli" )
#vardnica
tel = {
"direktors":"20405567",
"vietnieks":"67211996",
"sekritare":"64954712"
  }
print(tel["direktors"]) #noradit atslegu, izdruka vertību

cenas = {'piens':1.12, 'aboli':0.95, 'apelsini':1.89  }
print(cenas['piens'])

d = {
"k1":123,
"k2":[10,11,12],
"k3":{'atsl1':100, 'atsl2':200}
}




