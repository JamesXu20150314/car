#!#/usr/bin/python

cmap = set([0,1,2,5,7,8,10,12,13,16,18,19,20,21,24,25,28,29,30])
f = open("data/train_features_sampling.csv", 'w')
for l in open("data/train.csv"):
    l = l.strip('\r\n')
    index = l.split(',')
    r = ''
    for i in range(0, 34):
        if i in cmap:
            r = r + ',' + index[i]
    r = r[1:] + '\n'
    f.write(r)
print 'train_features_sampling.csv'
f.close()

f = open('data/test_features_sampling.csv', 'w')
for l in open("data/test.csv"):
    l = l.strip('\r\n')
    index = l.split(',')
    r = ''
    for i in range(0, 34):
        if i in cmap:
            r = r + ',' + index[i]
    r = r[1:] + '\n'
    f.write(r)
print 'test_features_sampling.csv'
f.close()
