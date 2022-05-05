from application import app_commands
from entities.serializable_object import boozer_object
from serializers import general_serializer

if __name__ == '__main__':
    """Starting app with converting file types"""
    app_commands.convert_one_to_another()
