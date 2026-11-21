
# PRODUCT FEEDBACK AND REVIEW ANALYSIS
import pandas as pd
import numpy as np

df = pd.read_excel("cleaned_product_feedback.xlsx")

print("PRODUCT FEEDBACK DATA")
print(df.head())


print("\nTotal Records:", len(df))
print("Total Columns:", len(df.columns))
print("Dataset Shape:", df.shape)



print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())



print("\nAverage Rating:", np.mean(df["Rating"]))
print("Highest Rating:", np.max(df["Rating"]))
print("Lowest Rating:", np.min(df["Rating"]))
print("Median Rating:", np.median(df["Rating"]))
print("Total Helpful Votes:", np.sum(df["Helpful_Votes"]))



print("\nRating Distribution:")
print(df["Rating"].value_counts().sort_index())



positive = len(df[df["Sentiment"] == "Positive"])
negative = len(df[df["Sentiment"] == "Negative"])
neutral = len(df[df["Sentiment"] == "Neutral"])

print("\nPositive Reviews:", positive)
print("Negative Reviews:", negative)
print("Neutral Reviews:", neutral)

print("Positive Percentage:", positive/len(df)*100)
print("Negative Percentage:", negative/len(df)*100)


print("\nReviews by Category:")
print(df["Product_Category"].value_counts())

print("\nAverage Rating by Category:")
print(df.groupby("Product_Category")["Rating"].mean())



print("\nProduct Review Count:")
print(df["Product_Name"].value_counts())

print("\nAverage Product Rating:")
print(df.groupby("Product_Name")["Rating"].mean())



print("\nFeedback Topics:")
print(df["Feedback_Topic"].value_counts())



print("\nTop 5 Helpful Reviews:")
print(df.sort_values("Helpful_Votes", ascending=False)[
    ["Product_Name", "Rating", "Helpful_Votes"]
].head(5))



ratings = list(df["Rating"])
columns = ("Product_Name", "Rating", "Sentiment")

print("\nFirst 10 Ratings:", ratings[:10])
print("Selected Columns:", columns)



high = 0
low = 0

for r in ratings:
    if r >= 4:
        high += 1
    else:
        low += 1

print("\nHigh Ratings:", high)
print("Low Ratings:", low)



avg = df["Rating"].mean()

if avg >= 4:
    print("\nCustomer Satisfaction: GOOD")
elif avg >= 3:
    print("\nCustomer Satisfaction: AVERAGE")
else:
    print("\nCustomer Satisfaction: LOW")


print("\nANALYSIS COMPLETED!")
