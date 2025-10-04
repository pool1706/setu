import os
import cv2

# ======== CONFIG =======
# Paste your full absolute path to the folder containing raw images
input_dir = r"C:\Users\khush\detectsetu\islalphaeng"

# Folder where processed images will be saved
output_dir = r"C:\Users\khush\detectsetu\processed_dataset"

# Desired size for resized images
img_size = 128
# =======================

# Check if input folder exists
if not os.path.exists(input_dir):
    print(f"❌ ERROR: Input folder does not exist: {input_dir}")
    exit()

# Create output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all subfolders (letters/classes)
for letter in os.listdir(input_dir):
    letter_input_path = os.path.join(input_dir, letter)
    letter_output_path = os.path.join(output_dir, letter)

    # Skip if not a folder
    if not os.path.isdir(letter_input_path):
        continue

    # Create folder for this class in processed_dataset
    os.makedirs(letter_output_path, exist_ok=True)
    print(f"Processing folder: {letter_input_path} → {letter_output_path}")

    # Loop through images in this folder
    for img_name in os.listdir(letter_input_path):
        img_path = os.path.join(letter_input_path, img_name)

        # Skip non-image files
        if not img_name.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        # Read image
        img = cv2.imread(img_path)
        if img is None:
            print(f"⚠️  Skipped invalid image: {img_path}")
            continue

        # Resize
        img = cv2.resize(img, (img_size, img_size))

        # Convert to grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Save processed image
        save_path = os.path.join(letter_output_path, img_name)
        cv2.imwrite(save_path, img)

print("✅ Preprocessing completed successfully!")
print(f"Processed images saved in: {output_dir}")
