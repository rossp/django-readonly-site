class ReadOnlySiteMiddleware(object):
    
    def process_request(self, request):
        
        from django.conf import settings
        from django.shortcuts import render

        readonly = getattr(settings, 'SITE_READ_ONLY', False)
        exempt_path_starts = getattr(settings, 'READ_ONLY_EXEMPT_PATH_STARTS', [])
        exempt_paths = getattr(settings, 'READ_ONLY_EXEMPT_PATHS', [])
        path_starts = getattr(settings, 'READ_ONLY_PATH_STARTS', [])
        paths = getattr(settings, 'READ_ONLY_PATHS', [])
        template = getattr(settings, 'READ_ONLY_TEMPLATE', None)
        
        if not readonly:
            return None
        
        if exempt_path_starts or exempt_paths:
            for path in exempt_path_starts:
                if request.path.startswith(path):
                    return None
        
            for path in exempt_paths:
                if request.path == path:
                    return None
        else:
            is_black_listed_path = (request.path in paths) or \
                any(request.path.startswith(path) for path in path_starts)
            
            if not is_black_listed_path:
                return None

        return render(request, [template, 'readonly/readonly.html'])

