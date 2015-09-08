"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Dietz',
    'bio' : 'Contributor to FabricBolt web based Fabric Deployment system. ',
    'email' : '', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : '', # No @ symbol, just the handle.
    'github_username' : "paperreduction", 
    'headshot_url' : 'https://avatars2.githubusercontent.com/u/415984?v=3&s=460', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )
