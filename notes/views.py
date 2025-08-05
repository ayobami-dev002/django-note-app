from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

# Create your views here.

def note_list(request):
    notes = Note.objects.all().order_by('-created')
    return render(request, 'notes/note_list.html', {'notes': notes})

# Create a new note
def note_create(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'form': form})

# Update a note
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'form': form})

# Delete a note
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
