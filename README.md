# file_exlorer_tkinter

 mały projekt szoklny na zajęcia python
 
 ## Platrofy
 
 aplikcaj powinna działac na platormach windows, macos, linux jedak testowa była tylko na systemie windows 10

## Uruchomienie

Do uruchomiania potrzebne są 3 pliki w tym samym pliku: file.py, fileExplorer.py, main.py

Aby uruchomić nalęży otworzyć pliku main.py przy uzyciy pythona

przez terminal [ścieżka od python] main.py
![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/01665cbb-eec6-4598-b3be-7bd16403a1d2)

przez ekslporatora plików

![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/830c5fd7-5830-4a90-acb7-bc6662764c06)

## Instrukacj obsługi

Po uruchomieniu otworzą się dwa okna terminal oraz Eksploratro plików

![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/34b9ce63-0ce8-45fe-b5dd-1d47763ec448)

Okno terminal jest zbędne lecz zamknięcie go zakończy działanie aplikcaji

Po otworzeniu aplikacji wyświtlana jest tabla zawierająca pliki w domyslnej scieżce
Nad tabelą zdajuje się scieżla w której obecnie dział aplikcaj
![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/e1714939-90ee-4939-91ce-740395410b16)
Służy ona do nawigowania do scieżek nadżednych w któch znajduje się obecna sieżka, ostatni przysic scieżki to obecnie otworzeny folder, pozostałe to folder nadrzędne

Pierszy przycisk pozwala na zmianę dysku przegladanego
![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/bf57026f-b89a-4dd4-b590-06c1343ee4c0)

Nacisnięcie na koluny sortuje table (bez kolumny typ) według tej kolumny

Pojedyńcze naciśnięcie na wiersz table zaznaczy ją

Przytrzymianie klawisa Ctrl pozwala na zaznaczanie wielu wierszy oraz odznaczniu zaznaczonych wierszy

Podwujne naciśnięcie na otworzy plik na który wskazuje, jeśli jest to foder to otorzy go wyświetlając jego zawarotść, w przeciwnym wypadku otworzy go przy użyci domyśnego dla systemu oprogramowania służacego do otwieranie plików tek typu

Jeżeli plik, lub foler nie może zostać otorzny (np. z powodu braku uprawnień) wyświtlne zostanie okno z komunikatem błedu

Po naciśnięci prawego przysicku myszy na table wyświetlne zostanie menu kontekstowe, jego zawartość zależy os stanu aplikacji

![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/a88cfe07-329d-46ad-9cdf-90c20f3e9a78)

Jeżeli żadne pliki ani foldery nie są zaznaczone pozowli do:
- utorzenie nowego pliku
- utorzenie nowego folderu
- wklejenie skopiowach, bądz wyciętych plików i folderów jeżli jakieś znajdują się w schowku
- wyczyszenie schowka

W przypaku zaznaczeni wielu plkiów/folderów pozowli:
- kopiować je
- wytnąć (przenieść) je
- usunąć je

Zaznacznei pojedyńczego pliku dostępne są opjec takie sam jak przy zaznacznieu wielu pliku plus opcja zmiany nazwy

Torzenie plików i zmiana nazwy otrzorzą nowe okno w którymc nalży wpisać nazwe do zmiany/utworznia pliku

![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/1cfe4da5-569a-47e2-97ee-f8ad6cb35b0e)

Kopiowanie i wycianie pozwala skopiować plik i wkleić je puzniej działa zarówn dal plików jak i folderów z zwartości, w przupadku występowania indeycznej nazwy w docelowj scieżce wkejenia, wklejony zostanie plik z dokejonom data i czasem do nazwy, możliwe jest też kopiowanie plików z posta aplikacji np. przy użyciu ekspolartoa plików widows, i wklejanie go przy użyciu tej aplikacji, jednak funkcionalność ta niezostała w pełni przetestowana i może stwarzać problemy

## Opis kodu

Kod aplikacji jest bardzo chaotyczny, nieschludny i niekosystętny.

Kod składa się z 3 plików: file.py, fileExplorer.py, main.py

- main.py - służy jedynie do uruchomienia aplikacji
- file.py - modelu zawierający klasę pomocniczą File służącą do przechowanania danych o pliku
- fileExplorer.py - modeul zawierający klasę FileExplorer zajmującą się resztą to jest interfesem użytownika i operacjami na plikach

W aplikcaji zostały użyte wbudowane biblioteki python:
-  do przechowanie i wyświetlania czasu utworzeani i modeyfikacji pliku - datetime
-  do operacji na plikach takich jak kopiwanie, przenoszeni, torzenie - os, shutil
-  do otwierania plików przy użyci domyślengo oprogramoania - subprocess, sys
-  do torzenia interfejsu użytkowanika, oraz przchowania danych w schowku - tkinter

### Główne funkcje kodu:

#### Interface użytwkoania

Interface użytwkia budowany jest przy użyciu  metod:
- __init__ - inicializacaj interfacu 
- build_table - budowa tabeli
- build_breadcrumb - budowa scieżki nad tabela
- build_files_actions_menu - budawa contekstowgo menu akcji
- show_file_name_prompt_window - budawa wypisania nazwy do utrznenia nogo pliku lub zmiany nazwy pliku
- open_popup - budowa okna do wyswietlania błedu

Interafce jest przebudowanyw za każdy razem gdy okno zostaje wybrane lub wykonana zostaje opracaj na plikach (typu kopianie, tworzenie).
Otorzenie folderu (po przez podujne kliknięcie) sktukje w następujących akcjach:
- utorzenie nowj sieżki 
- sprawdzeni instniena ścieżki
- ustawienie tej scieżki jako obecną
- usunięcia wszystkich przysicków z interfejsu nawicji po scieżce
- wsawienia nowych przycisków
- wczytania plików zdajdujących się w nowej scieżce
- usunięcia wszystkich wierszy z tabeli
- wstawinieu nowych wierzy do table

Podabie wykoanyanie akcji na plikach wykonuj je następnie powtaza akcje niezbędne do przebudaowania interfajsu graficznego


#### Kopiowanie i wycinanie plików i fodlerów

W celu kopiania plików i fodlerów użwany jest schowek ok tkinter, kopiowane są do niego scieżki plków zazacznych w tabeli.

Wklejanie polega na proraniu ze schowak tych scieżek i skopiowania ich do obecnej sięciżki, przed wklejeniem sprawdzane jest czy w obecnej ścieżce nie występuje już taki plik, jeżli występuje to jego nazwa zostaje zmianion następnie plik są kopiawane.

Podobnie działa wycianaie używa tych samych metod (co nie jest najczytelniejsze), ustawai jedynie flage która kontroluje czy plik mają być przeniesione czy kopiowane.

Fragment kodu odpowiedzlany z kopiwanie / przenoszenie:
![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/08f973bc-cf25-49a5-8401-0dd4607f1aa6)

Mniejszą niedogodą okazało się kopiwanie folderów z zawortością, podczas gyd modul shutil dostarcza funkcji copytree kopiującą zawarość folderu, to niekopiuje on samego folderu, ostacznie rozwiąłem to torząc nowy folder o naziw kopiwanego folderu w miejszcu docelwmy i kopiwania zaworści do niego

#### Tworzenie, uswanie, zmiani nazwy

Pozostałe akcje na plikach używają wbudowanych metod dostarczynhc przez bilbioteki, nie ma tu dużo do mówienia

#### Pozostałe

Początkowon opracje na właściwościach aplikacji takich jak obecna scieżka czy lista plików w obecnje sciżce miały być zarządze metodami typ get, set zapweniającymi bezpieczeństow przed nieprawidłowaymi modyfikacjiam lecz szybsze okazła się używania ich jak zmiennych globalnych, w yniku czego jest kod zwiera kilka praktycznie bezurzytecznych metod użythc tylko raz czy 2.


#### Ostatecznie kod jako tako dział, lecz sporow można byłow by w nim porawić 




