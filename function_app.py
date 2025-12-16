import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(
    arg_name="myblob",
    path="aniketsand",
    connection="AzureWebJobsStorage"
)
def blob_trigger(myblob: func.InputStream):
    try:
        blob_name = myblob.name
        blob_size = myblob.length
        blob_content = myblob.read()  # Read full blob content if needed

        logging.info(f"Blob processed: Name={blob_name}, Size={blob_size} bytes")
        logging.info(f"Blob content (first 200 bytes): {blob_content[:200]}")

        # Example: further processing
        # process_blob_data(blob_content)

    except Exception as e:
        logging.error(f"Error processing blob {myblob.name}: {str(e)}")
