

# Projekt Django - CMS Portal eventowy

live: http://3.73.101.33:8000/

Ten projekt jest oparty na frameworku Django i zawiera aplikację internetową do zarządzania wydarzeniami i zakupem biletów.
Projekt wdrożony na AWS. Dodatkowo wykorzystuje Github Actions w celu automatycznego wdrażania zmian na serwer po zmianie kodu w repozytorium.

## Wymagania

Aby uruchomić ten projekt lokalnie, będziesz potrzebować następujących narzędzi:

- Python (wersja 3.9)
- Django (wersja 4.1.7)

## Instalacja

1. Sklonuj to repozytorium na swój lokalny komputer:

```
git clone https://github.com/KBorzy/CMS-portal-eventowy.git
```

2. Przejdź do katalogu projektu:

```
cd CMS-portal-eventowy
```

3. Utwórz wirtualne środowisko:

```
python -m venv myenv
```

4. Aktywuj wirtualne środowisko:

```
source myenv/bin/activate
```

5. Zainstaluj wymagane zależności:

```
pip install -r requirements.txt
```

6. Wykonaj migracje bazy danych:

```
python manage.py migrate
```

7. Uruchom serwer deweloperski:

```
python manage.py runserver
```

8. Otwórz przeglądarkę internetową i przejdź do adresu `http://localhost:8000/` aby zobaczyć projekt w działaniu.

## Dokumentacja
## Wkład


