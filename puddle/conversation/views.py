from django.shortcuts import render ,get_object_or_404,redirect
from item.models import Item
from .models import Conversation , ConversationMessage
from .forms import ConversationMessageForm
# Create your views here.
def new_conversation(request , item_pk):
    item = get_object_or_404(Item , pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members_in = [request.user.id])

    if Conversation:
        pass 
    if request.method == 'POST' :
        form = ConversationMessageForm(request.POST)
    if form.is_valid():
        conversation = Conversation.objects.create(item=item)
        conversation.members.add(request.user)
        conversation.members.add(request.created_by)
        conversation.save()
