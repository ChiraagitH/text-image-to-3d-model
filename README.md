# 🧠 Text & Image to 3D Model Generator using SHAP-E

This project uses OpenAI's **SHAP-E** model to generate 3D models from either **text prompts** or **2D images**. It demonstrates how AI can convert high-level input into usable `.glb` 3D assets, useful for applications in prototyping, gaming, AR/VR, and 3D printing.

---

## 🚀 Features

- 🔤 **Text-to-3D**: Generate 3D models from natural language descriptions  
- 🖼️ **Image-to-3D**: Convert 2D images into 3D representations  
- 💾 Outputs `.glb` (GLTF Binary) files  
- 🧠 Powered by **OpenAI’s SHAP-E** model  
- ⚙️ Fully Python-based with modular code structure

---

## 📁 Project Structure

text-image-to-3d-model/
├── shap_e/ # SHAP-E model (cloned or extracted)
├── utils/
│ ├── text_to_3d.py # Text-to-3D conversion logic
│ └── image_to_3d_model.py # Image-to-3D conversion logic
├── input/
│ ├── prompt.txt # Sample text prompt
│ └── image.jpg # Sample image input
├── output/ # Generated 3D models
├── main.py # Entry point CLI
└── README.md


---

## 🛠️ Setup Instructions

### 1. Prepare the Project Folder

Download the SHAP-E repo from [OpenAI’s GitHub](https://github.com/openai/shap-e), extract it manually into the `shap_e/` folder inside your main project directory.

### 2. Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Run the CLI

python main.py

a small red toy car with four wheels

 3D model saved to: output/red_car.glb


