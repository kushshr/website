from django.utils import translation

class TranslatedField(object):
    def __init__(self, en_field, nl_field):
        self.en_field = en_field
        self.nl_field = nl_field

    def __get__(self, instance, owner):
        if translation.get_language() == 'nl':
            field = getattr(instance, self.nl_field)
            if field == None or field == '':
                return getattr(instance, self.en_field)
            else:
                return field
        else:
            field = getattr(instance, self.en_field)
            if field == None or field == '':
                return getattr(instance, self.nl_field)
            else:
                return field