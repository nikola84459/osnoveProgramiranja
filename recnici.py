korisnici={'pera':['12345','Petar','Markovic','prodavac'], 'perica':['12346','Petar','Markov','prodavac'], 'milojko':['12345678','Milovan','Perić','prodavac'], 'darko123':['12345','Darko','Milošević','menadzer'], 'nidza':['1111','Nikola','Vidović','menadzer']}
zanrovi=['Akcija', 'Komedija','Avantura','Drama','Fantazija','Misterija', 'Triler', 'Romantika', 'Horor']
filmovi={'f1':['Edvard Makazoruki','Fantazija'], 'f2':['Pirati sa Kariba', 'Avantura'], 'f3':[ 'Čokolada', 'Romantika'], 'f4':    [ 'Titanik', 'Romantika'], 'f5':[ 'Sam u Kući', 'Komedija'], 'f6':[ 'Hari Poter', 'Avantura'], 'f7':[' Gospodar Prstenova', 'Avantura'], 'f8':[ 'Spajdermen', 'Akcija'], 'f9':[ 'Biser Bojane', 'Komedija'], 'f10':[ 'Čudesni spajdermen', 'Avantura']} 
projekcije={'p1':['15.11.2017.','15:50', 120, 250, 'f1', 'S5'], 'p2':['15.11.2017.', '16:50',100 , 300 ,'f2','S4' ], 'p3':['16.11.2017.', '10:30',150 ,500 , 'f3', 'S1'],'p4':['16.11.2017.',
    '11:20', 90 , 150, 'f4', 'S2'], 'p5':['17.11.2017.', '17:30', 100, 500 , 'f5' ,'S2'], 
    'p6':['17.11.2017.', '18:30', 120 , 400 , 'f4','S1'], 'p7':['18.11.2017.', '20:30', 120, 600 , 'f6', 'S4'], 'p8':['18.11.2017.', '17:30', 150, 350 , 'f1', 'S3'], 'p9':['18.11.2017.', '14:30', 90 , 250, 'f2', 'S2'], 'p10':['19.11.2017.', '19:20', 120, 400 ,'f5', 'S2']}
sale={'S1':50, 'S2': 200, 'S3': 300,'S4': 100, 'S5': 100} 
racuni={1:['16.11.2017.', '17:34', [['p1', 3],['p2', 1]], 0]}
for p in projekcije.keys():
	projekcije[p].append(False)
	projekcije[p].append(0)