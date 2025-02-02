import json
import qrcode
import io
import base64

def lambda_handler(event, context):
    # Get the URL from query parameters (for a GET request)
    params = event.get("queryStringParameters") or {}
    url = params.get("url")
    
    # Validate that a URL was provided
    if not url:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "Missing 'url' parameter"})
        }
    
    try:
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,  # smallest size QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image to a bytes buffer
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        img_bytes = buffer.getvalue()

        # Encode the image to base64 so it can be returned in JSON
        base64_img = base64.b64encode(img_bytes).decode("utf-8")
        
        # Return the QR code in JSON
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"qr_code": base64_img})
        }
        
    except Exception as e:
        # If there's an error during processing, return an error response
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }
