from enviromates import db
from enviromates.models.url import ShortUrls

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()