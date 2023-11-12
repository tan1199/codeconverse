
import sqlite3

def insert_user(user_name, password, email_id , apikey, timestamp):
    insert_status="user_registered"
    try:
        conn = sqlite3.connect('user_credentials.db')
        cursor = conn.cursor()
        create_table_query = '''
CREATE TABLE IF NOT EXISTS user_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
        apikey TEXT,
        timestamp INTEGER
)
'''

        cursor.execute(create_table_query)
        insert_query = '''
        INSERT INTO user_info (username, password, email, apikey, timestamp)
        VALUES (?, ?, ?, ?, ?)
        '''
        # print(message_id, chat_id, avatar, username, message_content, timestamp)
        cursor.execute(insert_query, (user_name, password, email_id, apikey, timestamp))
        print("klklkl")
        conn.commit()    
    except sqlite3.Error as e:
        print("SQLite error:", e)
        insert_status=e.sqlite_errorname
        conn.rollback()  # Roll back the transaction in case of an error
    finally:
        conn.close()
    return insert_status

def select_user(username):
    message=None
    try:
        conn = sqlite3.connect('user_credentials.db')
        cursor = conn.cursor()
        # de = 'delete FROM chistory where 1=1'
        select_query = 'select * from user_info  where username=?'
        cursor.execute(select_query, (username,))
        result = cursor.fetchall()

        for row in result:
            message = {
                'id': row[0],        
                'username': row[1],     
                'password': row[2],    
                'email_id': row[3],    
                'apikey': row[4],
                'timestamp': row[5]
            }


    except sqlite3.Error as e:
        print("SQLite error:", e)
        conn.rollback()  # Roll back the transaction in case of an error
    finally:
        conn.close()
    return message

def insert_message(message_id, chat_id, avatar, username, message_content,num_token, timestamp,user_id):      
    print("ppppppppp")  
    try:
        conn = sqlite3.connect('chats.db')
        cursor = conn.cursor()
        create_table_query = '''
CREATE TABLE IF NOT EXISTS chathistory (
    id INTEGER ,
    chat_id INTEGER,
    avatar TEXT,
    username TEXT,
    message TEXT,
    num_token INTEGER,
    timestamp INTEGER,
    user_id TEXT
)
'''

        cursor.execute(create_table_query)
        insert_query = '''
        INSERT INTO chathistory (id, chat_id, avatar, username, message,num_token, timestamp,user_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        # print(message_id, chat_id, avatar, username, message_content, timestamp)
        cursor.execute(insert_query, (message_id, chat_id, avatar,
                       username, message_content,num_token, timestamp, user_id))
        print("klklkl")
        conn.commit()    
    except sqlite3.Error as e:
        print("SQLite error:", e)
        conn.rollback()  # Roll back the transaction in case of an error
    finally:
        conn.close()


def select_all_chats(user_id):
    print("sss") 
    conversation_data = []
 
    try:
        conn = sqlite3.connect('chats.db')
        cursor = conn.cursor()
        # de = 'delete FROM chistory where 1=1'
        sel = 'select * FROM chathistory where user_id=?'

        # cursor.execute(de)
        # conn.commit() 
        cursor.execute(sel, (user_id,))

        result = cursor.fetchall()

        for row in result:
            message = {
                'id': row[0],           # Assuming id is in the second column
                'avatar': row[2],       # Assuming avatar is in the third column
                'username': row[3],     # Assuming username is in the fourth column
                'message': row[4],      # Assuming message is in the fifth column
                'usage': row[5],
                'timestamp': row[6]     # Assuming timestamp is in the sixth column
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


def usage_for_user(user_id): 
    try:
        conn = sqlite3.connect('chats.db')
        cursor = conn.cursor()
        # de = 'delete FROM chistory where 1=1'
        sel = 'select * FROM chathistory where user_id=?'
        sel = 'SELECT  SUM(num_token) AS total_tokens FROM chathistory  where user_id=? GROUP BY user_id'
        cursor.execute(sel, (user_id,))

        usage = cursor.fetchone()
        print("uususu",usage)
        # return usage[0]
    except sqlite3.Error as e:
        print("SQLite error:", e)
        conn.rollback()  # Roll back the transaction in case of an error
    finally:
        conn.close()
        if usage is not None:
            return usage[0]
        return 0

def deletechatId(chatId, user_id):
    print("del") 
    try:
        conn = sqlite3.connect('chats.db')
        cursor = conn.cursor()
        strchatid=str(chatId)
        delete_query = 'delete from chathistory  where user_id = ? and (chat_id is NULL or chat_id = ?)'
        cursor.execute(delete_query, (user_id,strchatid,))
        conn.commit() 
    except sqlite3.Error as e:
        print("SQLite error:", e)
        conn.rollback()  # Roll back the transaction in case of an error
    finally:
        conn.close()

def update_api_key(api_key,user_id):
    try:
        print("klklkl", api_key, user_id)
        conn = sqlite3.connect('user_credentials.db')
        cursor = conn.cursor()

        update_query = '''
        UPDATE user_info SET apikey = ? WHERE username = ?
        '''
        # print(message_id, chat_id, avatar, username, message_content, timestamp)
        update_status = cursor.execute(update_query, (api_key, user_id))
        
        conn.commit()    
    except sqlite3.Error as e:
        print("SQLite error:", e)
        update_status=e.sqlite_errorname
        conn.rollback()  # Roll back the transaction in case of an error
    finally:
        conn.close()
    return update_status
