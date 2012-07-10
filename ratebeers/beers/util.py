import json as _json
from django import http

def json(view):
    def wrapped_view(req, *args, **kwargs):
        r = view(req, *args, **kwargs)

        # If the response is already an HttpResponse, just send it
        # directly back.
        if isinstance(r, http.HttpResponse):
            return r

        jsonp = req.GET.get('jsonp', False)
        if jsonp:
            # This is for IE
            content_type='text/javascript'
        else:
            content_type='application/json'

        res = http.HttpResponse(content_type=content_type)
        if jsonp:
            res.write(jsonp + '(')

        _json.dump(r, res, cls=_json.encoder.JSONEncoder)

        if jsonp:
            res.write(');')

        return res

    return wrapped_view
