import pandas as pd

df = pd.read_csv('Red.csv')
print(df.head())
print(df.columns.tolist())
print(df.info())
print(df.describe())

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('Red.csv')

# 把空格和连字符都替换成下划线，保持完整名称
text = ' '.join(
    df['Region']
    .astype(str)
    .str.replace(r'[\s\-]', '_', regex=True)
    .tolist()
)

# 生成词云
wordcloud = WordCloud(
    width=1600,
    height=900,
    background_color='white',
    stopwords=STOPWORDS,
    max_words=150,
    collocations=False,
    colormap='Reds'
).generate(text)

# 显示
plt.figure(figsize=(16, 9))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Wine Region Word Cloud', fontsize=20, pad=20)
plt.tight_layout()
plt.show()
