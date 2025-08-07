from py4web import Session, Cache, DAL

# Basic database and session setup for py4web

# adapt connection string as needed
DB_URI = 'sqlite://storage.db'

session = Session(secret='some secret key')
cache = Cache(size=1000)
db = DAL(DB_URI, folder="databases")

