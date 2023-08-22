import sqlite3
# # Connect to the database (a new database file named 'conversation.db' will be created if it doesn't exist)
conn = sqlite3.connect('conversation1.db')

# # Create a cursor object to interact with the database
cursor = conn.cursor()
# # Define the schema for the messages table
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS messages (
#     id INTEGER PRIMARY KEY,
#     chat_id TEXT,
#     avatar TEXT,
#     username TEXT,
#     message TEXT,
#     timestamp INTEGER
# )
# '''

# # Execute the query to create the table
# cursor.execute(create_table_query)






conversation_data1 = [{'chatId': '1692436170698', 'messages': [{'id': 1692436175759, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'hello', 'timestamp': 1692436175759}, {'id': 1692436181744, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': 'Hello! How can I assist you today?', 'timestamp': 1692436181744}, {'id': 1692436191162, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'how are you', 'timestamp': 1692436191162}, {'id': 1692436198048, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': "As an AI, I don't have feelings, but I'm here to help you with any questions or tasks you have. How can I assist you today?", 'timestamp': 1692436198048}, {'id': 1692436211157, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'what is the capital of denmark', 'timestamp': 1692436211157}, {'id': 1692436216969, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': 'The capital of Denmark is Copenhagen.', 'timestamp': 1692436216969}, {'id': 1692436225940, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'best cricker of world', 'timestamp': 1692436225940}, {'id': 1692436233668, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': 'There have been many great cricketers throughout history, and it is subjective to determine the best cricketer of all time. However, some of the most highly regarded cricketers include Sir Donald Bradman, Sachin Tendulkar, Sir Vivian Richards, Sir Garfield Sobers, and Sir Jack Hobbs. These players have achieved remarkable records and have left a lasting impact on the game of cricket.', 'timestamp': 1692436233668}]}, {'chatId': '1692436239709', 'messages': []}, {'chatId': '1692436243005', 'messages': [{'id': 1692436251519, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'some icream flovors', 'timestamp': 1692436251519}, {'id': 1692436259952, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': '1. Vanilla\n2. Chocolate\n3. Strawberry\n4. Mint chocolate chip\n5. Cookies and cream\n6. Butter pecan\n7. Rocky road\n8. Coffee\n9. Pistachio\n10. Salted caramel\n11. Neapolitan\n12. Cherry Garcia (cherry ice cream with chocolate chunks and cherries)\n13. Peanut butter cup\n14. Coconut\n15. Birthday cake\n16. Matcha green tea\n17. Black raspberry\n18. Dulce de leche\n19. Red velvet\n20. Lemon sorbet', 'timestamp': 1692436259952}, {'id': 1692436267399, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'different color of apple', 'timestamp': 1692436267399}, {'id': 1692436279132, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': 'There are several different colors of apples, including:\n\n1. Red: This is the most common color for apples, with varieties such as Red Delicious, Gala, and Fuji.\n\n2. Green: Green apples, such as Granny Smith and Golden Delicious, have a tart flavor and are often used in baking or for making apple cider.\n\n3. Yellow: Yellow apples, like Yellow Transparent and Yellow Newtown Pippin, have a sweet and tangy taste.\n\n4. Pink: Pink Lady apples have a distinctive pinkish-red skin and a crisp, sweet-tart flavor.\n\n5. Bi-colored: Some apples have a combination of colors, such as the popular Honeycrisp apple, which has a red and yellow skin.\n\n6. Striped: Certain apple varieties, like the McIntosh apple, have a striped pattern on their skin, with a mix of red and green.\n\n7. Purple: There are a few varieties of purple apples, such as the Black Diamond apple, which have a deep purple or almost black skin.\n\nThese are just a few examples of the different colors of apples available. The specific color and appearance of an apple can vary depending on the variety and ripeness.', 'timestamp': 1692436279132}, {'id': 1692436280326, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'japan to india distance', 'timestamp': 1692436280326}, {'id': 1692436286987, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': 'The distance between Japan and India is approximately 4,500 kilometers (2,800 miles) when measured in a straight line. However, the actual distance may vary depending on the route taken for travel.', 'timestamp': 1692436286987}, {'id': 1692436288296, 'avatar': 'https://example.com/avatar.png', 'username': 'User', 'message': 'bye bye', 'timestamp': 1692436288296}, {'id': 1692436294137, 'avatar': 'https://example.com/avatar.png', 'username': 'AI Assistant', 'message': 'Goodbye! Have a great day!', 'timestamp': 1692436294137}]}]


# for chat in conversation_data:
#     chat_id = chat['chatId']
#     messages = chat['messages']
    
#     for message in messages:
#         message_id = message['id']
#         avatar = message['avatar']
#         username = message['username']
#         message_content = message['message']
#         timestamp = message['timestamp']
        

def insert_query(cursor,message_id, chat_id, avatar, username, message_content, timestamp):      
    print("ppppppppp")  
    # global cursor
    insert_query = '''
    INSERT INTO messagesh (id, chat_id, avatar, username, message, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
    print(message_id, chat_id, avatar, username, message_content, timestamp)
    cursor.execute(insert_query, (message_id, chat_id, avatar, username, message_content, timestamp))
# # Commit the changes to the database
    conn.commit()
# insert_query(86207,"sdi","io","lp","yt",869)
select_query = 'SELECT * FROM messages'

cursor.execute(select_query)
result = cursor.fetchall()

for row in result:
    print(row)
cursor.close()
conn.close()

# Convert retrieved data into the original structure

conversation_data = []

for row in result:
    message = {
        'id': row[0],           # Assuming id is in the second column
        'avatar': row[2],       # Assuming avatar is in the third column
        'username': row[3],     # Assuming username is in the fourth column
        'message': row[4],      # Assuming message is in the fifth column
        'timestamp': row[5]     # Assuming timestamp is in the sixth column
    }
    print("ytyt",row[4])
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
print("ioioioio")
# Print the reconstructed conversation data
print(conversation_data)
print("fvfvf")
print(conversation_data1)

if conversation_data1==conversation_data:
    print("acha")