from flask import Flask #Iz modula flask importujemo klasu Flask
from flask import render_template, request

app = Flask(__name__)
#Pravimo jednu instancu aplikacije Flask preko dunder/magic atributa __name__
# __name__ ima vrednost __main__ u svim fajlovima u kojima se pokrece

@app.route('/') #Dekorator dodaje neku dodatnu funkcionalnost funkciji
@app.route('/home')
def home():
    return 'Hello World'


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

#