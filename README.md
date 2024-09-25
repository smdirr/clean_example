```.
├── app/
│   ├── domain/
│   │   ├── entities.py
│   │   ├── interfaces.py
│   ├── application/
│   │   ├── use_cases.py
│   ├── infrastructure/
│   │   ├── repositories.py
│   │   ├── config.py
│   ├── ui/
│   │   ├── cli.py
├── main.py
```

## Clean Architecture example

Features:

- The application is divided into well-defined layers, such as the domain layer, the application layer, and the infrastructure layer, each with a clear and specific responsibility.
- The Domain layer encapsulates the logic and business rules.
- The internal layers of Clean Architecture do not depend on external frameworks or libraries.
- The Dependency Inversion Principle is used to decouple dependencies between layers, allowing internal layers to not depend on external layers.

https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
https://www.geeksforgeeks.org/complete-guide-to-clean-architecture/
