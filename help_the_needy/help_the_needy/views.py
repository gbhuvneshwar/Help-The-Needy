from django.shortcuts import render_to_response

def map(request):
    loc = ''
    if request.method == 'PUT':
        loc = request.PUT.get('location', '')
    return render_to_response("display_map.html", {'location': loc})