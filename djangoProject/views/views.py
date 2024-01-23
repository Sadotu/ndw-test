# djangoProject/views/views.py

from django.shortcuts import render, get_object_or_404, redirect
from djangoProject.models.bridge_administration import BridgeAdministration
from django.views.generic import ListView, DetailView
from djangoProject.forms import BridgeAdministrationForm  # You need to create this ModelForm


# Read: List view
class BridgeAdministrationListView(ListView):
    model = BridgeAdministration
    template_name = 'bridge_administration_list.html'


# Read: Detail view
class BridgeAdministrationDetailView(DetailView):
    model = BridgeAdministration
    template_name = 'bridge_administration_detail.html'


# Create: New entry view
def bridge_administration_create(request):
    if request.method == 'POST':
        form = BridgeAdministrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bridge_administration_list')
    else:
        form = BridgeAdministrationForm()
    return render(request, 'bridge_administration_form.html', {'form': form})


# Update: Edit entry view
def bridge_administration_update(request, pk):
    administration = get_object_or_404(BridgeAdministration, pk=pk)
    if request.method == 'POST':
        form = BridgeAdministrationForm(request.POST, instance=administration)
        if form.is_valid():
            form.save()
            return redirect('bridge_administration_detail', pk=administration.pk)
    else:
        form = BridgeAdministrationForm(instance=administration)
    return render(request, 'bridge_administration_form.html', {'form': form})


# Delete: Delete entry view
def bridge_administration_delete(request, pk):
    administration = get_object_or_404(BridgeAdministration, pk=pk)
    if request.method == 'POST':
        administration.delete()
        return redirect('bridge_administration_list')
    return render(request, 'bridge_administration_confirm_delete.html', {'object': administration})
