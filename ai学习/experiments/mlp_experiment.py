
import torch
from torch import nn
from pathlib import Path
from mlp_model import MLP

torch.manual_seed(42)

# 生成 160 个输入点，范围 [-2, 2]
x_all = torch.linspace(-2, 2, 160).unsqueeze(1)

# 真实函数 y = x²
y_all = x_all ** 2

# 随机打乱样本索引
indices = torch.randperm(160)

# 120 个样本用于训练，40 个用于测试
train_idx = indices[:120]
test_idx = indices[120:]

x_train = x_all[train_idx]
y_train = y_all[train_idx]

x_test = x_all[test_idx]
y_test = y_all[test_idx]

print("训练集形状：", x_train.shape)
print("测试集形状：", x_test.shape)


# 模型 A：普通线性模型
linear_model = nn.Linear(1, 1)

# 模型 B：带 ReLU 的多层感知机
mlp_model = MLP(hidden_dim=16)

print(
    "Linear 参数数量：",
    sum(p.numel() for p in linear_model.parameters())
)

print(
    "MLP 参数数量：",
    sum(p.numel() for p in mlp_model.parameters())
)



def train_model(model, name, epochs=1000):

    loss_fn = nn.MSELoss()

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.01
    )

    print(f"\n开始训练：{name}")

    for epoch in range(epochs + 1):

        # 进入训练模式
        model.train()

        # 清除上一次的梯度
        optimizer.zero_grad()

        # 前向传播
        predictions = model(x_train)

        # 计算训练损失
        loss = loss_fn(predictions, y_train)

        # 反向传播
        loss.backward()

        # 更新参数
        optimizer.step()

        # 每 200 轮观察一次训练和测试误差
        if epoch % 200 == 0:

            model.eval()

            with torch.no_grad():

                train_mse = loss_fn(
                    model(x_train), y_train
                ).item()

                test_mse = loss_fn(
                    model(x_test), y_test
                ).item()

            print(
                f"Epoch {epoch:4d} | "
                f"Train MSE: {train_mse:.6f} | "
                f"Test MSE: {test_mse:.6f}"
            )

    return model


# 训练普通线性模型
linear_model = train_model(
    linear_model,
    name="Linear"
)

# 训练多层感知机
mlp_model = train_model(
    mlp_model,
    name="MLP"
)


# 模型参数保存路径
save_path = (
    Path(__file__).resolve().parent
    / "checkpoints"
    / "mlp_x2.pth"
)

# 确保文件夹存在
save_path.parent.mkdir(parents=True, exist_ok=True)

# 保存训练后的模型参数
torch.save(
    mlp_model.state_dict(),
    save_path
)

print("模型已保存到：", save_path)



# 查看两个模型的预测
sample_x = torch.tensor([
    [-1.5],
    [0.0],
    [1.5]
])

linear_model.eval()
mlp_model.eval()

with torch.no_grad():
    linear_result = linear_model(sample_x)
    mlp_result = mlp_model(sample_x)

print("\n真实值：", (sample_x ** 2).squeeze().tolist())
print("Linear预测：", linear_result.squeeze().tolist())
print("MLP预测：", mlp_result.squeeze().tolist())
