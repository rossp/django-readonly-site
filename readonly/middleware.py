from django.shortcuts import render

class ReadOnlySiteMiddleware(object):
    
    def process_request(self, request):

        """
        If we are in read-only mode, figure out whether or not to render the request.
        We read in settings at the last possible minute sure that any dynamic
        settings are honored (eg django-dbsettings or similar)
        """
        
        from django.conf import settings

        readonly = getattr(settings, 'SITE_READ_ONLY', False)
        
        if not readonly:
            # Shortcut out if we aren't in read-only mode
            return None

        
        exempt_path_starts = getattr(settings, 'READ_ONLY_EXEMPT_PATH_STARTS', [])
        exempt_paths = getattr(settings, 'READ_ONLY_EXEMPT_PATHS', [])
        blacklist_path_starts = getattr(settings, 'READ_ONLY_PATH_STARTS', [])
        blacklist_paths = getattr(settings, 'READ_ONLY_PATHS', [])
        template = getattr(settings, 'READ_ONLY_TEMPLATE', None)


        if request.method <> 'GET':
            # Shortcut - will skip rest of this if statement
            # and just render the 'read only' template.
            pass

        elif exempt_path_starts or exempt_paths:
            # Deal with whitelisted items
            for path in exempt_path_starts:
                if request.path.startswith(path):
                    return None
        
            if request.path in exempt_paths:
                return None
        else:
            # Deal with blacklist
            is_blacklisted = False

            if request.path in blacklist_paths:
                is_blacklisted = True

            for path in blacklist_path_starts:
                if request.path.startswith(path):
                    is_blacklisted = True
            
            if not is_blacklisted:
                return None

        return render(request, [template, 'readonly/readonly.html'])

