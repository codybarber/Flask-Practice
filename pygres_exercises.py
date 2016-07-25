import pg

# Connect to the PostgreSQL database
db = pg.DB(dbname='github_db')



# Make a query
query = db.query('select * from project')
print '----------------'
print query # shows you the data from the query
print '----------------'

# Inserting a new project into the Project table
# new_project = raw_input('What is the name of the project you would like to add? ')
# new_project_stars = raw_input('How many stars does this project have? ')
# new_project_date = raw_input('What date was this project completed? ')
#
# db.insert('project', name=new_project, stars=new_project_stars, date=new_project_date)

# Updating a project in the Project table
# update_project = raw_input('What is the ID of the project you would like to update? ')
# update_stars = raw_input('What is the updated amount of stars for this project? ')
#
# db.update('project', {'id': update_project, 'stars': update_stars})

# Deleting a row from a table
delete_project = raw_input('What is the ID of the project you would like to delete? ')
db.delete('project', {'id': delete_project})
