from wtforms import Form, StringField, validators


class SearchProfileForm(Form):
    username = StringField('Username', [validators.required(), validators.Length(min=1, max=25), validators.Regexp(
        r'^[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*$', flags=0, message="Must only contain alphanumeric characters and dash")])
