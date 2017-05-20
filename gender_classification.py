from sklearn import tree

X=[[67,140],[71,165],[73,168],[71,142],[74,200],[74,175],[68,135],[73,145],[71,150],[72,155],[69,168],[66,106],[71,132],[70,140],[71,140],[70,140],[69,130],[70,150],[74,170],[63,117],[62,107],[75,170],[61,91],[62,118],[63,130],[66,135],[63,120],[67,125],[67,117],[64,135],
[61,88],[64,110],[63,123],[64,110],[71,134],[64,129],[62,129],[65,123]]
Y=['male','male','male','male','male','male','male','male','male','male','male','male','male','male','male','male','male','male','male','female','female','female','female','female','female','female','female','female','female','female','female','female','female','female','female','female','female','female']

clf=tree.DecisionTreeClassifier()
clf.fit(X,Y)

prediction=clf.predict([[70,170]])
print(prediction)

