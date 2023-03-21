from pydoc import describe
import mysql.connector
from datetime import date
from portfolio_database import DatabaseActions



class Media:

    def searchByName(name):
          mydb = DatabaseActions.connect()
          cursor= mydb.cursor()
          query = f"SELECT * FROM `media` WHERE name LIKE '%{name}%'"
          cursor.execute(query)
          rows = cursor.fetchall()
          if len(rows) == 0:
              print('There is no record found')
          else: 
              for row in rows:
                  print(row)


    def addMedia(duration = ''):
        mydb = DatabaseActions.connect()
        cursor = mydb.cursor()
        name = input("Insert media title:")
        filesize = input("Insert filesize (only number):")
        price = int(input("Insert price (USD):"))
        resolution = (input("Insert media height and width (example 1500,4000):"))
        path = (input("Insert image path:"))
        is_video = (input("Is media video or photo? Insert p or v:"))
        if is_video == "p":
            is_video = 0
            print(is_video)
        if is_video == 'v':
            is_video = 1
            duration = (input("Insert video duration:"))
        query = f"INSERT INTO `media` (`mediaId`, `name`, `fileSize`, `mediaPrice`, `resolution`, `path`, `is_video`, `video_duration`) \
            VALUES (NULL, '{name}', '{filesize}', '{price}', '{resolution}', '{path}', '{is_video}', '{duration}');"
        cursor.execute(query)
        mydb.commit()
        print(cursor.rowcount, "record inserted.")

    def delete_media(mediaName):
        DatabaseActions.delete('media', mediaName)


class Collection:

    def createCollection():
        mydb = DatabaseActions.connect()
        cursor = mydb.cursor()
        name = input("Insert collection name:")
        price = int(input("Insert price (USD):"))
        description = (input("Insert collection description:"))
        query = f"INSERT INTO `collection` (`collectionId`, `name`, `collectionPrice`, `description`) \
            VALUES (NULL, '{name}', '{price}', '{description}');"
        cursor.execute(query)
        mydb.commit()
        print(cursor.rowcount, "record inserted.")

    def deleteCollection(collName):
        DatabaseActions.delete('media', collName)


    def addMedia():
        mydb = DatabaseActions.connect()
        cursor = mydb.cursor()
        created_date = date.today()
        cursor.execute("SELECT collectionId, name FROM `collection`")
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('There is no record found')
        else: 
            for row in rows:
                print(row)
        collectionId = input("Insert id of the collection you want to add media:")
        cursor.execute("SELECT mediaId, name FROM `media`")
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('There is no record found')
        else: 
            for row in rows:
                print(row)
        mediaId = input("Select media id:")

        # mediaName = cursor.execute(f"SELECT name FROM `media` where mediaId = '{int(mediaId)}'")
        # collectionName = cursor.execute(f"SELECT * FROM `collection` WHERE `collectionId` = '{collectionId}'")
        
        query = f"INSERT INTO `mediacollection` (`date`, `collectionId`, `mediaId`) VALUES ('{created_date}', '{collectionId}', '{mediaId}');"
        cursor.execute(query)
        mydb.commit()
        print("Selected media added to the collection")


    def searchByName(name):
        mydb = DatabaseActions.connect()
        cursor= mydb.cursor()
        query = f"SELECT * FROM `collection` WHERE name LIKE '%{name}%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('There is no record found')
        else: 
            for row in rows:
                print(row)
    

class Music:

    def addMusic():
        mydb = DatabaseActions.connect()
        cursor = mydb.cursor()
        category = input("Insert music category:")
        duration = input("Insert duration:")
        path = (input("Insert music path:"))
        name = (input("Insert music name:"))
        query = f"INSERT INTO `music` (`musicId`, `category`, `duration`, `name`, `path`) VALUES (NULL, '{category}', '{duration}', '{name}', '{path}');"
        cursor.execute(query)
        mydb.commit()
        print(cursor.rowcount, "record inserted.")

    def delete_music(musicName):
        DatabaseActions.delete('music', musicName)
    
    def searchByName(name):
        mydb = DatabaseActions.connect()
        cursor= mydb.cursor()
        query = f"SELECT * FROM `music` WHERE name LIKE '%{name}%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('There is no record found')
        else: 
            for row in rows:
                print(row)

class Album:
    
    def createAlbum(self):
        mydb = DatabaseActions.connect()
        cursor = mydb.cursor()
        category = input("Insert album category:")
        name = (input("Insert album name:"))
        description = (input("Insert album description:"))
        query = f"INSERT INTO `album` (`albumId`, `name`, `description`, `category`) VALUES (NULL, '{name}', '{description}', '{category}');"
        cursor.execute(query)
        mydb.commit()
        print(cursor.rowcount, "record inserted.")

    def addMusic():
        mydb = DatabaseActions.connect()
        cursor = mydb.cursor()
        created_date = date.today()
        cursor.execute("SELECT albumId, name FROM `album`")
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('There is no record found')
        else: 
            for row in rows:
                print(row)
        albumId = input("Insert id of the album you want to add music:")
        cursor.execute("SELECT musicId, name FROM `music`")
        rows = cursor.fetchall() 
        if len(rows) == 0:
            print('There is no record found')
        else:
            for row in rows:
                print(row)
        musicId = input("Select music id:")

        # mediaName = cursor.execute(f"SELECT name FROM `media` where mediaId = '{int(mediaId)}'")
        # collectionName = cursor.execute(f"SELECT * FROM `collection` WHERE `collectionId` = '{collectionId}'")
        
        query = f"INSERT INTO `musicalbum` (`date`, `albumId`, `musicId`) VALUES ('{created_date}', '{albumId}', '{musicId}');"
        cursor.execute(query)
        mydb.commit()
        print("Selected music added to the album")

    
    def searchByName(name):
        mydb = DatabaseActions.connect()
        cursor= mydb.cursor()
        query = f"SELECT * FROM `album` WHERE name LIKE '%{name}%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) == 0:
            print('There is no record found')
        else: 
            for row in rows:
                print(row)


class Download:

    def cancelDownload(self):
        print(f"{self.mediaIdD.mediaId} media downloading was cancelled")


class Payment:

    def proceedPurchase(self):
         print(f'Purchase for {self.downloadId} proceeded!')

    def sendEmail(self):
         print(f'An email was sent to {self.email.customerEmail} for {self.id.mediaId} download purchase!')


    def cancelPayment(self):
        print(f"Payment for {self.id.downloadId} doownload was cancelled")



class Input:
  def showMenu():
    print("Please choose list item")
    print("1 - List")
    print("2 - Search")
    print("3 - Insert")
    print("q - Exit")

  def inputMenu():
    menu_command = input()
    if menu_command == "1":
      print("List")
      Database.showTable()
    elif menu_command == "2":
      print("Search")
      DatabaseActions.search_by_name()
    elif menu_command == "3":
      print("Insert")
      Database.Insert()
    else:
        print("Exit")

class Database:
    def showTable():
        print("Please choose folder")
        print("1 - Media")
        print("2 - Music") 
        print("3 - Album") 
        print("4 - Collection")
    
    def showActions():
        print("Please select what you want to add,")
        print("1 - media")
        print("2 - music") 
        print("3 - album") 
        print("4 - collection")
        print("5 - media to collection")
        print("6 - music to album")

    def selectTable():
        table = input()
        if table == "1":
            print("Showing Media List")
            Database.showList("1")
        elif table =="2":
            print("Showing Music List")
            Database.showList("2")
        elif table =="3":
            print("Showing Album List")
            Database.showList("3")
        elif table =="4":
            print("Showing Collection List")
            Database.showList("4")
    
    def showList(list_number):
        if list_number=="1":
            DatabaseActions.selectMedia()
        elif list_number=="2":
            DatabaseActions.selectMusic()
        elif list_number=="3":
            DatabaseActions.selectAlbum()
        elif list_number=="4":
            DatabaseActions.selectCollection()

    def Insert():
        Database.showActions()
        action = input()
        if action == '1':
            Media.addMedia()
        elif action == '2':
            Music.addMusic()
        elif action == '3':
            Album.createAlbum()
        elif action == '4':
            Collection.createCollection()
        elif action == '5':
            Collection.addMedia()
        elif action == '6':
            Album.addMusic()
        else:
            pass

    


Input.showMenu()
Input.inputMenu()
Database.selectTable()
