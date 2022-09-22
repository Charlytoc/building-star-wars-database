from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Usuario(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorito = db.relationship('Favorites', backref='user', lazy=True)
    
    def __repr__(self):
        return '<Usuario %r>' % self.nombre

    def serialize(self):
        return {
            "nombre": self.nombre,
            "id": self.id,
            "email": self.email,
            "favorito": list(map(lambda item: item.serialize(), self.favorito))
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    # __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    favorito = db.relationship('Favorites', backref='people', lazy=True)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    # __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    weather = db.Column(db.String(80), unique=False, nullable=False)
    favorito = db.relationship('Favorites', backref='planets', lazy=True)
    
    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "weather": self.weather
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    # __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'),
        nullable=True)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'),
        nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'),
        nullable=False)

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize2(self):
        people = People.query.filter_by(id=self.people_id).first()
        gentuza = people.serialize()
        print(gentuza, "ESTE ES")

        return {
            "nombre": gentuza['name']
        }


    def serialize(self):
        return {
            "id": self.id,
            "people_id": self.people_id,
            "planets_id": self.planets_id,
            "usuario_id": self.usuario_id
            # do not serialize the password, its a security breach
        }
