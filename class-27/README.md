# Django Models

Django provides a powerful way to reason about an application's resources whether they are objects in our code or records persisted in a database.

#### Describe and Define

- Object Relational Mapper.
- Different mental models between application and persistence layers.
- Good code is "easier to reason about" code.

#### Execute

- Django project with data persistence
- Create inter-related models
- Use Django's Generic views to handle displaying Models

## Outline
- [x] Warm Up
- [x] Lecture / Demo / Review
- [x] Lab Preview
## Models

- **Why**
  - Python tends to express in terms of Objects
  - Databases are oriented around Tables/Rows/Columns and communicate via SQL
  - This dissonance can make it more difficult to reason about the problem domain
- **What**
  - Object Relational Mappers ( ORM ) bridges that gap by allowing developers to *mostly* think about Objects while the mappers handles interaction with the database.
- **How**
  - Django's ORM is called a Model
  - A model can be corresponds to a Database Table but is authored as a Python class
  - The model's attributes are analogous to the columns in a table
  - The values of those attributes are like the DB table rows.

### View + Model

- **Why**
  - While it's nice to see our `things` in admin panel, that's not meant for end users
  - We need for those models to be viewable (and eventually editable) by end user
- **What**
  - It is possible create custom views that interact with models
  - But often times model data is displayed in common ways
- **How**
  - Django provides `generic` class based views that make interacting with surprisingly little code
