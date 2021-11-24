import pandas
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn import metrics


df = pandas.read_csv("C:/Users/User/Documents/EARIN/[EARIN] Exercice 6 BARBE Victor DEBEAUVAIS Guillaume/arcene_train1.txt")
target = pandas.read_csv("C:/Users/User/Documents/EARIN/[EARIN] Exercice 6 BARBE Victor DEBEAUVAIS Guillaume/arcene_train.txt")

digits = load_digits()
dir(digits)
df = pandas.DataFrame(digits.data)
df.head()
df['target'] = digits.target
X = df.drop('target',axis='columns')
y = df.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2) #spliting the data into 2 parts

forestClassifer = RandomForestClassifier(n_estimators=20) #random forest
forestClassifer.fit(X_train, y_train)
forestClassifer.score(X_test, y_test)
y_predictedForest = forestClassifer.predict(X_test)
print("this is the predicted y with the random forest method \n")
print(y_predictedForest,"\n")
confusionMatrixRandomForest = confusion_matrix(y_test, y_predictedForest)
print("this is the confusion matrix with the random forest method \n ")
print(confusionMatrixRandomForest,"\n")


classifierGradientBoosting = GradientBoostingClassifier(n_estimators=20) #gradient boosting
classifierGradientBoosting.fit(X_train,y_train)
classifierGradientBoosting.score(X_test, y_test)
y_predictedGradient = classifierGradientBoosting.predict(X_test)
print("this is the predicted y with the gradient boosting method ")
print(y_predictedGradient,"\n")
confusionMatrixGradientBoosting = confusion_matrix(y_test, y_predictedGradient)
print("this is the confusion matrix with the gradient boosting method\n")
print(confusionMatrixGradientBoosting,"\n")


print("this is the recall score for the random forest classification") #random forest scores
randomForestRecallScore = recall_score(y_test, y_predictedForest,average = 'micro')
print(randomForestRecallScore)
print("F1 score for the random forest ")
f1ScoreRandomForest = metrics.f1_score(y_test, y_predictedForest,average='micro')
print(f1ScoreRandomForest)
print("accuracy score for random forest ")
accuracyScoreRandomForest = metrics.accuracy_score(y_test, y_predictedForest)
print(accuracyScoreRandomForest,"\n")



print("this is the recall score for the gradient boosting classification") #gradient boosting score
gradientBoostingRecallScore = recall_score(y_test, y_predictedGradient,average = 'micro')
print(gradientBoostingRecallScore)
print("F1 score for the gradient boosting")
f1ScoreGradientBoosting = metrics.f1_score(y_test, y_predictedGradient,average='micro')
print(f1ScoreGradientBoosting)
print("accuracy score for gradient boosting")
accuracyScoreGradientBoosting = metrics.accuracy_score(y_test, y_predictedGradient)
print(accuracyScoreGradientBoosting)
