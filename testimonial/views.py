# views.py do app testimonial

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Testimonial
from checkout.models import Order
from .forms import TestimonialForm

# Função para exibir a lista de testimonials
def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    order = Order.objects.filter(user_profile=request.user.userprofile).last()  # Pega o último pedido do usuário
    context = {
        'testimonials': testimonials,
        'order': order,  # Certifique-se de passar o order com order_number
    }
    return render(request, 'testimonial/testimonial_list.html', context)

# Função para adicionar um testimonial (já foi descrita anteriormente)
@login_required
def add_testimonial(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user_profile=request.user.userprofile)
    
    try:
        Testimonial.objects.get(order=order)
        messages.error(request, "You have already submitted a testimonial for this order.")
        return redirect('testimonial_list')
    except Testimonial.DoesNotExist:
        pass
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.order = order
            testimonial.save()
            messages.success(request, "Thank you for your testimonial!")
            return redirect('testimonial_list')
    else:
        form = TestimonialForm()

    context = {
        'form': form,
        'order': order,
    }
    return render(request, 'testimonial/add_testimonial.html', context)

# Função para deletar um testimonial
@login_required
def delete_testimonial(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if testimonial.user == request.user:
        testimonial.delete()
        messages.success(request, "Testimonial deleted successfully!")
    else:
        messages.error(request, "You don't have permission to delete this testimonial.")
    return redirect('testimonial_list')


@login_required
def edit_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id, user=request.user)

    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your testimonial has been updated successfully.')
            return redirect('testimonial_list')  # Ou outra página para redirecionar após a edição
    else:
        form = TestimonialForm(instance=testimonial)

    return render(request, 'testimonial/edit_testimonial.html', {'form': form})
