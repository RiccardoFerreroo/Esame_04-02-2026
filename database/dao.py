from database.DB_connect import DBConnect
from model.artist import Artist


class DAO:

    @staticmethod
    def get_authorship():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ SELECT * 
                    FROM authorship"""
        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_ruoli():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """ select distinct a.role as role
                    from authorship a """
        cursor.execute(query)
        result =[row['role'] for row in cursor]

       # print(result)
        return result

    @staticmethod
    def get_artists(role):
        conn = DBConnect.get_connection()
        artists = []
        print(role)
        role = str(role)
        print(role)
        cursor = conn.cursor(dictionary=True)
        query = """select distinct ap.artist_id, ar.name
                    from artists ar, authorship ap, objects o
                    where ap.artist_id = ar.artist_id and ap.role= %s"""
        print("siamo qui")

        cursor.execute(query, (role,))
        print("ggggg")
        artists = [Artist(row["artist_id"], row["name"],0) for row in cursor] # artist_id, name, num_objects=0


        cursor.close()
        conn.close()
        return artists


    #def productivity_calcola(ar_id):
    #conn = DBConnect.get_connection()
    #cursor = conn.cursor(dictionary=True)
    #
    #query = """select count(o.object_id) as productivity
    #from artists ar, authorship ap, objects o
    #where ap.artist_id = 972 and ap.artist_id = ar.artist_id and ap.role = 'Designer' and ap.object_id = o.object_id and o.curator_approved = 1
    #group by ap.artist_id, ar.name, ap.role"""
    #cursor.execute(query, (ar_id,))
    #for row in cursor:
    #    result.row['productivity] #essendo per un artistar_id da un solo result
    #select distinct ap.artist_id, ar.name, ap.role, count(o.object_id) as productivity
#####from artists ar, authorship ap, objects o
#####where ap.artist_id = ar.artist_id and ap.role='Designer' and ap.object_id = o.object_id and o.curator_approved = 1
#####group by  ap.artist_id, ar.name, ap.role
