__author__ = 'takacs'

afa_data = {}
afa_data_list = []
table = []
eredmeny_list = []
afakulcs = '25%'
afaertek = 500
ujafaertek = 1000
afaalap = 300
ujafaalap = 600


for afakulcs in ['25%', '10%', '25%']:
    if afakulcs not in afa_data:
       afa_data[afakulcs] = [afaalap, afaertek]
    else:
       afa_data[afakulcs][0] += ujafaalap
       afa_data[afakulcs][1] += ujafaertek

for key,value in afa_data.items():
    eredmeny_list.append([key,value[0], value[1]])


print(afa_data.items())
print (repr(eredmeny_list))


'''
temp_list = []
for index, afakulcs in enumerate(['25%', '10%', '25%']):
    if afakulcs not in temp_list:
       temp_list.append(afakulcs)
       afa_data[afakulcs] = [afaalap, afaertek]
       afa_data_list.append([afakulcs, afaalap, afaertek])
    else:
       list_existing_afavalue = afa_data[afakulcs]
       list_existing_afavalue[0] += ujafaalap
       list_existing_afavalue[1] += ujafaertek
       #list_existing_afavalue = afa_data[afakulcs]
       #afa_data_list.remove()
       #afa_data_list.append([afakulcs, list_existing_afavalue[0],list_existing_afavalue[1] ])

print ("afa_data::  " + repr(afa_data))
print ("afa_data_list:: " + repr(afa_data_list))
print ("|".join(str(v) for v in afa_data_list))

derp = (('Cat','Pet'),('Dog','Pet'),('Spock','Vulcan'))
derp= [['25%', 300, 500], ['10%', 300, 500], ['27%', 800, 900]]
i = None
for index, item in enumerate(derp):
    if item[0] == '27%':
         i = index
         break
print (i)

for key,value in afa_data.items():
    print (key, 'corresponds to', value[0], value[1])
    eredmeny_list.append([key,value[0], value[1]])
    print ('{0} corresponds to {1}'.format(key, value))

print(repr(eredmeny_list))

'''
ceg = [["Szolgáltató"],
       ['selectedCeg.nev'],
       ['cegcim1'],
       ['cegadoszam'],
       ['cegbankszamlaszam'],
       ['cegemail'],
       ['cegweblap1'],
       ['']]
megrendelo = [["Megrendelő:"],
              ['selectedVevo.nev'],
              ['vevocim'],
              ['vevorendszam'],
              ['vevogyartmany'],
              ['vevogepjarmutipus'],
              ['vevogepjarmufajta'],
              ['vevogepjarmukmh']]
cegadatoklist = [[ceg, megrendelo]]

while None in megrendelo:
    megrendelo.remove(None)
megrendelo = list(filter(None, megrendelo))

print(cegadatoklist)