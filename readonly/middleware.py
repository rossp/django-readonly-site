class ReadOnlySiteMiddleware(object):
    def process_request(self, request):
        from django.conf import settings
        from django.shortcuts import render

        readonly = getattr(settings, 'SITE_READ_ONLY', False))
        exempt_path_starts = getattr(settings, 'READ_ONLY_EXEMPT_PATH_STARTS', ('/admin'))
        exempt_paths = getattr(settings, 'READ_ONLY_EXEMPT_PATHS', [])
        template = getattr(settings, 'READ_ONLY_TEMPLATE', None)

        if not readonly:
            return None

        for path in exempt_paths:
            if request.path.startswith(path):
                return None


        return render(request, [template, 'readonly/readonly.html'])

