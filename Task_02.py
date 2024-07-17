from PIL import Image

def encrypt_image(image_path):
    """
    Encrypt the image by swapping the RGB values of each pixel.

    Args:
        image_path (str): Path to the input image.

    Returns:
        str: Path to the encrypted image.
    """
    img = Image.open(image_path)
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            # Swap the RGB values (R->B, G->R, B->G)
            new_pixel = (pixel[2], pixel[0], pixel[1])
            img.putpixel((x, y), new_pixel)

    encrypted_path = f"{image_path.split('.')[0]}_encrypted.png"
    img.save(encrypted_path)
    print("Image encrypted successfully.")
    return encrypted_path

def decrypt_image(encrypted_image_path):
    """
    Decrypt the image by reversing the swapping of the RGB values of each pixel.

    Args:
        encrypted_image_path (str): Path to the encrypted image.

    Returns:
        str: Path to the decrypted image.
    """
    img = Image.open(encrypted_image_path)
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            # Reverse the RGB swap (B->R, R->G, G->B)
            new_pixel = (pixel[1], pixel[2], pixel[0])
            img.putpixel((x, y), new_pixel)

    decrypted_path = f"{encrypted_image_path.split('_encrypted')[0]}_decrypted.png"
    img.save(decrypted_path)
    print("Image decrypted successfully.")
    return decrypted_path

def main():
    """
    Main function to handle user input for encrypting or decrypting images.
    """
    while True:
        choice = input("Do you want to encrypt or decrypt an image? (e/d): ").lower()
        if choice == "e":
            image_path = input("Enter the path of the image: ")
            encrypted_image_path = encrypt_image(image_path)
            print(f"Encrypted image saved as: {encrypted_image_path}")
        elif choice == "d":
            encrypted_image_path = input("Enter the path of the encrypted image: ")
            decrypted_image_path = decrypt_image(encrypted_image_path)
            print(f"Decrypted image saved as: {decrypted_image_path}")
        else:
            print("Invalid choice! Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        cont = input("Do you want to continue? (y/n): ").lower()
        if cont != "y":
            break

if __name__ == "__main__":
    main()
