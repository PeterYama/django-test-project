def validate_video_file(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.avi', '.flv', '.webm', '.wmv', '.3gp', '.mp4', '.mov']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported video extension.')

def validate_image_file(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpeg', '.gif', '.bmp', '.png', '.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported image extension.')