import datetime
import korisnici as k
import projekcije as p
from recnici import projekcije
from recnici import racuni
from recnici import sale
from recnici import filmovi
from beautifultable import BeautifulTable


def prva_prodaja():
	rbr_racuna = len(list(racuni.keys()))+1
	datum = ''
	vreme = ''
	racuni[rbr_racuna] = [datum, vreme, [], 0]
	prodaja(rbr_racuna)

#funkcija za meni prodaje karata 
def prodaja(rbr_racuna):
	print('\n1. Prodaja karata\n2. Izdavanje računa\n3. Poništenje računa')
	
	b=1
	while b:
		uneto=input('\nUnesite redni broj željene opcije: ')
		if uneto == '':
			print('\nMolimo Vas unesite redni broj ispred opcije koju želite.')
			prodaja(rbr_racuna)
		else:
			b=0	
			if uneto=='1':
				prodaja_karte(rbr_racuna)
			elif uneto=='2':
				izdavanje_racuna(rbr_racuna)
			elif uneto=='3':
				print('\nUspešno ste poništili račun.\nUkoliko želite da prodate karte, izaberite opciju 1.\nUkoliko želite da izađete iz menija za prodaju karata, izaberite opciju 3.')
				k.meni_prodavac()
			else:
				print('\nTražena opcija ne postoji')
				prodaja(rbr_racuna)	

#funkcija za prodaju karata
def prodaja_karte(rbr_racuna):
	
	lista = []
	for idp in projekcije.keys():
		if projekcije[idp][6]==False:
			lista.append(idp)

	p.stampanje_projekcije(lista)
	b=1
	while b:
		b=1
		while b:					
			idp=input('\nZa koju projekciju želite da prodate karte? Unesite ID: ')
			if idp == '':
				print('\nUnos ne može biti prazan. Molimo Vas unesite ponovo.')
			else:
				if idp in projekcije.keys() and projekcije[idp][6]==False: #uneti id je dobar
					b=0
				else:
					print('\nTrenutno ne možemo da prodamo kartu sa traženim ID-em.')
	b=1
	while b:
		brk=input('\nKoliko karta želite da prodate? ')		
		b=0 # pp da će biti dobro uneti
		try: brk=int(brk)
		except ValueError: b=1
		
		if b:
			print('\nMolimo unesite broj karata.')	
		else: #b=0 int je unet
			if brk <=0:
				b=1
				print('\nNiste dobro uneli broj karata,pokušajte ponovo.')
	if brk > sale[projekcije[idp][5]]-projekcije[idp][7]: #traženo je više mesta nego što je dostupno	
		print('\nTražili ste više mesta nego što je slobodno')
		prodaja_karte(rbr_racuna)
	else: #treba da se pridruži računu
		print('\nBroj karata: {} za projekciju {} je pridruženo računu.\n\nUkoliko želite da završite prodaju karata i izdate račun izaberite opciju 2.\nUkoliko želite da prodate još karata izaberite opciju 1.\nUkoliko želite da poništite račun izaberite opciju 3.'.format(brk, idp))
		racuni[rbr_racuna][2].append([idp, brk]) #pridruživanje računu
		racuni[rbr_racuna][3] = racuni[rbr_racuna][3] + brk * projekcije[idp][3]
		projekcije[idp][7] = projekcije[idp][7] + brk

		prodaja(rbr_racuna)	
#funkcija za izdavanje računa
def izdavanje_racuna(rbr_racuna):
	if racuni[rbr_racuna][2]==[]:
		print('\nVaš račun je trenutno prazan.\n\nUkoliko želite da pordate karte odaberite opciju 1.\nUkoliko želite da izadjete iz menija za pordaju karata odaberite opciju 3.')
		prodaja(rbr_racuna)
	else:
		stampanje_racuna(rbr_racuna)
		k.meni_prodavac()

#funkcija za tabelarni prikaz prodate karte
def stampanje_racuna(rbr_racuna):
	from korisnici import ime_prodavca
	div = str(datetime.datetime.now()) #dobijamo d i v u obliku yyyy-mm-dd hh:mm:ss
	datum = div[0:10]
	d1=datum[8:10]+'.'+ datum[5:7]+'.'+ datum[0:4] + '.'
	vreme = div[11:16]	
	racuni[rbr_racuna][0] = d1
	racuni[rbr_racuna][1] = vreme
	print('\nRačun broj: {}'.format(rbr_racuna))
	print('\nIzdat: {} {}'.format(d1,vreme))
	print('\nProdavac: {}'.format(ime_prodavca))
	t = BeautifulTable()
	t.column_headers=['Datum', 'Vreme', 'Film', 'Sala', 'Broj karata']
	for p in racuni[rbr_racuna][2]:
		idp = p[0]
		brk = p[1]
		d = projekcije[idp][0]
		v = projekcije[idp][1]
		f = filmovi[projekcije[idp][4]][0]
		s = projekcije[idp][5]
		t.append_row([d, v, f, s, brk])
	t.top_border_char = '='
	t.bottom_border_char = '='
	t.header_seperator_char = '='
	print(t)
	print('\nUkupno za uplatu: {}'.format(racuni[rbr_racuna][3]))
	print('\nHvala na poverenju. Vaš Bioskop')