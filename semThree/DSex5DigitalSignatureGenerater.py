
import hmac
import hashlib

def sign_document(document, secret_key):
    return hmac.new(secret_key.encode(), document.encode(), hashlib.sha256).hexdigest()

def verify_signature(document, secret_key, signature):
    return sign_document(document, secret_key) == signature

if __name__ == "__main__":
    # Get user input for the document and the secret key
    secret_key = input("Enter the secret key: ")
    document = input("Enter the document text: ")
    
    # Sign the document
    signature = sign_document(document, secret_key)
    print("\nGenerated Signature:", signature)
    
    # Verify the signature
    is_valid = verify_signature(document, secret_key, signature)
    print("Signature valid for original document:", is_valid)

    # Test with a modified document
    modified_document = input("\nEnter a modified document text: ")
    is_valid_modified = verify_signature(modified_document, secret_key, signature)
    print("Signature valid for modified document:", is_valid_modified)
