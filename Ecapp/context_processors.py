from .models import category


def menu_links(request):
    link = category.objects.all()
    return dict(link=link)
