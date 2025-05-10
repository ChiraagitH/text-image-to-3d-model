import os
import torch
import cv2
import numpy as np
import open3d as o3d
from torchvision.transforms import Compose, Resize, ToTensor

def load_midas_model(model_path, device):
    from torchvision.models.segmentation import deeplabv3_resnet101
    model = torch.hub.load("intel-isl/MiDaS", "DPT_Hybrid", model_map={"DPT_Hybrid": model_path})
    model.to(device)
    model.eval()
    return model

def process_image(image_path, output_path="output/image_model.obj"):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    midas = load_midas_model("weights/dpt_hybrid_384.pt", device)

    transform = Compose([Resize(384), ToTensor()])
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    input_tensor = transform(img_rgb).unsqueeze(0).to(device)

    with torch.no_grad():
        prediction = midas(input_tensor)
        depth_map = prediction.squeeze().cpu().numpy()

    h, w = depth_map.shape
    xx, yy = np.meshgrid(np.arange(w), np.arange(h))
    xyz = np.stack((xx, yy, depth_map), axis=-1).reshape(-1, 3)
    colors = img.reshape(-1, 3) / 255.0

    
    mask = depth_map.flatten() > 0
    xyz = xyz[mask]
    colors = colors[mask]

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd.colors = o3d.utility.Vector3dVector(colors)

    mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8)
    mesh.compute_vertex_normals()

    
    o3d.io.write_triangle_mesh(output_path, mesh)
    return output_path
