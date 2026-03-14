import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel dataset
df = pd.read_excel(r"C:\OLA internship project\OLA_DataSet.xlsx")
print(df.head())

# Check structure and data types
print("\nDataset info:")
print(df.info())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 4: Basic Cleaning
# Fill missing ratings with 0

df['Customer_Rating'].fillna(0, inplace=True)
df['Driver_Ratings'].fillna(0, inplace=True)

# Convert 'Date' to datetime (if not already)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Combine 'Date' and 'Time' to create 'ride_time'
# Convert 'Time' to string first to avoid errors
df['ride_time'] = pd.to_datetime(df['Date'].dt.strftime('%Y-%m-%d') + ' ' + df['Time'].astype(str))

# Extract ride hour, day, month, weekday
df['ride_hour'] = df['ride_time'].dt.hour
df['ride_day'] = df['ride_time'].dt.day
df['ride_month'] = df['ride_time'].dt.month
df['ride_weekday'] = df['ride_time'].dt.day_name()

# ----------------------------
# Step 3: Check cleaned dataset
# ----------------------------
print("\nData cleaning completed. Sample data:")
print(df[['Date','Time','ride_time','ride_hour','ride_day','ride_month','ride_weekday']].head())

# ----------------------------
# Optional: Save cleaned dataset
# ----------------------------
df.to_csv("ola_data_cleaned.csv", index=False)
print("\nCleaned dataset saved as 'ola_data_cleaned.csv'.")

# Step 3: Total Rides & Completed Rides
# ----------------------------
total_rides = df.shape[0]
completed_rides = df[df['Booking_Status'] == 'Completed'].shape[0]

print("\nTotal rides:", total_rides)
print("Completed rides:", completed_rides)


# Step 4: Cancelled & Incomplete Rides
# ----------------------------
cancelled_by_customer = df['Canceled_Rides_by_Customer'].notna().sum()
cancelled_by_driver = df['Canceled_Rides_by_Driver'].notna().sum()
incomplete_rides = df['Incomplete_Rides'].notna().sum()

print("\nRides cancelled by customers:", cancelled_by_customer)
print("Rides cancelled by drivers:", cancelled_by_driver)
print("Incomplete rides:", incomplete_rides)


# Step 5: Revenue Analysis
# ----------------------------
total_revenue = df['Booking_Value'].sum()
revenue_by_payment = df.groupby('Payment_Method')['Booking_Value'].sum()

print("\nTotal booking value (revenue):", total_revenue)
print("\nRevenue by Payment Method:")
print(revenue_by_payment)


# Step 6: Top 5 Customers by Rides
# ----------------------------
top_customers = df.groupby('Customer_ID')['Booking_ID'].count().sort_values(ascending=False).head(5)
print("\nTop 5 customers by number of rides:")
print(top_customers)


# Step 7: Average Ratings
# ----------------------------
avg_customer_rating = df['Customer_Rating'].mean()
avg_driver_rating = df['Driver_Ratings'].mean()

print("\nAverage Customer Rating:", round(avg_customer_rating, 2))
print("Average Driver Rating:", round(avg_driver_rating, 2))


# Step 8: Ride Patterns
# ----------------------------
# Rides per hour
rides_per_hour = df.groupby('ride_hour')['Booking_ID'].count()
print("\nRides per hour:")
print(rides_per_hour)

# Rides per weekday
rides_per_weekday = df.groupby('ride_weekday')['Booking_ID'].count()
print("\nRides per weekday:")
print(rides_per_weekday)

# Rides per month
rides_per_month = df.groupby('ride_month')['Booking_ID'].count()
print("\nRides per month:")
print(rides_per_month)


# Step 9: Vehicle Type Analysis
# ----------------------------
rides_per_vehicle = df.groupby('Vehicle_Type')['Booking_ID'].count()
avg_distance_vehicle = df.groupby('Vehicle_Type')['Ride_Distance'].mean()

print("\nRides per Vehicle Type:")
print(rides_per_vehicle)

print("\nAverage Ride Distance per Vehicle Type:")
print(avg_distance_vehicle)


# Optional: Save EDA Results
# ----------------------------
eda_summary = pd.DataFrame({
    'Total_Rides':[total_rides],
    'Completed_Rides':[completed_rides],
    'Cancelled_by_Customer':[cancelled_by_customer],
    'Cancelled_by_Driver':[cancelled_by_driver],
    'Incomplete_Rides':[incomplete_rides],
    'Total_Revenue':[total_revenue],
    'Avg_Customer_Rating':[round(avg_customer_rating,2)],
    'Avg_Driver_Rating':[round(avg_driver_rating,2)]
})

eda_summary.to_csv("ola_eda_summary.csv", index=False)
print("\nEDA summary saved as 'ola_eda_summary.csv'.")



eda_summary = pd.DataFrame({
    'Total_Rides':[total_rides],
    'Completed_Rides':[completed_rides],
    'Cancelled_by_Customer':[cancelled_by_customer],
    'Cancelled_by_Driver':[cancelled_by_driver],
    'Incomplete_Rides':[incomplete_rides],
    'Total_Revenue':[total_revenue],
    'Avg_Customer_Rating':[round(avg_customer_rating,2)],
    'Avg_Driver_Rating':[round(avg_driver_rating,2)]
})

eda_summary.to_csv("ola_eda_summary.csv", index=False)
print("\nEDA summary saved as 'ola_eda_summary.csv'.")

#visualization

#Ride volume per hour (Peak hours)
plt.figure(figsize=(10,5))
sns.barplot(x=rides_per_hour.index, y=rides_per_hour.values)

plt.title("Ride Volume by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Rides")

plt.show()

#Ride distribution by weekday

plt.figure(figsize=(10,5))
sns.barplot(x=rides_per_weekday.index, y=rides_per_weekday.values)

plt.title("Ride Distribution by Weekday")
plt.xlabel("Day")
plt.ylabel("Total Rides")

plt.xticks(rotation=45)
plt.show()

#Vehicle type demand

plt.figure(figsize=(10,5))
sns.barplot(x=rides_per_vehicle.index, y=rides_per_vehicle.values)

plt.title("Ride Demand by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.ylabel("Total Rides")

plt.xticks(rotation=45)
plt.show()

#Revenue by payment method

plt.figure(figsize=(8,5))

revenue_by_payment.plot(kind='bar')

plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Revenue")

plt.xticks(rotation=45)
plt.show()

#Ratings distribution

plt.figure(figsize=(8,5))

sns.histplot(df['Customer_Rating'], bins=10, kde=True)

plt.title("Customer Rating Distribution")
plt.xlabel("Customer Rating")
plt.ylabel("Frequency")

plt.show()



