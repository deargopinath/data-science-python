"""
2. Given is the Confusion Matrix. It represents the cancer detection report. 
   Here, 0 means “No” and 1 means “Yes”. 
   Find out the Sensitivity and Specificity of the given matrix. 

n = 192    |   Predicted : 0    |    Predicted: 1    |
-----------------------------------------------------
Actual: 0  |     TN = 118       |      FP = 12       |
-----------------------------------------------------
Actual: 1  |     FN =  47       |      TP = 15       |
-----------------------------------------------------

Sensitivity = TP / (TP + FN)
Specificity = TN / (TN + FP)
Accuracy = (TP + TN) / (TP + TN + FP + FN)

"""
import numpy as np
confusionMatrix = np.array([[0, 0],[0, 0]])
confusionMatrix[0][0] = int(input("Enter True Negative: "))
confusionMatrix[0][1] = int(input("Enter False Positive: "))
confusionMatrix[1][0] = int(input("Enter False Negative: "))
confusionMatrix[1][1] = int(input("Enter True Positive: "))

print("Confusion Matrix is: \n", confusionMatrix)
print("sensitivity = ", (confusionMatrix[1][1] / (confusionMatrix[1][1] + confusionMatrix[1][0])))
print("specificity = ", (confusionMatrix[0][0] / (confusionMatrix[0][0] + confusionMatrix[0][1])))