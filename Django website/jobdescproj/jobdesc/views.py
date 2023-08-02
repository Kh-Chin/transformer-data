from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import CustomForm
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
import re

def init_model():
    path = 'D:\migration\model\keehua-gpt2-final-cleaner'
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2', padding_side='left')
    tokenizer.pad_token_id = tokenizer.eos_token_id
    SPECIAL_TOKENS_MAPPING = {
        'bos_token': '<bos>',
        'eos_token': '<eos>',
        'pad_token': '<pad>',
        'additional_special_tokens': ['<desc>']
    }

    orig_num_tokens = len(tokenizer.get_vocab())
    num_special_tokens = tokenizer.add_special_tokens(SPECIAL_TOKENS_MAPPING)
    model = TFGPT2LMHeadModel.from_pretrained(path, pad_token_id=tokenizer.eos_token_id)
    return tokenizer, model


def homepage(request):
    context = {}
    text_model = None
    if request.method == "POST":

        form = CustomForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            job_title = form.cleaned_data['job_title']
            company_name = form.cleaned_data['company_name']
            email = form.cleaned_data['email']
            location = form.cleaned_data['location']
            keywords = form.cleaned_data['keywords']
            if text_model is None:
                tokenizer, text_model = init_model()
                input = f"<bos>\nJob Description for {job_title} which uses {keywords} skill:\n<desc>\n"
                tokens = tokenizer(input, truncation=True, max_length=128, padding='max_length', return_tensors='tf')
                pred = text_model.generate(tokens['input_ids'],
                                    max_length = 1024,
                                    no_repeat_ngram_size = 3,
                                    early_stopping = True
                                    )
                output = tokenizer.decode(pred[0], skip_special_tokens=True)
                output = re.sub('\{job\}', job_title, output)
                output = re.sub('\{company\}', company_name, output)
                output = re.sub('\{email\}', email, output)
                output = re.sub('\{location\}', location, output)
                context['job_title'] = job_title
                context['company_name'] = company_name
                context['email'] = email
                context['location'] = location
                context['keywords'] = keywords
                context['output'] = output
    return render(request, 'jobdesc/index1.html', context=context)

def model_page(request):
    return render(request, 'jobdesc/about.html')