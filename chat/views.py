from django.shortcuts import render, redirect
import os
import openai
import json
from .models import Chat

 
def chat(request): 
    
    if request.method == 'POST':
        question = request.POST['chat']
        openai.api_key = "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"
        # openai.api_key = os.getenv("MY_KEY")
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