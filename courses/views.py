from django.shortcuts import render , get_object_or_404, redirect
from django.contrib import messages
from .models import Course, Student

# Create your views here.

def course_list(request):
    courses = Course.objects.all()
    print(courses)
    return render(request,'courses/course_list.html',{'courses': courses})

def register_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    title = course.title
    
    if course.current_enrolled >= course.maximum_capacity:
        messages.error(request, 'This course is full! ')
        return redirect('course_list')
    # return render(request, 'courses/register_course.html',)

    # If POST method, get data and save to the database. If not, render registeration page.

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        if not email or not name:
            return redirect('course_list')

        student , created = Student.objects.get_or_create(email = email, defaults={'name': name})

        if course in student.enrolled_courses.all():
            messages.error(request, 'You have already registered for this course!')
            return redirect('course_list')
        
        student.enrolled_courses.add(course)
        course.current_enrolled +=1
        course.save()

        messages.success(request, 'You have successfully registered for the new course! ')
        return redirect('course_list')
    
    return render(request , 'courses/register_course.html',{'title': title})


