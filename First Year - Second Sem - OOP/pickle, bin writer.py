import pickle

names_gwas = [
    ("Andrei", 2.3),
    ("Chesca", 2.1),
    ("Gabby", 2.5),
    ("Juan", 2.7),
    ("Miguel", 2.4),
    ("Chayne", 2.0),
    ("Jerrod", 2.8),
    ("Mherzaki", 2.6),
    ("Christian", 2.2),
    ("Joseph", 2.9),
    ("Preenz", 2.5),
    ("Merdeen", 2.1),
    ("Sebastian", 2.7),
    ("Paul", 2.4),
    ("Zander", 2.3),
    ("Richard", 2.6),
    ("Vladimir", 2.2),
    ("Blessie", 2.0),
    ("Mark", 2.4),
    ("Jovit", 2.1)
]

\
names = open("students.bin","wb")
pickle.dump(names_gwas,names)
names.close()

