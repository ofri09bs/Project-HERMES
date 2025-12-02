import stegano_module
import crypto_module
import text_processing
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(r"""
  _    _ ______ _____  __  __ ______  _____ 
 | |  | |  ____|  __ \|  \/  |  ____|/ ____|
 | |__| | |__  | |__) | \  / | |__  | (___  
 |  __  |  __| |  _  /| |\/| |  __|  \___ \ 
 | |  | | |____| | \ \| |  | | |____ ____) |
 |_|  |_|______|_|  \_\_|  |_|______|_____/ 
    Steganography Suite v1.0
    """)


def encode_mode():
    print("\n--- [ ENCODE MODE ] ---")
    
    img_path = input("Enter path to source image (PNG only): ").strip('"')
    if not os.path.exists(img_path):
        print("❌ Error: File not found.")
        return

    secret_msg = input("Enter the secret message: ")
    password = input("Enter encryption password: ")

    if not secret_msg or not password: return print("❌ Cannot be empty.")

    output_path = input("Enter output filename (e.g., secret.png): ")
    if not output_path.endswith(".png"):
        output_path += ".png"

    print("\nProcessing...")

    try:
        encrypted_msg = crypto_module.encrypt_data(secret_msg, password)
        bits = text_processing.text_to_bits(encrypted_msg)
        print(f"[*] Converted text to {len(bits)} bits.")

        result = stegano_module.embed_bits(bits, img_path, output_path)
        
        if result == 'Too many bits!':
            print("❌ Error: Message is too long for this image!")
        else:
            print(f"✅ SUCCESS! Secret image saved to: {output_path}")
            
    except Exception as e:
        print(f"❌ Critical Error: {e}")

def decode_mode():
    print("\n--- [ DECODE MODE ] ---")
    
    img_path = input("Enter path to image: ").strip('"')
    if not os.path.exists(img_path):
        print("❌ Error: File not found.")
        return
    
    password = input("Enter decryption password: ")

    print("\nExtracting data...")

    try:
        extracted_bits = stegano_module.extract_bits(img_path)
        
        if not extracted_bits:
            print("[-] No hidden message found (or format invalid).")
            return

        encrypted_text = text_processing.bits_to_text(extracted_bits)
        print(f"\n[DEBUG] Extracted Raw Data (First 50 chars): {encrypted_text[:50]}...")
        secret_msg = crypto_module.decrypt_data(encrypted_text, password)
        
        print("\n" + "="*30)
        print("🔓 DECODED MESSAGE:")
        print(secret_msg)
        print("="*30 + "\n")
        
    except Exception as e:
        print(f"❌ Decoding Error: {e}")

def main():
    while True:
        clear_screen()
        print_banner()
        print("1. Hide a message (Encode)")
        print("2. Reveal a message (Decode)")
        print("3. Exit")
        
        choice = input("\nSelect option: ")
        
        if choice == '1':
            encode_mode()
        elif choice == '2':
            decode_mode()
        elif choice == '3':
            print("Bye.")
            break
        else:
            print("Invalid choice.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()




