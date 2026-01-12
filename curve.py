import numpy as np
import matplotlib.pyplot as plt

# 参数设置
m = 10         # 论文中的设定
alpha = 0.2    # 论文中的设定
y_hat = np.linspace(0, 1, 100) # 自变量：从 0 到 1

# 公式计算：Soft Margin (NCR Equation 7)
alpha_hat = ((m ** y_hat - 1) / (m - 1)) * alpha

# 对比组：如果是线性的 (Linear)
alpha_linear = y_hat * alpha

# 绘图
plt.figure(figsize=(8, 5))
plt.plot(y_hat, alpha_hat, label=f'NCR Soft Margin (m={m})', color='red', linewidth=2.5)
plt.plot(y_hat, alpha_linear, label='Linear Reference (y=x)', color='gray', linestyle='--', alpha=0.6)

# 标注关键点
plt.scatter([0, 0.5, 1], [0, ((m**0.5-1)/(m-1))*alpha, alpha], color='black', zorder=5)
plt.text(0.02, 0.01, 'Noise (0, 0)', fontsize=10)
plt.text(0.95, 0.19, 'Clean (1, 0.2)', fontsize=10, ha='right')

# 装饰
plt.title(r'Curve of Eq.7: $\hat{\alpha}_i = \frac{m^{\hat{y}_i} - 1}{m - 1} \alpha$', fontsize=14)
plt.xlabel(r'Rectified Label $\hat{y}_i$ (Confidence)', fontsize=12)
plt.ylabel(r'Soft Margin $\hat{\alpha}_i$', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
# plt.show()
plt.savefig('Noisy Correspondence/2021-NeurIPS-NCR-main/soft_margin_curve.png', dpi=300)
print("✅ 绘图完成！图片已保存为 'soft_margin_curve.png'，请下载到本地查看。")