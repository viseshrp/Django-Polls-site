from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse

from .models import Question, Choice


# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    # response = "Results of question %s."
    # return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # when there's no choice selected, re display the vote form
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "No choice, idiot!", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# return HttpResponse("Voting on question %s." % question_id)
