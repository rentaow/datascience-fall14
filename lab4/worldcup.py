import pandas as pd
import re

wcin = open('worldcup.txt', 'r')
wctext = wcin.read()

splitcountry = re.split('\|-',wctext)
del splitcountry[0]
clen = len(splitcountry)
countries = re.findall('fb\|([A-Z]{3})',wctext)
n = re.compile('\|([\d]) \(\[\[')
yr = re.compile('\|([\d]{4})\]')
df = []

for i in range(clen):
	num = n.findall(splitcountry[i])
	num = [int(x) for x in num]
	years = yr.findall(splitcountry[i])
	places = []
	rank = 1
	for a in range(len(num)):
		for b in range(num[a]):
			places.append(rank)
		rank += 1
	ind = [str(x) for x in range(len(years))]
	df.append(pd.DataFrame({'Country': countries[i], 'Year': years, 'Place': places}, 	index=ind))
wc1 = pd.concat([df[x] for x in range(clen)], keys=[x for x in range(clen)])
wc1 = wc1.reset_index(drop=True)
#world cup1
print wc1

#world cup 2
wc2 = wc1.pivot('Country', 'Year', 'Place')
print(wc2)
