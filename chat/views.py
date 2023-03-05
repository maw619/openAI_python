from django.shortcuts import render, redirect
import os
import openai
import json
from .models import Chat

def home(request):
    return render(request, 'chat/index.html')


def chat(request): 
    if request.method == 'POST':
        question = request.POST['chat']
        openai.api_key = "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"
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.3,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
         
        answer = response['choices'][0].text
        response_text = {}
       
        mychat = Chat(
            prompt=question,
            answer=answer 
        )

        mychat.save()
        
     
        context = {'data': answer}
        return render(request, 'chat/index.html', context)
    print('inside the Chat function')
    return render(request, 'chat/index.html')