# file_exlorer_tkinter

 mały projekt szoklny na zajęcia python
 
 ## Platrofy
 
 aplikcaj powinna działac na platormach windows, macos, linux jedak testowa była tylko na systemie windows 10

## Uruchomienie

Do uruchomiania potrzebne są 3 pliki w tym samym pliku: file.py, fileExplorer.py main.py

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





