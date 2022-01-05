from flask import Flask #Iz modula flask importujemo klasu Flask
from flask import render_template, request, redirect, url_for, session
import mysql.connector


app = Flask(__name__)
#Pravimo jednu instancu aplikacije Flask preko dunder/magic atributa __name__
# __name__ ima vrednost __main__ u svim fajlovima u kojima se pokrece

app.config['SECRET_KEY'] = "sdnah237y7hdiajfn3o9af9ajm2dlamfdoq"

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'baza_igrica' #naziv iz phpmyadmina
)


@app.route('/') #Dekorator dodaje neku dodatnu funkcionalnost funkciji
@app.route('/home')
def home():
    return 'Hello World sa bazom'


@app.route('/nova_ruta')
def nova_ruta():
    return 'Ovo je nova ruta'


@app.route('/ruta_html')
def ruta_html():
    return '<h1>Darko Pokoracki</h1>'


@app.route('/ruta_vise_html')
def ruta_vise_html():
    html = """
        <h1>Naslov</h1>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
    """

    return html


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/ruta_sa_vrednoscu')
def ruta_sa_vrednoscu():
    name = 'Darko'

    return render_template(
        'ruta_sa_vrednoscu.html',
        name = name
    )


@app.route('/ruta_sa_vise_vrednosti')
def ruta_sa_vise_vrednosti():
    naziv_proizvoda = 'Cipele'
    slika_proizvoda = 'https://www.djaksport.com/image.aspx?imageId=126153'
    cena_proizvoda = 3600


    return render_template(
        'proizvod.html',
        naziv_proizvoda = naziv_proizvoda,
        slika_proizvoda = slika_proizvoda,
        cena_proizvoda = cena_proizvoda
    )


@app.route('/ruta_sa_parametrom/<parametar>')
def ruta_sa_parametrom(parametar):
    
    return parametar


@app.route('/studenti/<indeks>')
def studenti(indeks):

    return render_template(
        'student.html',
        indeks = indeks
    )


class Student:
    indeks : str
    ime : str
    prezime: str

    def __init__(self, ime, prezime, indeks) -> None:
        self.ime = ime
        self.prezime = prezime
        self.indeks = indeks


@app.route('/ruta_sa_klasom')
def ruta_sa_klasom():
    s1 = Student('Darko', 'Pokoracki', "S23/20")

    return render_template(
        'moj_student.html',
        student = s1
    )

@app.route('/ruta_sa_recnikom')
def ruta_sa_recnikom():
    student = {
        "ime": "Darko",
        "prezime": "Pokoracki"
    }

    return render_template(
        'ruta_sa_recnikom.html',
        osoba = student
    )


@app.route('/privilegije_uslovi')
def privilegije_uslovi():
    nivo_privilegije = 3
    # 1 -> korisnik nije ulogovan = register i login
    # 2 -> korisnik je ulogovan ali nije administrator -> logout
    # 3 -> Administrator = ima opicju za brisanje i update

    return render_template(
        'privilegije.html',
        nivo_privilegije = nivo_privilegije
    )


@app.route('/ruta_sa_petljom')
def ruta_sa_petljom():
    drzave = ['Srbija', 'Bosna', 'Hrvatska']

    return render_template(
        'forma_za_petlje.html',
        drzave = drzave
    )

@app.route('/ruta_sa_listom_listi')
def ruta_sa_listom_listi():
    automobili = [
        ['Bmw', 'x6', 2012],
        ['opel', 'Astra', 2009],
        ['Ford', 'Fusion', 2005],
        ['Porsche', 'Panarema', 2020]
    ]

    return render_template(
        'automobili.html',
        automobili = automobili
    )

class Proizvod:
    naziv : str
    cena : float
    kolicina: int
    slika: str

    def __init__(self, naziv, cena, kolicina, slika) -> None:
        self.naziv = naziv
        self.cena = cena
        self.kolicina = kolicina
        self.slika = slika

    def __repr__(self) -> str:
        return self.naziv

    def __str__(self) -> str:
        res = f"Naziv: {self.naziv}\n"
        res += f"Cena: {self.cena}\n"
        res += f"Kolicina: {self.cena * self.kolicina}"
        return res


@app.route('/ruta_sa_listom_objekata')
def ruta_sa_listom_objekata():
    p1 = Proizvod('Jakna', 5000, 4, 'https://www.djaksport.com/image.aspx?imageId=224295')
    p2 = Proizvod('Patike', 4500, 3, 'https://www.djaksport.com/image.aspx?imageId=202899')
    p3 = Proizvod('Trenerke', 10000, 7, 'https://www.djaksport.com/image.aspx?imageId=168879')

    p = [p1, p2, p3]

    return render_template(
        'proizvodi.html',
        proizvodi = p
    )


@app.route('/ruta_sa_listom_recnika')
def ruta_sa_listom_recnika():
    s1 = {
        "naziv": "Suncokreti",
        "autor": "Van gog"
    }

    s2 = {
        "naziv": "Suncokreti2",
        "autor": "Van gog2"
    }

    s3 = {
        "naziv": "Suncokreti3",
        "autor": "Van gog3"
    }

    s = [s1, s2, s3]

    return render_template(
        'slike.html',
        slike = s
    )

@app.route('/za_request')
def za_request():
    
    return render_template(
        'za_request.html',
        hederi = request.headers
    )


@app.route('/razlicite_metode')
def razlicite_metode():
    return request.method #GET

@app.route('/ruta_sa_postom', methods=['GET', 'POST'])
def ruta_sa_postom():
    if request.method == 'GET':
        return render_template(
            'forma_za_post.html'
        )
    else:
        username = request.form['username']
        password = request.form['password']

        if password == "":
            return render_template(
                'forma_za_post.html',
                greska = 'ne sme biti prazan password',
                username = username
            )

        pol = request.form['pol']
        drzava = request.form['drzave']

        return drzava


@app.route('/sve_igrice')
def sve_igrice():
    
    cursor = mydb.cursor(prepared = True) #mydb je objekat koji slika ponasanje neke baze
    # cursor je objekat koji nam omogucava da prolazimo kroz redove baze i da vrsimo upite nad bazom
    sql = "SELECT * FROM Igrica"

    cursor.execute(sql) #izvrsava sql upit
    rez = cursor.fetchall()

    n = len(rez)
    m = len(rez[0])

    for i in range(n):
        rez[i] = list(rez[i]) #menjamo tuple u listu
        for j in range(m):
            if isinstance(rez[i][j], bytearray):  # isinstance(objekat, naziv_klase)
                rez[i][j] = rez[i][j].decode()

    return render_template(
        'igrice.html',
        igrice = rez
    )
    #Svaka ruta mora da vrati string kao rezultat

@app.route("/dodaj_igricu", methods=['GET', 'POST'])
def dodaj_igricu():
    if request.method == 'GET':
        return render_template(
            'dodaj_igricu.html'
        )

    else:
        #Nije bitno kojim metodom uzimamo podatke sa forme,
        #recnik moze na ova dva nacina: 
        naziv = request.form['naziv']
        opis = request.form.get('opis')
        godina = request.form['godina']
        zanr = request.form['zanr']
        vrsta_igre = request.form.getlist('vrsta')
        vrsta_igre = ",".join(vrsta_igre)

        cursor = mydb.cursor(prepared = True)
        sql_statment = "INSERT INTO Igrica VALUES(null, ?, ?, ?, ?, ?)"
        vrednosti = (naziv, opis, godina, zanr, vrsta_igre)
        cursor.execute(sql_statment, vrednosti)

        mydb.commit() #kada vrsimo neku izmenu nad bazom moramo da komitujemo

        return redirect(
            url_for('sve_igrice')
        )
        # prepared statment sprecava sql injection


@app.route('/sve_igrice/<id_igrice>')
def igrica_pojedinacno(id_igrice):

    cursor = mydb.cursor(prepared = True)
    sql = "SELECT * FROM Igrica WHERE igricaID=?"
    parametar = (id_igrice, ) #mora da postoji zarez kada imamo jednu vrednost
    #Da bi bio tuple tj. kolekcija slicna listi
    cursor.execute(sql, parametar)

    rez = cursor.fetchone()
    #fetchone vraca None ako nemamo odgovarajuci Id u bazi
    if rez == None:
        return '<h1>ne postoji taj ID</h1>'

    else:
        rez = list(rez)
        n = len(rez)
        for i in range(n):
            if isinstance(rez[i], bytearray):
                rez[i] = rez[i].decode()

        return render_template(
            'igrica_pojedinacno.html',
            igrica = rez
        )

    return id_igrice

@app.route('/delete/<id_igrice>', methods=['POST'])
def delete(id_igrice):
    cursor = mydb.cursor(prepared = True)

    sql = "DELETE FROM Igrica WHERE igricaID = ?"
    vrednosti = (id_igrice, )

    cursor.execute(sql ,vrednosti)
    mydb.commit() #Posto menjamo stanje u bazi moramo da commitujemo

    return redirect(
        url_for('sve_igrice') #Ovo je ustvari naziv funkcije a nije putanja
    )


@app.route('/update/<id_igrice>', methods=['POST', 'GET'])
def update(id_igrice):
    if request.method == 'GET':
        cursor = mydb.cursor(prepared = True)
        sql = "SELECT * FROM Igrica WHERE igricaID=?"
        parametar = (id_igrice, ) #mora da postoji zarez kada imamo jednu vrednost
        #Da bi bio tuple tj. kolekcija slicna listi
        cursor.execute(sql, parametar)

        rez = cursor.fetchone()
        #fetchone vraca None ako nemamo odgovarajuci Id u bazi
        if rez == None:
            return '<h1>ne postoji taj ID</h1>'
        else:
            rez = list(rez)
            n = len(rez)
            for i in range(n):
                if isinstance(rez[i], bytearray):
                    rez[i] = rez[i].decode()

            return render_template(
                'update.html',
                podaci = rez
            )

    else:
        naziv = request.form['naziv']
        opis = request.form.get('opis')
        godina = request.form['godina']
        zanr = request.form.get('zanr')
        vrsta_igre = request.form.getlist('vrsta')
        vrsta_igre = ",".join(vrsta_igre)

        cursor = mydb.cursor(prepared = True)
        sql_statment = "UPDATE Igrica SET naziv=?, opis=?, godina=?, zanr=?, vrstaIgre=? WHERE igricaID = ?"
        vrednosti = (naziv, opis, godina, zanr, vrsta_igre, id_igrice)
        cursor.execute(sql_statment, vrednosti)

        mydb.commit() #kada vrsimo neku izmenu nad bazom moramo da komitujemo

        return redirect(
            url_for('sve_igrice')
        )

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template(
            'register.html'
        )

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['confirm']
        email = request.form['email']
        privilegija = request.form['privilegija']

        cursor = mydb.cursor(prepared = True)
        sql = "SELECT * FROM korisnik WHERE username=?"
        value = (username, )
        cursor.execute(sql, value)

        res = cursor.fetchone()

        if res != None:
            return render_template(
                'register.html',
                username_error = 'Vec postoji nalog sa tim usernamom'
            )

        if password != confirm:
            return render_template(
                'register.html',
                password_error = "Lozinke se ne poklapaju!"
            )

        cursor = mydb.cursor(prepared = True)
        sql = "INSERT INTO korisnik VALUES(null, ?, ?, ?, ?)"
        values = (username, password, email, privilegija)
        cursor.execute(sql, values)
        mydb.commit()

        return "Usepsno ste se registrovali"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(
            url_for('korisnici')
        )

    if request.method == 'GET':
        return render_template(
            'login.html'
        )

    else:
        username = request.form['username']
        password = request.form['password']

        cursor = mydb.cursor(prepared = True)
        sql = "SELECT * FROM korisnik WHERE username=?"
        value = (username, )
        cursor.execute(sql, value)

        res = cursor.fetchone()

        if res == None:
            return render_template(
                'login.html',
                username_login_error = "Ovaj nalog ne postoji"
            )

        if password != str(res[2].decode()):
            return render_template(
                'login.html',
                password_login_error = "Pogresna Sifra!"
            )

        session['username'] = username
        session['privilegija'] = int(res[4])
        return render_template(
            'test_sesije.html'
        )

@app.route('/korisnici')
def korisnici():
    cursor = mydb.cursor(prepared = True)
    sql = "SELECT * FROM korisnik"
    cursor.execute(sql)

    res = cursor.fetchall()

    n = len(res)
    for i in range(n):
        res[i] = list(res[i])
        m = len(res[i])
        for j in range(m):
            if isinstance(res[i][j], bytearray):
                res[i][j] = res[i][j].decode()


    return render_template(
        'korisnici.html',
        korisnici = res
    )


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
        session.pop('privilegija')

        return redirect(
            url_for('login')
        )

    else:
        return redirect(
            url_for('korisnici')
        )

app.run(debug = True) #pokrece aplikaciju




#pip list
#modul flask se bavi backendom tj serversom stranom aplikacije na webu
#Modul predstavlja python fajl koji se ne izvrsava nego koji se uvozi.

#Kada dohvatimo korisnika iz baze, moramo ga predstaviti u obliku klase ili recnika
#Vue.js je dobar za mid range aplikacije
#Vue.js je najbolji izbor js frameworka za kombinaciju sa flaskom

#model = klasa
# viewer = nacin na koji se predstavlja
#controler = kontrolise komunikaciju sa bazom

#Kada se trazi slanje forme, nikako nemoj koristiti GET request.

#Ekstenzija za flask: flask-snippets
#za sada treba flask i mysql connector
# kasnije ce nam trebati hashlib pip install hashlib!

#input type=hidden?

"""
- sha256 se koristi.
- Passwordovi se nikad ne cuvaju kao plain text
- hashlib biblioteka se koristi za heshovanje
- passwordi i osteljivei informacije cuvamo u formi hash-a
- secrey key mora da postoji da bismo pristupili sesiji

- Pristup sesiji imamo i u aplikaciji i na templejtu
"""
