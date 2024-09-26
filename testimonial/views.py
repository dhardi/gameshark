
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm

@login_required
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Your testimonial has been submitted.')
            return redirect('testimonial_list')
    else:
        form = TestimonialForm()
    return render(request, 'testimonial/add_testimonial.html', {'form': form})

@login_required
def delete_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id, user=request.user)
    testimonial.delete()
    messages.success(request, 'Your testimonial has been deleted.')
    return redirect('testimonial_list')

def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonial/testimonial_list.html', {'testimonials': testimonials})
