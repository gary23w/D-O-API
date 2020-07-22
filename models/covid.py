from db import db

class CovidModel(db.Model):
    __tablename__ = 'covid'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    confirmed = db.Column(db.String(80))
    recovered = db.Column(db.String(80))
    critical = db.Column(db.String(80))
    deaths = db.Column(db.String(80))
    last_update = db.Column(db.String(80))

    def __init__(self, name, confirmed, recovered, critical, deaths, last_update):
        self.name = name
        self.confirmed = confirmed
        self.recovered = recovered
        self.critical = critical
        self.deaths = deaths
        self.last_update = last_update

    def json(self):
        return {
        'name': self.name,
         'confirmed': self.confirmed,
         'recovered': self.recovered,
         'critical': self.critical,
         'deaths': self.deaths,
         'last_update': self.last_update
         }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
