# Backend Developer Test

At Sorted we work with a range of modern technology and tools, but most of our services are written in Python & Django. This test has been designed to give you an opportunity to show your knowledge of Django and API design. There is no 'right' answer - we're most interested in how you choose to solve the problem and why you chose to solve it in that way. There are no wrong answers, as long as your code successfully runs.

Be sure to read **all** of this document carefully, and follow the guidelines within.

## Task Outline
Everyone at Sorted is passionate about food - and we're creating tools to help foodies all around the world cook better, and smarter. We give people the tools and know-how, but the rest is up to them.

We're helping people reduce food waste and better understand how much their weekly shop costs by generating smart shopping lists for them. We'd like you to create a **REST API** for creating, retrieving and updating ingredient and shopping list data. We'll give you the building blocks, but you'll have to fill in the blanks.

## Requirements
To be successful in this task, you'll need to satisfy the following use cases:

**Add ingredients to the database**

An ingredient must have name, category (fresh, staple), unit (g, ml, tsp, tbsp) and cost per unit (£/unit)

**Update ingredients**

Following Brexit and increases in inflation, the cost of ingredients is changing rapidly. An ingredient must have the ability for its cost per unit to be updated based on the most up-to-date pricing information.

**Flag ingredient as no longer available**

With the future supply of some ingredients looking uncertain, we may have to change the availability of certain ingredients. When this happens, we need to flag the ingredient as no longer available.

A flagged ingredient cannot be included in new shopping lists, but already generated shopping lists aren't impacted.

**Retrieve shopping lists**

Shopping lists should only be retrievable by the user that created them/they belong to. The total cost of a shopping list should be calculated the first time it's retrieved, and subsequently if it's changed

## Notes
* Seed the ingredient & shopping list tables with the provided data. Add these as part of the initial migrations.
* The shopping list API(s) will need user authentication. The ingredient API(s) should be publicly accessible.
* Don't forget to add documentation comments to the API endpoints to explain how to use them
* Add an indication of how you would approach testing across the layers of the API
* Write concise and clear commit messages
* How you might add caching backed with redis _(optional)_
* Add rate limiting to the API at 60 req/min _(optional)_

## Q&A
> How should I submit my test when I'm done?

Fork this repo and send a pull request when you think you are done.
