django app "Faktury i Rozrachunki", in short "fakir"
---------------------------------------------------






# Instalacja środowiska

Po sklonowaniu repo do katalogu XXX mamy taką strukturę:


```
.
├── app
│   ├── app
│   │   ├── asgi.py
│   │   ├── env.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── fakir
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── manage.py
│   ├── README.md
│   └── requirements.txt
├── docs
│   ├── Dawid Pabis.md
│   ├── Kamil Terelak.md
│   └── Tomasz Gryn.md
├── env
│   ├── debian-install-as-root.sh
│   ├── Makefile.rules.mk
│   └── Makefile.sample.mk
└── README.md
```


## Biblioteki potrzebne do budowy CPython

Jako `root`, w katalogu `env` uruchom skrypt `debian-install-as-root.sh`

```
bash# cd env
bash# ./debian-install-as-root.sh
```

## Budowanie interpretera

W katalogu `env`, z pliku `Makefile.sample.mk` utwórz własny plik `Makefile`

```
bash$ cp Makefile.sample.mk Makefile
bash$ vim Makefile
```

Przeedytuj plik Makefile i ustaw APPPORT na wartość powyżej 8000 (w zasadzie dowolny port)


Następnie uruchom budowanie środowiska poleceniem `make`

```
bash$ make
```

Powinieneś dostać podobym wynik na konsoli:


```
curl -O https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 24.2M  100 24.2M    0     0  6911k      0  0:00:03  0:00:03 --:--:-- 6909k
touch Python-3.9.2.tgz
tar zxf Python-3.9.2.tgz
touch Python-3.9.2
cd Python-3.9.2 ; \
./configure --prefix=/app/fakir/py --enable-optimizations ; \
make ;\
make install
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-pc-linux-gnu
checking for python3.9... no
```

Po zbudowaniu środowiska, pownny się odbyć testy:

```
make[2]: Wejście do katalogu '/app/fakir/env/Python-3.9.2'
./python -m test --pgo || true
0:00:00 load avg: 1.45 Run tests sequentially
0:00:00 load avg: 1.45 [ 1/43] test_array
0:00:01 load avg: 1.45 [ 2/43] test_base64
0:00:02 load avg: 1.45 [ 3/43] test_binascii
0:00:02 load avg: 1.45 [ 4/43] test_binop
0:00:02 load avg: 1.45 [ 5/43] test_bisect
0:00:02 load avg: 1.45 [ 6/43] test_bytes
0:00:07 load avg: 1.41 [ 7/43] test_bz2
0:00:09 load avg: 1.38 [ 8/43] test_cmath
0:00:09 load avg: 1.38 [ 9/43] test_codecs
0:00:12 load avg: 1.38 [10/43] test_collections
0:00:14 load avg: 1.35 [11/43] test_complex
0:00:15 load avg: 1.35 [12/43] test_dataclasses
0:00:16 load avg: 1.35 [13/43] test_datetime
0:00:26 load avg: 1.30 [14/43] test_decimal
```

Proces instalacji powinien się zakończyć tak:

```
Running setup.py install for psycopg2 ... done
Successfully installed Django-3.2.8 Pillow-8.4.0 ...
touch done.req
../bin/nb.++ => ../bin/nb
../bin/rs.++ => ../bin/rs
../.env.++ => ../.env
touch done.pre
```

## Ustawienie środowiska (zmiennych)

Każdorazowo, kiedy chcesz zacząć pracę z projektem musisz zaczytać zmienne środowiskowe z pliku `.env`

```
cd XXX
. .env
```

## Uruchamianie serwera deweloperskiego

Django posiada wbudowany serwer HTTP. Można z niego skorzystać pisząc:

```
bash$ ./manage.py runserver
```

albo używając polecenia `rs`.
W obu przypadkach wynik działania powinien być następujący:

```
bash$ rs
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 26, 2021 - 08:01:10
Django version 3.2.8, using settings 'app.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

