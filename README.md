# hackjps-2023-project: RateMyTeachers
This is my HackJPS project for 2023. What is it? A RateMyProfessor for middle and high
school students, done in a way so that each district could have their own instance running,
allowing for a much better integration with students.
## How does it work?
This app uses a Django backend that serves as an account system, and a way to manage
all teachers added in the system. If you want to see, go to "127.0.0.1:8000/admin" and 
log in with the credentials, username: "admin1", password: "testuser". All teachers are
added in the admin panel, and then can be viewed by regular students. All schools are added
the same way. However, this could change, allowing for a more automated system, where 
students can vote if a new teacher has joined the school, or a old one has left. 

Teachers are connected to their school, and the school lists all teachers in it. This
allows the teacher information page to show what school they teach in, and the school
information page to list all teachers that are teaching at their school. 

Teachers also contain metadata on what classes they teach, or what grades they teach. This
makes it simpler to use the search functionality, as people can find the teacher they are
looking for without searching 20 teachers with the last name "Smith".

Lastly, teachers contain reviews, and an average rating. This allows students to write
appropriate reviews for their teachers, and allows other students to see what the teacher
might be like next year.

## What features could be added?
Features like verification while creating an account, or a way to verify that you are a member of
said city/school district could be added. This would allow for a more secure system, and would
protect the privacy of teachers. Also, automated moderation could be added, to prevent spam or
inappropriate reviews from being posted. A voting system to add new teachers and schools could
also be added, to allow for a more automated system. Lastly, a way to add classes to teachers
could be added, to allow for a more specific search.

## Another site like this already exists though?
There is a website called RateMyTeacher. However, I had actually not seen this before starting my project.
I think that my project is different, as it is more focused on the school district/city, and allows for a 
more personalized experience. If a math teacher switches grades, a student could **possibly** contest that
in a voting system, allowing for accurate information to be displayed. 

## How do I run this?
First, you need to install Django. You can do this by running `python -m pip install django` in your terminal. Then,
you need to run `python manage.py runserver` in the directory with the manage.py file. Then, you can go to
"127.0.0.1:8000" to view the site. You can also go to "<127.0.0.1>:8000/admin"
to view the admin panel. The default username is "admin1" and the default password is "testuser". You can
change this in the admin panel.

## How do I add a teacher?
You can add a teacher by going to the school_teachers page, and clicking "Add Teacher". You can then fill out
the form, and click "Save". You can also add a school by going to the schools page, and clicking "Add School".
Keep in mind, reviews is a list field, that takes in many dictionaries like [{"student", "date", "review", "rating"}, ...]

