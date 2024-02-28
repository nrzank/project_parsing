import pandas as pd


df1 = pd.read_csv('Alser_macbook_Almaty.csv')
df2 = pd.read_csv('Sulpak_macbook_Almaty.csv')
df3 = pd.read_csv('technodom_macbook_Almaty.csv')


df1['Новая цена'] = df1['Новая цена'].str.replace('[^\d]', '', regex=True)
df1['Новая цена'] = pd.to_numeric(df1['Новая цена'], errors='coerce')

df1['Старая цена'] = df1['Старая цена'].str.replace('[^\d]', '', regex=True)
df1['Старая цена'] = pd.to_numeric(df1['Старая цена'], errors='coerce')

df2['Новая цена'] = df2['Новая цена'].str.replace('[^\d]', '', regex=True)
df2['Новая цена'] = pd.to_numeric(df2['Новая цена'], errors='coerce')

df2['Старая цена'] = df2['Старая цена'].str.replace('[^\d]', '', regex=True)
df2['Старая цена'] = pd.to_numeric(df2['Старая цена'], errors='coerce')

df3['Новая цена'] = df3['Новая цена'].str.replace('[^\d]', '', regex=True)
df3['Новая цена'] = pd.to_numeric(df3['Новая цена'], errors='coerce')

df3['Старая цена'] = df3['Старая цена'].str.replace('[^\d]', '', regex=True)
df3['Старая цена'] = pd.to_numeric(df3['Старая цена'], errors='coerce')


df1['Минимальная стоимость'] = df1[['Новая цена', 'Старая цена']].min(axis=1)
df2['Минимальная стоимость'] = df2[['Новая цена', 'Старая цена']].min(axis=1)
df3['Минимальная стоимость'] = df3[['Новая цена', 'Старая цена']].min(axis=1)


df1['Минимальная старая цена'] = df1['Старая цена']
df2['Минимальная старая цена'] = df2['Старая цена']
df3['Минимальная старая цена'] = df3['Старая цена']

# Выбор магазина с минимальной стоимостью и минимальной старой ценой
df_min_cost = pd.concat([df1[['Имя магазина', 'Минимальная стоимость', 'Минимальная старая цена']],
                         df2[['Имя магазина', 'Минимальная стоимость', 'Минимальная старая цена']],
                         df3[['Имя магазина', 'Минимальная стоимость', 'Минимальная старая цена']]])

df_min_cost = df_min_cost.groupby('Имя магазина').min()

df_count = pd.DataFrame({
    'Имя магазина': ['Alser', 'Sulpak', 'Technodom'],
    'Количество продуктов': [len(df1), len(df2), len(df3)]
})
df_max_count = df_count[df_count['Количество продуктов'] == df_count['Количество продуктов'].max()]


df_avg_price = pd.DataFrame({
    'Имя магазина': ['Alser', 'Sulpak', 'Technodom'],
    'Средняя цена': [(df1['Новая цена'] + df1['Старая цена']).mean(),
                    (df2['Новая цена'] + df2['Старая цена']).mean(),
                    (df3['Новая цена'] + df3['Старая цена']).mean()]
})

df_min_cost.to_csv('result_min_cost.csv', index=False)
df_max_count.to_csv('result_max_count.csv', index=False)
df_avg_price.to_csv('result_avg_price.csv', index=False)

print('Операций успешно завершены!')
