# models.py
from Models import db

class CoffeeDomesticConsumption(db.Model):
    __tablename__ = 'Coffee_domestic_consumption'
    
    Country = db.Column(db.String(50), primary_key=True)
    Coffee_type = db.Column(db.String(50))
    _1990_91 = db.Column(db.Float)
    _1991_92 = db.Column(db.Float)
    _1992_93 = db.Column(db.Float)
    _1993_94 = db.Column(db.Float)
    _1994_95 = db.Column(db.Float)
    _1995_96 = db.Column(db.Float)
    _1996_97 = db.Column(db.Float)
    _1997_98 = db.Column(db.Float)
    _1998_99 = db.Column(db.Float)
    _1999_00 = db.Column(db.Float)
    _2000_01 = db.Column(db.Float)
    _2001_02 = db.Column(db.Float)
    _2002_03 = db.Column(db.Float)
    _2003_04 = db.Column(db.Float)
    _2004_05 = db.Column(db.Float)
    _2005_06 = db.Column(db.Float)
    _2006_07 = db.Column(db.Float)
    _2007_08 = db.Column(db.Float)
    _2008_09 = db.Column(db.Float)
    _2009_10 = db.Column(db.Float)
    _2010_11 = db.Column(db.Float)
    _2011_12 = db.Column(db.Float)
    _2012_13 = db.Column(db.Float)
    _2013_14 = db.Column(db.Float)
    _2014_15 = db.Column(db.Float)
    _2015_16 = db.Column(db.Float)
    _2016_17 = db.Column(db.Float)
    _2017_18 = db.Column(db.Float)
    _2018_19 = db.Column(db.Float)
    _2019_20 = db.Column(db.Float)
    Total_domestic_consumption = db.Column(db.Float)

    @classmethod
    def find_by_country(cls, country):
        return cls.query.filter_by(Country=country).all()

    @classmethod
    def get_all_data(cls):
        return cls.query.all()

    @classmethod
    def find_by_country_and_year(cls, country, year):
        year_col = f'_{year-1}_{year}'
        # Consulta la base de datos y devuelve el registro
        return cls.query.filter_by(Country=country).first()