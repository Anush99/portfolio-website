import mysql.connector

class DatabaseActions:
    def connect():
      mydb = mysql.connector.connect(
      host="localhost",
      user="anush",
      password="i5tk--vntH_zDVAt",
      database="portfolio"
)
      return mydb

    def selectMedia():
        mydb = DatabaseActions.connect()
        cursor= mydb.cursor()
        query = f"SELECT * FROM `media`"
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('There is no record found')
        else: 
            for row in rows:
                datastring = '@'.join(map(str, row))
                photo = "path@0"
                # print(datastring)
                if photo in datastring:
                    list = datastring.split(sep="@", maxsplit=6)
                    resolution = list[4].split(',')
                    resolution = 'x'.join(resolution)
                    show = f"Image with {list[0]} id, '{list[1]}' title, {resolution} pixel resolution, {list[3]}$ price and {list[2]}MB size."
                    print(show)
                video = "path@1@"
                if video in datastring:
                    list = datastring.split(sep="@", maxsplit=8)
                    resolution = list[4].split(',')
                    resolution = 'x'.join(resolution)
                    show = f"Video with {list[0]} id, '{list[1]}' title, {resolution} pixel resolution, {list[7]} duration, {list[4]}$ price and {list[3]}MB size."
                    print(show)

    def selectMusic():
        mydb = DatabaseActions.connect()
        cursor= mydb.cursor()
        query = f"SELECT * FROM `music`"
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('There is no record found')
        else: 
            for row in rows:
                datastring = '@'.join(map(str, row))
                # print(datastring)
                list = datastring.split(sep="@")
                show = f"Music with {list[0]} id, '{list[3]}' name, in {list[1]} category and {list[2]} minutes duration."
                print(show)


    def selectCollection():
        mydb = DatabaseActions.connect()
        cursor= mydb.cursor()
        query = f"SELECT * FROM `collection`"
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('There is no record found')
        else: 
            for row in rows:
                datastring = '@'.join(map(str, row))
                # print(datastring)
                list = datastring.split(sep="@")
                show = f"Collection with {list[0]} id, '{list[1]}' name, {list[2]} price and '{list[3]}' description."
                print(show)
                print(" Includes:")
                query2=f"SELECT * FROM media INNER JOIN mediacollection ON media.mediaId=mediacollection.mediaId and mediacollection.collectionId = {list[0]}"
                cursor.execute(query2)
                rows = cursor.fetchall()
                if len(rows) == 0:
                    print('There is no record found')
                else:
                    for row in rows:
                        datastring = '@'.join(map(str, row))
                        photo = "path@0"
                        # print(datastring)
                        if photo in datastring:
                            list = datastring.split(sep="@", maxsplit=6)
                            resolution = list[4].split(',')
                            resolution = 'x'.join(resolution)
                            show = f" Image with {list[0]} id, '{list[1]}' title, {resolution} pixel resolution, {list[3]}$ price and {list[2]}MB size."
                            print(show)
                        video = "path@1@"
                        if video in datastring:
                            list = datastring.split(sep="@", maxsplit=8)
                            resolution = list[4].split(',')
                            resolution = 'x'.join(resolution)
                            show = f" Video with {list[0]} id, '{list[1]}' title, {resolution} pixel resolution, {list[7]} duration, {list[4]}$ price and {list[3]}MB size."
                            print(show)
                    print("\n")

    def selectAlbum():
        mydb = DatabaseActions.connect()
        cursor= mydb.cursor()
        query = f"SELECT * FROM `album`"
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('There is no record found')
        else: 
            for row in rows:
                datastring = '@'.join(map(str, row))
                # print(datastring)
                list = datastring.split(sep="@")
                show = f"Album with {list[0]} id, '{list[1]}' name, {list[3]} category and '{list[2]}' description."
                print(show)
                print(" Includes:")
                query2=f"SELECT * FROM music INNER JOIN musicalbum ON music.musicId=musicalbum.musicId and musicalbum.albumId = {list[0]}"
                cursor.execute(query2)
                rows = cursor.fetchall()
                if len(rows) == 0:
                    print('There is no record found')
                else: 
                    for row in rows:
                        datastring = '@'.join(map(str, row))
                        # print(datastring)
                        list = datastring.split(sep="@")
                        show = f" Music with {list[0]} id, '{list[3]}' name, in {list[1]} category and {list[2]} minutes duration."
                        print(show)
                print("\n")
    
                

    def search_by_name():
        print("Type a name of the item you want to find...")
        name = input()
        mydb = DatabaseActions.connect()
        cursor= mydb.cursor()
        query = f'SELECT name FROM media WHERE name LIKE "%{name}%" UNION SELECT name FROM collection WHERE name LIKE "%{name}%" UNION SELECT name FROM music WHERE name LIKE "%{name}%" UNION SELECT name FROM album WHERE name LIKE "%{name}%"'
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('There is no record found')
        else: 
            for row in rows:
                for name in row:
                    print(name)
        print("\nDo you want to search in folder? Y/n")
        advanced = input()
        if advanced == "Y" or advanced == 'y':
            DatabaseActions.searchByNameinTable()
        else:
            print("Exit")

    def showTable():
        print("Please choose folder")
        print("1 - Media")
        print("2 - Music") 
        print("3 - Album") 
        print("4 - Collection")
        
    def searchByNameinTable():
        DatabaseActions.showTable()
        print("Type a name of the item you want to find...")
        name = input()
        mydb = DatabaseActions.connect()
        cursor= mydb.cursor()
        table = input()
        if table == "1":
            print("Searching in media List")
            query = f"SELECT * FROM `media` WHERE name LIKE '%{name}%'"
        elif name =="2":
            print("Searching in music List")
            query = f"SELECT * FROM `music` WHERE name LIKE '%{name}%'"
        elif name =="3":
            print("Searching in Album List")
            query = f"SELECT * FROM `album` WHERE name LIKE '%{name}%'"
        elif name =="4":
            print("Searching in Collection List")
            query = f"SELECT * FROM `collection` WHERE name LIKE '%{name}%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('There is no record found')
        else: 
            for row in rows:
                print(row)
        

    def update(query):
      mydb = DatabaseActions.connect()
      cursor= mydb.cursor()
      try:
        cursor.execute(query)
        mydb.commit()
        rowcount = cursor.rowcount
        print(f"There were {rowcount} record changes")
      except:
        mydb.rollback()
        print("There were no changes")
       

    def delete(table, name):
      mydb = DatabaseActions.connect()
      cursor= mydb.cursor()
      query = f"DELETE FROM {table} WHERE name LIKE '%{name}%'"
      cursor.execute(query)
      print(cursor.rowcount, "record(s) deleted")
      mydb.commit()
