n = int(input())
res = []
for _ in range(n):
    nframe = int(input())
    thisDic = {}
    preDic = {}
    maxCount = 0
    for _ in range(nframe):
        features = input().split(" ")
        features = [int(i) for i in features]
        nfeature = features[0]
        for i in range(nfeature):
            feature = str(features[2 * i + 1]) + str(features[2 * i + 2])
            nPre = preDic.get(feature, 0)
            if nPre:
                thisDic[feature] = nPre + 1
            else:
                thisDic[feature] = 1
            maxCount = max(maxCount, thisDic[feature])
        preDic = thisDic.copy()
        thisDic.clear()
    res.append(maxCount)
    print(res)
