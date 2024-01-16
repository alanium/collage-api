from models.data import Photo, db

def add_photo(url):
    new_photo = Photo(url=url)
    db.session.add(new_photo)
    db.session.commit()

def get_all_photos():
    return Photo.query.all()
