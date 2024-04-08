from database.postgre import postgreConnection

def insert_t(data):
    query = """
        INSERT INTO
            aiinstagram_t_comments
            (id_instagram, comments, sentiment_ai, insert_date, threshold)
        VALUES
            (%s, %s, %s, %s, %s)
    """
    print(query)
    SECTION = 'local'
    postgrecon = postgreConnection(SECTION)
    connection = postgrecon.connection
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()
    cursor.close()
    connection.close()
    
    
if __name__ == "__main__":
    from datetime import datetime
    
    insert_t(['test', 'test', datetime.now(), 0.5])