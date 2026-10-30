
import torch
from pathlib import Path
from mlp_model import MLP


# 1. 创建与训练时相同结构的新模型
model = MLP(hidden_dim=16)


# 2. 找到模型权重文件
model_path = (
    Path(__file__).resolve().parent
    / "checkpoints"
    / "mlp_x2.pth"
)


# 3. 从磁盘读取状态字典
state = torch.load(
    model_path,
    map_location="cpu",
    weights_only=True
)


# 4. 将训练后的参数加载到模型
model.load_state_dict(state)


# 5. 切换到评估模式
model.eval()


# 6. 使用训练好的模型进行推理
x = torch.tensor([
    [-1.5],
    [0.0],
    [1.5]
])

with torch.inference_mode():
    predictions = model(x)


print("真实值：", (x ** 2).squeeze().tolist())
print("模型预测：", predictions.squeeze().tolist())
