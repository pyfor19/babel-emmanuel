path("ajaxsubmiturl/", SubmitFormView.as_view(), name="submiturl"),


        context["form"] = SubmitURLForm()
        context["form"].fields["dewey_number"].initial = self.currentdewey.number


class SubmitURLForm(forms.Form):
    url = forms.URLField()
    dewey_number = forms.CharField(widget=forms.HiddenInput())


class SubmitFormView(FormView):
    form_class = SubmitURLForm
    success_url = reverse_lazy("publication")
    template_name = "catalog/base.html"

    def form_invalid(self, form):
        n = self.form.cleaned_data["dewey_number"]
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)

        try:
            r = get_url(form.cleaned_data["url"])
        except Exception as e:
            print(str(e))
        print("form_valid")
        url = form.cleaned_data["url"]
        dewey_number = form.cleaned_data["dewey_number"]
        print(f"form valid : {url} {dewey_number}")

        if self.request.is_ajax():
            data = {
                "pk": self.object.pk,
            }
            return JsonResponse(data)
        else:
            return reverse("publication-dewey", kwargs={"deweynumber": dewey_number})


{%if form %}
<div>form
  <form method="post" id="form-url" action="{% url 'submiturl' %}">
      {% csrf_token %}
      {{ form|crispy  }}   
      <button type="submit">submit</button> 
  </form>
</div>
{% endif %}




    def post(self, request, *args, **kwargs):
        print(f'{str(self.kwargs["deweynumber"])}')
        form = self.get_form()
        if form.is_valid():
            print("ok")
            # print(form.clean()["url"])
            return reverse("publication-dewey", kwargs={"deweynumber": n, "form": form})
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
            return reverse("publication-dewey", kwargs={"deweynumber": n, "form": form})

    def get_success_url(self):
        n = self.kwargs["deweynumber"]
        print(f"{str(n)}")
        return reverse("publication-dewey", kwargs={"deweynumber": n})
