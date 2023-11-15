import sqlite3 
conn = sqlite3.connect('test_database')
c = conn.cursor()
c.execute("""
          
          CREATE TABLE IF NOT EXISTS Author 
          (id integer  primary key AutoIncrement ,
          name varchar(100) )
          """)


authors_list =[]
with open('cleaned_authors.txt','r',encoding='utf-8') as file :
    for line in file :
        line=line.replace('\n','')
        authors_list.append(line)

print(authors_list)
authors_unique_dict = {}
for author in authors_list :
    if author in authors_unique_dict :
        authors_unique_dict[author] +=1 
    else :
        authors_unique_dict[author] = 1 

print(authors_unique_dict)
authors_unique_names= [author for author in authors_unique_dict.keys()]
print('And The Author Unique names are ')
print(authors_unique_names)
c.executemany("""
                    insert into Author (name) 
            values (?);


                """,zip(authors_unique_names))


conn.commit()

c.execute('select * from author')
rows = c.fetchall()
for row in rows :
    print(row) 
