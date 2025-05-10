import os
import sys
sys.path.append('C:\\Users\\chiraag\\text-image-to-3d-model\\shap_e')


from utils.image_to_3d_model import process_image
from utils.text_to_3d import generate_3d_from_text

def main():
    input_type = input("Enter input type (image/text): ").strip().lower()

    if input_type == 'image':
        image_path = input("Enter image path (e.g., input/chair.jpg): ").strip()
        output_file = process_image(image_path)
    elif input_type == 'text':
        prompt_path = input("Enter prompt file path (e.g., input/prompt.txt): ").strip()
        with open(prompt_path, 'r') as f:
            prompt = f.read().strip()
        output_file = generate_3d_from_text(prompt)
    else:
        print("Invalid input type. Use 'image' or 'text'.")
        return

    print(f"3D model saved to: {output_file}")

if __name__ == "__main__":
    main()
