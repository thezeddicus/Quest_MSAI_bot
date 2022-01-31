from pony.orm import *

db = Database()

# create model
class Sentence(db.Entity):
	words = Required(str)

# bind db
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

db.generate_mapping(create_tables=True)

# Save info in database
@db_session
def save():
	p1 = Sentence(words="Empire isn’t just about New York.")
	p2 = Sentence(words="It’s about hope.")
	p3 = Sentence(words="No matter where we’re from")
	p4 = Sentence(words="we all want the opportunity to work hard")
	p5 = Sentence(words="Breathe life into our ambitions.")

# return info
@db_session
def return_words(number):
	p = Sentence[number]
	return p.words


#save()

word1, word2, word3, word4, word5 = return_words(1),return_words(2),return_words(3),return_words(4),return_words(5)
