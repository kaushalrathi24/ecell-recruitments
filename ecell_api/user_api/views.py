from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import os
from django.conf import settings

import json
from .forms import *
# Create your views here.


def all_users(request):
    file = open(os.path.join(settings.STATIC_ROOT, 'users.json'))
    data = json.load(file)
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 4})

def specific_users(request, id):
    file = open(os.path.join(settings.STATIC_ROOT, 'users.json'))
    data = json.load(file)
    for object in data:
        if object["_id"] == id:
            res = object
    return JsonResponse(res, safe=False, json_dumps_params={'indent': 4})

def update(request, id):
    with open(os.path.join(settings.STATIC_ROOT, 'users.json')) as jsonFile:
        data = json.load(jsonFile)
    for i in range(len(data)):
        if data[i]["_id"] == id:
            res = data[i].copy()
            break
    context = {}
    form = UpdateForm(request.POST or None, initial=res)
    context['form'] = form
    if context['form'].is_valid(): 
        new_data={}
        new_data["_id"] = res['_id']
        new_data["name"] = context['form'].cleaned_data["name"]
        new_data["email"] = context['form'].cleaned_data["email"]
        new_data["role"] = context['form'].cleaned_data["role"]
        new_data["active"] = context['form'].cleaned_data["active"]
        new_data["password"] = res['password']
        data[i] = new_data
        with open(os.path.join(settings.STATIC_ROOT, 'users.json'), "w") as jsonFile:
            json.dump(data, jsonFile, indent=4)
        return redirect('all_users')

    return render(request, "input.html", context)

def create(request):
    context = {}
    form = NewForm(request.POST or None)
    context['form'] = form
    if context['form'].is_valid(): 
        new_data={}
        new_data["_id"] = context['form'].cleaned_data['_id']
        new_data["name"] = context['form'].cleaned_data["name"]
        new_data["email"] = context['form'].cleaned_data["email"]
        new_data["role"] = context['form'].cleaned_data["role"]
        new_data["active"] = context['form'].cleaned_data["active"]
        new_data["password"] = context['form'].cleaned_data['password']
        data = [new_data]
        with open(os.path.join(settings.STATIC_ROOT, 'newUser.json'), "w") as jsonFile:
            json.dump(data, jsonFile, indent=4)
        return redirect('all_users')

    return render(request, "input.html", context)

def delete(request, id):
    with open(os.path.join(settings.STATIC_ROOT, 'users.json')) as jsonFile:
        data = json.load(jsonFile)
    for i in range(len(data)):
        if data[i]["_id"] == id:    
            break
    context = {}
    if request.method =="POST": 
        data.remove(data[i])
        with open(os.path.join(settings.STATIC_ROOT, 'deletedUser.json'), "w") as jsonFile:
            json.dump(data, jsonFile, indent=4)
        return redirect('all_users')

    return render(request, "delete.html", context)




