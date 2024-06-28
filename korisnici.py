import getpass
import projekcije as p
import recnici as r
import racuni as rac
from beautifultable import BeautifulTable


#funkcija koja definiše uloge
def prijava():
	uloga = logovanje()
	if uloga == 'prodavac':
		meni_prodavac()   
	else:
		meni_menadzer()

#funkcija za logovanje korisnika na servis
def logovanje():
	uneto = input('\nUkoliko želite da se prijavite na servis pritisnite P \nUkoliko želite da izađete pritisnite I, a zatim enter. \n')
	if uneto =='P' or uneto =='p':	
		flag=0
		lepa_stampa('PRIJAVA NA SERVIS')
		while 1:
			ime = input('\nUnesite korisničko ime: ')
			#proveravamo da li to korisnicko ime postoji
			if ime in r.korisnici.keys():
				while 1:
					sifra = getpass.getpass('\nUnesite šifru: ')
					if sifra==r.korisnici[ime][0]:
						print('\nUspešno ste se prijavili kao korisnik', r.korisnici[ime][1], r.korisnici[ime][2])
						global ime_prodavca
						ime_prodavca = r.korisnici[ime][1] + ' ' + r.korisnici[ime][2]
						return r.korisnici[ime][3] #vraća ulogu prodavac ili menadzer
					else:
						print('\nUneta šifra ne odgovara unetom korisničkom imenu.')
			else:
				print('\nUneto korisničko ime ne postoji.')
	elif uneto== 'I' or uneto =='i':
		quit() #funkcija koja služi za izlaz iz programa ukoliko korisnik pritisne slovo I na tastaturi
	else:
		logovanje()	

# funkcija za meni prodavca
def meni_prodavac():
	lepa_stampa('M E N I')
	print('\n1. Pretraga projekcije \n2. Prodaja karata \n3. ODJAVA')

	b=1
	while b:
		uneto=input('\nUnesite broj željene opcije iz menija: ')
		if uneto == '':
			print('\nMolimo Vas unesite redni broj ispred opcije koju želite.')
			meni_prodavac()
		else:
			b=0
	
			if uneto== '1':
				lepa_stampa('Pretraga')
				p.pretraga('prodavac')
			elif  uneto== '2':
				lepa_stampa('Prodaja karata')
				rac.prva_prodaja()
			elif uneto== '3':
				prijava() 		
			else:
				print('\nNe postoji tražena opcija.')
				meni_prodavac()	

# funkcija za meni menadzera    
def meni_menadzer():
	lepa_stampa('M E N I')

	print('\n1. Pretraga projekcije \n2. Unos projekcije\n3. Brisanje projekcije \n4. Izmena projekcije \n5. Unos novog prodavca \n6. ODJAVA')

	b=1
	while b:
		uneto = input('\nUnesite broj željene opcije iz menija: ')
		if uneto =='':
			print('\nMolimo Vas unesite redni broj ispred opcije koju želite.')
			meni_menadzer()
		else:
			b=0	
	 	
			if uneto == '1':
				lepa_stampa('Pretraga projekcije')
				p.pretraga('menadzer')

			elif uneto == '2': 
				lepa_stampa('Unos projekcije')
				p.unos_projekcije()
			elif uneto == '3':
				lepa_stampa('Brisanje projekcije')
				p.brisanje()

			elif uneto == '4':
				lepa_stampa('Izmena projekcije')
				p.unos_id()
			elif uneto == '5':
				unos_prodavca() 	
			elif uneto == '6':
				prijava() 	
			else:
				print('\nNe postoji tražena opcija.\n')
				meni_menadzer()

#funkcija za unos novog prodavca
def unos_prodavca():
	print('\nDa biste uneli novog prodavca u sistem unesite podatke.\n')	
	b=1
	while b:
		ime=input('\nIme: ')
		if ime == '':
			print('\nUnos ne može biti prazan. Molim Vas unesite ponovo')
		else:
			b=0
	b=1
	while b:
		prezime=input('\nPrezime: ')
		if prezime =='':
			print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo')
		else:
			b=0	
	b=1
	while b:
		b=1
		while b:
			kime=input('\nKorisničko ime: ')
			if kime=='':
				print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo')
			else:
				b=1	
				if kime in r.korisnici.keys():
					print('\nUneto korisničko ime je zauzeto. Izaberite neko drugo korisničko ime.\n')
				else:
					b=0

	b=1
	while b:	
		sifra=getpass.getpass('\nŠifra: ')
		if sifra=='':
			print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo.')
		else:
			b=0	
	r.korisnici[kime]=[sifra,ime,prezime,'prodavac']
	print('\nUspešno ste uneli novog prodavca', ime,prezime)
	meni_menadzer()

#funkcija za lepsi prikaz odredjenih tekstova u programu
def lepa_stampa(a):
	l=len(a)
	b='+'
	for i in list(range(1,l+3)):
		b=b+'='
	b=b+'+'
	print('\n')
	print(b)
	print('| {} |'.format(a))
	print(b)

	print('\n')