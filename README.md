django-rest-knox
================

[![Jazzband](https://jazzband.co/static/img/badge.svg)](https://jazzband.co/)
[![image](https://github.com/jazzband/django-rest-knox/workflows/Test/badge.svg?branch=develop)](https://github.com/jazzband/django-rest-knox/actions)

Authentication Module for django rest auth

Knox provides easy to use authentication for [Django REST
Framework](https://www.django-rest-framework.org/) The aim is to allow
for common patterns in applications that are REST based, with little
extra effort; and to ensure that connections remain secure.

Knox authentication is token based, similar to the `TokenAuthentication`
built in to DRF. However, it overcomes some problems present in the
default implementation:

-   DRF tokens are limited to one per user. This does not facilitate
    securely signing in from multiple devices, as the token is shared.
    It also requires *all* devices to be logged out if a server-side
    logout is required (i.e. the token is deleted).

    Knox provides one token per call to the login view - allowing each
    client to have its own token which is deleted on the server side
    when the client logs out.

    Knox also provides an option for a logged in client to remove *all*
    tokens that the server has - forcing all clients to re-authenticate.

-   DRF tokens are stored unencrypted in the database. This would allow
    an attacker unrestricted access to an account with a token if the
    database were compromised.

    Knox tokens are only stored in a secure hash form (like a password). Even if the
    database were somehow stolen, an attacker would not be able to log
    in with the stolen credentials.

-   DRF tokens track their creation time, but have no inbuilt mechanism
    for tokens expiring. Knox tokens can have an expiry configured in
    the app settings (default is 10 hours.)

More information can be found in the
[Documentation](https://jazzband.github.io/django-rest-knox/)

# Run the tests locally

If you need to debug a test locally and if you have [docker](https://www.docker.com/) installed:

simply run the ``./docker-run-tests.sh`` script and it will run the test suite in every Python /
Django versions.

You could also simply run regular ``tox`` in the root folder as well, but that would make testing the matrix of
Python / Django versions a bit more tricky.

# Work on the documentation

Our documentation is generated by [Mkdocs](https://www.mkdocs.org).

You can refer to their documentation on how to install it locally.

Another option is to use `mkdocs.sh` in this repository.
It will run mkdocs in a [docker](https://www.docker.com/) container.

Running the script without any params triggers the `serve` command.
The server is exposed on localhost on port 8000.

To configure the port the `serve` command will be exposing the server to, you
can use the following env var:

```
MKDOCS_DEV_PORT="8080"
```

You can also pass any `mkdocs` command like this:

```
./mkdocs build
./mkdocs --help
```

Check the [Mkdocs documentation](https://www.mkdocs.org/) for more.
