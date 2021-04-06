from django import forms
from django.core.exceptions import ValidationError

from home import models
from shared.forms import FormRenderMixin


class InscriptionForm(FormRenderMixin, forms.ModelForm):

	class Meta:
		model = models.InterludesParticipant
		fields = (
			"school", "sleeps", # "mug",
			"meal_friday_evening", "meal_saturday_morning", "meal_saturday_midday",
			"meal_saturday_evening", "meal_sunday_morning", "meal_sunday_midday",
		)

	field_groups = [["school"], ["sleeps"], #["mug"],
		[
			"meal_friday_evening", "meal_saturday_morning", "meal_saturday_midday",
			"meal_saturday_evening", "meal_sunday_morning", "meal_sunday_midday",
		]
	]

	def save(self, *args, commit=True, **kwargs):
		participant = super().save(*args, commit=False, **kwargs)
		participant.is_registered = True
		if commit:
			participant.save()
		return participant

class ActivityForm(FormRenderMixin, forms.ModelForm):
	class Meta:
		model = models.InterludesActivityChoices
		fields = ("slot",)
		labels = {"slot":""}

	def __init__(self, *args, **kwargs):
		super(ActivityForm, self).__init__(*args, **kwargs)
		slots = models.InterludesSlot.objects.filter(subscribing_open=True)
		self.fields['slot'].queryset = slots

class BaseActivityFormSet(forms.BaseFormSet):
	"""Form set that fails if duplicate activities"""
	def clean(self):
		"""Checks for duplicate activities"""
		if any(self.errors):
			# Don't bother validating the formset unless each form is valid on its own
			return
		activities = []
		for form in self.forms:
			if self.can_delete and self._should_delete_form(form):
				continue
			activity = form.cleaned_data.get('slot')
			if activity is None:
				continue
			if activity in activities:
				raise ValidationError("Vous ne pouvez pas sélectionner une même activtté plusieurs fois")
			activities.append(activity)
