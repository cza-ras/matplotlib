#importujemy niezbędne biblioteki
import pandas
import matplotlib.pyplot as _wykres
import numpy

#wskazujemy ścieżkę do pliku Excel
_plik_z_danymi = 'Projects/sentiment/sentyment_data.xlsx'

#definicja struktury danych poprzez ich odczytanie oraz przyporządkowanie do zmiennej 
_dane = pandas.read_excel(_plik_z_danymi)

#generujemy wykres na podstawie danych - każda kolejna kolumna zaczyna się w momencie końca poprzedniej
_x = numpy.arange(len(_dane['Marka']))
_wykres.bar(_x, _dane['Pozytywny'], label='Pozytywny', color='g')
_wykres.bar(_x, _dane['Neutralny'], bottom=_dane['Pozytywny'], label='Neutralny', color='b')
_wykres.bar(_x, _dane['Negatywny'], bottom=numpy.array(_dane['Pozytywny']) + numpy.array(_dane['Neutralny']), label='Negatywny',color='r')

#formatujemy wygląd wykresu
_wykres.xlabel("Marka")
_wykres.ylabel("Porcent sentymentu")
_wykres.title('Analiza sentymendtu dla marek')
_wykres.xticks(_x,_dane['Marka'])
_wykres.legend(loc=4)

#pokaż dane w formie wykresu
_wykres.show()