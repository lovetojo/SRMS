from django.shortcuts import render
from .forms import StudentForm

def signin(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Do something with the form data (save to the database, etc.)
            form.save()
    else:
        form = StudentForm()

    # Render the signin page with the form
    return render(request, 'project/component/signin/signin.html', {'form': form})
