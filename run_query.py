import sqlite3

# Connect to database
conn = sqlite3.connect("ola_database.db")

# Create cursor
cursor = conn.cursor()

# 1️⃣ Retrieve all successful bookings
cursor.execute("""
SELECT *
FROM ola_rides
WHERE Booking_Status='Success'
LIMIT 5
""")
print("\nSuccessful Bookings (Sample):")
for row in cursor.fetchall():
    print(row)

# 2️⃣ Average ride distance for each vehicle type
cursor.execute("""
SELECT Vehicle_Type, AVG(Ride_Distance)
FROM ola_rides
GROUP BY Vehicle_Type
""")
print("\nAverage Ride Distance by Vehicle Type:")
for row in cursor.fetchall():
    print(row)

# 3️⃣ Total number of cancelled rides by customers
cursor.execute("""
SELECT COUNT(*)
FROM ola_rides
WHERE Booking_Status='Canceled by Customer'
""")
print("\nCancelled Rides by Customers:", cursor.fetchone()[0])

# 4️⃣ Top 5 customers who booked highest rides
cursor.execute("""
SELECT Customer_ID, COUNT(*) AS total_rides
FROM ola_rides
GROUP BY Customer_ID
ORDER BY total_rides DESC
LIMIT 5
""")
print("\nTop 5 Customers by Number of Rides:")
for row in cursor.fetchall():
    print(row)

# 5️⃣ Rides cancelled by drivers
cursor.execute("""
SELECT COUNT(*)
FROM ola_rides
WHERE Booking_Status='Canceled by Driver'
""")
print("\nRides Cancelled by Drivers:", cursor.fetchone()[0])

# 6️⃣ Max and Min driver ratings for Prime Sedan
cursor.execute("""
SELECT MAX(Driver_Ratings), MIN(Driver_Ratings)
FROM ola_rides
WHERE Vehicle_Type='Prime Sedan'
""")
result = cursor.fetchone()
print("\nPrime Sedan Driver Ratings:")
print("Max Rating:", result[0])
print("Min Rating:", result[1])

# 7️⃣ Rides paid using UPI
cursor.execute("""
SELECT *
FROM ola_rides
WHERE Payment_Method='UPI'
LIMIT 5
""")
print("\nUPI Payment Rides (Sample):")
for row in cursor.fetchall():
    print(row)

# 8️⃣ Average customer rating per vehicle type
cursor.execute("""
SELECT Vehicle_Type, AVG(Customer_Rating)
FROM ola_rides
GROUP BY Vehicle_Type
""")
print("\nAverage Customer Rating by Vehicle Type:")
for row in cursor.fetchall():
    print(row)

# 9️⃣ Total booking value of successful rides
cursor.execute("""
SELECT SUM(Booking_Value)
FROM ola_rides
WHERE Booking_Status='Success'
""")
print("\nTotal Booking Value (Successful Rides):", cursor.fetchone()[0])

# 🔟 Incomplete rides with reason
cursor.execute("""
SELECT Booking_ID, Booking_Status
FROM ola_rides
WHERE Booking_Status!='Success'
LIMIT 10
""")
print("\nIncomplete Rides with Reason:")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()