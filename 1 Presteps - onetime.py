# Databricks notebook source
dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list('efnkvault')

# COMMAND ----------

dlaccesskey=dbutils.secrets.get('efnkvault','efnblob')

# COMMAND ----------

dbutils.fs.mount(
    source='wasbs://data@efnblob.blob.core.windows.net/',
    mount_point='/mnt/deltaProject',
    extra_configs={'fs.azure.account.key.efnblob.blob.core.windows.net':dlaccesskey}
)

# COMMAND ----------

from delta.tables import DeltaTable

# 1 Specify the Delta table name
delta_table_name = "delta_customers"

# Create a Delta table for Customers
DeltaTable.create(spark) \
    .tableName(delta_table_name) \
    .addColumn("CustomerID", "INT") \
    .addColumn("FirstName", 'STRING') \
    .addColumn("LastName", 'STRING') \
    .addColumn("Email", 'STRING') \
    .addColumn("Phone", 'STRING') \
    .addColumn("CreatedDate", 'DATE') \
    .addColumn("ModifiedDate", 'DATE') \
    .execute()

# 2 Specify the Delta table name

delta_table_name = "delta_products"

# Create a Delta table for Products
DeltaTable.create(spark) \
    .tableName(delta_table_name) \
    .addColumn("ProductID", "INT") \
    .addColumn("ProductName", 'STRING') \
    .addColumn("Price", 'DECIMAL(10,2)') \
    .addColumn("Category", 'STRING') \
    .addColumn("CreatedDate", 'DATE') \
    .addColumn("ModifiedDate", 'DATE') \
    .execute()    


# 3 Specify the Delta table name
delta_table_name = "delta_orders"

# Create a Delta table for Orders
DeltaTable.create(spark) \
    .tableName(delta_table_name) \
    .addColumn("OrderID", "INT") \
    .addColumn("CustomerID", "INT") \
    .addColumn("OrderDate", 'DATE') \
    .addColumn("OrderStatus", 'STRING') \
    .addColumn("CreatedDate", 'DATE') \
    .addColumn("ModifiedDate", 'DATE') \
    .execute()

# 4 Specify the Delta table name
delta_table_name = "delta_orderitems"

# Create a Delta table for OrderItems
DeltaTable.create(spark) \
    .tableName(delta_table_name) \
    .addColumn("OrderItemID", "INT") \
    .addColumn("OrderID", "INT") \
    .addColumn("ProductID", "INT") \
    .addColumn("Quantity", "INT") \
    .addColumn("TotalPrice", 'DECIMAL(10,2)') \
    .addColumn("CreatedDate", 'DATE') \
    .addColumn("ModifiedDate", 'DATE') \
    .execute()

# 5 Specify the Delta table name
delta_table_name = "delta_Inventory"

# Create a Delta table for Inventory
DeltaTable.create(spark) \
    .tableName(delta_table_name) \
    .addColumn("ProductID", "INT") \
    .addColumn("StockQuantity", "INT") \
    .addColumn("CreatedDate", 'DATE') \
    .addColumn("ModifiedDate", 'DATE') \
    .execute()

# 6 Specify the Delta table name
delta_table_name = "delta_Payments"

# Create a Delta table for Payments
DeltaTable.create(spark) \
    .tableName(delta_table_name) \
    .addColumn("PaymentID", "INT") \
    .addColumn("OrderID", "INT") \
    .addColumn("PaymentAmount", 'DECIMAL(10,2)') \
    .addColumn("PaymentDate", 'DATE') \
    .addColumn("CreatedDate", 'DATE') \
    .addColumn("ModifiedDate", 'DATE') \
    .addColumn("Status","INT")\
    .execute()

# 7 Specify the Delta table name
delta_table_name = "delta_promotions"

# Create a Delta table for Promotions
DeltaTable.create(spark) \
    .tableName(delta_table_name) \
    .addColumn("PromotionID", "INT") \
    .addColumn("PromotionName", 'STRING') \
    .addColumn("Discount", 'DECIMAL(5,2)') \
    .addColumn("StartDate", 'DATE') \
    .addColumn("EndDate", 'DATE') \
    .addColumn("CreatedDate", 'DATE') \
    .addColumn("ModifiedDate", 'DATE') \
    .execute()

# 8 Specify the Delta table name
delta_table_name = "delta_reviews"

# Create a Delta table for Reviews
DeltaTable.create(spark) \
    .tableName(delta_table_name) \
    .addColumn("ReviewID", "INT") \
    .addColumn("ProductID", "INT") \
    .addColumn("CustomerID", "INT") \
    .addColumn("Rating", "INT") \
    .addColumn("Comment", 'STRING') \
    .addColumn("CreatedDate", 'DATE') \
    .addColumn("ModifiedDate", 'DATE') \
    .execute()

# 9 Specify the Delta table name
delta_table_name = "delta_shipping_details"

# Create a Delta table for ShippingDetails
DeltaTable.create(spark) \
    .tableName(delta_table_name) \
    .addColumn("ShippingID", "INT") \
    .addColumn("OrderID", "INT") \
    .addColumn("ShippingMethod", 'STRING') \
    .addColumn("TrackingNumber", 'STRING') \
    .addColumn("ShipDate", 'DATE') \
    .addColumn("CreatedDate", 'DATE') \
    .addColumn("ModifiedDate", 'DATE') \
    .execute()

# 10 Specify the Delta table name
delta_table_name = "delta_Returns"

# Create a Delta table for Returns
DeltaTable.create(spark) \
    .tableName(delta_table_name) \
    .addColumn("ReturnID", "INT") \
    .addColumn("OrderID", "INT") \
    .addColumn("ProductID", "INT") \
    .addColumn("ReturnReason", 'STRING') \
    .addColumn("ReturnDate", 'DATE') \
    .addColumn("CreatedDate", 'DATE') \
    .addColumn("ModifiedDate", 'DATE') \
    .execute()

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta_customers
