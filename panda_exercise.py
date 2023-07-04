import pandas as pd

df = pd.read_excel('team.xlsx')
print(df)

s = pd.Series([i for i in range(0, 100)])
df = df.set_index(s)
print(df)

df = df.set_index([s])
print(df)

# 检查 MultiIndex 是否包含指定的值
values = [100]
mask = df.index.isin(values)
result = df[mask]

print(df.mean(axis=1))


