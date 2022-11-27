
Design : https://drive.google.com/file/d/1MbZh5hT5hjadOlLS3zNTZzy6tnzpEVFE/view?usp=sharing
```
A ticket booking system provides its customers the ability to purchase tickets online

BookMyShow

1. Functional Requirment
    - List cities where affilted cinema are located
    - Once user select the city, list all movies released in particular city
    - Once user select the movie, the service should show threater running 
      that movie and availble show-times
    - User should able to choose particular (cinema,movie,show-time) and book ticket
    - User should able to distinguish btw booked and available seat
    - User can put seat on hold for 5 minutes before making payment
    - User should able to wait if chance of seat becoming availble
    - Waiting custmer should be served in FIFO order
    
2. Non-Functional Requirement
    - The system should be highly concurrent, There will be multiple booking request for same seat
    - Ticket booking should be transactional and ACID compliant

3. Capacity Estimation
    Assumption
        - Service doesn't require any authentication
        - System will not handle partial booking
        - Restrict to book 10 seats at a time
        - High available and scalable
        
    Assume 500 millions page-view request and 1 millions tickets books per day
    Traffic estimation(Read QPS, Write QPS)

        -Read queries estimation
            500 x 10^6
            ---------- = 5000 request/sec
              86400

        -Write queries estimation
            1 x 10^6
            -------- = 10 request/sec
              86400

    Storage estimation(Persistence storage)
        Assume cinemas and seats details of movie including thumbnail is 100KB
        Assumptions
            -Number of cities = 500
            -Number of cinemas in cities = 10
            -Number of seats in cinemas = 1000
            -Number of shows in cinemas = 4

        Total number of cities = 500 x 10 x 1000 x 4 x 100 KB = 2 x 10^9 x 10^3 B = 2TB per day 
        Storage estimation for year = 2TB  x 365  = 730 TB 
        
4. Architecture deep-dive
        API:
            searchMovie(city, keyword, lat, long, radius, start_time, endTime, pincode)
            reserveCity(sessionId, movieId, show_id, seatsToResearve[])
            
        Database Schema
            Each City have mutiple cinema
            Each cinema have mutiple screen
            Each screen have mutipl show
            
            User(userId, name, email, phone)
            City(id, name, state,  pincode)
            Cinema(id, name, totalScreen, cityId)
            Screen(screenId, name, totalSeat, cinemaId)
            Seat(seatId, screenId, name)
            Movie(movieId, name, duration, language, releaseDate, country etc)
            Show(showId, date, startTime, endTime, cinema, movieId)
            ShowSeat(showSeatId, showId, seatId, status(enum), bookingId)
            Booking(bookindId, numberOfSeat, timeStamp,status, userId, showId)
            Payment(paymentId, bookingId, amount, timstamp, transactionId)
        
        Caching
        
        Database Sharding
            -movieId (hot-box problem)
            -showId (load get distributed among different server)
        
        Component Design
            - UserService
            - ReservationService
            - ShowService
            - NotificationService(Email, SMS)
            - Mysql(booking, payment etc)
            - NoSql(reviews, comments, rating etc.)
            - Caching
            - Master-Slave
            - CDN(store movie trailer and photos)
            
        How to solve concurrency issue
            If two server instance receive requset to book same seat,
            Here first request will take a lock at row in database and perform opertion till expiry
            If ticket booked by request-1, then request-2 will be informed with error-message otherwise
            seat will be available for second request-2 to book
            
            SET TRANSACTION ISOLATION LEVEL SERIALIZABLE
        
        Keeping Track of Active Reservation that not booked yet
            Will store active-reservation in in-memory data-structure along with database
            LinkHashMap : key = showId and value = {bookingId, creationTimeStamp}
            - As soon as booking is completed with payment, change status=Booked and remove entry from linkedHashMap
            - When reservation is expired, change status=expired and remove entry from linkedHashMap
            
```