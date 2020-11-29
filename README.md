Test assessment application
===========================

Implementation of a REST API call `/search?q=<needle>` that searches repository on GitHub, GitLab, Bitbucket and possibly other providers (only GitHub is implemented)

How to build and run
--------------------

```bash
make runserver
```

To test endpoint:

```bash
curl -L 'http://127.0.0.1:8000/search?q=example'
```
