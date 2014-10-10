#Rentao Wu
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import pandas as pd

schema = avro.schema.parse(open("country.avsc").read())
reader = DataFileReader(open("countries.avro","r"), DatumReader())

rlist = []

for country in reader:
	rlist.append(country)


df = pd.DataFrame(rlist)

str1 = "Num countries with > 10,000,000 population:"
print str1, df[df.population > 10000000].population.count()
reader.close()
