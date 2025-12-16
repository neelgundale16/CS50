from django.shortcuts import render, redirect

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = ["foo", "bar", "baz"]

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        request.session["tasks"].append(request.POST["task"])
        request.session.modified = True
        return redirect("tasks:index")

    return render(request, "tasks/add.html")
