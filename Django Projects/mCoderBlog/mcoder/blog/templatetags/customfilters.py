

from django import template

register = template.Library()


@register.filter(name='getReplyListFromReplyDict')
def getReplyListFromReplyDict(replyDict,comment_sno):
    return replyDict.get(comment_sno)



