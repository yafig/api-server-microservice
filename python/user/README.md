# User Service in Python

This service is developed in Hexagonal / Port & Adapter architecture. The main reference is from here:

- http://connor-johnson.com/2018/06/26/ports-and-adapters-pattern-example-in-python/
- https://github.com/ajgrover/hexagonal-architecture-python

## What I learned while building this

- **Flask Dependency Injection**
- **Python Strict typing**

  It feels weird at first to write function signatures like `def get_user(username: str) -> User` in Python but now I love this.
- **Python Abstract Base Class**

  When defining an interface class with ABC, my Python code won't run unless all the abstract methods in the interface class is implemented in the implementation class, just like Golang and Java. Now I can set a strict contract for my classes.
- **Other new Python 3.8 features**

  eg. dataclass, dataclass_json, fstring, walrus operator

- **Alembic automigration**

  Use Alembic package with SQLAlchemy to generate, define and run migrations atomically

- **SQLAlchemy Core**

  In contract to SQLAlchemy ORM, SQLAlchemy Core is for interacting with databases with raw queries rather than interacting in ORM manner. The data structure is defined with dataclass, so using SQLAlchemy ORM to define the data structure again is not really good and not DRY.

Overall, the Python 3.8 writing experience is totally different from Python 2.7 writing style. Personally, it feels like writing Go now but with no compilation issues (but runtime issue).
