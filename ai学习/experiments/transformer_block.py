
import torch
from torch import nn


class TransformerBlock(nn.Module):

    def __init__(self):
        super().__init__()

        # 多头自注意力
        self.attention = nn.MultiheadAttention(
            embed_dim=8,
            num_heads=2,
            batch_first=True
        )

        # 第一次归一化
        self.norm1 = nn.LayerNorm(8)

        # FFN：8维 → 16维 → 8维
        self.ffn = nn.Sequential(
            nn.Linear(8, 16),
            nn.ReLU(),
            nn.Linear(16, 8)
        )

        # 第二次归一化
        self.norm2 = nn.LayerNorm(8)

    def forward(self, x):

        # 1. Self-Attention
        attn_output, _ = self.attention(
            x, x, x,
            need_weights=False
        )

        # 2. 残差连接 + LayerNorm
        x = self.norm1(x + attn_output)

        # 3. FFN
        ffn_output = self.ffn(x)

        # 4. 残差连接 + LayerNorm
        x = self.norm2(x + ffn_output)

        return x


model = TransformerBlock()

# 2句话，每句话3个Token，每个Token 8维
x = torch.randn(2, 3, 8)

y = model(x)

print("输入形状：", x.shape)
print("输出形状：", y.shape)
