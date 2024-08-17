# Pizza Runner Challenge Case Study

## A. Pizza Metrics

1. **How many pizzas were ordered?**
   - Determine the total count of pizzas ordered across all customer orders.

2. **How many unique customer orders were made?**
   - Calculate the number of distinct orders placed by customers.

3. **How many successful orders were delivered by each runner?**
   - Find the number of orders successfully delivered by each delivery runner.

4. **How many of each type of pizza was delivered?**
   - Count how many deliveries were made for each type of pizza.

5. **How many Vegetarian and Meatlovers pizzas were ordered by each customer?**
   - Analyze the count of Vegetarian and Meatlovers pizzas ordered by each customer.

6. **What was the maximum number of pizzas delivered in a single order?**
   - Identify the maximum number of pizzas delivered in any single order.

7. **For each customer, how many delivered pizzas had at least 1 change and how many had no changes?**
   - Determine the count of delivered pizzas with and without changes for each customer.

8. **How many pizzas were delivered that had both exclusions and extras?**
   - Count the number of pizzas delivered that included both exclusions and extras.

9. **What was the total volume of pizzas ordered for each hour of the day?**
   - Calculate the volume of pizzas ordered for each hour of the day.

10. **What was the volume of orders for each day of the week?**
    - Determine the volume of orders placed on each day of the week.

## B. Runner and Customer Experience

1. **How many runners signed up for each 1-week period?**
   - Count the number of runners who signed up each week, starting from a specific date.

2. **What was the average time in minutes it took for each runner to arrive at the Pizza Runner HQ to pick up the order?**
   - Compute the average time taken for each runner to reach the pickup point.

3. **Is there any relationship between the number of pizzas and how long the order takes to prepare?**
   - Analyze the correlation between the number of pizzas in an order and the preparation time.

4. **What was the average distance travelled for each customer?**
   - Calculate the average distance traveled for deliveries to each customer.

5. **What was the difference between the longest and shortest delivery times for all orders?**
   - Find the range between the longest and shortest delivery times.

6. **What was the average speed for each runner for each delivery and do you notice any trend for these values?**
   - Analyze the average speed of runners for each delivery and identify any trends.

7. **What is the successful delivery percentage for each runner?**
   - Determine the percentage of successful deliveries made by each runner.

## C. Ingredient Optimization

1. **What are the standard ingredients for each pizza?**
   - List the standard ingredients for each type of pizza.

2. **What was the most commonly added extra?**
   - Identify the most frequently added extra ingredient across all orders.

3. **What was the most common exclusion?**
   - Determine the most common excluded ingredient.

4. **Generate an order item for each record in the `customer_orders` table in the following format:**
   - Format each order item to reflect the base pizza name, exclusions, and extras.

5. **Generate an alphabetically ordered, comma-separated ingredient list for each pizza order:**
   - Produce a formatted ingredient list with "2x" prefix for any relevant ingredients.

6. **What is the total quantity of each ingredient used in all delivered pizzas sorted by most frequent first?**
   - Calculate the total quantity of each ingredient used in all delivered pizzas, sorted by frequency.

## D. Pricing and Ratings

1. **If a Meat Lovers pizza costs $12 and Vegetarian costs $10, how much money has Pizza Runner made so far?**
   - Calculate the total revenue based on fixed prices and no delivery fees.

2. **What if there was an additional $1 charge for any pizza extras?**
   - Recalculate the total revenue including the extra charge for pizza extras.

3. **Add cheese is $1 extra.**
   - Adjust revenue calculations to include the extra charge for cheese.

4. **Design a new ratings table schema and insert sample data:**
   - Create a table for customer ratings of runners and insert sample rating data.

5. **Join all information to form a table with delivery details and ratings:**
   - Create a summary table combining customer, order, runner, and rating information.

6. **If a Meat Lovers pizza was $12 and Vegetarian $10 fixed prices with no cost for extras and each runner is paid $0.30 per kilometer traveled - how much money does Pizza Runner have left over after these deliveries?**
   - Calculate the remaining money after deducting runner payments from total revenue.

## E. Bonus Questions

1. **If Danny wants to expand his range of pizzas, how would this impact the existing data design?**
   - Discuss potential impacts on data design and write an INSERT statement for a new pizza type.
