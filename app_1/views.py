from django.shortcuts import render, redirect
from django.forms import modelformset_factory, ModelForm
from .models import Schedule, SClass, Registration, Ways
from django.views.generic.edit import CreateView
from .forms import RegistrationForm

def index(request):
    return render(request, 'app_1/shedule.html')


def by_class(request, class_id):
    shedule = Schedule.objects.filter(class_id__name=class_id).order_by('time_id')
    return render(request, 'app_1/index.html', {'shedule': shedule})


def project(request):
    return render(request, 'app_1/projects.html')


def timetable_edit(request, class_id):
    if request.user.is_authenticated:

        SheduleFormSet = modelformset_factory(Schedule, fields=('class_id', 'lesson_id', 'time_id', 'week_day'),
                                              can_delete=True,
                                              labels={'lesson_id': 'Название урока', 'time_id': 'Время урока'}, extra=3)

        if request.method == 'POST':
            formset = SheduleFormSet(request.POST, queryset=Schedule.objects.filter(class_id__name=class_id))
            if formset.is_valid():
                formset.save()
                return render(request, 'app_1/shedule.html')
        else:
            formset = SheduleFormSet(queryset=Schedule.objects.filter(class_id__name=class_id).order_by('time_id').order_by('week_day'))
        context = {'formset': formset}
        return render(request, 'app_1/form_timetable.html', context)

    else:
        return render(request, 'app_1/shedule.html')



#От 01.03.2022
def all_classes(request):
    all_class = SClass.objects.all().order_by('name')
    return render(request, 'app_1/all_classes.html', {'all': all_class})


def courses(request):
    return render(request, 'app_1/courses.html')


def gallery(request):
    return render(request, 'app_1/gallery.html')





class RegistrationCreateView(CreateView):
    template_name = 'app_1/registration.html'
    form_class = RegistrationForm
    success_url = 'app_1'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ways'] = Ways.objects.all()
        return context


