from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import r2_score
from sklearn.naive_bayes import GaussianNB

class AnalyticsCore:

    def __init__(self, X_training_set, X_test_set, y_training_set, y_test_set):
        self.X_train = X_training_set
        self.X_test = X_test_set
        self.y_train = y_training_set
        self.y_test = y_test_set

    def RandomForest(self, n_estimators, random_state):
        RF = RandomForestClassifier(n_estimators, random_state)
        RF.fit(self.X_train, self.y_train)
        y_pred = RF.predict(self.X_test)
        return r2_score(y_pred, self.y_test)

    def SVM(self, random_state):
        SVM = SVC(random_state)
        SVM.fit(self.X_train, self.y_train)
        y_pred = SVM.predict(self.X_test)
        return r2_score(y_pred, self.y_test)

    def DecisionTree(self, random_state):
        decisionTree = DecisionTreeClassifier(random_state)
        decisionTree.fit(self.X_train, self.y_train)
        y_pred = decisionTree.predict(self.X_test)
        return r2_score(y_pred, self.y_test)

    def NB(self):
        NB = GaussianNB()
        NB.fit(self.X_train, self.y_train)
        y_pred = NB.predict(self.X_test)
        return r2_score(y_pred, self.y_test)

    def FitnessFunction(phenotype):
        try:
            score = eval(phenotype)
        except:
            score = 0
            print("Invalid phenotype")
        return score