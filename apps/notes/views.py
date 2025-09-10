from apps.notes.forms import NoteForm
from apps.notes.models import Note

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


@login_required
def notes_create(request):
    if request.method == 'GET':
        form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('notes:list')

    context = {'form': form}
    return render(request, 'notes_form.html', context)


@login_required
def notes_list(request):
    notes = Note.objects.filter(user=request.user)
    context = {'notes': notes}
    return render(request, 'notes_list.html', context)


@login_required
def notes_update(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'GET':
        form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:list')
    context = {'form': form}
    return render(request, 'notes_form.html', context)


@login_required
def notes_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:list')
    context = {'note': note}
    return render(request, 'notes_confirm_delete.html', context)
