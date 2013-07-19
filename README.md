django-readonly-site
====================

Take parts of your Django website offline by changing `settings.SITE_READ_ONLY = True`.

It does this by rendering a static template for your data-modifying views. I use this for my accounts page & signup page, so I can effectively freeze the site during big changes or migrations.

Note that django-readonly-site doesn't prevent any database updates. If you need to do this, then you should look at tools that override your database cursor, such as [django-db-readonly](https://github.com/streeter/django-db-readonly) or by doing it at the database level with Postgres slaves or similar. I don't require this for my purposes, and there's no point adding duplicate functionality to this app.

Pre-Requisites
--------------

Django >= 1.0 (In theory - I have only tested on 1.4 & 1.5)


Installation & Usage
--------------------

1. Install the Python package

   `pip install django-readonly-site`

2. Add to your Django `INSTALLED_APPS`

   `INSTALLED_APPS += ('readonly',)`

3. Add to your middleware

   `MIDDLEWARE_CLASSES += ('readonly.middleware.ReadOnlySiteMiddleware',)`

4. You are able to chose beetwen white or black listed paths (but not both at the same time) :

   Define the URLs that are still accessible when your site is in read-only mode :

   ```python
   READ_ONLY_EXEMPT_PATHS = ('/', '/about/', '/tour/')
   READ_ONLY_EXEMPT_PATH_STARTS = ('/admin/')
   ```

   Or the URLs that are NOT accessible when your site is in read-only mode :

   ```python
   READ_ONLY_PATHS = ('/private/')
   READ_ONLY_PATH_STARTS = ('/edit/', '/create/')
   ```


5. Optionally, define the template used when your site goes into read-only mode:

   `READ_ONLY_TEMPLATE = 'readonly/readonly.html' # This is the default`

6. When you're ready to go offline, toggle `SITE_READ_ONLY`. You'll probably have to `SIGHUP` your site.

   `SITE_READ_ONLY = True`

7. Any visit to a URL defined in the settings in #4, above, will render the `READ_ONLY_TEMPLATE` to the user instead. Your database isn't made read-only, or anything else like that.

Contributing
------------

Want to help improve django-readonly-site? Your help is welcomed! Please log issues and pull requests via GitHub https://github.com/rossp/django-readonly-site


License
-------

Copyright (c) 2013, Ross Poulton <ross@rossp.org>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

