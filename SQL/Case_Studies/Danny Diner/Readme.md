### **Case Study: Restaurant Loyalty Program Analysis**

#### **Background**
A local restaurant chain introduced a loyalty program to reward its regular customers. The program tracks purchases, offers special points for certain items, and includes time-sensitive promotions for newly joined members. The restaurant wants to analyze customer behavior and the effectiveness of the loyalty program.

#### **Data Overview**
Three tables are provided:

1. **Sales Table (`sales`)**: Records each sale made, including the `customer_id`, `order_date`, and `product_id`.
2. **Menu Table (`menu`)**: Lists each item available for purchase, including the `product_id`, `product_name`, and `price`.
3. **Members Table (`members`)**: Contains details of customers who joined the loyalty program, including the `customer_id` and `join_date`.

#### **Objectives**
The restaurant management seeks to answer the following questions:

1. **Total Spending Per Customer**:
   - Calculate the total amount spent by each customer across all their visits.

2. **Visit Frequency**:
   - Determine how many days each customer visited the restaurant.

3. **First Purchase Item**:
   - Identify the first item purchased by each customer.

4. **Most Popular Item**:
   - Determine the most purchased item on the menu and how many times it was bought by all customers.

5. **Customer-Specific Favorite Item**:
   - Find the most popular item for each customer.

6. **First Purchase Post-Membership**:
   - Identify the first item each customer purchased after joining the loyalty program.

7. **Last Purchase Before Membership**:
   - Identify the item each customer purchased just before they became a member.

8. **Pre-Membership Purchases**:
   - Calculate the total number of items and the total amount spent by each customer before joining the program.

9. **Points Accumulation**:
   - Compute the points each customer has earned, given that every $1 spent earns 10 points, with sushi having a 2x multiplier.

10. **Points in First Week Post-Membership**:
    - Determine the total points accumulated by customers A and B by the end of January, considering that in the first week after joining, they earn 2x points on all items.

#### **SQL Solutions**

1. **Total Spending Per Customer**:
   ```sql
   SELECT S.customer_id, SUM(M.price) AS total_spent
   FROM Menu m
   JOIN Sales s ON m.product_id = s.product_id
   GROUP BY S.customer_id;
   ```

2. **Visit Frequency**:
   ```sql
   SELECT customer_id, COUNT(DISTINCT(order_date)) AS visit_days
   FROM Sales
   GROUP BY customer_id;
   ```

3. **First Purchase Item**:
   ```sql
   WITH Rank AS (
       SELECT S.customer_id, 
              M.product_name, 
              S.order_date,
              DENSE_RANK() OVER (PARTITION BY S.Customer_ID ORDER BY S.order_date) AS rank
       FROM Menu m
       JOIN Sales s ON m.product_id = s.product_id
   )
   SELECT Customer_id, product_name
   FROM Rank
   WHERE rank = 1;
   ```

4. **Most Popular Item**:
   ```sql
   SELECT TOP 1 M.product_name, COUNT(S.product_id) AS purchase_count
   FROM Menu m
   JOIN Sales s ON m.product_id = s.product_id
   GROUP BY M.product_name
   ORDER BY COUNT(S.product_id) DESC;
   ```

5. **Customer-Specific Favorite Item**:
   ```sql
   WITH rank AS (
       SELECT S.customer_ID,
              M.product_name, 
              COUNT(S.product_id) AS Count,
              DENSE_RANK() OVER (PARTITION BY S.Customer_ID ORDER BY COUNT(S.product_id) DESC) AS Rank
       FROM Menu m
       JOIN Sales s ON m.product_id = s.product_id
       GROUP BY S.customer_id, S.product_id, M.product_name
   )
   SELECT Customer_id, Product_name, Count
   FROM rank
   WHERE rank = 1;
   ```

6. **First Purchase Post-Membership**:
   ```sql
   WITH Rank AS (
       SELECT S.customer_id,
              M.product_name,
              DENSE_RANK() OVER (PARTITION BY S.Customer_id ORDER BY S.Order_date) AS Rank
       FROM Sales S
       JOIN Menu M ON m.product_id = s.product_id
       JOIN Members Mem ON Mem.Customer_id = S.customer_id
       WHERE S.order_date >= Mem.join_date  
   )
   SELECT customer_ID, Product_name
   FROM Rank
   WHERE Rank = 1;
   ```

7. **Last Purchase Before Membership**:
   ```sql
   WITH Rank AS (
       SELECT S.customer_id,
              M.product_name,
              DENSE_RANK() OVER (PARTITION BY S.Customer_id ORDER BY S.Order_date DESC) AS Rank
       FROM Sales S
       JOIN Menu M ON m.product_id = s.product_id
       JOIN Members Mem ON Mem.Customer_id = S.customer_id
       WHERE S.order_date < Mem.join_date  
   )
   SELECT customer_ID, Product_name
   FROM Rank
   WHERE Rank = 1;
   ```

8. **Pre-Membership Purchases**:
   ```sql
   SELECT S.customer_id, COUNT(S.product_id) AS quantity, SUM(M.price) AS total_sales
   FROM Sales S
   JOIN Menu M ON m.product_id = s.product_id
   JOIN Members Mem ON Mem.Customer_id = S.customer_id
   WHERE S.order_date < Mem.join_date
   GROUP BY S.customer_id;
   ```

9. **Points Accumulation**:
   ```sql
   WITH Points AS (
       SELECT *, CASE WHEN product_id = 1 THEN price * 20
                      ELSE price * 10
                      END AS Points
       FROM Menu
   )
   SELECT S.customer_id, SUM(P.points) AS Points
   FROM Sales S
   JOIN Points p ON p.product_id = S.product_id
   GROUP BY S.customer_id;
   ```

10. **Points in First Week Post-Membership**:
    ```sql
    SELECT
           s.customer_id,
           SUM(CASE
                 WHEN (DATEDIFF(DAY, me.join_date, s.order_date) BETWEEN 0 AND 7) OR (m.product_ID = 1) 
                 THEN m.price * 20
                 ELSE m.price * 10
              END) AS Points
    FROM members AS me
    INNER JOIN sales AS s ON s.customer_id = me.customer_id
    INNER JOIN menu AS m ON m.product_id = s.product_id
    WHERE s.order_date >= me.join_date AND s.order_date <= CAST('2021-01-31' AS DATE)
    GROUP BY s.customer_id;
    ```

#### **Conclusion**
The above SQL queries provide insights into customer spending habits, product popularity, and the effectiveness of the loyalty program. These insights can help the restaurant optimize its menu, tailor promotions, and improve customer retention strategies.
