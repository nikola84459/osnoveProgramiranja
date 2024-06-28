import korisnici as k
import recnici as r
from beautifultable import BeautifulTable


# funkcija koja izvršava pretragu projekcija
def pretraga(uloga):
	print('Ako želite da vidite sve projekcije pritisnite enter,ako ne unesite pojam za pretragu.')
	uneto=input('Ukoliko želite da pretražite određeni pojam, unesite pojam za pretragu: ')
	lista = []
	for i in r.projekcije.keys():
		#da li je projekcija obrisana?
		if r.projekcije[i][6]==False:
			if uneto==i or uneto.lower() in r.filmovi[r.projekcije[i][4]][0].lower() or uneto.lower() in r.filmovi[r.projekcije[i][4]][1].lower() or uneto.lower() in r.projekcije[i][5].lower():
			 	lista.append(i)

			 	

	
	if lista == []:
		print('\nNije pronađena ni jedna projekcija koja sadrži uneti pojam.\n')
		pretraga(uloga)
	else:
		stampanje_projekcije(lista)
	if uloga == 'prodavac':
		k.meni_prodavac()
	else:
		k.meni_menadzer()



#Funkcija za unos novih projekcija
def unos_projekcije():
	print('\nUnesite podatke o projekciji: ')
	b=1
	while b:
		b=1
		while b:
			idp=input('\nID: ')
			if idp =='':
				print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo.')
			else:
				b=0	
		if idp in r.projekcije.keys():
			print('\nVeć postoji projekcija sa unetim ID-em.\n')
			b=1
		else:
			b=0
	
			
	datum1 = unos_datuma()
	vreme1 = unos_vremena()
	trajanje1 = vreme_trajanja()
	cenaa = unos_cene()
	film1 = unos_filma()
	sala1 = unos_sale()
	
	# PROVERA KONFLIKTA 
	konf=konflikt(datum1, vreme1, trajanje1, sala1)
	if konf:
		r.projekcije[idp] = [datum1, vreme1, trajanje1, cenaa, film1, sala1, False, 0]
		print('\nUspešno ste uneli novu projekciju.')
		lista = []
		lista.append(idp)
		stampanje_projekcije(lista)
		k.meni_menadzer()
	else:
		print('Ova projekcija ne može biti uneta, jer je u konfliktu sa već postojećom projekcijom u istoj sali i u isto vreme.')
		k.meni_menadzer()	

#funkcija za unos novog filma	
def unos_novog_filma(idf):
	b=1
	while b:
		naziv=input('\nUnesite ime filma: ')
		if naziv =='':
			print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo.')
		else:
			b=0	
		
	rb=1
	for z in r.zanrovi:
		print('{}. {}'.format(rb, z))
		rb+=1

	b=1
	while b:
		b=1
		while b:
			zanr_br=input('\nUnesite redni broj žanra za film: ')
			if zanr_br == '':
				print('\nUnos ne može biti prazan. Molimo Vas unesite ponvo.')
			else:
				b=0
				bb=1 #pp da će uneti integer (zanr_br)
				try: zanr_br = int(zanr_br) 
				except ValueError: bb=0
				if bb and zanr_br >= 1 and zanr_br <= rb-1:
					zanr = r.zanrovi[int(zanr_br)-1]
					r.filmovi[idf]=[naziv,zanr]
					b=0
				else:
					b=1
					print('\nNiste uneli ispravan žanr, molimo Vas pokušajte ponovo.')	

#funkcija za brisanje projekcije
def brisanje():
	b=1
	while b:
		b=1
		while b:
			idp=input('\nUnesite ID projekcije koju želite da izbrišete: ')
			if idp == '':
				print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo.')
			else:
				b=0	
				if idp in r.projekcije.keys():
					if r.projekcije[idp][6]==False:
						r.projekcije[idp][6]=True
						print('\nUspešno ste obrisali projekciju.')
						k.meni_menadzer()
					else:
						print('\nOva projekcija je već obrisana.')
						k.meni_menadzer()
				else:
					print('\nNe postoji projekcija sa unetim ID-em.')	
					brisanje()		
						
#funkcija za unos ID-a projekcije	
def unos_id():
	b=1
	while b:
		unet_id=input('\nUnesite id projekcije koju želite da izmenite: ')
		if unet_id =='':
			print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo.\n')
		else:
			b=0	
			if unet_id not in r.projekcije.keys():
				print('\nNe postoji projekcija sa unetim ID-em.')
				unos_id()
			else:
				izmena_projekcije(unet_id)

#funkcija za izmenu projekcije
def izmena_projekcije(unet_id):	
	print('\n1. Datum projkecije\n2. Vreme projekcije\n3. Vreme trajanja projekcije\n4. Cena karte\n5. ID filma\n6. Sala prikazivanja\n7. Povratak u glavni meni')
	b=1
	while b:
		uneto=input('\nIzaberite odredjenu stavku koju želite da izmenite: ')
		if uneto == '':
			print('\nMolimo Vas unesite redni broj ispred stavke koju želite da izmenite.')
			izmena_projekcije(unet_id)
		else:
			b=0	

	if uneto=='1':
		datum1 = unos_datuma()
		r.projekcije[unet_id][0]=datum1
		print('\nUspešno ste promenili datum projekcije.\n\nUkoliko želite da promenite još neki podatak odabrane projekcije,odaberite željenu stavku. U suprotnom odaberite povratak u meni.')
		izmena_projekcije(unet_id)
	elif uneto=='2':
		vreme1 = unos_vremena()
		r.projekcije[unet_id][1]=vreme1
		print('\nUspešno ste promenili vreme projekcije.\n\nUkoliko želite da promenite još neki podatak odabrane projekcije,odaberite željenu stavku. U suprotnom odaberite povratak u meni.')
		izmena_projekcije(unet_id)
	elif uneto=='3':
		vreme1 = vreme_trajanja()
		r.projekcije[unet_id][2]=vreme1
		print('\nUspešno ste promenili vreme trajanja projekcije.\n\nUkoliko želite da promenite još neki podatak odabrane projekcije,odaberite željenu stavku. U suprotnom odaberite povratak u meni.')
		izmena_projekcije(unet_id)
	elif uneto=='4':
		cena1 = unos_cene()
		r.projekcije[unet_id][3]=cena1
		print('\nUspešno ste promenili cenu projekcije.\n\nUkoliko želite da promenite još neki podatak odabrane projekcije,odaberite željenu stavku. U suprotnom odaberite povratak u meni.')
		izmena_projekcije(unet_id)
	elif uneto=='5':
		film = unos_filma()
		r.projekcije[unet_id][4]=film
		print('\nUspešno ste promenili ID filma projekcije.\n\nUkoliko želite da promenite još neki podatak odabrane projekcije,odaberite željenu stavku. U suprotnom odaberite povratak u meni.')
		izmena_projekcije(unet_id)
	elif uneto=='6':
		sala1 = unos_sale()
		r.projekcije[unet_id][5]=sala1
		print('\nUspešno ste promenili salu projekcije.\n\nUkoliko želite da promenite još neki podatak odabrane projekcije,odaberite željenu stavku. U suprotnom odaberite povratak u meni.')
		izmena_projekcije(unet_id)	
	elif uneto=='7':
		k.meni_menadzer()
	else:
		print('\nTražena opcija ne postoji.')	
		izmena_projekcije(unet_id)		

#funkcija za unos datuma	
def unos_datuma():
	b=1
	while b:
		b=1
		while b:
			datum=input('\nUnesite datum projekcije [dd.mm.yyyy.]: ')
			if datum =='':
				print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo.')
			else:
				b=0
				broj = 1
				try: dd = int(datum[0:2])
				except ValueError: broj=0
				try: mm = int(datum[3:5])
				except ValueError: broj=0
				try: yyyy = int(datum[6:10])
				except ValueError: broj=0

		if  broj and len(datum)==11 and dd >0 and dd<=31 and mm > 0 and mm <= 12 and yyyy >=2018 and datum[2] == datum[5] == datum[10] == '.':
			b=0
			return datum
		else:
			b=1
			print('\nMolimo Vas unesite datum u traženoj formi.')

#funkcija za unos vremena	
def unos_vremena():
	b=1
	while b:
		b=1
		while b:
			vreme=input('\nUnesite vreme projekcije: [hh:mm]: ')
			if vreme =='':
				print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo')
			else:
				b=0
				br=1
				try: hh = int(vreme[0:2])
				except ValueError: br=0
				try: mm = int(vreme[3:5])
				except ValueError: br=0

		if br and len(vreme)==5 and hh>=0 and hh<24 and mm>=0 and mm<60 and vreme[2]==':':
			b=0
			return vreme
		else:
			b=1
			print('\nMolimo Vas unesite vreme u traženoj formi.')

#funkcija za unos vremena trajanja projekcije
def vreme_trajanja():
	b=1
	while b:
		b=1
		while b:
			minuti=input('\nUnesite vreme trajanje u minutima:  ')
			if minuti == '':
				print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo.')
			else:
				b=0	
			
		b=0 # pp da će biti dobro uneti
		try: minuti = int(minuti)
		except ValueError: b=1 #minuti nisu dobro uneti
		if b:
			print('\nMolimo unesite minute u traženoj formi')	
		else:
			if minuti <= 0:
				print('\nNiste dobro uneli broj, unesite broj veći od nule.')
				b=1
			else:
				return minuti

#funkcija za unos cene karata
def unos_cene():
	b=1
	while b:
		b=1
		while b:
			cena=input('\nCena karte: ')
			if cena == '':
				print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo.')
			else:
				b=0	
			
		b=0 # pp da će biti dobro uneti
		try: cena = float(cena)
		except ValueError: b=1

		if b:
		 	print('\nMolimo unesite cenu u traženoj formi.')
		else:
			if cena > 0:
				return cena
			else:
				print('Cena ne može biti manja od nule.')
				b=1

#funkcija za unos filma
def unos_filma():
	b=1
	while b:
		idf = input('\nUnesite ID filma: ')
		if idf == '':
			print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo.')
		else:
			b=0	
	if idf not in r.filmovi.keys():
		print('\nTraženi film ne postoji, molimo Vas unesite podatke o tom filmu.')
		unos_novog_filma(idf)
	return idf

#funkcija za unos sale u kojoj je projekcija
def unos_sale():
	b=1
	while b:
		b=1
		while b:
			sala=input('\nUnesite salu prikazivanja: ')
			if sala =='':
				print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo.')
			else:
				b=1	
				if sala not in r.sale.keys():
					print('\nNe postoji navedena sala.')
				else:
					return sala
					b=0

#funkcija za tabelarni prikaz
def stampanje_projekcije(lista):
    t = BeautifulTable()
    t.column_headers=['ID', 'Datum', 'Vreme', '[min]', '[RSD]', 'Film', 'Žanr', 'Sala','Mesta']
    for idp in lista:
    	d = r.projekcije[idp][0]
    	v = r.projekcije[idp][1]
    	tr = r.projekcije[idp][2]
    	c = r.projekcije[idp][3]
    	idf = r.projekcije[idp][4]
    	#print(r.projekcije[idp][4], r.filmovi[idf][0], r.projekcije[idp][5])
    	f = r.filmovi[idf][0]
    	z = r.filmovi[idf][1]
    	s = r.projekcije[idp][5]
    	b = int(r.sale[r.projekcije[idp][5]])-int(r.projekcije[idp][7])
    	t.append_row([idp, d, v, tr, c, f, z, s, b])
    t.top_border_char = '='
    t.bottom_border_char = '='
    t.header_seperator_char = '='
    print('\n')
    print(t)			

#funkcija za proveru konflikta dve projekcije
def konflikt(d, v, t, s):
	p=int(v[0:2])*60+int(v[3:5])
	k=p+t
	int1= range(p,k)
	lista=[]

	for i in r.projekcije.keys():
		if r.projekcije[i][0]==d and r.projekcije[i][5]==s:
			lista.append(i)
	if lista == []:
		return 1 #nema konflikta
	else:
		for i in lista:
			v1=r.projekcije[i][1]
			t1=r.projekcije[i][2]
			p1=int(v1[0:2])*60+int(v1[3:5])
			k1=p1+t1
			int2=range(p1,k1)
			if list(set(int1) & set(int2))==[]:
				return 1 #nema konflikta
			else:
				return 0 #postoji konflikt				