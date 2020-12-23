# AI_lab5
Lab 5: Add a search with a ranked parameter query on the recommendation system (make a mini survey in the input, set the price range and discount range):  
-Sorting method: used to add points for matching items.  
-If nothing is found in the parameter query, similar objects are given
![image](https://github.com/PrettyWitch/AI_lab5/blob/master/image/lab5.png)  

As shown in the figure, the search price range is 110-123, and the discount range is 8-18.
No eligible objects were found, so the search range was automatically expanded, the price range was 90-143, and the discount range was 0-28. Five eligible objects were found.

1.SoyBean  
Price is not in the original search range  
Discount is not in the original search range  
match = 0

2.Corn  
The price is in the original search range -> match++  
Discount is not in the original search range  
match = 1

3.Cherry  
Price is not in the original search range  
Discount is not in the original search range  
match = 0

4.Grape  
Price is not in the original search range  
The discount is in the original search range -> match++  
match = 1

5.Banana  
Price is not in the original search range  
Discount is not in the original search range  
match = 0

Sort by the number of matches from high to low, so the sorting is Corn, Grape, SoyBean, Cherry, Banana
