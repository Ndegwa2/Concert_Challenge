from model import Band, Venue, Concert, sessionmaker, engine

Session = sessionmaker(bind=engine)
session = Session()

# Adding some bands and venues
band1 = Band(name="The Rolling Stones", hometown="London")
band2 = Band(name="The Beatles", hometown="Liverpool")
venue1 = Venue(title="Wembley Stadium", city="London")
venue2 = Venue(title="Madison Square Garden", city="New York")

session.add_all([band1, band2, venue1, venue2])
session.commit()

# Adding a concert
concert1 = Concert(band=band1, venue=venue1, date="2024-12-01")
session.add(concert1)
session.commit()

# Query and print the data
concerts = session.query(Concert).all()
for concert in concerts:
    print(f"{concert.band.name} will perform at {concert.venue.title} on {concert.date}")
