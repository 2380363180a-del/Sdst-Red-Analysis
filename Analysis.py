import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# ====================== 1. 读取并查看数据 ======================
df = pd.read_csv('Red.csv')

print("=" * 50)
print("前5行数据：")
print(df.head())

print("\n" + "=" * 50)
print("所有列名：")
print(df.columns.tolist())

print("\n" + "=" * 50)
print("数据基本信息：")
print(df.info())

print("\n" + "=" * 50)
print("数值列统计：")
print(df.describe())

# ====================== 2. 生成 Region 词云 ======================
print("\n" + "=" * 50)
print("正在生成词云...")

text = ' '.join(
    df['Region']
    .astype(str)
    .str.replace(r'[\s\-]', '_', regex=True)
    .tolist()
)

wordcloud = WordCloud(
    width=1600,
    height=900,
    background_color='white',
    stopwords=STOPWORDS,
    max_words=150,
    collocations=False,
    colormap='Reds'
).generate(text)

plt.figure(figsize=(16, 9))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Wine Region Word Cloud', fontsize=20, pad=20)
plt.tight_layout()

# 保存图片而不是 show
plt.savefig('wordcloud.png', dpi=150, bbox_inches='tight')
plt.close()
print("词云已保存为：wordcloud.png")

# ====================== 3. Top20 频率 + 平均价格 双条形图 ======================
print("\n" + "=" * 50)
print("正在绘制 Top20 地区 频率 vs 平均价格 图...")

top20_regions = df['Region'].value_counts().head(20).index
avg_price = df[df['Region'].isin(top20_regions)].groupby('Region')['Price'].mean()
counts = df['Region'].value_counts().loc[top20_regions]
avg_price = avg_price.loc[top20_regions]

fig, ax1 = plt.subplots(figsize=(14, 10))

y = np.arange(len(top20_regions))
height = 0.35

# 红色条：出现频率
bars1 = ax1.barh(y + height/2, counts.values[::-1], height=height, 
                 color='firebrick', label='Frequency (Count)')

for bar in bars1:
    width = bar.get_width()
    ax1.text(width + 1, bar.get_y() + bar.get_height()/2,
             f'{int(width)}', va='center', fontsize=9, color='firebrick')

ax1.set_xlabel('Frequency (Count)', color='firebrick', fontsize=12)
ax1.tick_params(axis='x', labelcolor='firebrick')
ax1.set_yticks(y)
ax1.set_yticklabels(top20_regions[::-1])

# 蓝色条：平均价格
ax2 = ax1.twiny()
bars2 = ax2.barh(y - height/2, avg_price.values[::-1], height=height,
                 color='steelblue', label='Average Price')

for bar in bars2:
    width = bar.get_width()
    ax2.text(width + 0.5, bar.get_y() + bar.get_height()/2,
             f'{width:.1f}', va='center', fontsize=9, color='steelblue')

ax2.set_xlabel('Average Price', color='steelblue', fontsize=12)
ax2.tick_params(axis='x', labelcolor='steelblue')

plt.title('Top 20 Regions: Frequency (Red) vs Average Price (Blue)', fontsize=14, pad=20)
plt.tight_layout()

# 保存图片
plt.savefig('top20_regions.png', dpi=150, bbox_inches='tight')
plt.close()
print("条形图已保存为：top20_regions.png")

print("\n全部完成！请在左侧文件列表中查看 wordcloud.png 和 top20_regions.png")
