# file_exlorer_tkinter

 mały projekt szkolny na zajęcia python
 
 ## Platformy
 
 aplikacja powinna działać na platformach windows, macos, linux jedak testowa była tylko na systemie windows 10

## Uruchomienie

Do uruchomiania potrzebne są 3 pliki w tym samym pliku: file.py, fileExplorer.py, main.py

Aby uruchomić należy otworzyć pliku main.py przy użycia pythona

przez terminal [ścieżka od python] main.py
![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/01665cbb-eec6-4598-b3be-7bd16403a1d2)

przez eksploratora plików

![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/830c5fd7-5830-4a90-acb7-bc6662764c06)

## Instrukcja obsługi

Po uruchomieniu otworzą się dwa okna terminal oraz eksplorator plików

![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/34b9ce63-0ce8-45fe-b5dd-1d47763ec448)

Okno terminal jest zbędne lecz zamknięcie go zakończy działanie aplikacji

Po otworzeniu aplikacji wyświetlana jest tabla zawierająca pliki w domyślnej ścieżce
Nad tabelą znajduje się ścieżka w której obecnie dział aplikacja
![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/e1714939-90ee-4939-91ce-740395410b16)
Służy ona do nawigowania do ścieżek nadrzędnych w których znajduje się obecna ścieżka, ostatni przycisk ścieżki to obecnie otworzony folder, pozostałe to folder nadrzędne

Pierwszy przycisk pozwala na zmianę dysku przeglądanego
![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/bf57026f-b89a-4dd4-b590-06c1343ee4c0)

Naciśnięcie na kolumny sortuje table (bez kolumny typ) według tej kolumny

Pojedyncze naciśnięcie na wiersz table zaznaczy ją

Przytrzymanie klawisz Ctrl pozwala na zaznaczanie wielu wierszy oraz odznaczaniu zaznaczonych wierszy

Podwójne naciśnięcie na otworzy plik na który wskazuje, jeśli jest to folder to otworzy go wyświetlając jego zawartość, w przeciwnym wypadku otworzy go przy użyci domyślnego dla systemu oprogramowania służącego do otwieranie plików tek typu

Jeżeli plik, lub folder nie może zostać otworzony (np. z powodu braku uprawnień), wyświetlone zostanie okno z komunikatem bledu

Po naciśnięci prawego przycisku myszy na table wyświetlone zostanie menu kontekstowe, jego zawartość zależy os stanu aplikacji

![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/a88cfe07-329d-46ad-9cdf-90c20f3e9a78)

Jeżeli żadne pliki ani foldery nie są zaznaczone pozwoli do:
- utworzenie nowego pliku
- utworzenie nowego folderu
- wklejenie skopiowanych, bądź wyciętych plików i folderów jeżeli jakieś znajdują się w schowku
- wyczyszczenie schowka

W przypadku zaznaczeni wielu plików/folderów pozwoli:
- kopiować je
- wyciąć (przenieść) je
- usunąć je

Zaznaczenie pojedynczego pliku dostępne są opcje takie sam jak przy zaznaczaniu wielu pliku plus opcja zmiany nazwy

Torzewie plików i zmiana nazwy otworzą nowe okno w którym należy wpisać nazwę do zmiany/utworzenia pliku

![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/1cfe4da5-569a-47e2-97ee-f8ad6cb35b0e)

Kopiowanie i wycinanie pozwala skopiować plik i wkleić je później działa zarówno dal plików jak i folderów z zwartości, w przypadku występowania indyczej nazwy w docelowej ścieżce wklejenia, wklejony zostanie plik z doklejoną data i czasem do nazwy, możliwe jest też kopiowanie plików z posta aplikacji np. przy użyciu eksplorator plików widows, i wklejanie go przy użyciu tej aplikacji, jednak funkcjonalność ta nie została w pełni przetestowana i może stwarzać problemy

## Opis kodu

Kod aplikacji jest bardzo chaotyczny, nieschludny i niekonsystentny.

Kod składa się z 3 plików: file.py, fileExplorer.py, main.py

- main.py - służy jedynie do uruchomienia aplikacji
- file.py - modelu zawierający klasę pomocniczą File służącą do przechowania danych o pliku
- fileExplorer.py - moduł zawierający klasę FileExplorer zajmującą się resztą to jest interfejsem graficznym użytkownika i operacjami na plikach

W aplikacji zostały użyte wbudowane biblioteki python:
-  do przechowanie i wyświetlania czasu utworzenia i modyfikacji pliku - datetime
-  do operacji na plikach takich jak kopiowanie, przenoszeni, torzewie - os, shutil
-  do otwierania plików przy użyci domyślnego programomania - subprocess, sys
-  do tworzenia interfejsu użytkowania, oraz przechowania danych w schowku - tkinter

### Główne funkcje kodu:



#### Interface użytwkoania

Interfejs użytkownika jest tworzony przy użyciu następujących metod:
- `__init__` - inicializacja interfejsu
- `build_table` - budowa tabeli
- `build_breadcrumb` - budowa ścieżki nad tabelą
- `build_files_actions_menu` - budowa kontekstowego menu akcji
- `show_file_name_prompt_window` - budowa okna do wprowadzenia nowej nazwy pliku lub zmiany istniejącej nazwy
- `open_popup` - budowa okna do wyświetlania błędu

Interfejs jest przebudowywany za każdym razem, gdy wybrana zostaje nowa ścieżka lub wykonana zostaje operacja na plikach (np. kopiowanie, tworzenie).
Otwarcie folderu (poprzez podwójne kliknięcie) powoduje wykonanie następujących akcji:
- Utworzenie nowej ścieżki
- Sprawdzenie istnienia ścieżki
- Ustawienie tej ścieżki jako obecnej
- Usunięcie wszystkich przycisków nawigacji nad ścieżką w interfejsie
- Wstawienie nowych przycisków nawigacji
- Wczytanie plików znajdujących się w nowej ścieżce
- Usunięcie wszystkich wierszy z tabeli
- Wstawienie nowych wierszy do tabeli

Podobnie, wykonanie akcji na plikach prowadzi do wykonania niezbędnych kroków w celu przebudowy interfejsu graficznego. Przepisz tekst bez błędów ortograficznych.




#### Kopiowanie i wycinanie plików i folderów

W celu kopiowania plików i folderów wykorzystywany jest schowek tkinter. Ścieżki zaznaczonych plików są kopiowane do schowka.

Proces wklejania polega na odczytaniu ścieżek z schowka i skopiowaniu ich do obecnej lokalizacji. Przed wklejeniem, sprawdzane jest, czy w obecnej lokalizacji nie istnieje już plik o tej samej nazwie. Jeśli tak, to nazwa pliku zostaje zmieniona przez dołączenie daty i czasu, a następnie plik jest skopiowany.

Procedura wycinania działa podobnie, korzystając z tych samych metod. Różnica polega na ustawieniu flagi, która kontroluje, czy pliki mają być przeniesione czy skopiowane.

Poniżej przedstawiam fragment kodu odpowiedzialny za kopiowanie/przenoszenie:
![image](https://github.com/piotrSzokalski/file_exlorer_tkinter/assets/101019797/08f973bc-cf25-49a5-8401-0dd4607f1aa6)

Mniejszym problemem okazało się kopiowanie folderów wraz z zawartością. Moduł `shutil` dostarcza funkcję `copytree`, która kopiuje zawartość folderu, ale nie kopiuje samego folderu. Ostatecznie rozwiązałem to, tworząc nowy folder o nazwie kopiowanego folderu w miejscu docelowym i kopiując jego zawartość do tego nowego folderu.

#### Tworzenie, usuwanie, zmiana nazwy

Pozostałe operacje na plikach wykorzystują wbudowane metody dostarczane przez biblioteki. Nie ma zbyt wiele do powiedzenia na ten temat.

#### Pozostałe

Początkowo operacje na właściwościach aplikacji, takich jak obecna ścieżka czy lista plików w obecnej ścieżce, miały być obsługiwane za pomocą metod typu get i set, zapewniających bezpieczeństwo przed nieprawidłowymi modyfikacjami. Jednak okazało się, że szybszym rozwiązaniem było używanie ich jak zmiennych globalnych. W rezultacie kod zawiera kilka praktycznie bezużytecznych metod używanych tylko raz lub dwa razy.

#### Ostatecznie kod działa w miarę poprawnie, ale nadal można sporo poprawić.

