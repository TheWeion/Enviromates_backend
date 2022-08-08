from enviromates import db

# Clear it all out

db.drop_all()
print("drop db")
# Set it back up

db.create_all()
print("reinitialise db")