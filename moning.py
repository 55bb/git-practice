import torch

# 1. 检查 PyTorch 版本
print(torch.__version__)

# 2. 检查 CUDA（GPU）是否可用
print(torch.cuda.is_available())

# 3. 如果 CUDA 可用，查看 GPU 设备和数量
if torch.cuda.is_available():
    print(torch.cuda.device_count())  # GPU 数量
    print(torch.cuda.get_device_name(0))  # 第一个 GPU 的名称