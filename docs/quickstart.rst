Quickstart
==========

I'll include some example apps on a different page

Before we can get the oauth url, we need to install and setup DiscoAuth

.. _installation:

Installation
------------

To use DiscoAuth, you need to first install it using pip:

.. code-block:: console

  (.venv) $ pip install discoauth


Now it's time to get started

.. _auth-url:

Authorization URL
-----------------

To make a url, you'll first need to set some variables, or at the very least know what to put in :class:`auth`

:class:`auth` takes *three* arguments, ``scope``, ``client_id``, and `redirect_uri``. The arguments are literally just the Discord scopes you want to use, your app's client ID, and the redirect URI you want to use.

Just be aware of the fact that ``scope`` is a list of strings, and each string is a valid Discord scope. ::

  from discoauth import auth

  client_id = "{Your app's client ID}"
  scope = ["identify", "email"]
  redirect_uri = "{Your redirect uri}"

  url = await auth(client_id, scope, redirect_uri).url()

and ``url`` would be your authorization url

Now you need to redirect the user to the auth url. If you use `Quart <https://quart.palletsprojects.com>`__, which I highly recommend, use ``redirect``

After redirecting the user will authorize (or not) and be redirected to the ``redirect_uri`` that you gave to AuthUrl, and you will need to get, and save that users ``code``. If you are using `Quart <https://quart.palletsprojects.com>`__, I suggest using the ``request.args.get()`` function

Now that we have the code, make sure to set it as a variable. I'll set it as ``code``

Access Token
------------

We'll need to uses a different class to get the token. Now let's go and add :class:`discord` to the ``import`` statement::

  from discoauth import auth, discord

Now, we need a new variable, ``client_secret``. Which is your app's client secret.

using the other three variables and ``client_secret`` we can use :class:`discord`. ::

  api = discord(client_id, client_secret, scope, redirect_uri)
  token = await api.token(code)

Now, ``token`` is the response, which can contain a new token. Save this somewhere safe.

Remember, :func:`token` returns a dictionary, containing the entire response, so you can still get the ``refresh_token``

User Data
---------

Now it's time to get the user data! We can use the subclass :class:`user` to get user data.::

  r = await discord.user(token).fetch()

After the :func:`fetch` you will get a response(``r``), which is an object-turned-dictionary, based off of the Discord User Object

The end... ?
------------

Hooray! Now we can get the username and avatar

While this is the end of the guides for this version, more will come later

And if you can't wait, make sure to visit the :doc:`API <api>` reference.







