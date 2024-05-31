from PIL import Image
import numpy as np

def load_image(image_path):
    return Image.open(image_path)

def save_image(image, path):
    image.save(path)

def encrypt_image(image, key):
    # Convert image to numpy array
    img_array = np.array(image)
    # Apply a simple encryption operation (e.g., add a constant value to each pixel)
    encrypted_array = (img_array + key) % 256  # Ensure values stay within byte range
    # Convert back to image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    return encrypted_image

def decrypt_image(encrypted_image, key):
    # Convert image to numpy array
    encrypted_array = np.array(encrypted_image)
    # Reverse the encryption operation
    decrypted_array = (encrypted_array - key) % 256
    # Convert back to image
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    return decrypted_image

# Example usage
if __name__ == "__main__":
    key = 50  # Example encryption key

    # Load the original image
    original_image = load_image("path_to_your_image.jpg")

    # Encrypt the image
    encrypted_image = encrypt_image(original_image, key)
    save_image(encrypted_image, "encrypted_image.jpg")

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key)
    save_image(decrypted_image, "decrypted_image.jpg")

    print("Encryption and decryption completed successfully.")
