fo = open("foo.txt", "wb+")
fo.write( b"Python is a great language.\nYeah its great!!\n");
fo.seek(0)
print(fo.read())
# Close opend file
fo.close()
