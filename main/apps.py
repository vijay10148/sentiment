from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class MainConfig(AppConfig):
    path=os.path.join(settings.MODELS, 'models.p')
    with open(path,'rb')as pickled:
        data=pickle.load(pickled)
    model=data['model']
    vectorizer=data['vectorizer']    
    name = 'main'
