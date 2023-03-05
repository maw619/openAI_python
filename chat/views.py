from django.shortcuts import render, redirect
import os
import openai
import json
from .models import Chat

 
def chat(request): 
    
    if request.method == 'POST':
        question = request.POST['chat']
        openai.api_key = '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'
        # openai.api_key = os.getenv("MY_KEY")
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.52,
        presence_penalty=0.5,
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