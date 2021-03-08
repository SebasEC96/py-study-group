from wtforms import Form, StringField, validators


class SearchProfileForm(Form):
    username = StringField('Username', [validators.required(), validators.Length(min=1, max=25), validators.regexp(
        r'^[a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38}$', message="Must only contain alphanumeric characters and dash")])
