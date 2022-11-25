
Design: https://drive.google.com/file/d/1FPdKJ8htTCgIPCm9Wj-CzMNHgKmA-Vyw/view?usp=sharing
```
1. Functional Requirement
    - One to one user conversation
    - Group Chat
    - User Online/Offline
    - Message sent, delivered and received status
    - Last seen
    - Persistent storage Chat history 
    - Encryption

2. Non-functional requirement
    - User should have real time chat experience with minimum latency
    - Highly consistent(Same chat history on all devices)
    - Highly available
    - Dedicated and persistent connection
    - BiDuplex connection (user can send and receive message over same data-channel)

3. Capacity Estimation
    Assumption
        Daily active user: 500 Million
        Each user sent, on average 10 message send per day
        Total message send per day => 10 x 500 x 10^6 => 5 x 10^9 (5 billion)
        Size of each message = 1 kb

    Storage Estimation
        500 x 10^9(messages per day) x 1 kb(message size) => 5TB per/day
        5 TB per/day  * 30(days in month) * 12(month in year) => 1800 TB/year
        For 10 years
            1800 Tb/year x  10 =>  18000 TB  => 18 PB

    Bandwidth Required
         Read and Write QPS
            5 TB per/day
         -----------------    => 57 mbps
         86400(SecondsInDay)
         
4. Architectural Deep-dive
    API : 
        - uploadPhoto(userId, photo)
        - registerUser(userId, name, phone, dob, otp-verified = False, createdAt)
        - sendMessage(messageId, sourceUserId, destinationUserId, data, media)
        - getMessages(userId)
        - lastSeen(userId)
        - userStatus(userId)
        
    Schema:
        - User(userId, name, phone, dob, otp-verified, createdAt)
        - Message(messageId, senderUserId, destinationUserId, data, media-path)
        - UserPidInfo(userId, serverIpaddress, pid)
        - MediaMetadata(uuid, s3bucket-path, title, createdAt)
        - Group(groupId, listOfusers = [])
    
    Database Sharding:
        - userId (hot box problem) but better in case for fetching message history of user
        - groupId(for group messaging)
        - messageId(solve hot box problem) but aggregation of result increases latency of result
        
    Component Desing:
        - Messaging service 
        - Media service
        - S3 storage
        - Application Load Balancer
        - MySQL (metadata store)
        - BigTable (Message store)
        
    Messaging Service
        1. Using HTTP Protocol and Rest API: Pull Method
           Issue with approach
           - For each request connection will be established with server, that is big overhead
           - Receiver have to keep asking to server for new messages at regular interval,
             Some times resources get waste, when there is no messages
        
        2. Web Socket Connection Protocol: Push Method
            In this second approach, where all the active users keep a connection open with the server, 
            then as soon as the server receives a message it can immediately pass the message to the intended user. 
            This way, the server does not need to keep track of the pending messages, and we will have minimum 
            latency, as the messages are delivered instantly on the opened connection.
           
           Who will keep track of open connection?
               Redis Cache to keep track of open connections
               [ConnectionObject | PID | UserId]
               [10.78.45.90      | 899 | userA ]
               [10.13.45.33      | 767 | userB ]
           
           How Many Messasing server needed?
               Modern server can handle 10K web-socket connection
               500 x 10^9 user at any given time
                                            500 x 10^6
               No. of sever required =>  ---------------  = 5 K server
                                            100 x 10^3
                                            
           How to maintain order of message send?     
               We need to keep a sequeence number with each message for client, 
               This sequence number  will determine  extact ordering
               
           Storing Messages in database? 
               - Server will send an asynchronous request to the database to store the message
               - We need to have a database that can support a very high rate of small updates and 
                 also fetch a range of records quickly
               - We cannot use RDBMS like MySQL or NoSQL like MongoDB because we cannot afford to read/write 
                 a row from the database every time a user receives/sends a message. Both of our requirements 
                 can be easily met with a wide-column database
                    {userId : messageColumnWise}
                    
           Ack Mechanism (Message(sent, receive,  delivered))
               {
                  "messageId" : "uixqen89JJhd",
                  "text": "ACK",
                  "type": 1
                }
              
                {
                  "type" : {
                    1:"SENT",
                    2: "RECEIVED",
                    3: "DELIVERED"
                  }
                }
                
           Ack (LastSeen, Online)
               Server will send heart-beat probe at regular interval to check client status 
               and maintain in db-record
               [userId | last_seen_time_stamp]
               [userA  | 699986899]
               [userB  | 699986786]
               
        3. Http-Media service
           Media exchange will be through Http resp-api (Upload the media on s3bucket_storage and generate path)
           Now, generated path share as a message with thumbnail.
           
           UserA send photo/gif to userB. UserA first call media-service and upload the data to s3-object-store
           and also save respective meta-data to databse and return { id, s3Url} to  userA
   
           MediaMetadata(uuid, s3bucket-path, title, createdAt)
   
           Now userA will send metadata of photo userB instead of actual media-file
           {srcUserId, destUserId, s3Url, type[Media]}
           Once userB received packet can download media-file from url
          
```






