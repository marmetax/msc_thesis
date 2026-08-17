import pandas as pd
import string
import problog
from problog.program import PrologString
from problog.learning import lfi

#Reading the cleaned datset
df = pd.read_csv('../dataset/breast_cancer_cleaned.csv')

#Setting the program's basic predicates
#res(A) corresponds to result with A either being n(o) or y(es)
#level(A) corresponds to the levels of the data with A being l(ow), m(edium) or h(igh)
program = "res(n). res(y). " \
          "level(vl). level(l). level(m). level(h). level(vh)." \
          "\n"

#Binning each column of the data to form everything into a categorical model.
for label in df:
    if label == "diagnosis": 
        labels = ["n", "y"]  # no, yes -> res().
        bins = [0, 0.5, 1]
    elif label == "radius_mean":
        labels = ["vl", "l", "m", "h", "vh"]  # very low, low, medium, high, very high -> level().
        bins = [0, 9.09, 11.21, 17.55, 21.77, 29]
    elif label == "texture_mean":
        labels = ["vl", "l", "m", "h", "vh"]  # very low, low, medium, high, very high -> level().
        bins = [0, 12.67, 15.62, 24.50, 30.41, 40]
    elif label == "perimeter_mean":
        labels = ["vl", "l", "m", "h", "vh"]  # very low, low, medium, high, very high -> level().
        bins = [0, 58.26, 72.73, 116.15, 145.09, 195]
    elif label == "area_mean":
        labels = ["vl", "l", "m", "h", "vh"]  # very low, low, medium, high, very high -> level().
        bins = [0, 379.25, 615, 1086.50, 1322.25, 3000]
    elif label == "smoothness_mean":
        labels = ["vl", "l", "m", "h", "vh"]  # very low, low, medium, high, very high -> level().
        bins = [0, 0.07, 0.09, 0.11, 0.13, 0.20]
    elif label == "compactness_mean":
        labels = ["vl", "l", "m", "h", "vh"]  # very low, low, medium, high, very high -> level().
        bins = [0, 0.05, 0.12, 0.18, 0.25, 0.35]
    elif label == "concavity_mean":
        labels = ["vl", "l", "m", "h", "vh"] # very low, low, medium, high, very high -> level().
        bins = [0, 0.04, 0.09, 0.17, 0.26, 0.45]
    elif label == "concave_points_mean":
        labels = ["vl", "l", "m", "h", "vh"]  # very low, low, medium, high, very high -> level().
        bins = [0, 0.02, 0.06, 0.10, 0.14, 0.30]
    elif label == "symmetry_mean":
        labels = ["vl", "l", "m", "h", "vh"]  # very low, low, medium, high, very high -> level().
        bins = [0., 0.15,  0.17, 0.22, 0.24, 0.35]
    elif label == "fractal_dimension_mean":
        labels = ["vl", "l", "m", "h", "vh"]  # very low, low, medium, high, very high -> level().
        bins = [0, 0.05, 0.06, 0.07, 0.08, 0.1]
    df[label] = pd.cut(df[label], bins=bins, labels=labels, include_lowest=True)
    #Forming the model as strings
    if label == "diagnosis":
        num = len(df.columns) - 1
        for n in range(pow(2, num)):
            params = "(A,"
            bstr = format(n, "0" + str(num) + "b")
            clause = ""
            comma = ""
            n = 1
            for l in df:
                if l == "diagnosis":
                    continue
                params += comma + string.ascii_uppercase[n]

                if bstr[n - 1] == "0":
                    l = "\+" + l
                clause += comma + l + "(A," + string.ascii_uppercase[n] + ")"
                n += 1
                comma = ", "
                pass
            params += ")"
            program += (
                    label + params + ":- " + clause + ", res(A).\n"
            )
            pass
    else:
        program += "t(0.5,A,B)::" + label + "(A,B):- level(B).\n"

#Variables to store the length of the training samples and the testing samples
training_samples = int(len(df) * 0.9)
testing_samples = len(df) - training_samples

# Get the first 90% of the dataset for training
training_data = df.head(training_samples)

# Save the training data to a CSV file
training_data.to_csv("../dataset/training_data.csv", index=False)

# Get the last 10% of the dataset for testing
testing_data = df.tail(testing_samples)

# Save the testing data to a CSV file
testing_data.to_csv("../dataset/testing_data.csv", index=False)

#Starting the create the evidence based on the training data
evidence = ""

#Loop to create the evidence based on the training data
for i in range(len(training_data)):
    data = df.iloc[i]
    print ("data from iloc", data)
    data = data.tolist()
    print ("data tolist", data)
    print("Data -1", data[0])
    comma = ""
    #We start d from 1 as the position 0 is the column where the diagnosis is stored
    d = 1
    for label in df.columns: 
        print("label", label)
        #We bypass the diagnosis column as it shouldn't be added as a sole predicate of evidence
        if label == "diagnosis" or d == 11:
            continue
        if data[0] == "y":
            evidence += (
                "evidence(" + label + "(" + data[0] + "," + data[d] + "), true).\n"
            )
            new_d = "n"
            evidence += (
                "evidence(" + label + "(" + new_d + "," + data[d] + "), false).\n"
            )
        else:
            evidence += (
                "evidence(" + label + "(" + data[0] + "," + data[d] + "), true).\n"
            )
            new_d = "y"
            evidence += (
                "evidence(" + label + "(" + new_d + "," + data[d] + "), false).\n"
            )
        d += 1
    evidence += "----\n"

#Need to check what is wrong as it says that there is the second value missing while it is there
#score, weights, atoms, iteration, lfi_problem = lfi.run_lfi(PrologString(program), evidence)
#trained_model = lfi_problem.get_model()

#with open("trained_model.pl", "w") as tr_model:
#    tr_model.write(trained_model)

#Save the training evidence and the untrained model
with open("training_evidence.pl", "w") as evidence_file:
    evidence_file.write(evidence)

with open("untrained_model.pl", "w") as prob_file:
    prob_file.write(program)
