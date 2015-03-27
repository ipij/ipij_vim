:syntax off
:syntax on
:set wrapmargin=45
:set wrapmargin=1
:set wrapmargin=49
:set wrapmargin=0
:set background=light
:set background=dark
:set nows
:set noet
:set et
:set noai
:set ai
:set shiftwidth=1
:set isprint=@,128-255
" Nawiasy Scheme w kilku liniach
:imap <F12> (<CR>)<esc>O <esc>kA
" Uruchomienie slownika
:imap <F12> <esc>:pyfile ~/bin/slownik.py<CR>A
:imap <F12> <Esc>zzO
" Nawiasy Scheme w jednej linii
:imap <F11> ()<esc>i
" Klamry C, wciecie na 4 spacje
:imap <F10> {<CR>}<esc>O<space><space><space><space>
" Komentarz C
:imap <F9> /*  */<esc>hhi
" Klamry C dla if-then-else
:imap <F7> <F10><esc>joelse<esc>o<F10><esc>a
:imap <F12> <Esc>j0a
:map <F11> V%<
:map <F11> %zz
:map <F10> V%d<C-W><C-W>P
" Nastepny i poprzedni
:map <F8> :n<C-M>
:map <F7> :N<C-M>
:map <F6> <C-W>j
:map <F5> <C-W>k
:map <F5> ebde"aP
:map <F4> 99<C-W>+
:map <F4> mzbve"ay`z
" Wyjscie jednym klawiszem
:map <F3> :q<cr>
:map ,3 :q<cr>
:map <F2> :let &background = ( &background == "dark"? "light" : "dark")<cr>
:map ,b :let &background = ( &background == "dark"? "light" : "dark")<cr>
" Wlacz podswietlenie skladni wedlug FoxPro
:map ,f :set syntax=foxpro<cr>
:map <F2> 99<C-W>+
:map <F2> <C-W><C-W>
"Przejdz do okna ponizej
:map <F2> <C-W><C-W>
"Num 7/Home - przejdz do okna powyzej
:map <esc>Ow <C-W>W
" Przyda sie szybkie rozszczepianie okienka
:map <F4> :sp<cr>zz
:map ,4 :sp<cr>zz
"<C-W><C-W>zz
:set tabstop=4
:map <F1> @q
" Trwale kopiowanie slowa
:map <F5> "ayiw
" Wstawienie slowa skopiowanego do rejestru "a
:map <F6> ciwX<Esc>v"ap
" Po wyjsciu z edytora pozostaw podglad edytowanego tekstu
:set t_ti= t_te=
" Dlugie teksty Pythona potrzebuja szerokiej synchronizacji
:map ,s :syntax sync minlines=5000<cr>
"Ustawienia dla edycji programu w C
:map ,c :so ~/.exrc_c<cr>
" Przelaczanie zawijania dlugich linii
:map ,w :set wrap!<cr>
" Przelaczanie automatycznego wcinania tekstu
:map ,a :set ai!<cr>
" Podzial ekranu na czesc lewa i prawa
:map ,v :vsplit<cr>
" Usuniecie Ctrl-M z calego pliku
" :map ,m :%s/\r//g<cr>
" Przelaczenie obslugi myszy
:map ,m :let &mouse = ( &mouse == "a"? "" : "a")<cr>
" Przelaczenie na UTF-8
":map ,e :set fileencoding=utf-8<cr>
" Wczytanie pliku w tym samym obszarze roboczym
:map ,e :e<space>
" Gdy wczytal sie i nie rozpoznal ISO-8859-2, to wymus rozpoznanie
:map ,u :e ++enc=iso-8859-2<cr>
" Wymus rozpoznanie CP-1250
:map ,y :e ++enc=cp1250<cr>
" Pomniejszenie biezacego okna
:map ,-  <c-w>99-
" Powiekszenie biezacego okna
:map ,=  <c-w>99+zz
" Wstawienie aktualnej daty - Num -
":imap <esc>OS <esc>:pyfile ~/bin/data_vim.py<cr>a
:imap <esc>OQ <esc>:python import sys<cr>:python sys.argv = ["-", "godz_pocz"]<cr>:pyfile ~/bin/data_vim.py<cr>:update<cr>a
:imap <esc>OR <esc>:python import sys<cr>:python sys.argv = ["-", "godz_kon"]<cr>:pyfile ~/bin/data_vim.py<cr>:update<cr>a
:imap <esc>OS <esc>:python import sys<cr>:python sys.argv = ["-", "data"]<cr>:pyfile ~/bin/data_vim.py<cr>:update<cr>a
"Num 8, Num 9 - nawigacja po jednakowych wcieciach dla jezyka Python
:map <esc>Ox :pyfile /home/kwadrat/bin/vimMotion.py<cr>:python blockMotion(-1)<CR>^zz
:map <esc>Oy :pyfile /home/kwadrat/bin/vimMotion.py<cr>:python blockMotion(1)<CR>^zz
"Num 2, Num 3 - nawigacja po nadrzednych wcieciach dla jezyka Python
:map <esc>Or :pyfile /home/kwadrat/bin/vimMotion.py<cr>:python blockMotion(-2)<CR>^zz
:map <esc>Os :pyfile /home/kwadrat/bin/vimMotion.py<cr>:python blockMotion(2)<CR>^zz
":set fileencodings=utf-8,latin2
":set fileencodings=utf-8,latin2
":set encoding=utf-8
":set fileencodings=utf-8
":set termencoding=iso8859-2
" Num / - wyszukiwanie w gore
:map <esc>OQ #zz
" Num * - wyszukiwanie w dol
:map <esc>OR *zz
" Num - - przeskok po dopasowanych nawiasach
:map <esc>OS %zz
" Num PageUp i Num PageDown - wylaczone, aby miec nawigacje dla Pythona Num 8, Num 9
" :map <esc>Oy <C-B>
" Num PageDown
" :map <esc>Os <C-F>
" Num Home - w trybie wstawiania nadpisuje od poczatku linii (do wyrzucenia?)
:imap <esc>Ow <esc>^R
" Num Insert - wstawienie komentarza
:imap <esc>Op #<space>
" Num Insert - zapis pliku, jesli w pliku cos zmieniono
:map <esc>Op :update<cr>
" Podkreslenie zamiast Insert
:imap <esc>[2~ _
"   """"""""""""""""""" Dla zmiany nazw w plikach
"   " Znajdz pierwsze wystapienie wzorca i przejdz do nastepnego okna
"   :map <F1> 1Gnzz<c-w><c-w>
"   " wytnij poczatkowy przedrostek, przejdz na koniec slowa i dodaj koncowke.
"   " Znajdz nastepny.
"   :map <F3> xxxea_kw<esc>nzz
"   :map <F4> :q<cr>
" Zaznacz "V" na gorze bloku, a "F4" na dole - warunkowe wykonanie kodu
:vmap <F4> mbomaVOif conf_kw.DomyslnieAktywne:<cr>else:<esc>0ji<space><space><esc>gvykPztkkjj
:vmap <F4> mbomaVOif 1:<cr>else:<cr><space><space><space><space>#<esc>77a#<esc>yypVkykP`aV`b4>gvxkP3kP2kwzz
" Tylko jedna spacja po zlaczeniu dwoch zdan zakonczonych kropka
:set nojoinspaces
" Zastap nawiasy kwadratowe nawiasami okraglymi
:map ,z r(f]r)
" Przygotowanie do otworzenia nowego pliku
:map ,n :new<space>
" Przygotowanie do otworzenia nowego pliku z starego kodu (w aktualnym lub nowym oknie)
:map ,l :e<space>../dkw/src/
:map ,k :new<space>../dkw/src/
" Num . - przejdz do wpisanej linii i wycentruj widok
:map <esc>On Gzz
" Zaznacz wizualnie wiersze, a potem zapisz do pliku o nazwie "c"
:vmap ,j :w c<cr>
" Dla praktyki
":set tabstop=4
":set noet
" Num 5 - polacz linie za pomoca wielkiej litery J
":map <esc>Ou J
" Num 5 - przejdz na glebszy poziom wciec, w nastepnej linii
:map <esc>Ou j^zz
"" Num 1 - End - przejdz na koniec linii
":map <esc>Oq $
" Num 1 - End - przejdz na poczatek linii
:map <esc>Oq ^zz
"" Wykasowanie wciec
":map <F12> 1G^h<c-v>G0x:w<cr><c-w><c-w>zz
"" Przeniesienie biezacej linijki ponizej
":map <F12> ddpzz
" Wyjscie ze wszystkich buforow naraz
:map <F12> :qa<cr>
" Wyciecie bloku miedzy dwoma case
:map <F11> ^ma:pyfile /home/kwadrat/bin/vimMotion.py<CR>:python blockMotion(1)<CR>^zzmbkkV`aj,j`b^zz<c-w><c-w>zz
"Num 4 - wciecie w lewo
:map <esc>Ot V4<
:vmap <esc>Ot 4<gv
"Num 6 - wciecie w prawo
:map <esc>Ov V4>
:vmap <esc>Ov 4>gv
"Szybkie zakomentowanie biezacej linii
:map ,h ^i#<esc>zz
"Proba implementacji Game of Life - w katalogu /home/kwadrat/code
":map <F12> :pyfile abc.py<CR>:python wykonaj()<CR>
"Otaczanie nawiasami w jezyku Python dla formatowania procentem: %(nazwa)s
:map ,5 yiwi%(<esc>lea)s<esc>
"Num + - Aktualizacja zawartosci pliku
:map <esc>Ol :e<cr>1G
"Lazy redraw - przyspieszenie wykonywania makrodefinicji przez brak
"aktualizacji ekranu
:set lz
:set hlsearch
" Ubuntu: go to the last visited line (not to first line of file)
if has("autocmd")
  autocmd BufReadPost * if line("'\"") > 0 && line ("'\"") <= line("$") | exe "normal! g'\"" | endif
endif
"Pozwala wyszukiwac nazwy polaczone kropkami na Ubuntu
:set iskeyword=@,48-57,_,192-255
":set undofile
":set undodir=$HOME/.undo_vim
":set undolevels=100
":set undoreload=1000
