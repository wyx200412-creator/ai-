

import torch
from torch import nn

# 1. 固定随机种子，方便重复实验
torch.manual_seed(42)


# 2. 准备训练数据
x = torch.tensor([
    [0.0],
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

y = 3 * x + 2


# 3. 定义模型
class LinearRegressionModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


model = LinearRegressionModel()


# 4. 损失函数
loss_fn = nn.MSELoss()


# 5. 优化器
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.1
)


# 6. 训练模型
model.train()

for epoch in range(501):

    optimizer.zero_grad()

    prediction = model(x)

    loss = loss_fn(prediction, y)

    loss.backward()

    optimizer.step()

    if epoch % 100 == 0:
        print(
            f"Epoch {epoch}, "
            f"Loss = {loss.item():.6f}"
        )


# 7. 查看最终参数
print("训练得到的 w：", model.linear.weight.item())
print("训练得到的 b：", model.linear.bias.item())


# 8. 使用模型推理
model.eval()

with torch.no_grad():
    test_x = torch.tensor([[10.0]])
    result = model(test_x)

print("x = 10 时的预测：", result.item())
