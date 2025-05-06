
import os  

# 🔹 AWS Configuration  
AWS_REGION = "us-west-2"  

# 🔹 DynamoDB Settings  
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE", "Receipts")  

# 🔹 SES Email Settings  ********ADD YOUR EMAIL********
SES_SENDER_EMAIL = os.environ.get("SES_SENDER_EMAIL", "YOUR_EMAIL")  
SES_RECIPIENT_EMAIL = os.environ.get("SES_RECIPIENT_EMAIL", "YOUR_EMAIL")  

# 🔹 S3 Bucket Configuration  
S3_BUCKET = os.environ.get("S3_BUCKET", "auto-reciepts-aaron")  
S3_UPLOAD_PATH = "incoming/"  # Default path for new receipts  

# 🔹 Textract Settings  
TEXTRACT_MODE = "analyze_expense"  # This defines how Textract processes receipts  

# 🔹 Other Constants  
DEFAULT_DATE_FORMAT = "%Y-%m-%d"  
