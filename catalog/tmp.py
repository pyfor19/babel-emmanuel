def function(request):
   template_name = 'template'
   context = {}
   if request.method == 'GET' :
       
       pass
   if request.method == 'POST' :
       
   return render(request,template_name,context)



from django.views import View
class Name(View):
   def get(self, request):
       # Code block for GET request

   def post(self, request):
       # Code block for POST request


class Name(forms.Form):
   field = forms.CharField(max_length = length, required = True, widget=forms.TextInput(
       attrs = {
           'class':'form-control',
           'type':'text',
           'placeholder':'field',
       }
   ),
       error_messages = {
           'required' : "This field is required",
           'invalid' : "This field is invalid",
   })

   def clean(self):
       cleaned_data = super().clean()
       #Do Stuff

class Name(forms.ModelForm):
   field = forms.CharField(min_length = 32, widget=forms.TextInput(
       attrs = {
           'placeholder':'field',
           'class':'form-control',
       }
   ),
       error_messages = {
           'required' : "This field is required",
           'invalid' : "This field is invalid",
   })

   #Metadata
   class Meta:
       model = model
       fields = []


from django.core.mail import send_mail
send_mail(
   'subject',
   'message',
   'from',
   ['to'],
   fail_silently=False,
)


'''
get_email_sent(request,receiver=[],subject='',context = {},template='emails/progress.html') 

'''
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def function(request,**kwargs):
   sender = settings.EMAIL_HOST_USER
   receiver = kwargs['receiver']
   subject = kwargs['subject']
   context = kwargs['context']
   html_content = render_to_string(kwargs['template'], context) # render with dynamic value
   text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
   email = EmailMultiAlternatives(subject, text_content, sender, receiver)
   email.attach_alternative(html_content, "text/html")
   email.send(fail_silently=True)
   return True

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def paginate_it(request,query,count):
   paginator = Paginator(query, count)
   page = request.GET.get('page')

   try:
       results = paginator.page(page)
   except PageNotAnInteger:
       results = paginator.page(1)
   except EmptyPage:
       results = paginator.page(paginator.num_pages)

   return [results, page]


from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template

def render_to_pdf(template_src, context_dict={}):
   template = get_template(template_src)
   html  = template.render(context_dict)
   result = BytesIO()
   pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
   if not pdf.err:
       return HttpResponse(result.getvalue(), content_type='application/pdf')
   return None


obj = get_object_or_404(Model, pk=

name = models.ForeignKey('Target', related_name='', on_delete=models.CASCADE))

name = models.CharField(max_length=length, ${blank=True, null=True})

field = models.ManyToManyField(Target)