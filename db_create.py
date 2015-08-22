from default import db
from models import Institutes
from loremipsum import generate_paragraph, generate_sentence

#db.create_all()
# db.session.add(Institutes("a","b"))
# db.session.add(Institutes("a1","b"))
# db.session.add(Institutes("a2","b"))
# db.session.add(Institutes("a3","b"))
# db.session.add(Institutes("a4","b"))
# db.session.add(Institutes("a5","b"))
# db.session.add(Institutes("a6","b"))
# db.session.add(Institutes("a7","b"))
# db.session.add(Institutes("a8","b"))
# db.session.add(Institutes("a9","b"))
# db.session.add(Institutes("a10","b"))
# db.session.add(Institutes("a11","b"))
# db.session.add(Institutes("a12","b"))
# db.session.add(Institutes("a13","b"))

for i in range(0,1000):
    a1,a2,title = generate_sentence()
    b1,b2,paragraph = generate_paragraph()
    db.session.add(Institutes(title,paragraph))

db.session.commit()
