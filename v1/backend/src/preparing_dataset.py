import pandas as pd

# Load the initial dataset
df = pd.read_csv('../dataset/breast_cancer.csv')
distinct_count = len(df.drop_duplicates())
duplicate_count = len(df) - distinct_count
print(f'{distinct_count} distinct rows and {duplicate_count} duplicated rows')

# Dropping the duplicated values
df = df.drop_duplicates()

# Dropping the columns that are not used for model prediction
columns_to_drop = ['id', 'radius_se', 
    'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 
    'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst', 
    'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']  # Specify the columns you want to drop
df = df.drop(columns_to_drop, axis=1)

#Replacing 'B' and 'M' with 0 for B and 1 for M.
mapping = {'B': 0, 'M': 1}
df = df.replace({'diagnosis': mapping})

#Renaming the concave points_mean column to concave_points_mean
df.rename(columns = {'concave points_mean':'concave_points_mean'}, inplace = True)

# Saving the modified dataset
df.to_csv('../dataset/breast_cancer_cleaned.csv', index=False)

#Rereading the saved file to drop the Unnamed column
df = pd.read_csv('../dataset/breast_cancer_cleaned.csv')
df = df.drop('Unnamed: 32', axis=1)

#Saving the file
df.to_csv('../dataset/breast_cancer_cleaned.csv', index=False)

