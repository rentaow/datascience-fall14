import pandas as pd

ground_true = pd.read_csv("product_mapping.csv")
test = pd.read_csv("products_out.csv")

amazon = test[test['source'] == 'amazon']
google = test[test['source'] == 'google']

dupe = pd.merge(amazon, google, on='Cluster ID')
dupe = dupe[['id_x', 'id_y']]
print 'found duplicate', len(dupe)


dupe.rename(columns={'id_x':'idAmazon', 'id_y':'idGoogleBase'}, inplace=True)

intersect = pd.merge(ground_true, dupe, on=['idAmazon', 'idGoogleBase'])
precision = float(len(intersect))/len(dupe)
recall = float(len(intersect))/len(ground_true)

print 'precision', precision
print 'recall', recall
