from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Agent


def agents_list(request):
    """List all agents"""
    agents = Agent.objects.all().order_by('-rating')
    
    # Pagination
    paginator = Paginator(agents, 12)
    page_number = request.GET.get('page')
    agents = paginator.get_page(page_number)
    
    context = {
        'agents': agents,
    }
    return render(request, 'agents/agents_list.html', context)


def agent_detail(request, agent_id):
    """Agent detail page with their properties"""
    agent = get_object_or_404(Agent, pk=agent_id)
    properties = agent.properties.all()
    
    # Pagination
    paginator = Paginator(properties, 6)
    page_number = request.GET.get('page')
    properties = paginator.get_page(page_number)
    
    context = {
        'agent': agent,
        'properties': properties,
    }
    return render(request, 'agents/agent_detail.html', context)

