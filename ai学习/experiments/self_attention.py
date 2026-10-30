
import torch
import torch.nn.functional as F

# 1. 两个 Token，每个 Token 是二维向量
X = torch.tensor([
    [1.0, 0.0],
    [0.0, 1.0]
])

# 2. 使用单位矩阵作为 QKV 投影
W_Q = torch.eye(2)
W_K = torch.eye(2)
W_V = torch.eye(2)

Q = X @ W_Q
K = X @ W_K
V = X @ W_V

# 3. 计算缩放后的匹配分数
d_k = Q.shape[-1]

scores = (Q @ K.T) / (d_k ** 0.5)

# 4. 每一行分别进行 Softmax
weights = F.softmax(scores, dim=-1)

# 5. 对 Value 向量加权求和
output = weights @ V

print("Q =\n", Q)
print("K =\n", K)
print("V =\n", V)

print("Scores =\n", scores)
print("Attention Weights =\n", weights)
print("Attention Output =\n", output)

print("权重矩阵形状：", weights.shape)
print("输出形状：", output.shape)
