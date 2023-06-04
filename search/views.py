from django.shortcuts import render

from school_teachers.models import Teacher


# Create your views here.

def search_query(request, query):
    context = {"results": []}
    for x in Teacher.objects.all():
        if query.lower() in x.name.lower():
            context["results"].append({
                "name": x.name,
                "id": x.id,
                "school": x.school.name,
                "classes": x.classes,
                "grades": x.grades,
                "overall_rating": round(x.overall_rating, 1),
            })
    if not context["results"]:
        context["results"] = None
        context["query"] = query
    return render(request, "search/searchpage.html", context=context)