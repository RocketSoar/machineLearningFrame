import json
class ModelBaseClass:
    def train(self, features, labels, *args, **dicts):
        """
        train the model
        :param features:features of the training set
        :param labels: labels of the training set
        :param args: other args
        :param dicts: other args
        :return: None
        """
        pass

    def predict(self, features):
        """
        predict the label of the test set with the trained model
        :param features:features of the test set
        :return:an one dimension np.array of labels
        """
        pass

    def save(self, para):
        """
        save the model's parameters
        :param para: parameters dict
        :return:None
        """
        with open(f"../parameters/{self.__class__.__name__}Para.json", "w") as f:
            json.dump(para, f, indent=4)

    def loadJson(self):
        """
        load the saved parameters json file
        :return: None
        """
        with open(f"../parameters/{self.__class__.__name__}Para.json", "r") as f:
            para = json.load(f)
        return para

    def loadPara(self):
        """
        load the saved parameters
        :return:
        """
        pass
