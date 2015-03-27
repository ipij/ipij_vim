#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import re
import unittest

zncz_pocz = 'godz_pocz'
zncz_kon = 'godz_kon'

etkt_pocz = 'BEGIN:'
etkt_kon = 'END:'
znak_daty_pocz = 7
znak_daty_kon = 32
rozmiar_daty = 19

wzorcowa_data_pocz = 'BEGIN: 2012.12.29_13.01.23 END: 0000.00.00_00.00.00'
sama_wzorcowa_data = '2012.12.29_13.01.23'
inna_wzorcowa_data = '2012.12.29_13.52.09'

pusty_czas = '0000.00.00_00.00.00'

znane_wzorce = frozenset([zncz_pocz, zncz_kon])

def wstaw_na_pozycji(linia, wspx, Teraz):
    pocz = linia[:wspx + 1]
    kon = linia[wspx + 1:]
    wynik = pocz + Teraz + kon
    return wynik

def pobierz_czas(wzorzec):
    return time.strftime(wzorzec, time.localtime(time.time()))

def wstaw_date_z_dzis(vim):
    linia = vim.current.line
    Teraz = pobierz_czas('%Y.%m.%d')
    wspy, wspx = vim.current.window.cursor
    wynik = wstaw_na_pozycji(linia, wspx, Teraz)
    wspx += len(Teraz)
    vim.current.line = wynik
    vim.current.window.cursor = wspy, wspx

def jestem_w_ostatniej_linii(vim):
    wspy, wspx = vim.current.window.cursor
    return wspy == len(vim.current.buffer)

def kursor_w_dol(vim):
    wspy, wspx = vim.current.window.cursor
    wspy += 1
    vim.current.window.cursor = wspy, wspx

def rozepchnij_ponizej_i_wstaw(vim, napis):
    nr_linii, _ = vim.current.window.cursor
    vim.current.buffer[nr_linii + 1:] = vim.current.buffer[nr_linii:]
    vim.current.buffer[nr_linii] = napis

def dolacz_na_koncu_pliku(vim, napis):
    vim.current.buffer.append(napis)

def wstaw_ponizej_tresc_linii(vim, napis):
    if jestem_w_ostatniej_linii(vim):
        dolacz_na_koncu_pliku(vim, napis)
    else:
        rozepchnij_ponizej_i_wstaw(vim, napis)
    kursor_w_dol(vim)

def moment_czasowy():
    return pobierz_czas('%Y.%m.%d_%H.%M.%S')

def wyznacz_tresc_poczatkowa():
    return ''.join([etkt_pocz, ' ', moment_czasowy(), ' ', etkt_kon, ' ', pusty_czas])

def kursor_na_koniec_linii(vim):
    wspy, wspx = vim.current.window.cursor
    wspx = len(vim.current.line) - 1
    vim.current.window.cursor = wspy, wspx

def mamy_linie_miernicza(vim):
    return ksztalt_linii_mierniczej(vim.current.line)

def miarka_ma_zakonczenie(napis):
    return wytnij_kon(napis) != pusty_czas

def linia_jest_pelna(vim):
    return miarka_ma_zakonczenie(vim.current.line)

def aktywnie_wstaw_poczatek_pomiaru(vim):
    poczatkowy = wyznacz_tresc_poczatkowa()
    wstaw_ponizej_tresc_linii(vim, poczatkowy)
    kursor_na_koniec_linii(vim)

def stempel_poczatkowy(vim):
    if not mamy_linie_miernicza(vim) or linia_jest_pelna(vim):
        aktywnie_wstaw_poczatek_pomiaru(vim)

def wstaw_date_koncowa(vim):
    vim.current.line = vim.current.line[:znak_daty_kon] + moment_czasowy()

def stempel_koncowy(vim):
    if mamy_linie_miernicza(vim) and not linia_jest_pelna(vim):
        wstaw_date_koncowa(vim)

def obsluga_stempli_czasowych(rodzaj, vim):
    if rodzaj == zncz_pocz:
        stempel_poczatkowy(vim)
    elif rodzaj == zncz_kon:
        stempel_koncowy(vim)
    else:
        raise RuntimeError(rodzaj)

def wykonaj(rodzaj, vim):
    if rodzaj in znane_wzorce:
        obsluga_stempli_czasowych(rodzaj, vim)
    else:
        wstaw_date_z_dzis(vim)

format_linii = r'''
BEGIN:
\s    # Spacja po słowie BEGIN
\d{4} # Rok
\.    # Kropka
\d{2} # Miesiąc
\.    # Kropka
\d{2} # Dzień
_     # Oddzielenie dnia od godziny
\d{2} # Godzina
\.    # Kropka
\d{2} # Minuta
\.    # Kropka
\d{2} # Sekunda
\s    # Spacja po dacie początkowej
END:
\s    # Spacja po słowie END
\d{4} # Rok
\.    # Kropka
\d{2} # Miesiąc
\.    # Kropka
\d{2} # Dzień
_     # Oddzielenie dnia od godziny
\d{2} # Godzina
\.    # Kropka
\d{2} # Minuta
\.    # Kropka
\d{2} # Sekunda
$     # Koniec tekstu
'''

wzor = re.compile(format_linii, re.VERBOSE)

def data_od_znaku(napis, nr_pocz):
    return napis[nr_pocz:nr_pocz + rozmiar_daty]

def wytnij_pocz(napis):
    return data_od_znaku(napis, znak_daty_pocz)

def wytnij_kon(napis):
    return data_od_znaku(napis, znak_daty_kon)

def ksztalt_linii_mierniczej(napis):
    return wzor.match(napis)

def wyznacz_krotke_czasu(napis):
    return map(int, [
        napis[0:4],
        napis[5:7],
        napis[8:10],
        napis[11:13],
        napis[14:16],
        napis[17:19],
        ])

def wyznacz_moment(napis):
    paczka_do_sekundy = wyznacz_krotke_czasu(napis)
    razem = paczka_do_sekundy + [0, 0, 0]
    return int(time.mktime(razem))

def wyznacz_jeden_kawalek(label, yyyy_mm, day):
    return ''.join([
        label,
        ' ',
        yyyy_mm,
        '.',
        '%02d' % day,
        '_',
        '00.00',
        '.00',
        ])

def wyznacz_linie_dnia(yyyy_mm, day):
    return ''.join([
        wyznacz_jeden_kawalek(etkt_pocz, yyyy_mm, day),
        ' ',
        wyznacz_jeden_kawalek(etkt_kon, yyyy_mm, day),
        ])

class TestRdzeniaDlaEdytora(unittest.TestCase):

    def test_lokalnej_paczki_danych(self):
        '''
        TestRdzeniaDlaEdytora:
        '''
        self.assertEqual(wstaw_na_pozycji('abcd', 1, 'x'), 'abxcd')
        self.assertEqual(len(moment_czasowy()), rozmiar_daty)

    def test_formatu_linii(self):
        '''
        TestRdzeniaDlaEdytora:
        '''
        self.assertTrue(ksztalt_linii_mierniczej(wzorcowa_data_pocz))
        wyznaczony_napis = wyznacz_tresc_poczatkowa()
        self.assertTrue(ksztalt_linii_mierniczej(wyznaczony_napis))
        self.assertEqual(wytnij_pocz(wzorcowa_data_pocz), sama_wzorcowa_data)
        self.assertEqual(wytnij_kon(wzorcowa_data_pocz), '0000.00.00_00.00.00')
        self.assertEqual(wyznacz_krotke_czasu(sama_wzorcowa_data), [2012, 12, 29, 13,  1, 23])
        self.assertEqual(wyznacz_krotke_czasu(inna_wzorcowa_data), [2012, 12, 29, 13, 52,  9])
        self.assertEqual(wyznacz_moment(sama_wzorcowa_data), 1356782483)

    def test_szkieletu_miesiaca(self):
        '''
        TestRdzeniaDlaEdytora:
        '''
        odp = wyznacz_jeden_kawalek(etkt_pocz, '2012.10', 31)
        self.assertEqual(odp,
            'BEGIN: 2012.10.31_00.00.00')
        odp = wyznacz_linie_dnia('2013.11', 1)
        self.assertEqual(odp,
            'BEGIN: 2013.11.01_00.00.00 END: 2013.11.01_00.00.00')
        odp = wyznacz_linie_dnia('2013.12', 1)
        self.assertEqual(odp,
            'BEGIN: 2013.12.01_00.00.00 END: 2013.12.01_00.00.00')

if __name__ == '__main__':
    unittest.main()
