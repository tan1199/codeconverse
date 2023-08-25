
import sqlite3




def insert_message(message_id, chat_id, avatar, username, message_content, timestamp):      
    print("ppppppppp")  
    try:
        conn = sqlite3.connect('chats.db')
        cursor = conn.cursor()
        create_table_query = '''
CREATE TABLE IF NOT EXISTS chistory (
    id INTEGER ,
    chat_id INTEGER,
    avatar TEXT,
    username TEXT,
    message TEXT,
    timestamp INTEGER
)
'''

        cursor.execute(create_table_query)
        insert_query = '''
        INSERT INTO chistory (id, chat_id, avatar, username, message, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        # print(message_id, chat_id, avatar, username, message_content, timestamp)
        cursor.execute(insert_query, (message_id, chat_id, avatar, username, message_content, timestamp))
        print("klklkl")
        conn.commit()    
    except sqlite3.Error as e:
        print("SQLite error:", e)
        conn.rollback()  # Roll back the transaction in case of an error
    finally:
        conn.close()

def select_all_chats():
    print("sss") 
    conversation_data = []
 
    try:
        conn = sqlite3.connect('chats.db')
        cursor = conn.cursor()
        # de = 'delete FROM chistory where 1=1'
        sel = 'select * FROM chistory'

        # cursor.execute(de)
        # conn.commit() 
        cursor.execute(sel)

        result = cursor.fetchall()

        for row in result:
            message = {
                'id': row[0],           # Assuming id is in the second column
                'avatar': row[2],       # Assuming avatar is in the third column
                'username': row[3],     # Assuming username is in the fourth column
                'message': row[4],      # Assuming message is in the fifth column
                'timestamp': row[5]     # Assuming timestamp is in the sixth column
            }
            # print("ytyt",row[4])
            chat_exists = False
            for chat in conversation_data:
                if chat['chatId'] == row[1]:  # Assuming chatId is in the seventh column
                    chat['messages'].append(message)
                    chat_exists = True
                    break
    
            if not chat_exists:
                conversation_data.append({
                    'chatId': row[1],       # Assuming chatId is in the seventh column
                    'messages': [message]
                 })
    except sqlite3.Error as e:
        print("SQLite error:", e)
        conn.rollback()  # Roll back the transaction in case of an error
    finally:
        conn.close()
    return conversation_data




def deletechatId(chatId):
    print("del") 
    try:
        conn = sqlite3.connect('chats.db')
        cursor = conn.cursor()
        strchatid=str(chatId)
        delete_query = 'delete from chistory  where chat_id is NULL or chat_id =?'
        cursor.execute(delete_query, (strchatid,))
        conn.commit() 
    except sqlite3.Error as e:
        print("SQLite error:", e)
        conn.rollback()  # Roll back the transaction in case of an error
    finally:
        conn.close()

