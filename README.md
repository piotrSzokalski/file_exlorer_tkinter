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


