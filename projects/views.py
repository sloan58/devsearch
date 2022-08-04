from django.shortcuts import render

projects_list = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },

    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },

    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    return render(request, 'projects/index.html', {'projects': projects_list})


def project(request, pk):
    project_object = None

    for project_item in projects_list:
        if project_item['id'] == pk:
            project_object = project_item

    context = {
        'project': project_object
    }

    return render(request, 'projects/show.html', context)
