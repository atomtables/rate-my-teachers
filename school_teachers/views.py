from datetime import datetime

from django.shortcuts import render, redirect

from school_teachers.forms import ReviewForm
from school_teachers.models import Teacher, School


# Create your views here.

def teacher_info(request, teacher_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            teacher.comments.append({
                "student": f"{request.user.first_name} {request.user.last_name}",
                "date": datetime.now().strftime("%m/%d/%Y"),
                "review": form.data.get("review"),
                "rating": float(form.data.get("rating"))
            })
            teacher.overall_rating = sum([x["rating"] for x in teacher.comments]) / len(teacher.comments)
            teacher.save()
            return redirect(f"/info/teacher/{teacher_id}")
        except Teacher.DoesNotExist:
            return render(request, "base/404.html", status=404)
    else:
        form = ReviewForm()
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return render(request, "base/404.html", status=404)
        context = {
            "teacher": teacher.name,
            "teaching": teacher.teaching if teacher.teaching else "N/A",
            "school": teacher.school.name,
            "school_id": teacher.school.id,
            "school_address": teacher.school.address,
            "overall_rating": round(teacher.overall_rating, 1),
            "comments": teacher.comments,
            "classes": teacher.classes,
            "grades": teacher.grades,
            "how_many_comments": len(teacher.comments),
            "form": form if request.user.is_authenticated else None
        }
    return render(request, "school_teachers/teacher_info.html", context=context)


def school_info(request, school_id):
    try:
        school = School.objects.get(id=school_id)
    except School.DoesNotExist:
        return render(request, "base/404.html", status=404)
    context = {
        "school": school.name,
        "year_founded": school.year_founded if school.year_founded else "N/A",
        "address": school.address if school.address else "N/A",
        "principal": school.principal if school.principal else "N/A",
        "teachers": school.teachers.all(),
        "how_many_teachers": len(school.teachers.all()),
        "average_teacher_school_rating":
            round(sum([x.overall_rating for x in school.teachers.all()]) / len(school.teachers.all()), 1)
        }
    return render(request, "school_teachers/school_info.html", context=context)
