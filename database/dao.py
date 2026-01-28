from database.DB_connect import DBConnect

class DAO:
    def __init__(self):
        pass

    def read_album_by_durata(self,durata):
        cnx=DBConnect.get_connection()
        results=[]
        if not cnx:
            print("Errore di connessione")
            return []
        cursor=cnx.cursor(dictionary=True)
        query="""SELECT DISTINCT a.id,a.title,SUM(t.milliseconds)/60000 AS durata
         FROM album a,track t WHERE t.album_id=a.id 
         GROUP BY a.id,a.title 
         HAVING SUM(t.milliseconds)/60000>%s"""
        try:
            cursor.execute(query,(durata,))
            rows=cursor.fetchall()
            for row in rows:
                results.append(row)
        except Exception as e:
            print(f"Errore nell'esecuzione della query: {e}")
        finally:
            cursor.close()
            cnx.close()
        return results

    def read_albums(self):
        cnx=DBConnect.get_connection()
        results=[]
        if not cnx:
            print("Errore di connessione")
            return []
        cursor=cnx.cursor(dictionary=True)
        query="""SELECT DISTINCT t1.album_id AS id1,t2.album_id AS id2 FROM track t1,track t2,playlist_track pt1,playlist_track pt2 
        WHERE t1.album_id<t2.album_id AND pt1.playlist_id=pt2.playlist_id AND t1.id=pt1.track_id AND 
        t2.id=pt2.track_id;"""
        try:
            cursor.execute(query)
            rows=cursor.fetchall()
            for row in rows:
                results.append(row)
        except Exception as e:
            print(f"Errore nell'esecuzione della query: {e}")
        finally:
            cursor.close()
            cnx.close()
        return results






