from django.shortcuts import redirect, render, get_object_or_404
from .models import Image
from . import forms


def index(request):

    image = Image.objects.all()
    return render(
        request, "index.html",
        dict(
            image=image
        )
    )


def create(request, *args, **kwargs):

    form = forms.ImageForm()

    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/successful")

    return render(request, "create.html", dict(form=form))


def dashboard(request, *args, **kwargs):
    return render(request, 'dashboard.html')


def update(request, image_id=None):

    update = get_object_or_404(Image, pk=image_id)

    form = forms.ImageForm(
        request.POST,
        request.FILES,
        instance=update
    )

    if request.method == "POST":
        form = forms.ImageForm(
            request.POST,
            request.FILES,
            instance=update
        )
        if form.is_valid():
            form.save()
            return redirect("imageprocessor:index")

    return render(
        request,
        "edit.html",
        dict(
            update=update,
            form=form
        )
    )


def delete_image(request, image_id=None):

    image_to_delete = get_object_or_404(Image, pk=image_id)

    if request.method == "POST":
        image_to_delete.delete()
        return redirect("imageprocessor:index")

def success(request, *args, **kwargs):
    return render(request, 'success.html')
