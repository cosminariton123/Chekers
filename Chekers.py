#244 Ariton Cosmin

import time
import copy
import pygame
import sys

ADANCIME_MAX=2
		

def creaza_interfata(display, tabla_joc_matrice):
        w_gr=h_gr=100


        barbat_negru=pygame.image.load('data/black_man.png')
        barbat_alb=pygame.image.load('data/white_man.png')
        rege_negru=pygame.image.load('data/black_king.png')
        rege_alb=pygame.image.load('data/white_king.png')
        patrat_negru=pygame.image.load('data/black_square.png')
        patrat_alb=pygame.image.load('data/white_square.png')

        barbat_negru=pygame.transform.scale(barbat_negru,(w_gr,h_gr))
        barbat_alb=pygame.transform.scale(barbat_alb,(w_gr,h_gr))
        rege_negru=pygame.transform.scale(rege_negru,(w_gr,h_gr))
        rege_alb=pygame.transform.scale(rege_alb,(w_gr,h_gr))
        patrat_negru=pygame.transform.scale(patrat_negru,(w_gr,h_gr))
        patrat_alb=pygame.transform.scale(patrat_alb,(w_gr,h_gr))

        drt = []


        for i in range(len(tabla_joc_matrice[0])):
                line=[]

                aux = -1

                for j in range(len(tabla_joc_matrice[1])):
                        linie = i
                        coloana = j

                        patr= pygame.Rect(coloana*w_gr, linie*h_gr, w_gr, h_gr)

                        line.append(patr)
                        pygame.draw.rect(display,(255,255,255), patr)

                        if tabla_joc_matrice[i][j]=='a':
                                display.blit(barbat_alb, (coloana*w_gr, linie*h_gr))
                        
                        elif tabla_joc_matrice[i][j]=='A':
                                display.blit(rege_alb, (coloana*w_gr, linie*h_gr))
                        
                        elif tabla_joc_matrice[i][j]=='n':
                                display.blit(barbat_negru, (coloana*w_gr, linie*h_gr))
                        
                        elif tabla_joc_matrice[i][j]=='N':
                                display.blit(rege_negru, (coloana*w_gr, linie*h_gr))
                        
                        elif tabla_joc_matrice[i][j]=='#' and i % 2 == 0 and j % 2 ==1:
                                display.blit(patrat_negru, (coloana*w_gr, linie * h_gr))
                        
                        elif tabla_joc_matrice[i][j]=='#' and i % 2 == 1 and j % 2 == 0:
                                display.blit(patrat_negru, (coloana* w_gr, linie *h_gr))
                        
                        elif tabla_joc_matrice[i][j]=='#' and i % 2 == 0 and j % 2 == 0:
                                display.blit(patrat_alb, (coloana* w_gr, linie *h_gr))
                        
                        elif tabla_joc_matrice[i][j]=='#' and i % 2 == 1 and j % 2 == 1:
                                display.blit(patrat_alb, (coloana* w_gr, linie *h_gr))
                      
                
                drt.append(line)
        
        pygame.display.flip()

        return drt

class Joc:
	"""
	Clasa care defineste jocul. Se va schimba de la un joc la altul.
	"""
	NR_COLOANE=8
	JMIN=None
	JMAX=None
	GOL='#'
	def __init__(self,tabla=None):
		

		if tabla is not None:
			self.matr = tabla
		
		else:
			'''
			self.matr=[
					['#','#','#','#','#','#','#','#'],
					['a','#','#','#','#','#','#','#'],
					['#','a','#','a','#','#','#','#'],
					['#','#','#','#','#','#','#','#'],
					['#','#','#','#','#','#','#','#'],
					['#','#','#','#','#','#','#','#'],
					['#','n','#','n','#','#','#','#'],
					['#','#','#','#','n','#','#','#']
			
					]
			'''
			self.matr= []
			for i in range(8):

				self.matr.append(['#','#','#','#','#','#','#','#'])

			aux=-1
			auxn=1

			
			for i in range(len(self.matr)):
				for j in range(len(self.matr[0])):
					
					if aux == 1 and i%2 ==0 and i < 3:
						self.matr[i][j]='a'
						aux= -aux
					elif aux == -1 and i%2 == 1 and i<3:
						self.matr[i][j]='a'
						aux = -aux

					else:
						aux=-aux

					
					if auxn == 1 and i%2 == 1 and i > 4 :
						self.matr[i][j]='n'
						auxn=-auxn
					elif auxn == -1 and i%2 == 0 and i > 4 :
						self.matr[i][j]='n'
						auxn=-auxn
					else:
						auxn=-aux
						#'''


				

		

		

	

	def final(self):
		
		flagN=0
		flagA=0
		flagMiscA=0
		flagMiscN=0
		rez='NU'

		for linie in self.matr:
			for elem in linie:
				if elem == 'n' or elem == 'N':
					flagN= 1

				if elem =='a' or elem=='A':
					flagA = 1

		#Verifica daca se poate misca
		
		if flagA == 1 and flagN == 1: 

			for linie in range (8):
				for coloana in range (8):
					if self.matr[linie][coloana] == 'N':

						if linie - 1 >= 0 and coloana -1 >= 0:
							if verificare_stanga(self.matr, linie, coloana, linie -1, coloana -1) == True:
								flagMiscN = 1
						
						if linie -1 >= 0 and coloana +1 < 8:
							if verificare_dreapta(self.matr, linie, coloana, linie -1, coloana +1)== True:
								flagMiscN = 1

						if linie -2 >=0 and coloana -2 >=0:
							if verificare_saritura_stanga(self.matr, linie, coloana, linie -2, coloana -2) == True:
								flagMiscN = 1
						
						if linie -2 >=0 and coloana + 2 < 8:
							if verificare_saritura_dreapta(self.matr, linie, coloana, linie -2 , coloana +2)== True:
								flagMiscN = 1
						
						if linie +1 < 8 and coloana -1 >=0:
							if verificare_stanga_jos(self.matr, linie, coloana, linie + 1, coloana -1) == True:
								flagMiscN = 1
						
						if linie +1 < 8 and coloana +1 < 8:
							if verificare_dreapta_jos (self.matr, linie, coloana, linie +1, coloana +1) == True:
								flagMiscN = 1
						
						if linie +2 <8 and coloana -2 >=0:
							if verificare_saritura_stanga_jos(self.matr, linie, coloana, linie +2, coloana -2) == True:
								flagMiscN = 1
						
						if linie +2 <8 and coloana +2 <8:
							if verificare_saritura_dreapta_jos(self.matr, linie,coloana, linie +2, coloana +2) == True:
								flagMiscN = 1
					
					if self.matr[linie][coloana] == 'n':

						if linie -1 >=0 and coloana -1 >=0:
							if verificare_stanga(self.matr, linie, coloana, linie -1, coloana -1) == True:
								flagMiscN = 1
						
						if linie -1 >=0 and coloana +1<8:
							if verificare_dreapta(self.matr, linie, coloana, linie -1, coloana +1)== True:
								flagMiscN = 1

						if linie -2 >=0 and coloana -2 >=0:
							if verificare_saritura_stanga(self.matr, linie, coloana, linie -2, coloana -2) == True:
								flagMiscN = 1
						
						if linie -2>=0 and coloana+2 <8:
							if verificare_saritura_dreapta(self.matr, linie, coloana, linie -2 , coloana +2)== True:
								flagMiscN = 1
					
					if self.matr[linie][coloana] == 'A':

						if linie -1 >=0 and coloana -1 >=0:
							if verificare_stanga(self.matr, linie, coloana, linie -1, coloana -1) == True:
								flagMiscA = 1
						
						if linie -1 >=0 and coloana + 1<8:
							if verificare_dreapta(self.matr, linie, coloana, linie -1, coloana +1)== True:
								flagMiscA = 1

						if linie -2 >=0 and coloana -2 >=0:
							if verificare_saritura_stanga(self.matr, linie, coloana, linie -2, coloana -2) == True:
								flagMiscA = 1
						
						if linie -2 >=0 and coloana +2 <8:
							if verificare_saritura_dreapta(self.matr, linie, coloana, linie -2 , coloana +2)== True:
								flagMiscA = 1
						
						if linie+ 1 <8 and coloana -1 >=0:
							if verificare_stanga_jos(self.matr, linie, coloana, linie + 1, coloana -1) == True:
								flagMiscA = 1
						
						if linie +1 <8 and coloana +1 <8:
							if verificare_dreapta_jos (self.matr, linie, coloana, linie +1, coloana +1) == True:
								flagMiscA = 1
						
						if linie +2 <8 and coloana -2 >=0:
							if verificare_saritura_stanga_jos(self.matr, linie, coloana, linie +2, coloana -2) == True:
								flagMiscA = 1
						
						if linie +2 <8 and coloana +2 <8:
							if verificare_saritura_dreapta_jos(self.matr, linie,coloana, linie +2, coloana +2) == True:
								flagMiscA = 1
					
					if self.matr[linie][coloana] == 'a':
						if linie +1 <8 and coloana -1 >=0:
							if verificare_stanga_jos(self.matr, linie, coloana, linie + 1, coloana -1) == True:
								flagMiscA = 1
						
						if linie +1 <8 and coloana +1 <8:
							if verificare_dreapta_jos (self.matr, linie, coloana, linie +1, coloana +1) == True:
								flagMiscA = 1
						
						if linie +2 <8 and coloana -2 >=0:
							if verificare_saritura_stanga_jos(self.matr, linie, coloana, linie +2, coloana -2) == True:
								flagMiscA = 1
						
						if linie +2 <8 and coloana +2< 8:
							if verificare_saritura_dreapta_jos(self.matr, linie,coloana, linie +2, coloana +2) == True:
								flagMiscA = 1


		if flagA==0:
			rez='negru'
		
		elif flagN==0:
			rez='alb'

		elif flagMiscA == 0:
			rez = 'negru'
		
		elif flagMiscN == 0:
			rez = 'alb'
		

		if(rez == 'alb' or rez == 'negru'):
			return rez
		else:
			return False

	def mutari(self, jucator):
		l_mutari=[]

		if jucator =='a':
			for linie in range (8):
				for coloana in range (8):
					if self.matr[linie][coloana] == 'A':

						if linie -1 >=0 and coloana -1 >=0:
							if verificare_stanga(self.matr, linie, coloana, linie -1, coloana -1) == True and verificare_obligatii(self.matr,linie,coloana) == True and nu_este_piesa_obligata(self.matr,linie,coloana) ==True:
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie -1, coloana -1)
								l_mutari.append(Joc(copie_matr))
										
						if linie -1 >=0 and coloana + 1<8:
							if verificare_dreapta(self.matr, linie, coloana, linie -1, coloana +1)== True and verificare_obligatii(self.matr,linie,coloana) == True and nu_este_piesa_obligata(self.matr,linie,coloana) ==True:
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie -1, coloana +1)
								l_mutari.append(Joc(copie_matr))

						if linie -2 >=0 and coloana -2 >=0:
							if verificare_saritura_stanga(self.matr, linie, coloana, linie -2, coloana -2) == True:
								
								linieaux = linie
								coloanaaux = coloana
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie -2, coloana -2)
								linie = linie -2
								coloana = coloana - 2
								
								loop = True
								
								while loop == True:
									loop = False

									if verificare_saritura_stanga(copie_matr, linie, coloana, linie -2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie-2, coloana-2)
										linie= linie -2
										coloana = coloana -2
										loop = True
									
									elif verificare_saritura_dreapta(copie_matr, linie, coloana, linie -2, coloana +2) == True:
										update_matrice(copie_matr, linie, coloana, linie -2, coloana +2)
										linie = linie -2
										coloana = coloana +2
										loop = True
									
									elif verificare_saritura_stanga_jos(copie_matr, linie, coloana, linie +2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie+2, coloana -2)
										linie = linie +2
										coloana = coloana -2
										loop = True

									elif verificare_saritura_dreapta_jos(copie_matr, linie, coloana, linie +2, coloana +2) == True:
										update_matrice(copie_matr,linie,coloana, linie+2, coloana+2)
										linie = linie +2
										coloana = coloana +2
										loop = True
								
								linie = linieaux
								coloana=coloanaaux
								l_mutari.append(Joc(copie_matr))
										
						if linie -2 >=0 and coloana +2 <8:
							if verificare_saritura_dreapta(self.matr, linie, coloana, linie -2 , coloana +2)== True:
								linieaux = linie
								coloanaaux = coloana
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie -2, coloana +2)
								linie = linie -2
								coloana = coloana + 2
								
								loop = True
								
								while loop == True:
									loop = False

									if verificare_saritura_stanga(copie_matr, linie, coloana, linie -2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie-2, coloana-2)
										linie= linie -2
										coloana = coloana -2
										loop = True
									
									elif verificare_saritura_dreapta(copie_matr, linie, coloana, linie -2, coloana +2) == True:
										update_matrice(copie_matr, linie, coloana, linie -2, coloana +2)
										linie = linie -2
										coloana = coloana +2
										loop = True
									
									elif verificare_saritura_stanga_jos(copie_matr, linie, coloana, linie +2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie+2, coloana -2)
										linie = linie +2
										coloana = coloana -2
										loop = True

									elif verificare_saritura_dreapta_jos(copie_matr, linie, coloana, linie +2, coloana +2) == True:
										update_matrice(copie_matr,linie,coloana, linie+2, coloana+2)
										linie = linie +2
										coloana = coloana +2
										loop = True
								
								linie = linieaux
								coloana=coloanaaux
								l_mutari.append(Joc(copie_matr))
										
						if linie+ 1 <8 and coloana -1 >=0:
							if verificare_stanga_jos(self.matr, linie, coloana, linie + 1, coloana -1) == True and verificare_obligatii(self.matr, linie, coloana)== True and nu_este_piesa_obligata(self.matr,linie,coloana) ==True:
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie +1, coloana -1)
								l_mutari.append(Joc(copie_matr))
										
						if linie +1 <8 and coloana +1 <8:
							if verificare_dreapta_jos (self.matr, linie, coloana, linie +1, coloana +1) == True and verificare_obligatii(self.matr, linie, coloana) == True and nu_este_piesa_obligata(self.matr,linie,coloana) ==True:
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie +1, coloana +1)
								l_mutari.append(Joc(copie_matr))
										
						if linie +2 <8 and coloana -2 >=0:
							if verificare_saritura_stanga_jos(self.matr, linie, coloana, linie +2, coloana -2) == True:
								linieaux = linie
								coloanaaux = coloana
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie +2, coloana -2)
								linie = linie +2
								coloana = coloana - 2
								
								loop = True
								
								while loop == True:
									loop = False

									if verificare_saritura_stanga(copie_matr, linie, coloana, linie -2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie-2, coloana-2)
										linie= linie -2
										coloana = coloana -2
										loop = True
									
									elif verificare_saritura_dreapta(copie_matr, linie, coloana, linie -2, coloana +2) == True:
										update_matrice(copie_matr, linie, coloana, linie -2, coloana +2)
										linie = linie -2
										coloana = coloana +2
										loop = True
									
									elif verificare_saritura_stanga_jos(copie_matr, linie, coloana, linie +2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie+2, coloana -2)
										linie = linie +2
										coloana = coloana -2
										loop = True

									elif verificare_saritura_dreapta_jos(copie_matr, linie, coloana, linie +2, coloana +2) == True:
										update_matrice(copie_matr,linie,coloana, linie+2, coloana+2)
										linie = linie +2
										coloana = coloana +2
										loop = True
								
								linie = linieaux
								coloana=coloanaaux
								l_mutari.append(Joc(copie_matr))
										
						if linie +2 <8 and coloana +2 <8:
							if verificare_saritura_dreapta_jos(self.matr, linie,coloana, linie +2, coloana +2) == True:
								linieaux = linie
								coloanaaux = coloana
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie +2, coloana +2)
								linie = linie +2
								coloana = coloana + 2
								
								loop = True
								
								while loop == True:
									loop = False

									if verificare_saritura_stanga(copie_matr, linie, coloana, linie -2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie-2, coloana-2)
										linie= linie -2
										coloana = coloana -2
										loop = True
									
									elif verificare_saritura_dreapta(copie_matr, linie, coloana, linie -2, coloana +2) == True:
										update_matrice(copie_matr, linie, coloana, linie -2, coloana +2)
										linie = linie -2
										coloana = coloana +2
										loop = True
									
									elif verificare_saritura_stanga_jos(copie_matr, linie, coloana, linie +2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie+2, coloana -2)
										linie = linie +2
										coloana = coloana -2
										loop = True

									elif verificare_saritura_dreapta_jos(copie_matr, linie, coloana, linie +2, coloana +2) == True:
										update_matrice(copie_matr,linie,coloana, linie+2, coloana+2)
										linie = linie +2
										coloana = coloana +2
										loop = True
								
								linie = linieaux
								coloana=coloanaaux
								l_mutari.append(Joc(copie_matr))
									
					if self.matr[linie][coloana] == 'a':
						if linie +1 <8 and coloana -1 >=0:
							if verificare_stanga_jos(self.matr, linie, coloana, linie + 1, coloana -1) == True and verificare_obligatii(self.matr,linie, coloana) == True and nu_este_piesa_obligata(self.matr,linie,coloana) ==True:
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie +1, coloana -1)
								l_mutari.append(Joc(copie_matr))
										
						if linie +1 <8 and coloana +1 <8:
							if verificare_dreapta_jos (self.matr, linie, coloana, linie +1, coloana +1) == True and verificare_obligatii(self.matr, linie, coloana) ==True and nu_este_piesa_obligata(self.matr,linie,coloana) ==True:
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie +1, coloana +1)
								l_mutari.append(Joc(copie_matr))
									
						if linie +2 <8 and coloana -2 >=0:
							if verificare_saritura_stanga_jos(self.matr, linie, coloana, linie +2, coloana -2) == True:
								linieaux = linie
								coloanaaux = coloana
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie +2, coloana -2)
								linie = linie +2
								coloana = coloana - 2

								
								
								loop = True
								
								if linie == 7:
									loop = False

								while loop == True:
									loop = False
									if verificare_saritura_stanga_jos(copie_matr, linie, coloana, linie +2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie+2, coloana -2)
										linie = linie +2
										coloana = coloana -2
										loop = True

										if linie == 7:
											loop = False

									elif verificare_saritura_dreapta_jos(copie_matr, linie, coloana, linie +2, coloana +2) == True:
										update_matrice(copie_matr,linie,coloana, linie+2, coloana+2)
										linie = linie +2
										coloana = coloana +2
										loop = True

										if linie == 7:
											loop = False
								
								linie = linieaux
								coloana=coloanaaux
								l_mutari.append(Joc(copie_matr))
										
						if linie +2 <8 and coloana +2< 8:
							if verificare_saritura_dreapta_jos(self.matr, linie,coloana, linie +2, coloana +2) == True:
								linieaux = linie
								coloanaaux = coloana
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie +2, coloana +2)
								linie = linie +2
								coloana = coloana + 2
								
								loop = True

								if linie == 7:
									loop = False
								
								
								
								while loop == True:
									loop = False
									if verificare_saritura_stanga_jos(copie_matr, linie, coloana, linie +2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie+2, coloana -2)
										linie = linie +2
										coloana = coloana -2
										loop = True

										if linie == 7:
											loop = False

									elif verificare_saritura_dreapta_jos(copie_matr, linie, coloana, linie +2, coloana +2) == True:
										update_matrice(copie_matr,linie,coloana, linie+2, coloana+2)
										linie = linie +2
										coloana = coloana +2
										loop = True

										if linie == 7:
											loop = False
								
								linie = linieaux
								coloana=coloanaaux
								l_mutari.append(Joc(copie_matr))
		else:
			for linie in range (8):
				for coloana in range (8):
					if self.matr[linie][coloana] == 'N':

						if linie -1 >=0 and coloana -1 >=0:
							if verificare_stanga(self.matr, linie, coloana, linie -1, coloana -1) == True and verificare_obligatii(self.matr,linie,coloana) == True and nu_este_piesa_obligata(self.matr,linie,coloana) ==True:
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie -1, coloana -1)
								l_mutari.append(Joc(copie_matr))
										
						if linie -1 >=0 and coloana + 1<8:
							if verificare_dreapta(self.matr, linie, coloana, linie -1, coloana +1)== True and verificare_obligatii(self.matr,linie,coloana)==True and nu_este_piesa_obligata(self.matr,linie,coloana) ==True:
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie -1, coloana +1)
								l_mutari.append(Joc(copie_matr))

						if linie -2 >=0 and coloana -2 >=0:
							if verificare_saritura_stanga(self.matr, linie, coloana, linie -2, coloana -2) == True:
								
								linieaux = linie
								coloanaaux = coloana
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie -2, coloana -2)
								linie = linie -2
								coloana = coloana - 2
								
								loop = True
								
								while loop == True:
									loop = False

									if verificare_saritura_stanga(copie_matr, linie, coloana, linie -2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie-2, coloana-2)
										linie= linie -2
										coloana = coloana -2
										loop = True
									
									elif verificare_saritura_dreapta(copie_matr, linie, coloana, linie -2, coloana +2) == True:
										update_matrice(copie_matr, linie, coloana, linie -2, coloana +2)
										linie = linie -2
										coloana = coloana +2
										loop = True
									
									elif verificare_saritura_stanga_jos(copie_matr, linie, coloana, linie +2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie+2, coloana -2)
										linie = linie +2
										coloana = coloana -2
										loop = True

									elif verificare_saritura_dreapta_jos(copie_matr, linie, coloana, linie +2, coloana +2) == True:
										update_matrice(copie_matr,linie,coloana, linie+2, coloana+2)
										linie = linie +2
										coloana = coloana +2
										loop = True
								
								linie = linieaux
								coloana=coloanaaux
								l_mutari.append(Joc(copie_matr))
										
						if linie -2 >=0 and coloana +2 <8:
							if verificare_saritura_dreapta(self.matr, linie, coloana, linie -2 , coloana +2)== True:
								linieaux = linie
								coloanaaux = coloana
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie -2, coloana +2)
								linie = linie -2
								coloana = coloana + 2
								
								loop = True
								
								while loop == True:
									loop = False

									if verificare_saritura_stanga(copie_matr, linie, coloana, linie -2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie-2, coloana-2)
										linie= linie -2
										coloana = coloana -2
										loop = True
									
									elif verificare_saritura_dreapta(copie_matr, linie, coloana, linie -2, coloana +2) == True:
										update_matrice(copie_matr, linie, coloana, linie -2, coloana +2)
										linie = linie -2
										coloana = coloana +2
										loop = True
									
									elif verificare_saritura_stanga_jos(copie_matr, linie, coloana, linie +2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie+2, coloana -2)
										linie = linie +2
										coloana = coloana -2
										loop = True

									elif verificare_saritura_dreapta_jos(copie_matr, linie, coloana, linie +2, coloana +2) == True:
										update_matrice(copie_matr,linie,coloana, linie+2, coloana+2)
										linie = linie +2
										coloana = coloana +2
										loop = True
								
								linie = linieaux
								coloana=coloanaaux
								l_mutari.append(Joc(copie_matr))
										
						if linie+ 1 <8 and coloana -1 >=0:
							if verificare_stanga_jos(self.matr, linie, coloana, linie + 1, coloana -1) == True:
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie +1, coloana -1)
								l_mutari.append(Joc(copie_matr))
										
						if linie +1 <8 and coloana +1 <8:
							if verificare_dreapta_jos (self.matr, linie, coloana, linie +1, coloana +1) == True:
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie +1, coloana +1)
								l_mutari.append(Joc(copie_matr))
										
						if linie +2 <8 and coloana -2 >=0:
							if verificare_saritura_stanga_jos(self.matr, linie, coloana, linie +2, coloana -2) == True:
								linieaux = linie
								coloanaaux = coloana
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie +2, coloana -2)
								linie = linie +2
								coloana = coloana - 2
								
								loop = True
								
								while loop == True:
									loop = False

									if verificare_saritura_stanga(copie_matr, linie, coloana, linie -2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie-2, coloana-2)
										linie= linie -2
										coloana = coloana -2
										loop = True
									
									elif verificare_saritura_dreapta(copie_matr, linie, coloana, linie -2, coloana +2) == True:
										update_matrice(copie_matr, linie, coloana, linie -2, coloana +2)
										linie = linie -2
										coloana = coloana +2
										loop = True
									
									elif verificare_saritura_stanga_jos(copie_matr, linie, coloana, linie +2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie+2, coloana -2)
										linie = linie +2
										coloana = coloana -2
										loop = True

									elif verificare_saritura_dreapta_jos(copie_matr, linie, coloana, linie +2, coloana +2) == True:
										update_matrice(copie_matr,linie,coloana, linie+2, coloana+2)
										linie = linie +2
										coloana = coloana +2
										loop = True
								
								linie = linieaux
								coloana=coloanaaux
								l_mutari.append(Joc(copie_matr))
										
						if linie +2 <8 and coloana +2 <8:
							if verificare_saritura_dreapta_jos(self.matr, linie,coloana, linie +2, coloana +2) == True:
								linieaux = linie
								coloanaaux = coloana
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie +2, coloana +2)
								linie = linie +2
								coloana = coloana + 2
								
								loop = True
								
								while loop == True:
									loop = False

									if verificare_saritura_stanga(copie_matr, linie, coloana, linie -2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie-2, coloana-2)
										linie= linie -2
										coloana = coloana -2
										loop = True
									
									elif verificare_saritura_dreapta(copie_matr, linie, coloana, linie -2, coloana +2) == True:
										update_matrice(copie_matr, linie, coloana, linie -2, coloana +2)
										linie = linie -2
										coloana = coloana +2
										loop = True
									
									elif verificare_saritura_stanga_jos(copie_matr, linie, coloana, linie +2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie+2, coloana -2)
										linie = linie +2
										coloana = coloana -2
										loop = True

									elif verificare_saritura_dreapta_jos(copie_matr, linie, coloana, linie +2, coloana +2) == True:
										update_matrice(copie_matr,linie,coloana, linie+2, coloana+2)
										linie = linie +2
										coloana = coloana +2
										loop = True
								
								linie = linieaux
								coloana=coloanaaux
								l_mutari.append(Joc(copie_matr))
									
					if self.matr[linie][coloana] == 'n':
						if linie -1 >=0 and coloana -1 >=0:
							if verificare_stanga(self.matr, linie, coloana, linie - 1, coloana -1) == True and verificare_obligatii(self.matr,linie, coloana)==True and nu_este_piesa_obligata(self.matr,linie,coloana) ==True:
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie -1, coloana -1)
								l_mutari.append(Joc(copie_matr))
										
						if linie -1 >=0 and coloana +1 <8:
							if verificare_dreapta (self.matr, linie, coloana, linie -1, coloana +1) == True and verificare_obligatii(self.matr,linie,coloana)==True and nu_este_piesa_obligata(self.matr,linie,coloana) ==True:
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie -1, coloana +1)
								l_mutari.append(Joc(copie_matr))
									
						if linie -2 >=0 and coloana -2 >=0:
							if verificare_saritura_stanga(self.matr, linie, coloana, linie -2, coloana -2) == True:
								linieaux = linie
								coloanaaux = coloana
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie -2, coloana -2)
								linie = linie -2
								coloana = coloana - 2

								
								
								loop = True

								if linie == 0:
									loop = False
								
								while loop == True:
									loop = False
									if verificare_saritura_stanga(copie_matr, linie, coloana, linie -2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie+2, coloana -2)
										linie = linie -2
										coloana = coloana -2
										loop = True

										if linie == 0:
											loop = False

									elif verificare_saritura_dreapta(copie_matr, linie, coloana, linie -2, coloana +2) == True:
										update_matrice(copie_matr,linie,coloana, linie-2, coloana+2)
										linie = linie -2
										coloana = coloana +2
										loop = True

										if linie == 0:
											loop = False
								
								linie = linieaux
								coloana=coloanaaux
								l_mutari.append(Joc(copie_matr))
										
						if linie -2 >=0 and coloana +2< 8:
							if verificare_saritura_dreapta(self.matr, linie,coloana, linie -2, coloana +2) == True:
								linieaux = linie
								coloanaaux = coloana
								copie_matr=copy.deepcopy(self.matr)
								update_matrice(copie_matr, linie, coloana, linie -2, coloana +2)
								linie = linie -2
								coloana = coloana + 2

								
								
								loop = True
								if linie == 0:
									loop = False
								
								while loop == True:
									loop = False
									if verificare_saritura_stanga(copie_matr, linie, coloana, linie -2, coloana -2) == True:
										update_matrice(copie_matr, linie, coloana, linie-2, coloana -2)
										linie = linie +2
										coloana = coloana -2
										loop = True

										if linie == 0:
											loop = False

									elif verificare_saritura_dreapta(copie_matr, linie, coloana, linie -2, coloana +2) == True:
										update_matrice(copie_matr,linie,coloana, linie-2, coloana+2)
										linie = linie -2
										coloana = coloana +2
										loop = True

										if linie == 0:
											loop = False
								
								linie = linieaux
								coloana=coloanaaux
								l_mutari.append(Joc(copie_matr))

		

		return l_mutari
	

		
	def estimeaza_scor(self, adancime):
		t_final=self.final()
		#if (adancime==0):

		if t_final=='alb' :
			return (99+adancime)
		elif t_final=='negru':
			return (-99-adancime)
		else:

			scor= 0

			for linie in range (8):
				for coloana in range (8):
					if self.matr[linie][coloana] == 'a':
						scor +=10
					
					if self.matr[linie][coloana] == 'A':
						scor +=20
					
					if self.matr[linie][coloana] == 'n':
						scor -=10
					
					if self.matr[linie][coloana] == 'N':
						scor -=20
					
					if coloana == 0 or coloana == 7:
						if self.matr[linie][coloana] == 'a':
							scor +=4
					
						if self.matr[linie][coloana] == 'A':
							scor +=4
						
						if self.matr[linie][coloana] == 'n':
							scor -=4
						
						if self.matr[linie][coloana] == 'N':
							scor -=4
			
			return scor
					
			


	def __str__(self):
		sir= (" ".join([str(x) for x in self.matr[0:3]])+"\n"+
		" ".join([str(x) for x in self.matr[3:6]])+"\n"+
		" ".join([str(x) for x in self.matr[6:9]])+"\n")
 
		return sir
			

class Stare:
	"""
	Clasa folosita de algoritmii minimax si alpha-beta
	Are ca proprietate tabla de joc
	Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
	De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu configuratiile posibile in urma mutarii unui jucator
	"""
	def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
		self.tabla_joc=tabla_joc


		self.j_curent=j_curent
		
		#adancimea in arborele de stari
		self.adancime=adancime	
		
		#scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
		self.scor=scor
		
		#lista de mutari posibile din starea curenta
		self.mutari_posibile=[]
		
		#cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
		self.stare_aleasa=None

	def jucator_opus(self):
		if self.j_curent==Joc.JMIN:
			return Joc.JMAX
		else:
			return Joc.JMIN

	def mutari(self):		
		l_mutari=self.tabla_joc.mutari(self.j_curent)
		juc_opus=self.jucator_opus()
		l_stari_mutari=[Stare(mutare, juc_opus, self.adancime-1, parinte=self) for mutare in l_mutari]

		return l_stari_mutari
		
	
	def __str__(self):
		sir= str(self.tabla_joc) + "(Juc curent:"+self.j_curent+")\n"
		return sir
	

			
""" Algoritmul MinMax """

def min_max(stare):
	
	if stare.adancime==0 or stare.tabla_joc.final() :
		stare.scor=stare.tabla_joc.estimeaza_scor(stare.adancime)
		return stare
		
	#calculez toate mutarile posibile din starea curenta
	stare.mutari_posibile=stare.mutari()

	#aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
	mutari_scor=[min_max(x) for x in stare.mutari_posibile ] #expandez(constr subarb) fiecare nod x din mutari posibile
	


	if stare.j_curent==Joc.JMAX :
		#daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
		stare.stare_aleasa= max(mutari_scor, key= lambda x: x.scor)
	else:
		#daca jucatorul e JMIN aleg starea-fiica cu scorul minim
		stare.stare_aleasa=min(mutari_scor, key= lambda x: x.scor)
		
	stare.scor=stare.stare_aleasa.scor
	return stare

# ALGORITMUL AFLA BETA

def alpha_beta(alpha, beta, stare):
	if stare.adancime==0 or stare.tabla_joc.final() :
		stare.scor=stare.tabla_joc.estimeaza_scor(stare.adancime)
		return stare
	
	if alpha>beta:
		return stare #este intr-un interval invalid deci nu o mai procesez
	
	stare.mutari_posibile=stare.mutari()
		

	if stare.j_curent==Joc.JMAX :
		scor_curent=float('-inf')
		
		for mutare in stare.mutari_posibile:
			#calculeaza scorul
			stare_noua=alpha_beta(alpha, beta, mutare) #aici construim subarborele pentru stare_noua
			
			if (scor_curent<stare_noua.scor):
				stare.stare_aleasa=stare_noua
				scor_curent=stare_noua.scor
			if(alpha<stare_noua.scor):
				alpha=stare_noua.scor
				if alpha>=beta:
					break

	elif stare.j_curent==Joc.JMIN :
		scor_curent=float('inf')
		#completati cu rationament similar pe cazul stare.j_curent==Joc.JMAX
		for mutare in stare.mutari_posibile:
			#calculeaza scorul
			stare_noua=alpha_beta(alpha, beta, mutare) #aici construim subarborele pentru stare_noua
			
			if (scor_curent>stare_noua.scor):
				stare.stare_aleasa=stare_noua
				scor_curent=stare_noua.scor
			if(beta>stare_noua.scor):
				beta=stare_noua.scor
				if alpha>=beta:
					break
		
	stare.scor=stare.stare_aleasa.scor

	return stare



def afis_daca_final(stare_curenta):
	final=stare_curenta.tabla_joc.final()
	if(final):
		if (final=="remiza"):
			print("Remiza!")
		else:
			print("A castigat "+final)
			
		return True
		
	return False


def afiseaza_tabla(tabla_curenta):

	i=0

	print('    a   b   c   d   e   f   g   h')
	print('   ------------------------------')

	for linie in tabla_curenta.matr:

		print(i,end='  |')
		i+=1

		for elem in linie:
			print(elem,end='   ')
		print(' ')
	
	print('')



def verificare_saritura_stanga(matrice, line, coll, linie, coloana):
	
	raspuns_valid= False
	if matrice[line][coll] == '#':
		return False

	piesa_adv='eroare'
	piesa_adv_Mare='eroare'

	if matrice[line][coll] == 'a' or matrice[line][coll]== 'A':
		piesa_adv='n'
		piesa_adv_Mare='N'
	else:
		piesa_adv='a'
		piesa_adv_Mare='A'

	if linie  != line - 2:
		return raspuns_valid
	
	if coloana  != coll - 2:
		return raspuns_valid

	if matrice[line][coll] == 'a':
		return raspuns_valid


	if line -2 >=0 and coll-2 >=0 and matrice[line - 2][coll -2] == '#':
		if line -1>=0 and coll-1>=0 and (matrice[line - 1][coll - 1] == piesa_adv or matrice[line - 1][coll - 1] == piesa_adv_Mare):
			raspuns_valid = True

	return raspuns_valid

def verificare_saritura_dreapta(matrice, line, coll, linie, coloana):
	
	raspuns_valid= False
	if matrice[line][coll] == '#':
		return False

	piesa_adv='eroare'
	piesa_adv_Mare='eroare'

	if matrice[line][coll] == 'a' or matrice[line][coll] == 'A':
		piesa_adv='n'
		piesa_adv_Mare='N'
	else:
		piesa_adv='a'
		piesa_adv_Mare='A'

	if linie  != line - 2:
		return raspuns_valid
	
	if coloana  != coll + 2:
		return raspuns_valid

	if matrice[line][coll] =='a':
		return raspuns_valid
	

	if line-2>=0 and coll+2<8 and matrice[line - 2][coll + 2] == '#':
		if line -1 >=0 and coll+1<8 and (matrice[line - 1][coll + 1] == piesa_adv or matrice[line-1][coll+1] == piesa_adv_Mare):
			raspuns_valid = True

	return raspuns_valid
	

def verificare_stanga(matrice, line, coll, linie, coloana):
	
	raspuns_valid= False
	if matrice[line][coll] == '#':
		return False

	piesa_adv='eroare'
	piesa_adv_Mare='eroare'

	if matrice[line][coll] == 'a' or matrice[line][coll]== 'A':
		piesa_adv='n'
		piesa_adv_Mare='N'
	else:
		piesa_adv='a'
		piesa_adv_Mare='A'


	if linie  != line - 1:
		return raspuns_valid
	

	if coloana != coll - 1:
		return raspuns_valid
	
	if matrice[line][coll]== 'a':
		return raspuns_valid


	
	if line -1 >=0 and coll-1>=0 and matrice[line -1][coll -1] =='#': #daca in stanga e liber(unde vrem sa mergem)
		if line -1 >=0 and coll+1<8 and (matrice[line -1][coll +1] == piesa_adv or matrice[line -1][coll +1] == piesa_adv_Mare): #daca in dreapta e piesa adversa
			if coll + 2 < 8 and line -2 >=0: #daca nu se termina tabla
				if line-2 >=0 and coll+2<8 and  matrice[line -2][coll +2]== '#': #si daca se poate sari piesa, locul de dupa fiind liber 
					raspuns_valid = False #miscare ilegala
				else:
					raspuns_valid = True #miscare legala
			
			else:				# daca s-a terminat tabla
				raspuns_valid = True #miscare legala
		else:
			raspuns_valid = True


	return raspuns_valid

def verificare_dreapta(matrice, line, coll, linie, coloana):
	
	raspuns_valid= False
	if matrice[line][coll] == '#':
		return False

	piesa_adv='eroare'
	piesa_adv_Mare='eroare'

	if matrice[line][coll] == 'a' or matrice[line][coll] =='A':
		piesa_adv='n'
		piesa_adv_Mare='N'
	else:
		piesa_adv='a'
		piesa_adv_Mare='A'

	if linie  != line - 1:
		return raspuns_valid


	if coloana != coll +1:
		return raspuns_valid
	
	if matrice[line][coll] == 'a':
		return raspuns_valid

	
	if line -1 >=0 and coll+ 1<8 and matrice[line -1][coll +1] =='#': #daca in dreapta e liber(unde vrem sa mergem)
		if line-1>=0 and coll-1>=0 and (matrice[line -1][coll -1] == piesa_adv or matrice[line -1][coll -1] ==piesa_adv_Mare): #daca in stanga e piesa adversa
			if coll - 2 >= 0 and line -2 >=0: #daca nu se termina tabla
				if line -2 >=0 and coll-2 >=0 and matrice[line -2][coll -2]== '#': #si daca se poate sari piesa, locul de dupa fiind liber 
					raspuns_valid = False #miscare ilegala
				else:
					raspuns_valid = True #miscare legala
			
			else:				# daca s-a terminat tabla
				raspuns_valid = True #miscare legala
		
		else:
			raspuns_valid= True
	
	return raspuns_valid



def verificare_saritura_stanga_jos(matrice, line, coll, linie, coloana):
	raspuns_valid = False
	if matrice[line][coll] == '#':
		return False


	piesa_adv='eroare'
	piesa_adv_Mare='eroare'

	if matrice[line][coll] == 'a' or matrice[line][coll] == 'A':
		piesa_adv='n'
		piesa_adv_Mare='N'
	else:
		piesa_adv='a'
		piesa_adv_Mare='A'

	if linie != line + 2:
		return raspuns_valid


	if coloana != coll - 2:
		return raspuns_valid
	
	if matrice[line][coll] == 'n':
		return raspuns_valid

	
	if line +2 <8 and coll-2>0 and matrice[line + 2][coll -2] == '#':
		if line + 1 <8 and coll -1 >=0 and (matrice[line + 1][coll - 1] == piesa_adv or matrice[line + 1][coll - 1] == piesa_adv_Mare):
			raspuns_valid = True
	
	return raspuns_valid

def verificare_saritura_dreapta_jos(matrice, line, coll, linie, coloana):

	raspuns_valid = False
	if matrice[line][coll] == '#':
		return False

	piesa_adv='eroare'
	piesa_adv_Mare = 'eroare'

	if matrice[line][coll] == 'a' or matrice[line][coll] =='A':
		piesa_adv='n'
		piesa_adv_Mare='N'
	else:
		piesa_adv='a'
		piesa_adv_Mare='A'

	if linie != line + 2:
		return raspuns_valid


	if coloana != coll + 2:
		return raspuns_valid

	if matrice[line][coll] == 'n':
		return raspuns_valid


	
	if line+2<8 and coll+2<8 and matrice[line + 2][coll +2] == '#':
		if line +1 <8 and coll+1<8 and (matrice[line + 1][coll + 1] == piesa_adv or matrice[line + 1][coll + 1] ==piesa_adv_Mare):
			raspuns_valid = True
	
	return raspuns_valid	



def verificare_stanga_jos(matrice, line, coll, linie, coloana):
	
	raspuns_valid= False
	if matrice[line][coll] == '#':
		return False


	piesa_adv='eroare'
	piesa_adv_Mare = 'eroare'

	if matrice[line][coll] == 'a' or matrice[line][coll] == 'A':
		piesa_adv='n'
		piesa_adv_Mare='N'
	else:
		piesa_adv='a'
		piesa_adv_Mare='A'

	if linie  != line + 1:
		return raspuns_valid
	

	if coloana != coll - 1:
		return raspuns_valid
	
	if matrice[line][coll] == 'n':
		return raspuns_valid

	
	if line + 1 <8 and coll -1 > 0 and matrice[line + 1][coll - 1] =='#': #daca in stanga e liber(unde vrem sa mergem)
		if line + 1 <8 and coll + 1 < 8 and (matrice[line + 1][coll +1] == piesa_adv or matrice[line + 1][coll +1] == piesa_adv_Mare): #daca in dreapta e piesa adversa
			if coll + 2 < 8 and line + 2 <8 : #daca nu se termina tabla
				if line+2 <8 and coll+2<8 and matrice[line + 2][coll +2]== '#': #si daca se poate sari piesa, locul de dupa fiind liber 
					raspuns_valid = False #miscare ilegala
				else:
					raspuns_valid = True #miscare legala
			
			else:				# daca s-a terminat tabla
				raspuns_valid = True #miscare legala
		
		else:
			raspuns_valid = True


	return raspuns_valid


def verificare_dreapta_jos(matrice, line, coll, linie, coloana):
	
	raspuns_valid= False

	if matrice[line][coll] == '#':
		return False

	piesa_adv='eroare'
	piesa_adv_Mare = 'eroare'

	if matrice[line][coll] == 'a' or matrice[line][coll] == 'A':
		piesa_adv='n'
		piesa_adv_Mare='N'
	else:
		piesa_adv='a'
		piesa_adv_Mare='A'

	if linie  != line + 1:
		return raspuns_valid
	

	if coloana != coll + 1:
		return raspuns_valid

	if matrice[line][coll]== 'n':
		return raspuns_valid
	


	
	if line+1 <8 and coll+1 <8 and matrice[line + 1][coll + 1] =='#': 
		if line+1 <8 and coll-1>=0 and (matrice[line + 1][coll - 1] == piesa_adv or matrice[line + 1][coll - 1] == piesa_adv_Mare): 
			if coll - 2 >= 0 and line + 2 <8 :
				if line+2<8 and coll-2>=0 and matrice[line + 2][coll - 2]== '#': 
					raspuns_valid = False 
				else:
					raspuns_valid = True 
			
			else:				
				raspuns_valid = True 
		
		else :
			raspuns_valid = True


	return raspuns_valid


def verificare_obligatii (matrice , line, coll):
	
	raspuns_valid= True

	piesa_adv= 'eroare'
	piesa_adv_Mare='eroare'
	piesa_mea='eroare'
	piesa_mea_Mare='eroare'

	if matrice[line][coll] == 'a' or matrice[line][coll] == 'A':
		piesa_adv = 'n'
		piesa_adv_Mare = 'N'
		piesa_mea='a'
		piesa_mea_Mare='A'
	else:
		piesa_adv = 'a'
		piesa_adv_Mare = 'A'
		piesa_mea='n'
		piesa_mea_Mare='N'
	
	

	if verificare_saritura_dreapta(matrice, line, coll, line-2, coll+2) == True or verificare_saritura_stanga(matrice, line, coll, line -2, coll -2)== True or verificare_saritura_dreapta_jos(matrice, line, coll, line + 2, coll + 2) == True or verificare_saritura_stanga_jos(matrice, line, coll, line +2 , coll- 2)== True:
		return raspuns_valid
	
	for i in range (8):
		for j in range (8):
			if (piesa_mea == matrice[i][j] or piesa_mea_Mare == matrice[i][j]) and (line != i or coll != j):
				if verificare_saritura_dreapta(matrice,i,j,i - 2,j +2)== True:
					raspuns_valid=False
				
				if verificare_saritura_dreapta_jos(matrice, i, j, i + 2, j +2)== True:
					raspuns_valid=False
				
				if verificare_saritura_stanga(matrice, i, j, i -2, j -2) == True:
					raspuns_valid =False
				
				if verificare_saritura_stanga_jos(matrice,i,j,i + 2,j -2) == True:
					raspuns_valid = False
	
	return raspuns_valid


def nu_este_piesa_obligata(matrice, line, coll):
	
	piesa_adv= 'eroare'
	piesa_adv_Mare='eroare'
	piesa_mea='eroare'
	piesa_mea_Mare='eroare'

	raspuns_valid= True

	if matrice[line][coll] == 'a' or matrice[line][coll] == 'A':
		piesa_adv = 'n'
		piesa_adv_Mare = 'N'
		piesa_mea='a'
		piesa_mea_Mare='A'
	else:
		piesa_adv = 'a'
		piesa_adv_Mare = 'A'
		piesa_mea='n'
		piesa_mea_Mare='N'	
	
	if verificare_saritura_dreapta(matrice, line, coll, line-2, coll+2) == True or verificare_saritura_stanga(matrice, line, coll, line -2, coll -2)== True or verificare_saritura_dreapta_jos(matrice, line, coll, line + 2, coll + 2) == True or verificare_saritura_stanga_jos(matrice, line, coll, line +2 , coll- 2)== True:
		raspuns_valid= False
	
	return raspuns_valid
	






def update_matrice(matrice, line, coll, linie, coloana):

	piesa = matrice[line][coll]

	if piesa == 'n':
		if linie == 0:
			piesa ='N'
	
	if piesa == 'a':
		if linie == 7:
			piesa = 'A'

	if linie  == line - 2 and coloana  == coll - 2: #stanga saritura
			
		matrice[line][coll] = '#'
		matrice [line -1][coll -1]= '#'
		matrice [line -2][coll - 2] = piesa
	

	elif linie == line -2 and coloana == coll +2: #dreapta saritura

		matrice[line][coll] = '#'
		matrice [line -1][coll +1]= '#'
		matrice [line -2][coll + 2] = piesa

	
	elif linie  == line - 1 and coloana == coll - 1: #stanga

		matrice[line][coll] = '#'
		matrice [line -1][coll -1] = piesa
	
	elif linie  == line - 1 and coloana == coll + 1: #dreapta

		matrice[line][coll] = '#'
		matrice [line -1][coll +1] = piesa

	
	elif linie == line + 2 and coloana == coll - 2: #stanga jos saritura

		matrice[line][coll] = '#'
		matrice [line + 1][coll - 1]= '#'
		matrice [line + 2][coll - 2] = piesa


	elif linie == line + 2 and coloana == coll + 2: #dreapta jos saritura

		matrice[line][coll] = '#'
		matrice [line + 1][coll + 1]= '#'
		matrice [line + 2][coll + 2] = piesa

	elif linie  == line + 1 and coloana == coll - 1: #stanga jos
			
		matrice[line][coll] = '#'
		matrice [line +1][coll -1] = piesa
	
	elif linie  == line + 1 and coloana == coll + 1: #dreapta jos
	
		matrice[line][coll] = '#'
		matrice [line +1][coll +1] = piesa
	
	else :
		print('Eroare la updatarea matricei')




def main():

        raspuns_valid=False
        while not raspuns_valid:
                tip_algoritm=input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
                if tip_algoritm in ['1','2']:
                        raspuns_valid=True
                else:
                        print("Nu ati ales o varianta corecta.")


        raspuns_valid=False
        while not raspuns_valid:
                ADANCIME_MAX=input('Dificultatea dorita? (2-usor, 4-mediu, 6-greu)=')
                if ADANCIME_MAX in ['2','4','6']:
                        raspuns_valid = True
                else:
                        print('Nu ati ales o varianta corecta')
	
        ADANCIME_MAX=int(ADANCIME_MAX)

        Joc.JMAX= 'a'
	
        Joc.JMIN = 'n'
	
	
        tabla_curenta=Joc();
        print("Tabla initiala")
	
        afiseaza_tabla(tabla_curenta)
	

        stare_curenta=Stare(tabla_curenta,'n',ADANCIME_MAX)

        print(stare_curenta.j_curent)

        line=-1
        coll=-1

        cu_interfata='Nu'

        raspuns_valid= False
        while not raspuns_valid:
                cu_interfata= input('Doriti cu interfata(Da/Nu)=')
                if cu_interfata == 'Da' or cu_interfata == 'Nu':
                        raspuns_valid= True

        t_inainte_joc=int(round(time.time() * 1000))

        if cu_interfata=='Nu':

                while True :

                        t_inainte=int(round(time.time() * 1000))
                        if (stare_curenta.j_curent==Joc.JMIN):
                                line = -1
                                coll =-1
                                
                
                                raspuns_valid=False

                                

                                #ALEGEREA PIESEI

                                while not raspuns_valid:
                                        try:
                                                print('Selecteaza piesa')
                                                linie=int(input("linie="))
                                                coloana=input("coloana=")

                                                if coloana == 'exit':
                                                        exit(0)

                                                if coloana == 'a':
                                                        coloana = 0
                                                elif coloana == 'b':
                                                        coloana = 1
                                                elif coloana == 'c':
                                                        coloana = 2
                                                elif coloana == 'd':
                                                        coloana = 3
                                                elif coloana == 'e':
                                                        coloana = 4
                                                elif coloana == 'f':
                                                        coloana = 5
                                                elif coloana == 'g':
                                                        coloana = 6
                                                elif coloana == 'h':
                                                        coloana = 7
                                                
                                                else:
                                                        coloana = -1

                                        
                                                if (linie in range(0,8) and coloana in range(0,8) ):
                                                        
                                                       #DACA JUCATORUL ALEGE UN BARBAT
                                                        if stare_curenta.tabla_joc.matr[linie][coloana] == 'n':

                                                                if linie - 2 >= 0 and coloana + 2 < 8:
                                                                        if verificare_saritura_dreapta(stare_curenta.tabla_joc.matr, linie, coloana, linie - 2, coloana+2)== True:
										
                                                                                raspuns_valid=True
                                                                                line=linie
                                                                                coll=coloana
									
                                                                if linie - 2 >= 0 and coloana - 2 > -1:
                                                                        if verificare_saritura_stanga(stare_curenta.tabla_joc.matr, linie, coloana, linie - 2 , coloana - 2) == True:
                                                                                raspuns_valid=True
                                                                                line=linie
                                                                                coll=coloana
								

                                                                if linie - 1 >= 0 and coloana + 1 < 8:
                                                                        if verificare_dreapta(stare_curenta.tabla_joc.matr, linie, coloana, linie -1, coloana +1) == True:
                                                                                raspuns_valid=True

                                                                if linie - 1 >= 0 and coloana - 1 < 8:
                                                                        if verificare_stanga(stare_curenta.tabla_joc.matr, linie, coloana, linie -1, coloana -1 )== True:
                                                                                raspuns_valid=True

								
                                                                if raspuns_valid ==True and line == -1:
                                                                        if verificare_obligatii(stare_curenta.tabla_joc.matr,linie,coloana) != True:
                                                                                raspuns_valid= False
											

                                                                if raspuns_valid == True:
                                                                        line= linie
                                                                        coll= coloana


							#DACA JUCATORUL ALEGE UN REGE
                                                        elif stare_curenta.tabla_joc.matr[linie][coloana] == 'N':
                                                                if linie - 2 >= 0 and coloana + 2 < 8:
                                                                        if verificare_saritura_dreapta(stare_curenta.tabla_joc.matr, linie , coloana, linie-2, coloana +2) == True:
                                                                                raspuns_valid=True
                                                                                line=linie
                                                                                coll=coloana
									
                                                                if linie - 2 >= 0 and coloana - 2 > -1:
                                                                        if verificare_saritura_stanga(stare_curenta.tabla_joc.matr, linie, coloana, linie-2, coloana -2) == True:
                                                                                raspuns_valid=True
                                                                                line=linie
                                                                                coll=coloana
								


								#SPECIFIC REGILOR
                                                                if linie + 2 < 8 and coloana + 2 < 8:
                                                                        if verificare_saritura_dreapta_jos(stare_curenta.tabla_joc.matr, linie, coloana, linie+2, coloana+2) == True:
                                                                                raspuns_valid=True
                                                                                line=linie
                                                                                coll=coloana
									
                                                                if linie + 2 < 8 and coloana - 2 > -1:
                                                                        if verificare_saritura_stanga_jos(stare_curenta.tabla_joc.matr, linie, coloana, linie +2, coloana -2) == True:
                                                                                raspuns_valid=True
                                                                                line=linie
                                                                                coll=coloana

								#END SPECIFIC REGILOR
		

                                                                if linie + 1 < 8 and coloana + 1 < 8:
                                                                        if verificare_dreapta_jos(stare_curenta.tabla_joc.matr, linie, coloana, linie+1,coloana+1) == True:
                                                                                raspuns_valid=True

                                                                if linie + 1 < 8 and coloana - 1 < 8:
                                                                        if verificare_stanga_jos(stare_curenta.tabla_joc.matr, linie, coloana, linie + 1 , coloana - 1) == True:
                                                                                raspuns_valid=True

                                                                if linie - 1 < 8 and coloana + 1 < 8:
                                                                        if verificare_dreapta(stare_curenta.tabla_joc.matr, linie, coloana, linie-1, coloana +1) == True:
                                                                                raspuns_valid=True

                                                                if linie - 1 < 8 and coloana - 1 < 8:
                                                                        if verificare_stanga(stare_curenta.tabla_joc.matr, linie, coloana, linie -1, coloana -1) == True:
                                                                                raspuns_valid=True
								

                                                                if raspuns_valid ==True and line == -1:
                                                                        if verificare_obligatii(stare_curenta.tabla_joc.matr,linie,coloana) != True:
                                                                                raspuns_valid= False

								
                                                                if raspuns_valid == True:
                                                                        line= linie
                                                                        coll= coloana

                                                        else:
                                                                print('Piesa nenvalida')




                                                else:
                                                        print("Linie sau coloana invalida (trebuie sa fie unul dintre numerele 0-7 respectiv a-h).")		
                                
                                        except ValueError:
                                                print("Linia trebuie sa fie un numar intreg, iar coloana o litera de la a la h")
                                        

                                        if raspuns_valid != True:
                                                        print('Nu se pot face actiuni cu aceasta piesa')	

                                #END ALEGEREA PIESEI

                                



                                #ALEGEREA ACTIUNII CU PIESA ALEASA

                                raspuns_valid = False

                                while not raspuns_valid:
                                        try:
                                                
                                                print ('Selecteaza pozitia la care doresti sa ajungi')
                                                linie=int(input("linie="))
                                                coloana=input("coloana=")
                                                if coloana == 'a':
                                                        coloana = 0
                                                elif coloana == 'b':
                                                        coloana = 1
                                                elif coloana == 'c':
                                                        coloana = 2
                                                elif coloana == 'd':
                                                        coloana = 3
                                                elif coloana == 'e':
                                                        coloana = 4
                                                elif coloana == 'f':
                                                        coloana = 5
                                                elif coloana == 'g':
                                                        coloana = 6
                                                elif coloana == 'h':
                                                        coloana = 7
                                                
                                                else:
                                                        coloana = -1

                                                if linie in range (8) and coloana in range(8):
                                                        
                                                        #DACA A FOST ALES UN BARBAT
                                                        if stare_curenta.tabla_joc.matr[line][coll] == 'n':
							
								#verific daca mutarea e in stanga sus, in dreapta sus sau e cu saritura stanga sau dreapta

                                                                if verificare_stanga(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True and nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,line,coll) == True:
                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                        line = linie
                                                                        coll = coloana
                                                                        raspuns_valid = True
								
                                                                if verificare_dreapta(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True and nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,line,coll) == True:
                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                        line = linie
                                                                        coll = coloana
                                                                        raspuns_valid = True
								
                                                                if verificare_saritura_stanga(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True:
                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                        line = linie
                                                                        coll = coloana

                                                                        if nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,linie, coloana) == False and linie != 0:
                                                                                raspuns_valid = False
                                                                        else:
                                                                                raspuns_valid = True
								
                                                                if verificare_saritura_dreapta(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True:
                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                        line = linie
                                                                        coll = coloana


                                                                        if nu_este_piesa_obligata(stare_curenta.tabla_joc.matr, linie, coloana) == False and linie !=0:
                                                                                raspuns_valid = False
                                                                        else:
                                                                                raspuns_valid = True
									

							#PENTRU REGI
                                                        elif stare_curenta.tabla_joc.matr[line][coll] == 'N':

                                                                if verificare_stanga(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True and nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,line,coll) == True:
                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                        line = linie
                                                                        coll = coloana
                                                                        raspuns_valid = True
								
                                                                if verificare_dreapta(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True and nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,line,coll) == True:
                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                        line = linie
                                                                        coll = coloana
                                                                        raspuns_valid = True
								
                                                                if verificare_saritura_stanga(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True:
                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                        line = linie
                                                                        coll = coloana

                                                                        if nu_este_piesa_obligata(stare_curenta.tabla_joc.matr, linie, coloana) == False:
                                                                                raspuns_valid = False
                                                                        else:
                                                                                raspuns_valid = True
								
                                                                if verificare_saritura_dreapta(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True:
                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                        line = linie
                                                                        coll = coloana

                                                                        if nu_este_piesa_obligata(stare_curenta.tabla_joc.matr, linie, coloana) == False:
                                                                                raspuns_valid = False
                                                                        else:
                                                                                raspuns_valid = True
								
								#SPECIFIC REGI
                                                                if verificare_stanga_jos(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True and nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,line,coll) == True:
                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                        line = linie
                                                                        coll = coloana
                                                                        raspuns_valid = True
								
                                                                if verificare_dreapta_jos(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True and nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,line,coll) == True:
                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                        line = linie
                                                                        coll = coloana
                                                                        raspuns_valid = True
								
                                                                if verificare_saritura_stanga_jos(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True:
                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                        line = linie
                                                                        coll = coloana

                                                                        if nu_este_piesa_obligata(stare_curenta.tabla_joc.matr, linie, coloana) ==False:
                                                                                raspuns_valid = False
                                                                        else:
                                                                                raspuns_valid = True
								
                                                                if verificare_saritura_dreapta_jos(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True:
                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                        line = linie
                                                                        coll = coloana

                                                                        if nu_este_piesa_obligata(stare_curenta.tabla_joc.matr, linie, coloana) == False:
                                                                                raspuns_valid = False
                                                                        else:
                                                                                raspuns_valid = True

								
                                                        afiseaza_tabla(stare_curenta.tabla_joc)

                                        
                                        except ValueError:
                                                print("Linia trebuie sa fie un numar intreg, iar coloana o litera de la a la h")
                                        
                                        if raspuns_valid != True:
                                                print ('Miscare ilegala/Mai sunt miscari de facut')
                                
                                t_dupa=int(round(time.time() * 1000))
                                print("Ai gandit timp de "+str(t_dupa-t_inainte)+" milisecunde.")

                                #END ALEGEREA ACTIUNII


                                #testez daca jocul a ajuns intr-o stare finala
                                #si afisez un mesaj corespunzator in caz ca da
                                if (afis_daca_final(stare_curenta)):
                                        break
                                        
                                        
                                #S-a realizat o mutare. Schimb jucatorul cu cel opus
                                stare_curenta.j_curent=stare_curenta.jucator_opus()
                        
                        #--------------------------------
                        else: #jucatorul e JMAX (calculatorul)
                                #Mutare calculator
                                
                                #preiau timpul in milisecunde de dinainte de mutare
                                t_inainte=int(round(time.time() * 1000))
                                if tip_algoritm=='1':
                                        stare_actualizata=min_max(stare_curenta)
                                else: #tip_algoritm==2
                                        stare_actualizata=alpha_beta(-500, 500, stare_curenta)
                                stare_curenta.tabla_joc=stare_actualizata.stare_aleasa.tabla_joc #aici se face de fapt mutarea !!!
                                print("Tabla dupa mutarea calculatorului")
                                afiseaza_tabla(stare_curenta.tabla_joc)
                                
                                #preiau timpul in milisecunde de dupa mutare
                                t_dupa=int(round(time.time() * 1000))
                                print("Calculatorul a \"gandit\" timp de "+str(t_dupa-t_inainte)+" milisecunde.")
                                
                                if (afis_daca_final(stare_curenta)):
                                        t_dupa_joc=int(round(time.time() * 1000))
                                        print("Jocul a durat "+str(t_dupa_joc-t_inainte_joc)+" milisecunde.")
                                        break
                                        
                                #S-a realizat o mutare. Schimb jucatorul cu cel opus
                                stare_curenta.j_curent=stare_curenta.jucator_opus()

        else:
                pygame.init()
                pygame.display.set_caption('Chekers')
                ecran= pygame.display.set_mode(size=(100*8,100*8))
                patratele = creaza_interfata(ecran, tabla_curenta.matr)

                raspuns_valid2=False
                raspuns_valid = False
                line = -1
                coll = -1

                while True:
                        if (stare_curenta.j_curent==Joc.JMIN):
                                t_inainte=int(round(time.time() * 1000))
                                #muta jucatorul

 
                                

                                if raspuns_valid != True:
                                        for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                        pygame.quit()
                                                        sys.exit()
                                        
                                        
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        pos = pygame.mouse.get_pos()

                                                        for pozi in range(len(patratele)):
                                                                for pozj in range(len(patratele[0])):
                                                                        if patratele[pozi][pozj].collidepoint(pos):
                                                                                linie = pozi
                                                                                coloana = pozj

                                                                               
                                                                                if (linie in range(0,8) and coloana in range(0,8) ):
                                                                                        #DACA JUCATORUL ALEGE UN BARBAT
                                                                                        if stare_curenta.tabla_joc.matr[linie][coloana] == 'n':

                                                                                                if linie - 2 >= 0 and coloana + 2 < 8:
                                                                                                        if verificare_saritura_dreapta(stare_curenta.tabla_joc.matr, linie, coloana, linie - 2, coloana+2)== True:
														
                                                                                                                raspuns_valid=True
                                                                                                                line=linie
                                                                                                                coll=coloana
													
                                                                                                if linie - 2 >= 0 and coloana - 2 > -1:
                                                                                                        if verificare_saritura_stanga(stare_curenta.tabla_joc.matr, linie, coloana, linie - 2 , coloana - 2) == True:
                                                                                                                raspuns_valid=True
                                                                                                                line=linie
                                                                                                                coll=coloana
												

                                                                                                if linie - 1 >= 0 and coloana + 1 < 8:
                                                                                                        if verificare_dreapta(stare_curenta.tabla_joc.matr, linie, coloana, linie -1, coloana +1) == True:
                                                                                                                raspuns_valid=True

                                                                                                if linie - 1 >= 0 and coloana - 1 < 8:
                                                                                                        if verificare_stanga(stare_curenta.tabla_joc.matr, linie, coloana, linie -1, coloana -1 )== True:
                                                                                                                raspuns_valid=True

												
                                                                                                if raspuns_valid ==True and line == -1:
                                                                                                        if verificare_obligatii(stare_curenta.tabla_joc.matr,linie,coloana) != True:
                                                                                                                raspuns_valid= False
															

                                                                                                if raspuns_valid == True:
                                                                                                        line= linie
                                                                                                        coll= coloana


											#DACA JUCATORUL ALEGE UN REGE
                                                                                        elif stare_curenta.tabla_joc.matr[linie][coloana] == 'N':
                                                                                                if linie - 2 >= 0 and coloana + 2 < 8:
                                                                                                        if verificare_saritura_dreapta(stare_curenta.tabla_joc.matr, linie , coloana, linie-2, coloana +2) == True:
                                                                                                                raspuns_valid=True
                                                                                                                line=linie
                                                                                                                coll=coloana
													
                                                                                                if linie - 2 >= 0 and coloana - 2 > -1:
                                                                                                        if verificare_saritura_stanga(stare_curenta.tabla_joc.matr, linie, coloana, linie-2, coloana -2) == True:
                                                                                                                raspuns_valid=True
                                                                                                                line=linie
                                                                                                                coll=coloana
												


												#SPECIFIC REGILOR
                                                                                                if linie + 2 < 8 and coloana + 2 < 8:
                                                                                                        if verificare_saritura_dreapta_jos(stare_curenta.tabla_joc.matr, linie, coloana, linie+2, coloana+2) == True:
                                                                                                                raspuns_valid=True
                                                                                                                line=linie
                                                                                                                coll=coloana
													
                                                                                                if linie + 2 < 8 and coloana - 2 > -1:
                                                                                                        if verificare_saritura_stanga_jos(stare_curenta.tabla_joc.matr, linie, coloana, linie +2, coloana -2) == True:
                                                                                                                raspuns_valid=True
                                                                                                                line=linie
                                                                                                                coll=coloana

												#END SPECIFIC REGILOR
						

                                                                                                if linie + 1 < 8 and coloana + 1 < 8:
                                                                                                        if verificare_dreapta_jos(stare_curenta.tabla_joc.matr, linie, coloana, linie+1,coloana+1) == True:
                                                                                                                raspuns_valid=True

                                                                                                if linie + 1 < 8 and coloana - 1 < 8:
                                                                                                        if verificare_stanga_jos(stare_curenta.tabla_joc.matr, linie, coloana, linie + 1 , coloana - 1) == True:
                                                                                                                raspuns_valid=True

                                                                                                if linie - 1 < 8 and coloana + 1 < 8:
                                                                                                        if verificare_dreapta(stare_curenta.tabla_joc.matr, linie, coloana, linie-1, coloana +1) == True:
                                                                                                                raspuns_valid=True

                                                                                                if linie - 1 < 8 and coloana - 1 < 8:
                                                                                                        if verificare_stanga(stare_curenta.tabla_joc.matr, linie, coloana, linie -1, coloana -1) == True:
                                                                                                                raspuns_valid=True
												

                                                                                                if raspuns_valid ==True and line == -1:
                                                                                                        if verificare_obligatii(stare_curenta.tabla_joc.matr,linie,coloana) != True:
                                                                                                                raspuns_valid= False

												
                                                                                                if raspuns_valid == True:
                                                                                                        line= linie
                                                                                                        coll= coloana

                                elif raspuns_valid == True:
                                        for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                        pygame.quit()
                                                        sys.exit() 
                                                
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        pos = pygame.mouse.get_pos()

                                                        raspuns_valid2 = False

                                                        for pozi in range(len(patratele)):
                                                                for pozj in range(len(patratele[0])):
                                                                        if patratele[pozi][pozj].collidepoint(pos):
                                                                                linie = pozi
                                                                                coloana = pozj

                                                                                if linie in range (8) and coloana in range(8):
                                                                                        
                                                                                       #DACA A FOST ALES UN BARBAT
                                                                                        if stare_curenta.tabla_joc.matr[line][coll] == 'n':
											
												#verific daca mutarea e in stanga sus, in dreapta sus sau e cu saritura stanga sau dreapta

                                                                                                if verificare_stanga(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True and nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,line,coll) == True:
                                                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                                                        line = linie
                                                                                                        coll = coloana
                                                                                                        raspuns_valid2 = True
												
                                                                                                if verificare_dreapta(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True and nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,line,coll) == True:
                                                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                                                        line = linie
                                                                                                        coll = coloana
                                                                                                        raspuns_valid2 = True
												
                                                                                                if verificare_saritura_stanga(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True:
                                                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                                                        line = linie
                                                                                                        coll = coloana

                                                                                                        if nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,linie, coloana) == False and linie !=0:
                                                                                                                raspuns_valid2 = False
                                                                                                        else:
                                                                                                                raspuns_valid2 = True
												
                                                                                                if verificare_saritura_dreapta(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True:
                                                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                                                        line = linie
                                                                                                        coll = coloana


                                                                                                        if nu_este_piesa_obligata(stare_curenta.tabla_joc.matr, linie, coloana) == False and linie !=0:
                                                                                                                raspuns_valid2 = False
                                                                                                        else:
                                                                                                                raspuns_valid2 = True
													

											#PENTRU REGI
                                                                                        elif stare_curenta.tabla_joc.matr[line][coll] == 'N':

                                                                                                if verificare_stanga(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True and nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,line,coll) == True:
                                                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                                                        line = linie
                                                                                                        coll = coloana
                                                                                                        raspuns_valid2 = True
												
                                                                                                if verificare_dreapta(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True and nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,line,coll) == True:
                                                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                                                        line = linie
                                                                                                        coll = coloana
                                                                                                        raspuns_valid2 = True
												
                                                                                                if verificare_saritura_stanga(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True:
                                                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                                                        line = linie
                                                                                                        coll = coloana

                                                                                                        if nu_este_piesa_obligata(stare_curenta.tabla_joc.matr, linie, coloana) == False:
                                                                                                                raspuns_valid2 = False
                                                                                                        else:
                                                                                                                raspuns_valid2 = True
												
                                                                                                if verificare_saritura_dreapta(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True:
                                                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                                                        line = linie
                                                                                                        coll = coloana

                                                                                                        if nu_este_piesa_obligata(stare_curenta.tabla_joc.matr, linie, coloana) == False:
                                                                                                                raspuns_valid2 = False
                                                                                                        else:
                                                                                                                raspuns_valid2 = True
												
												#SPECIFIC REGI
                                                                                                if verificare_stanga_jos(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True and nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,line,coll) == True:
                                                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                                                        line = linie
                                                                                                        coll = coloana
                                                                                                        raspuns_valid2 = True
												
                                                                                                if verificare_dreapta_jos(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True and nu_este_piesa_obligata(stare_curenta.tabla_joc.matr,line,coll) == True:
                                                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                                                        line = linie
                                                                                                        coll = coloana
                                                                                                        raspuns_valid2 = True
												
                                                                                                if verificare_saritura_stanga_jos(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True:
                                                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                                                        line = linie
                                                                                                        coll = coloana

                                                                                                        if nu_este_piesa_obligata(stare_curenta.tabla_joc.matr, linie, coloana) ==False:
                                                                                                                raspuns_valid2 = False
                                                                                                        else:
                                                                                                                raspuns_valid2 = True
												
                                                                                                if verificare_saritura_dreapta_jos(stare_curenta.tabla_joc.matr,line, coll, linie, coloana) == True:
                                                                                                        update_matrice(stare_curenta.tabla_joc.matr, line, coll, linie, coloana)
                                                                                                        line = linie
                                                                                                        coll = coloana

                                                                                                        if nu_este_piesa_obligata(stare_curenta.tabla_joc.matr, linie, coloana) == False:
                                                                                                                raspuns_valid2 = False
                                                                                                        else:
                                                                                                                raspuns_valid2 = True
                                patratele = creaza_interfata(ecran,stare_curenta.tabla_joc.matr)


                                                                                        

                                if raspuns_valid2 == True:
                                        line=-1
                                        coll=-1
                                        raspuns_valid2=False
                                        raspuns_valid=False
                                        patratele= creaza_interfata(ecran, stare_curenta.tabla_joc.matr)
                                        t_dupa=int(round(time.time() * 1000))
                                        print ("Ai gandit timp de "+str(t_dupa-t_inainte)+" milisecunde.")
					
                                        if (afis_daca_final(stare_curenta)):
                                                t_dupa_joc=int(round(time.time() * 1000))
                                                print("Jocul a durat "+str(t_dupa_joc-t_inainte_joc)+" milisecunde.")
                                                break

                                        stare_curenta.j_curent=stare_curenta.jucator_opus()


                        else:
                                #jucatorul e JMAX (calculatorul)
                                #Mutare calculator
                                
                                #preiau timpul in milisecunde de dinainte de mutare
                                t_inainte=int(round(time.time() * 1000))
                                if tip_algoritm=='1':
                                        stare_actualizata=min_max(stare_curenta)
                                else: #tip_algoritm==2
                                        stare_actualizata=alpha_beta(-500, 500, stare_curenta)
                                stare_curenta.tabla_joc=stare_actualizata.stare_aleasa.tabla_joc #aici se face de fapt mutarea !!!
                                print("Tabla dupa mutarea calculatorului")
                                afiseaza_tabla(stare_curenta.tabla_joc)
                                patratele= creaza_interfata(ecran,stare_curenta.tabla_joc.matr)
                                
                                #preiau timpul in milisecunde de dupa mutare
                                t_dupa=int(round(time.time() * 1000))
                                print("Calculatorul a \"gandit\" timp de "+str(t_dupa-t_inainte)+" milisecunde.")
                                
                                if (afis_daca_final(stare_curenta)):
                                        t_dupa_joc=int(round(time.time() * 1000))
                                        print("Jocul a durat "+str(t_dupa_joc-t_inainte_joc)+" milisecunde.")
                                        break
                                        
                                #S-a realizat o mutare. Schimb jucatorul cu cel opus
                                stare_curenta.j_curent=stare_curenta.jucator_opus()
                                                                                 




	
if __name__ == "__main__" :
	main()