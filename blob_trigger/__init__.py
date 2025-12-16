import azure.functions as func
import logging

def main(myblob: func.InputStream):
    try:
        blob_name = myblob.name
        blob_size = myblob.length
        blob_content = myblob.read()  # Read full blob content

        logging.info(f"Blob processed: Name={blob_name}, Size={blob_size} bytes")
        logging.info(f"Blob content (first 200 bytes): {blob_content[:200]}")

        # Optional: add any custom processing here
        # process_blob_data(blob_content)

    except Exception as e:
        logging.error(f"Error processing blob {myblob.name}: {str(e)}")
