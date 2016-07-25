import pg

# Connect to the PostgreSQL database
db = pg.DB(dbname='github_db')



# Make a query
query = db.query('select * from coder')
print query # shows you the data from the query

# Multi-line query
query2 = db.query('''
    select
        *
    from
        project
    where
        stars is not NULL
    order by
        stars desc
    limit 10
''')

# 3 different ways to get the result of the query

# 1. Get a list of tuples
tupled_result = query2.getresult()
[(1, 'Matthew Brimmer', 'mbrimmer1@gmail.com'), (2, 'David Pham', 'dpham@gmail.com')]

# 2. Get a list of dictionaries
dictionaried_result = query2.dictresult()
[{'id': 1, 'name': 'Matthew Brimmer', 'email': 'mbrimmer1@gmail.com'}, {'id': 2, 'name': 'David Pham', 'email': 'dpham@gmail.com'}]

# 3. Get a list of named tuples, which are basically objexts with attributes
named_result = query2.namedresult()
# [Row(id=1, name='Matthew Brimmer', email='mbrimmer1@gmail.com'), Row(id=2, name='David Pham', email='dpham@gmail.com')]
for program in named_result:
    name = program.name,
    stars = program.stars,
    date = program.date
    print ('Name: %r---Stars: %r---Date: %r') % (name, stars, date)

# The API for inserting data is
# db.insert(TABLE_NAME, COLUMN1=VALUE1)
# For example
db.insert('coder', name='DeeAnn')

# The API for updating data is
# db.update(TABLE_NAME, DICTIONARY)
# The dictionary needs to contain
# 1. the primary key of the object to be updated
# 2. the columns to be updated in that Row

# For example
db.update('coder', {'id': 7, 'name': 'Matthew'})
