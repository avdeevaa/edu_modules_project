from rest_framework.serializers import ValidationError


def validate_title(value):
    """Реализует проверку на отсутствие
            в названии запрещенных слов крипта, биржа, мошенничество, спам, афера"""
    forbidden_words = ['крипта', 'биржа', 'мошенничество', 'спам', 'афера']
    for word in forbidden_words:
        if word in value.lower():
            raise ValidationError('Название содержит запрещенное слово')