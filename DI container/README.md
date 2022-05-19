## 📦**DI Container**📦

## 💡**Main idea**💡

```
Create a library with a dependency injection container that can create:
A) Singleton service (for one thread, we don’t go into multithreading)
B) Transient service -> each call - creation of a new object
The program must be able to:
- work with both your services and standard .Net classes.
- handle nested dependencies
- throw a custom error if there is a cyclic dependency (s1 -> s2 -> s1, s1-> s2 -> s3 -> s1, etc.. any
degree of nesting)
The result of the work should be an assembly of two projects.
1st project - library with DI container
2nd project - a test project with the result of the container operation (for example, a console application
with use cases,
or a test project with unit tests covering the functionality of the library)
``` 

## 🥽**Preview**🥽


## Python, OOP, DI Container
